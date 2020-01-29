import pytest

from api.api_mp import ApiMp
import api
from tool.get_log import GetLog
from tool.read_yaml import read_yaml
from tool.tool import Tool
log = GetLog.get_logger()


class TestMp:
    # 1. 初始化
    def setup_class(self):
        # 获取ApiMp对象
        self.mp = ApiMp()

    # 2. 登录接口测试方法
    @pytest.mark.parametrize("mobile,code", read_yaml("mp_login.yaml"))
    def test01_mp_login(self, mobile, code):
        # 调用登录接口
        r = self.mp.api_mp_login(mobile, code)
        # 打印输出结果
        print("登录的结果为：", r.json())
        try:
            # 提取token
            Tool.common_token(r)
            # 断言
            Tool.common_assert(r)
        except Exception as e:
            # 写日志
            log.error(e)
            # 抛异常
            raise
        # # 提取token
        # token = r.json().get("data").get("token")
        # # 追加请求信息头
        # api.headers['Authorization'] = "Bearer " + token
        # print("添加token后的headers为：", api.headers)
        # # 断言状态码
        # assert 201 == r.status_code
        # # 断言响应信息
        # assert "OK" == r.json().get("message")

    # 3. 发布文章测试接口方法
    def test02_mp_article(self, title=api.title, content=api.content, channel_id=api.channel_id):
        # 1. 调用发布文章接口
        r = self.mp.api_mp_article(title, content, channel_id)
        # 2. 提取id
        api.article_id = r.json().get("data").get("id")
        print("发布文章成功后的id值为：", api.article_id)
        try:
            # 3. 断言
            Tool.common_assert(r)
        except Exception as e:
            # 1. 日志
            log.error(e)
            # 2. 抛异常
            raise