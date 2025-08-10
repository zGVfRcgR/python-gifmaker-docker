from PIL import Image
import glob
import os

def make_gif(input_folder, output_path, duration=200, loop=0):
    # 入力フォルダ内の画像ファイルを取得
    image_files = sorted(glob.glob(os.path.join(input_folder, '*.png')))
    if not image_files:
        raise ValueError('画像ファイルが見つかりません')
    frames = [Image.open(img).copy() for img in image_files]
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=loop
    )
    print(f'GIFを保存しました: {output_path}')

if __name__ == '__main__':
    # 例: imagesフォルダ内のPNG画像からoutput.gifを作成
    make_gif('images', 'output.gif', duration=200, loop=0)
