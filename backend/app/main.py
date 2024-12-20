from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserPublic(BaseModel):
    name: str
    age: int

@app.get(
    "/api/v1/users/email/{user_email}",
)
def read_user_by_email(email: str) -> UserPublic | None:
    """
    Get a specific user by email.
    """
    if email != "":
        print("Not none")
        return UserPublic(name="User", age=10)
    print("None")
    return None