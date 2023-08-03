from fastapi import FastAPI, HTTPException, Request
from typing import Optional

from fastapi.responses import JSONResponse

app = FastAPI()


@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"status": exc.status_code, "message": exc.detail},
    )


@app.get("/fib")
async def fib(n: Optional[str | int] = None):
    if n is None:
        raise HTTPException(status_code=400, detail="Query parameter is required")

    try:
        n = int(n)
    except ValueError:
        raise HTTPException(status_code=400, detail="Number must be integer")

    if n < 0:
        raise HTTPException(
            status_code=400, detail="Number must be equal or greater than 0"
        )

    fib_result = await fibonacci(n)

    return {"result": fib_result}


async def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
