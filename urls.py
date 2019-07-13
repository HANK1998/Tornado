# -*-coding:utf-8-*-
from handlers.managehandlers.AddManifestHandler import AddManifestHandlers
from handlers.managehandlers.SelectAllManifestHandler import SelectAllManifestHandlers, SelectAllManifestByPHandlers
from handlers.apphandlers.AppLoginHandler import AppLoginHandlers
from handlers.indexHandler import IndexHandlers
from handlers.apphandlers.AppRegisterHandler import AppRegisterHandlers
from handlers.LoginHandler import LoginHandlers
from handlers.managehandlers.AddBatchHandler import AddBatchHandlers
from handlers.managehandlers.AddCompanyHandler import AddCompanyHandlers
from handlers.managehandlers.AddLogisticsHandler import AddLogisticsHandlers
from handlers.managehandlers.AddStaffHnadler import AddStaffHandlers
from handlers.managehandlers.AddWarehouseHandler import AddWarehouseHandlers
from handlers.managehandlers.DeleteBatchHandler import DeleteBatchHandlers
from handlers.managehandlers.DeleteCompanyHandler import DeleteCompanyHandlers
from handlers.managehandlers.DeleteStaffHandler import DeleteStaffHandlers
from handlers.managehandlers.DeleteUserHandler import DeleteUserHandlers
from handlers.managehandlers.DeleteWarehouseHandler import DeleteWarehouseHandlers
from handlers.managehandlers.SelectAllBatchHandler import SelectAllBatchHandlers
from handlers.managehandlers.SelectAllCompanyHandler import SelectAllCompanyHandlers
from handlers.managehandlers.SelectAllLogisticsHandler import SelectAllLogisticsHandlers
from handlers.managehandlers.SelectAllStaffHandler import SelectAllStaffHandlers
from handlers.managehandlers.SelectAllUserHandler import SelectAllUserHandlers
from handlers.managehandlers.SelectAllWarehouseHandler import SelectAllWarehouseHandlers
from handlers.managehandlers.SelectCompanyHandler import SelectCompanyHandlers
from handlers.managehandlers.SelectManifestHandler import SelectManifestHandlers
from handlers.managehandlers.SelectAllManifestHandler import SelectAllManifestByCHandlers
from handlers.managehandlers.SelectStaffByCompanyHandler import SelectStaffByCompanyHandlers
from handlers.managehandlers.SelectStaffHandler import SelectStaffHandlers
from handlers.managehandlers.UpdateBatchHandler import UpdateBatchHandlers
from handlers.managehandlers.UpdateCompanyHandler import UpdateCompanyHandlers
from handlers.managehandlers.UpdateManifestHandler import UpdateManifestHandlers
from handlers.managehandlers.UpdateManifestHandler import UpdateLogisticsHandlers
from handlers.managehandlers.UpdateStaffHandler import UpdateStaffHandlers
from handlers.managehandlers.UpdateUserHnadler import UpdateUserHandlers
from handlers.managehandlers.SelectUserHandler import SelectUserHandlers
from handlers.managehandlers.SelectBatchHandler import SelectBatchBsHandlers
from handlers.managehandlers.SelectLogisticsHandler import SelectLogisticsHandlers
from handlers.managehandlers.SelectLogisticsHandler import SelectAllMyLogGHandlers
from handlers.managehandlers.SelectLogisticsHandler import SelectAllMyLogPHandlers
from handlers.managehandlers.SelectAllProdHandler import SelectAllProdHandlers
from handlers.managehandlers.SelectAllProdHandler import SelectProdByNameHandlers
from handlers.managehandlers.UpdateWarehouseHandler import UpdateWarehouseHandlers
from handlers.apphandlers.SearchProductionByCodeHandler import SearchProductionByCodeHandlers
from handlers.test import testHandlers
from handlers.managehandlers.getAllwcsHandler import getAllwcsHandlers
from handlers.apphandlers.SelectByCodeHandler import SelectByCodeHandlers

urls = [
    (r"/index", IndexHandlers),
    # 管理员
    (r"/Login", LoginHandlers),  # 登录
    # 公司登录
    #(r"/companyLogin",)
    # 普通用户
    (r"/appRegister", AppRegisterHandlers),  # app用户注册
    (r"/appLogin", AppLoginHandlers),  # app用户登录
    (r"/deleteUser", DeleteUserHandlers),  # 删除app用户
    (r"/updateUser", UpdateUserHandlers),  # 修改用户信息
    (r"/selectUser", SelectUserHandlers),  # 查找用户信息
    (r"/selectAllUser", SelectAllUserHandlers),  # 查找所有用
    # 公司信息
    (r"/addCompany", AddCompanyHandlers),  # 添加公司信息
    (r"/deleteCompany", DeleteCompanyHandlers),  # 删除公司信息
    (r"/updateCompany", UpdateCompanyHandlers),  # 修改公司信息
    (r"/selectCompany", SelectCompanyHandlers),  # 查找用户信息
    (r"/selectAllCompany", SelectAllCompanyHandlers),  # 查找所有公司信息

    # 职员信息
    (r"/addStaff", AddStaffHandlers),  # 添加职员
    (r"/deleteStaff", DeleteStaffHandlers),  # 删除职员
    (r"/updateStaff", UpdateStaffHandlers),  # 修改职员信息
    (r"/selectStaff", SelectStaffHandlers),  # 查找职员信息
    (r"/SelectStaffByCompany",SelectStaffByCompanyHandlers),# 通过公司Id查找职员信息
    (r"/selectAllStaff", SelectAllStaffHandlers),  # 查找所有职员信息

    # 仓储信息
    (r"/addWarehouse", AddWarehouseHandlers),  # 添加仓储
    (r"/deleteWarehouse", DeleteWarehouseHandlers),  # 删除仓储
    (r"/updateWarehouse", UpdateWarehouseHandlers),  # 修改仓储信息
    (r"/selectAllProd", SelectAllProdHandlers),  # 查找本公司所有仓储产品
    (r"/selectProdBN", SelectProdByNameHandlers),  # 查找本公司指定名称仓储产品
    (r"/selectAllWarehouse", SelectAllWarehouseHandlers),  # 查找所有仓储信息

    # 物流信息
    (r"/addLogistics", AddLogisticsHandlers),  # 添加物流
    (r"/updateLogistics", UpdateLogisticsHandlers),  # 修改物流信息
    (r"/selectLogistics", SelectLogisticsHandlers),  # 查找物流信息
    (r"/selectAllLogistics", SelectAllLogisticsHandlers),  # 查找所有物流信息
    (r"/selectAllMyLogG", SelectAllMyLogGHandlers),  # 查找所有物流信息
    (r"/selectAllMyLogP", SelectAllMyLogPHandlers),  # 查找所有物流信息

    # 批次信息
    (r"/addBatch", AddBatchHandlers),  # 添加批次
    (r"/deleteBatch", DeleteBatchHandlers),  # 删除批次
    (r"/updateBatch", UpdateBatchHandlers),  # 修改批次信息
    (r"/selectBatchBs", SelectBatchBsHandlers),  # 查找本公司批次信息
    (r"/selectAllBatch", SelectAllBatchHandlers),  # 查找所有批次信息

    # 订单信息
    (r"/getAllwcs",getAllwcsHandlers),#弹出表单时，返回前台备选目标公司和本公司采购职员名单
    (r"/addManifest", AddManifestHandlers),  # 添加订单
    (r"/updateManifest", UpdateManifestHandlers),  # 修改订单
    (r"/selectManifest", SelectManifestHandlers),  # 查找订单信息
    (r"/selectAllManifestBcSend", SelectAllManifestByCHandlers),  # 通过公司查生成的订单
    (r"/selectAllManifestBcGet", SelectAllManifestByPHandlers),  # 通过公司查接收的订单
    (r"/selectAllManifest", SelectAllManifestHandlers),  # 查找所有订单信息

    # 溯源
    (r"/searchProductionByCode", SearchProductionByCodeHandlers),  # 用溯源码查询信息
    (r"/selectByCode",SelectByCodeHandlers),
    (r"/test",testHandlers),
]
