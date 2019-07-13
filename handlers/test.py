from dal.dal_batch import Dal_Batch
from handlers.BaseHandler import BaseHandler


class testHandlers(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("test.html")

    def post(self, *args, **kwargs):
        code = self.get_argument('code')
        Dal_Batch().createQrCode(code)