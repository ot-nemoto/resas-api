# resas-api

- RESASとRESAS-APIとで更新年度の差分があるようなので、直接RESASからデータを取得するRESAS-API。
- RESAS-APIにしか存在しない機能については、範囲外。

## Environment

```sh
python --version
  # Python 3.8.13
```

## Run locally

*Install libraries*

```sh
pip install -r requirements.txt
```

```sh
python src/resas_api/app.py
```

*by gunicorn*

```sh
gunicorn app:app --chdir src/resas_api/
```

## API Documents

- https://ot-nemoto.stoplight.io/docs/resas-api/616a7c582b6e6-
