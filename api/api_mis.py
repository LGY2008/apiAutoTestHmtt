import api
import requests

from tool.get_log import GetLog

log = GetLog.get_logger()


class ApiMis:
    # 1. 初始化
    def __init__(self):
        # 1. 登录url
        self.url_login = api.host + "/mis/v1_0/authorizations"
        log.info("正在初始化后台管理系统 登录url: {}".format(self.url_login))
        # 2. 查询文章url
        self.url_search = api.host + "/mis/v1_0/articles"
        log.info("正在初始化后台管理系统 查询文章url: {}".format(self.url_search))
        # 3. 审核文章url
        self.url_audit = api.host + "/mis/v1_0/articles"
        log.info("正在初始化后台管理系统 审核文章url: {}".format(self.url_audit))

    # 2. 登录
    def api_mis_login(self, account, password):
        """
        :param account: 账号
        :param password: 密码
        :return: 响应对象
        """
        # 1. 参数数据
        data = {"account": account, "password": password}
        log.info("正在调用后台管理系统 登录接口，请求数据: {} 请求信息头：{}".format(data, api.headers))
        # 2. 调用post方法
        return requests.post(url=self.url_login, json=data, headers=api.headers)

    # 3. 查询文章
    def api_mis_search(self):
        """
        :param title: 文章标题，数据来源发布文章
        :param channel: 文章频道，数据来源发布文章频道id对应的频道
        :return: 响应对象
        """
        # 1. 参数数据
        data = {"title": api.title, "channel": api.channel}
        log.info("正在调用后台管理系统 查询文章接口，请求数据: {} 请求信息头：{}".format(data, api.headers))
        # 2. 调用get方法
        return requests.get(url=self.url_search, params=data, headers=api.headers)

    # 4. 审核文章
    def api_mis_audit(self):
        """
        :article_ids: 文章id， 数据来源发布文章后，服务器返回
        :status 2 : 2为审核通过
        :return: 响应对象
        """
        # 1. 参数数据
        data = {"article_ids": [api.article_id], "status": 2}  # 2:为审核通过
        log.info("正在调用后台管理系统 审核文章接口，请求数据: {} 请求信息头：{}".format(data, api.headers))
        # 2. 调用put方法
        return requests.put(url=self.url_audit, json=data, headers=api.headers)
