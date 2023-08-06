from fastapi import FastAPI, HTTPException, Request
from typing import Optional

from fastapi.responses import JSONResponse

app = FastAPI()


@app.exception_handler(HTTPException)
def custom_http_exception_handler(request: Request, exc: HTTPException):
    """
    HTTPExceptionのカスタムハンドラー
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={"status": exc.status_code, "message": exc.detail},
    )


@app.get("/fib")
def fib(n: Optional[str | int] = None):
    """
    Request Parameters
    ----------
    n : int
        フィボナッチ数列のn番目の値を返す

    Returns
    -------
    result : int
        フィボナッチ数列のn番目の値
    """
    if n is None:
        raise HTTPException(status_code=422, detail="Query parameter is required")

    try:
        n = int(n)
    except ValueError:
        raise HTTPException(status_code=422, detail="Number must be integer")

    if n < 0:
        raise HTTPException(
            status_code=422, detail="Number must be equal or greater than 0"
        )

    fib_result = fibonacci(n)

    return {"result": fib_result}


def fibonacci(n: int) -> int:
    """
    フィボナッチ数列のn番目の値を返す
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n <= 1:
        return n
    fib0 = 0
    fib1 = 1
    for _ in range(2, n + 1):
        fib0, fib1 = fib1, fib0 + fib1
    return fib1
