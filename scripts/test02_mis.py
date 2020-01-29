import pytest

from api.api_mis import ApiMis
from tool.get_log import GetLog
from tool.read_yaml import read_yaml
from tool.tool import Tool
import api
log = GetLog.get_logger()


class TestMis:
    # 1. 初始化
    def setup_class(self):
        # 获取ApiMis对象
        self.mis = ApiMis()

    # 2. 登录
    @pytest.mark.parametrize("account,password", read_yaml("mis_login.yaml"))
    def test01_mis_login(self, account, password):
        # 1. 调用登录接口
        r = self.mis.api_mis_login(account, password)
        # 2. 提取token
        Tool.common_token(r)
        print("后台管理系统登录后，请求headers为：", api.headers)
        try:
            # 3. 断言
            Tool.common_assert(r)
        except Exception as e:
            # 1. 日志
            log.error(e)
            # 2. 抛异常
            raise

    # 3. 查询文章
    def test02_mis_search(self):
        # 1. 调用查询文章接口
        r = self.mis.api_mis_search()
        try:
            # 2. 断言
            Tool.common_assert(r, status_code=200)  # 注意：状态码为200并且为int型
        except Exception as e:
            # 1. 日志
            log.error(e)
            # 2. 抛异常
            raise

    # 4. 审核文章
    def test03_mis_audit(self):
        # 1. 调用审核文章接口
        r = self.mis.api_mis_audit()
        try:
            # 2. 断言
            Tool.common_assert(r)
        except Exception as e:
            # 1. 日志
            log.error(e)
            # 2. 抛异常
            raise
