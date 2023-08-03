# speee-assignment

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
