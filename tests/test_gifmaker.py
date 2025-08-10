import unittest
import os
from PIL import Image
from src.gifmaker import make_gif

class TestGifMaker(unittest.TestCase):
    def setUp(self):
        os.makedirs('test_images', exist_ok=True)
        # テスト用画像を2枚作成
        img1 = Image.new('RGB', (100, 100), color='red')
        img2 = Image.new('RGB', (100, 100), color='blue')
        img1.save('test_images/01.png')
        img2.save('test_images/02.png')

    def tearDown(self):
        # テスト画像とGIFを削除
        for f in ['test_images/01.png', 'test_images/02.png', 'test_images/output.gif']:
            if os.path.exists(f):
                os.remove(f)
        if os.path.exists('test_images'):
            os.rmdir('test_images')

    def test_make_gif(self):
        make_gif('test_images', 'test_images/output.gif', duration=100, loop=1)
        self.assertTrue(os.path.exists('test_images/output.gif'))
        # GIFファイルが正しく作成されているか確認
        gif = Image.open('test_images/output.gif')
        self.assertEqual(gif.format, 'GIF')
        self.assertEqual(gif.n_frames, 2)

if __name__ == '__main__':
    unittest.main()
