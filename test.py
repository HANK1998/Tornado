# -*-coding:utf-8-*-
import qrcode
import random
import barcode
from barcode.writer import ImageWriter

# 复杂的生成二维码
# version 控制二维码的大小，取值范围从1到40。取最小值1时，二维码大小为21 * 21。取值为None （默认）或者使用fit = true参数（默认）时，二维码会自动调整大小。
# error_correction 控制二维码纠错级别。
# ERROR_CORRECT_L：大约7%或者更少的错误会被更正。
# ERROR_CORRECT_M：默认值，大约15%或者更少的错误会被更正。
# ERROR_CORRECT_Q：大约25%或者更少的错误会被更正。
# ERROR_CORRECT_H：大约30%或者更少的错误会被更正
#box_size：控制二维码中每个格子的像素数，默认为 10。
#border：控制二维码四周留白包含的格子数，默认为4。
#image_factory：选择生成图片的形式，默认为 PIL 图像。
#mask_pattern：选择生成图片的的掩模。

#'code39', 'ean', 'ean13', 'ean8', 'gs1', 'gtin', 'isbn', 'isbn10', 'isbn13', 'issn', 'jan', 'pzn', 'upc', 'upca'
def make_code(text):
    qr = qrcode.QRCode(version=5,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=10,
                       border=4,
                       )
    # 添加数据
    qr.add_data(text)
    # 生成二维码
    qr.make(fit=True)
    img = qr.make_image()
    a = "C:\Users\chc\Desktop\Traceability\static\BarCode_img\\"
    b = str(random.randint(0,9))
    a = a+b+".png"
    print a
    img.save(a)
    img.show()
def make_brcode(text):
    Code = barcode.get_barcode_class('ean13')
    imagewriter = ImageWriter()
    text = str(text)
    bar = Code(text, writer=imagewriter, add_checksum=False)
    a = "C:\Users\chc\Desktop\Traceability\static\BarCode_img\\1"
    bar.save(a)

# 简单的生成二维码
# def make_code_easy(text):
#     image = qrcode.make(text)
#     image.save(r"C:\Users\lenovo\Desktop\002\TornadoServer\1.png")
#     image.show()



if __name__ == '__main__':
    text = input("请输入你想说的话:")
    make_code(text)
    #make_brcode(text)