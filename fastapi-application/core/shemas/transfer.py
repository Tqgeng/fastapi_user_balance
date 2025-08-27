from pydantic import BaseModel


class TransferRequest(BaseModel):
    # from_user_id: int
    to_user_id: int
    amount: int
