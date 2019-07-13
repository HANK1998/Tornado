# -*-coding:utf-8-*-
import json

import qrcode
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
from handlers.BaseHandler import BaseHandler


class GetQCodeHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        text='00001'
        qr = qrcode.QRCode(version=5,
                            error_correction=qrcode.constants.ERROR_CORRECT_L,
                            box_size=10,
                            border=4,
                            )
        # 添加数据
        qr.add_data(text)
        # 生成二维码
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        if img:
            #保存二维码
            img.save("./static/img/QCode.jpg")
            respon={'errorCode':0}
        else:
            respon={'errorCode':1}
        respon_json = json.dumps(respon)
        self.write(respon_json)



