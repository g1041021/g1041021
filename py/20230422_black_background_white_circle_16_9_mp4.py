import numpy as np
import cv2
from moviepy.editor import VideoClip
from moviepy.video.io.ffmpeg_writer import FFMPEG_VideoWriter


def make_frame(t):
    # 動画の長さをt秒として、白い円が画面内を移動する位置を算出する
    x = int(1920 * (1 - t / 5) + 200)
    y = 540
    r = int(200)

    # 黒い背景の画像を作成する
    img = np.zeros((1080, 1920, 3), dtype=np.uint8)

    # 白い円を描画する
    cv2.circle(img, (x, y), r, (255, 255, 255), -1)

    return img


# 動画ファイルを生成する
clip = VideoClip(make_frame, duration=10)
clip.write_videofile("output.mp4", fps=30, codec="mpeg4")
