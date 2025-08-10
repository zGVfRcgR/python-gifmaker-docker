# 🎞️ Python GIF Creator

Pythonで簡単にGIFアニメーションを作成できるツールです。画像の連続再生や、動的なグラフの可視化など、さまざまな用途に対応しています。

## 特徴
- 複数の画像を1つのGIFにまとめる
- フレームレートやループ設定のカスタマイズ
- `imageio`や`Pillow`を使った軽量な実装


## Dockerイメージをビルド
docker build -t python-gifmaker-docker -f docker/Dockerfile .

docker run --rm -v $(pwd)/images:/app/images python-gifmaker-docker

## 使い方

1. `images` フォルダにGIF化したいPNG画像を保存します。
	- 例: `images/01.png`, `images/02.png`, ...
2. 以下のコマンドでDockerコンテナを起動します。
	```sh
	docker run --rm -v $(pwd)/images:/app/images python-gifmaker-docker
	```
3. コンテナ起動後、`images` フォルダ内に `output.gif` が自動生成されます。

> ※ Dockerfileの設計により、`src/gifmaker.py` が `images` フォルダ内のPNG画像からGIF動画（output.gif）を作成します。

