import pytest
from httpx import AsyncClient, ASGITransport
import pytest_asyncio
from sqlalchemy import select

from core.models import db_helper
from main import main_app

from core.models import User
from .config import auth_register, auth_login


pytestmark = pytest.mark.asyncio


@pytest_asyncio.fixture
async def client():
    transport = ASGITransport(app=main_app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


@pytest_asyncio.fixture(autouse=True)
async def up_db():
    yield
    await db_helper.dispose()


@pytest_asyncio.fixture
async def auth_headers(client):
    user1_data = {"email": "user1@example.com", "password": "123"}
    await client.post(auth_register(), json=user1_data)

    user2_data = {"email": "user2@example.com", "password": "123"}
    await client.post(auth_register(), json=user2_data)

    login_data = {"username": user1_data["email"], "password": user1_data["password"]}
    response = await client.post(auth_login(), data=login_data)
    assert response.status_code == 200
    token = response.json()["access_token"]

    return {"Authorization": f"Bearer {token}"}


async def test_transfer_to_self(client, auth_headers):
    session_gen = db_helper.session_getter()
    session = await anext(session_gen)
    from_user = await session.scalar(
        select(User).where(User.email == "user1@example.com")
    )
    await session_gen.aclose()

    transfer_data = {"to_user_id": from_user.id, "amount": 50}

    response = await client.post(
        "/api/v1/transfer", json=transfer_data, headers=auth_headers
    )
    assert response.status_code == 400
    assert "cant send coins yourself" in response.json()["detail"]


async def test_transfer(client, auth_headers):
    session_gen = db_helper.session_getter()
    session = await anext(session_gen)

    to_user = await session.scalar(
        select(User).where(User.email == "user2@example.com")
    )
    to_user_id = to_user.id

    transfer_data = {"to_user_id": to_user_id, "amount": 50}

    response = await client.post(
        "/api/v1/transfer", json=transfer_data, headers=auth_headers
    )
    assert response.status_code == 200
    assert response.json()["message"] == "success"

    new_session_gen = db_helper.session_getter()
    new_session = await anext(new_session_gen)

    from_user = await new_session.scalar(
        select(User).where(User.email == "user1@example.com")
    )
    to_user = await new_session.scalar(
        select(User).where(User.email == "user2@example.com")
    )
    assert from_user.balance == 950
    assert to_user.balance == 1050

    await session_gen.aclose()
