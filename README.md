# Speeeインターンシップ課題

Fibonacci値を返すREST API

## 技術前提

Python, FastAPIを使用
- Pythonを使う理由：馴染んでいる言語で簡単に書ける
- FastAPIを使う理由：スピードが速い、REST API対応、型が書ける、テストが簡単、docが自動で生成される

## ユニットテスト

| テストケース               | クエリーパラメター | HTTP ステータスコード | 期待する結果                                                           |
| -------------------------- | ------------------ | --------------------- | ---------------------------------------------------------------------- |
| クエリーが空の場合         |                    | 400                   | `{"status": 400, "message": "Query parameter is required"}`            |
| クエリーが個数の場合       | n = 1.5            | 400                   | `{"status": 400, "message": "Number must be integer"}`                 |
| クエリーが string の場合   | n = xyz            | 400                   | `{"status": 400, "message": "Number must be integer"}`                 |
| クエリーが正数でないの場合 | n = -1             | 400                   | `{"status": 400, "message": "Number must be equal or greater than 0"}` |
| 正常の場合                 | n = 0              | 200                   | `{"result": 0}`                                                        |
| 正常の場合                 | n = 1              | 200                   | `{"result": 1}`                                                        |
| 正常の場合                 | n = 2              | 200                   | `{"result": 1}`                                                        |
| 正常の場合                 | n = 10             | 200                   | `{"result": 55}`                                                       |
| 正常の場合                 | n = 99             | 200                   | `{"result": 218922995834555169026}`                                    |

## 開発手段

課題はしっかり決まっているため、テストコードを先に書いた方がイメージがつくと思うので、Test Driven Development (TDD) を使用した
- RED：ユニットテストを設計して、テストを書く
- GREEN：APIを書く
- Refactor：コードをリダクターしたり、綺麗なコードを書く

この開発手段を何回もiterateする

## ディレクトリー説明

```
.
├── .flake8 # lintingの設定
├── .gitignore # gitに含まれないファイル
├── .vscode
│   └── settings.json
├── README.md 
├── app
│   ├── __init__.py
│   └── main.py # サーバーのファイル
├── requirements.txt # プロジェクトのdependencies
└── tests
    ├── __init__.py
    └── fibonacci_test.py # fibonacci APIのテスト
```

## ソースコード説明

app/main.py
```
from fastapi import FastAPI, HTTPException, Request
from typing import Optional

from fastapi.responses import JSONResponse

# FastAPIインスタンスを初期化する
app = FastAPI()


# HTTPExceptionのエラーハンドラーをオーバーライドし、カスタムのエラーメッセージをJSON形式で返す
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"status": exc.status_code, "message": exc.detail},
    )


@app.get("/fib")
async def fib(n: Optional[str | int] = None): # クエリパラメータnを受け取る
    # nが指定されていない、または整数に変換できない場合、または0未満の場合はHTTPステータス400と該当するエラーメッセージを返す
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


# Fibonacci数列を計算する非同期関数を定義し、整数nを引数に取り、そのn番目のFibonacci数を返す
async def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

tests/fibonacci_test.py
- 上記のユニットテスト設計表をFastAPIのpytestで書く
