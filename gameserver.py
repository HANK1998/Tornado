#-*-coding:utf-8
import tornado.web
import tornado.httpserver
import tornado.options
import tornado.ioloop
import tornado.log
import yaml
import logging
import logging.config
from application import webapplication
from tornado.options import define, options
from dal.dal_company import Dal_Company
from dal.dal_staff import Dal_Staff
from dal.dal_user import Dal_user
from dal.dal_warehouse import Dal_Warehouse
from dal.dal_logistics import Dal_Logistics
from dal.dal_batch import Dal_Batch
from dal.dal_manifest import Dal_Manifest

define("port", default=8010, help="run on the given port", type=int)

def initLog():
    #logging.config.fileConfig('configs/logging.conf')
    logging.config.dictConfig(yaml.load(open('configs/python_logging.yaml', 'r')))

def logTest():
    initLog()

def main():
    print (options.help)
    print ("Quit the server with CONTROL-C ")
    tornado.options.parse_command_line()
    http_server=tornado.httpserver.HTTPServer(webapplication)
    http_server.listen(options.port)
    ioInstance = tornado.ioloop.IOLoop.instance()
    ioInstance.start()

def initCache():
    Dal_user().initCache()
    Dal_Company().initCache()
    Dal_Staff().initCache()
    Dal_Warehouse().initCache()
    Dal_Logistics().initCache()
    Dal_Batch().initCache()
    Dal_Manifest().initCache()

if __name__ == "__main__":
    # api_cert_path = os.path.join(os.getcwd(), "configs/apiclient_cert.pem")
    initLog()
    initCache()
    main()
