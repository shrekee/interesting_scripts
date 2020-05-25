#!/usr/bin/python3
import qrcode
import sys
import hashlib
import time
import os.path

"""
运行环境 python3
通过外部传入的一个url，生成对应的QRcode（二维码）

"""

# 你自己的保存图片的路径
IMG_STORE_DIR = '/home/shrek/Pictures'


def generate_qr_code(url):
    """主要的起作用qrcode库，创建一个二维码实例，to generate a qrcode picture."""
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1
    )
    qr.add_data(url)
    qr.make(fit=True)
    img_ins = qr.make_image()
    return img_ins


def save_img(img_ins):
    """Save this new created picture."""
    time_str = time.strftime("%Y-%m-%d_%H:%M:%S")
    md5_ins = hashlib.md5()
    md5_ins.update(time_str.encode())
    IMG_name = time_str + '_' + md5_ins.hexdigest()[-5:] + ".png"
    img_path = os.path.join(IMG_STORE_DIR, IMG_name)
    img_ins.save(img_path)
    print("Img is saved in: ", img_path)


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        print("only need one argument")
        print("""
            For example: python3 <this script>  <http://www.baidu.com>
                """)
        sys.exit(1)
    img_ins = generate_qr_code(args[1])
    save_img(img_ins)
