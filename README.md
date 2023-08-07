# Fibonacci API 技術課題

Fibonacci 値を返す REST API

## 技術前提

Python, FastAPI を使用

- Python を使う理由：馴染んでいる言語で簡単に書ける
- FastAPI を使う理由：スピードが速い、REST API 対応、型が書ける、テストが簡単、doc が自動で生成される

## ユニットテスト

| テストケース               | クエリーパラメター | HTTP ステータスコード | 期待する結果                                                           |
| -------------------------- | ------------------ | --------------------- | ---------------------------------------------------------------------- |
| クエリーが空の場合         |                    | 422                   | `{"status": 422, "message": "Query parameter is required"}`            |
| クエリーが個数の場合       | n = 1.5            | 422                   | `{"status": 422, "message": "Number must be integer"}`                 |
| クエリーが string の場合   | n = xyz            | 422                   | `{"status": 422, "message": "Number must be integer"}`                 |
| クエリーが正数でないの場合 | n = -1             | 422                   | `{"status": 422, "message": "Number must be equal or greater than 0"}` |
| 正常の場合                 | n = 0              | 200                   | `{"result": 0}`                                                        |
| 正常の場合                 | n = 1              | 200                   | `{"result": 1}`                                                        |
| 正常の場合                 | n = 2              | 200                   | `{"result": 1}`                                                        |
| 正常の場合                 | n = 10             | 200                   | `{"result": 55}`                                                       |
| BigInt の場合              | n = 99             | 200                   | `{"result": 218922995834555169026}`                                    |

## 開発手段

課題はしっかり決まっているため、テストコードを先に書いた方がイメージがつくと思うので、Test Driven Development (TDD) を使用した

- RED：ユニットテストを設計して、テストを書く
- GREEN：API を書く
- Refactor：コードをリダクターしたり、綺麗なコードを書く

この開発手段を何回も iterate する

## Fibonacci アルゴリズム

Iteration アルゴリズムを使用して、フィボナッチ数列の n 番目の値を返す関数を作りました。

- Time Complexity: O(n)
- Space Complexity: O(1)

```python
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
```

## ディレクトリー説明

```
.
├── .flake8 # lintingの設定
├── .gitignore # gitに含まれないファイル
├── .vscode # IDEの設定
│   └── settings.json
├── README.md
├── app # サーバーのファイル
│   ├── __init__.py
│   └── main.py # サーバーのファイル
├── requirements.txt # プロジェクトのdependencies
└── tests # テストファイル
    ├── __init__.py
    └── fibonacci_test.py # fibonacci APIのテスト
```

## ローカルでの実行方法

1. リポジトリーをクローンする
2. `python -m venv venv`で環境を作成する
3. `source venv/bin/activate`で環境をアクティベートする
4. `pip install -r requirements.txt`で dependencies をインストールする
5. `uvicorn app.main:app --reload`でサーバーを起動する
