import random

from tools.api import request_tool
# '''
# 自动生成 数字 20,80   #生成20到80之间的数字 例：56
# 自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
# 自动生成 地址
# 自动生成 姓名
# 自动生成 手机号
# 自动生成 邮箱
# 自动生成 身份证号
# '''
#
# def test_addProd(pub_data):
#     pub_data["productCode"]="自动生成 字符串 5 数字字母"   #生成20到80之间的数字 例：56
#     method = "POST"  #请求方法，全部大写
#     feature = "商品模块"  # allure报告中一级分类
#     story = '增加产品'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/product/addProd"  # 接口地址
#     headers = {"token":pub_data["token"]}
#     status_code = 200  # 响应状态码
#     expect = ""  # 预期结果
#     json_data = '''{
#           "brand": "小米",
#           "colors": [
#             "炫酷黑","玫瑰金","天空蓝"
#           ],
#           "price": 5999,
#           "productCode": "${productCode}",
#           "productName": "红米",
#           "sizes": [
#             "32G","66G","88G"
#           ],
#           "type": "手机"
#         }'''
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
#     json_path = [{"skuCode": "$['data'][0]['skuCode']"}]
#     # method,pub_data和url为必传字段
#     r = request_tool.request(json_path=json_path, method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)
#
#
# def test_getSkuByProdCode(pub_data):
#     method = "GET"  #请求方法，全部大写
#     feature = "商品模块"  # allure报告中一级分类
#     story = '查询产品'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/product/getSkuByProdCode"  # 接口地址
#     headers = {"token":pub_data["token"]}
#     status_code = 200  # 响应状态码
#     expect = ""  # 预期结果
#     params={'prodCode': "${productCode}"}
#
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)
#
# def test_changePrice(pub_data):
#     method = "POST"  #请求方法，全部大写
#     feature = "商品模块"  # allure报告中一级分类
#     story = '修改商品价格'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/product/changePrice"  # 接口地址
#     headers = {"token":pub_data["token"]}
#     status_code = 200  # 响应状态码
#     expect = ""  # 预期结果
#     data={'SKU': '${skuCode}', 'price': '4999'}
#
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)



def test_recharge(pub_data,db):
    res = db.select_execute("SELECT account_name FROM `t_cst_account` WHERE STATUS=0 AND account_name IS NOT NULL ;")
    pub_data["account_name"] = random.choice(res)[0]
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    headers = {"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    json_data='''{
  "accountName": "${account_name}",
  "changeMoney": 100
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)