from typing import Annotated, Optional

from fastapi import Header, HTTPException
async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != "my-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
async def get_query_token(token: Optional[str] = "rohan"):
    if token is None or token != "rohan":
        raise HTTPException(status_code=400, detail="No rohan token provided")