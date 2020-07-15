import pytest

from tools.api import request_tool

'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''
@pytest.mark.smrz
def test__maoyan_sign(pub_data):
    pub_data["phone"] = "自动生成 手机号"
    pub_data["userName"] = "自动生成 字符串 3,5 数字字母 12q"
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '注册用户'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/signup"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
{
  "phone": "${phone}",
  "pwd": "qq123456",
  "rePwd": "qq123456",
  "userName": "${userName}"
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
    json_path = [{"cstId": '$.data.cstId'}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,json_path=json_path)
@pytest.mark.smrz
def test_sa(pub_data):
    pub_data["certno"] = "自动生成 身份证号"
    pub_data["cstName"] = "自动生成 姓名"
    pub_data["email"] = "自动生成 邮箱"
    headers = {
        "token":pub_data["token"]
    }
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '实名认证'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/cst/realname2"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
  {
  "cstId": "${cstId}",
  "customerInfo": {
    "birthday": "2000-07-07",
    "certno": "${certno}",
    "city": "上海市",
    "cstName": "${cstName}",
    "email": "${email}",
    "province":"上海市区",
    "sex": 2
  }
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

def test_maoyan_changepwd(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '修改密码'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/user/changepwd"  # 接口地址
    headers = {"token":pub_data["token"],'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Content-Type': 'application/json', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=user%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Cookie': 'csrftoken=K1b93CfwXCyVVJCKvGBr2z9gpODYDvE18eFgydclMwsw1wf6XtHjH9TveCqNjXC6'}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "newPwd": "qq1234567",
  "oldPwd": "qq123456",
  "reNewPwd": "qq1234567",
  "userName": "${userName}"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)


def test_login(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '修改密码后登录验证'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    headers = {"token": pub_data["token"], 'Host': '192.168.1.151:8084', 'Connection': 'keep-alive',
               'accept': 'application/json;charset=UTF-8',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
               'Content-Type': 'application/json', 'Origin': 'http://192.168.1.151:8084',
               'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=user%20apis',
               'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
               'Cookie': 'csrftoken=K1b93CfwXCyVVJCKvGBr2z9gpODYDvE18eFgydclMwsw1wf6XtHjH9TveCqNjXC6'}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data = '''{
                  "pwd": "qq1234567",
                  "userName": "${userName}"
                }'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, status_code=status_code, headers=headers,
                             expect=expect, feature=feature, story=story, title=title, json_data=json_data)
