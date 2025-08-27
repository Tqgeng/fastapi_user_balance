from core.config import settings


def auth_login() -> str:
    parts = (
        settings.api.prefix,
        settings.api.v1.prefix,
        settings.api.v1.auth,
        "/login",
    )
    path = "".join(parts)
    return path.removeprefix("/")


def auth_register() -> str:
    parts = (
        settings.api.prefix,
        settings.api.v1.prefix,
        settings.api.v1.auth,
        "/register",
    )
    path = "".join(parts)
    return path.removeprefix("/")
