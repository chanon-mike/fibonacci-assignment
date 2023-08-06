from fastapi import FastAPI, HTTPException, Request
from typing import Optional

from fastapi.responses import JSONResponse

# FastAPIインスタンスを初期化する
app = FastAPI()


# HTTPExceptionのエラーハンドラーをオーバーライドし、カスタムのエラーメッセージをJSON形式で返す
@app.exception_handler(HTTPException)
def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"status": exc.status_code, "message": exc.detail},
    )


@app.get("/fib")
def fib(n: Optional[str | int] = None):  # クエリパラメータnを受け取る
    # nが指定されていない、または整数に変換できない場合、または0未満の場合はHTTPステータス422と該当するエラーメッセージを返す
    if n is None:
        raise ValueError("Query parameter is required")

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


# Fibonacci数列を計算する関数を定義し、整数nを引数に取り、そのn番目のFibonacci数を返す
def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
