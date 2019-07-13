# -*-coding:utf-8-*-
'''
统计所有错误的可能性
'''
# 管理员错误
adminLogin_error = {
    'success': 0,  # 管理员登陆成功
    'adminInvaild': 1,  # 管理员不存在
}
# 普通用户错误
userLogin_error = {
    'success': 0,  # 登陆成功
    'wrong_password': 1,  # 密码错误
    'userInvaild': 2,  # 用户不存在
}
userRegister_error = {
    'success': 0,  # 添加成功
    'failed': 1,  # 添加失败
    'userExist': 2  # 用户已存在
}
deleteUser_error = {
    'success': 0,  # 删除成功
    'userInvaild': 1,  # 用户不存在
}
updateUser_error = {
    'success': 0,  # 修改成功
    'userInvaild': 1,  # 用户不存在
    'failed': 2,  # 修改失败
}
selectUser_error = {
    'success': 0,  # 查询成功
    'userInvaild': 1,  # 用户不存在
    'failed': 2,  # 查询失败
}
# 公司信息错误
addCompany_error = {
    'success': 0,  # 添加成功
    'failed': 1,  # 添加失败
    'companyExist': 2  # 公司已存在
}
deleteCompany_error = {
    'success': 0,  # 删除成功
    'companyInvaild': 1,  # 公司不存在
}
updateCompany_error = {
    'success': 0,  # 修改成功
    'companyInvaild': 1,  # 公司不存在
    'failed': 2,  # 修改失败
}
selectCompany_error = {
    'success': 0,  # 查询成功
    'companyInvaild': 1,  # 公司不存在
    'type_fail':2,#
    'failed': 3,  # 查询失败
}
# 职员信息错误
addStaff_error = {
    'success': 0,  # 添加成功
    'failed': 1,  # 添加失败
    'companyInvaild': 2,  # 公司不存在
    'staffExist': 3,  # 职员已存在
}
deleteStaff_error = {
    'success': 0,  # 删除成功
    'staffInvaild': 1,  # 职员不存在
}
updateStaff_error = {
    'success': 0,  # 修改成功
    'staffInvaild': 1,  # 职员不存在
    'failed': 2,  # 修改失败
}
selectStaff_error = {
    'success': 0,  # 查询成功
    'staffInvaild': 1,  # 职员不存在
    'failed': 2,  # 查询失败
}
# 产品信息错误
addProduction_error = {
    'success': 0,  # 添加成功
    'failed': 1,  # 添加失败
    'companyInvaild': 2,  # 公司不存在
    'productionExist': 3,  # 产品已存在
}
deleteProduction_error = {
    'success': 0,  # 删除成功
    'productionInvaild': 1,  # 产品不存在
}
updateProduction_error = {
    'success': 0,  # 修改成功
    'productionInvaild': 1,  # 产品不存在
    'failed': 2,  # 修改失败
}
selectProduction_error = {
    'success': 0,  # 查询成功
    'productionInvaild': 1,  # 产品不存在
    'failed': 2,  # 查询失败
}
# 仓库信息错误
addWarehouse_error = {
    'success': 0,  # 添加成功
    'failed': 1,  # 添加失败
    'shelvesInvaild': 2,  # 货架信息不存在
    'warehouseExist': 3,  # 仓库信息已存在
}
deleteWarehouse_error = {
    'success': 0,  # 删除成功
    'warehouseInvaild': 1,  # 仓库信息不存在
}
updateWarehouse_error = {
    'success': 0,  # 修改成功
    'warehouseInvaild': 1,  # 仓库信息不存在
    'shelvesInvaild': 2,  # 货架信息不存在
    'staffInvaild': 3,  # 职员不存在
    'failed': 4,  # 修改失败
}
selectWarehouse_error = {
    'success': 0,  # 查询成功
    'warehouseInvaild': 1,  # 仓库信息不存在
    'failed': 2,  # 查询失败
}
# 货架信息错误
addShelves_error = {
    'success': 0,  # 添加成功
    'failed': 1,  # 添加失败
    'staffInvaild': 2,  # 职员不存在
}
deleteShelves_error = {
    'success': 0,  # 删除成功
    'shelvesInvaild': 1,  # 货架不存在
}
updateShelves_error = {
    'success': 0,  # 修改成功
    'shelvesInvaild': 1,  # 货架不存在
    'failed': 2,  # 修改失败
}
selectShelves_error = {
    'success': 0,  # 查询成功
    'shelvesInvaild': 1,  # 货架不存在
    'failed': 2,  # 查询失败
}
# 物流信息错误
addLogistics_error = {
    'success': 0,  # 添加成功
    'failed': 1,  # 添加失败
    'companyInvaild': 2,  # 公司不存在
    'driverInvaild': 3,  # 司机不存在
    'batchInvaild': 4,  # 批次不存在
}
deleteLogistics_error = {
    'success': 0,  # 删除成功
    'logisticsInvaild': 1,  # 物流信息不存在
}
updateLogistics_error = {
    'success': 0,  # 修改成功
    'LogisticsInvaild': 1,  # 物流信息不存在
    'failed': 2,  # 修改失败
    'illegalAccess': 3,  # 非法访问
}
selectLogistics_error = {
    'success': 0,  # 查询成功
    'logisticsInvaild': 1,  # 物流信息不存在
    'failed': 2,  # 查询失败
    'companyInvaild': 3,  # 公司不存在
    'batchInvaild':4,#批次信息有错
}

# 批次信息错误
addBatch_error = {
    'success': 0,  # 添加成功
    'failed': 1,  # 添加失败
    'productionInvaild': 2,  # 商品不存在
    'staffInvaild': 3,  # 职员不存在
    'illegalAccess': 4,  # 非法访问
}
deleteBatch_error = {
    'success': 0,  # 删除成功
    'batchInvaild': 1,  # 批次不存在
}
updateBatch_error = {
    'success': 0,  # 修改成功
    'batchInvaild': 1,  # 批次不存在
    'failed': 2,  # 修改失败
}
selectBatch_error = {
    'success': 0,  # 查询成功
    'batchInvaild': 1,  # 批次信息不存在
    'failed': 2,  # 查询失败
}
# 订单信息错误
addManifest_error = {
    'success': 0,  # 添加成功
    'failed': 1,  # 添加失败
    'productionInvaild': 2,  # 商品不存在
    'staffInvaild': 3,  # 职员不存在
    'illegalAccess': 4,  # 非法访问
}
updateManifest_error = {
    'success': 0,  # 修改成功
    'manifestInvaild': 1,  # 订单不存在
    'failed': 2,  # 修改失败
}
selectManifest_error = {
    'success': 0,  # 查询成功
    'manifestInvaild': 1,  # 订单信息不存在
    'failed': 2,  # 查询失败
}
# 查询错误
searchProduction_error = {
    'success': 0,  # 查询成功
    'productionInvaild': 1,  # 商品不存在
    'batchInvaild': 2,  # 批次不存在
    'staffInvaild': 3,  # 职员不存在
    'companyInvaild': 4,  # 公司不存在
    'failed': 5,  # 查询失败
}
