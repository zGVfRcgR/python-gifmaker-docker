# ベースイメージ（Python 3.10を使用）
FROM python:3.13.7-slim

# 作業ディレクトリを作成
WORKDIR /app

# 必要なファイルをコピー
COPY requirements.txt ./
COPY ./src ./src

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# 実行コマンド（必要に応じて変更）
CMD ["python", "./src/gifmaker.py"]