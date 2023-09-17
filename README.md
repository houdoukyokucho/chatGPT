# ChatGPT を使用した BOT

CSV データを元に回答するチャット BOT です。  
使用する際は

## 階層

```
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── main.py
├── data.csv
└── .env
```

## ファイル

### main.py

ChatGPT の API を叩いて回答を出力します。

### data.csv

回答する材料となる情報を保持する CSV です。

### .env

ChatGPT の API キーを記載してください。  
記載例は以下の通りです。

```
OPEN_API_KEY=xxxxxxxxxx
```
