#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import requests
import sys
import time
import random
import logging
from oslo_serialization import jsonutils

LOG = logging.getLogger(__name__)
logfile = '/var/log/sign.log'
# groupId = "2000359" #IT事业部
groupId = "2001116"
userName = ""
userId = "9593"


class Client(object):
    """HTTP client.

    :param string endpoint: A user-supplied endpoint URL for the CPS service.
    :param integer timeout: Allows customization of the timeout for client http
                            requests. (optional)
    """
    def __init__(self, session=None, *args, **kwargs):
        pass

    def _json_request(self, method, url, **kwargs):
        LOG.debug("%s %s" % (method, url))
        response = requests.request(method, url, **kwargs)
        LOG.debug("Got response:%s" % response)
        try:
            body = response.content
            try:
                body = jsonutils.loads(body)
            except ValueError:
                LOG.debug('Could not decode response body as JSON')
        except KeyError, e:
            LOG.debug('Could not decode response Content-Type')
            body = None
        return response, body

    def get(self, url, **kwargs):
        return self._json_request("GET", url, **kwargs)

    def post(self, url, **kwargs):
        return self._json_request("POST", url, **kwargs)

    def put(self, url, **kwargs):
        return self._json_request("PUT", url, **kwargs)

    def delete(self, url, **kwargs):
        return self._json_request('DELETE', url, **kwargs)


class genarate_pos():
    def __init__(self):
        """
        左上角坐标: 114.391847,30.518829
        """
        self.start_x = 114.391847
        self.start_y = 30.518829
        self.max_offset_x = 0.011426
        self.max_offset_y = 0.006284

    def get_random_pos(self):
        return (self.start_x + random.uniform(0, self.max_offset_x),
                self.start_y + random.uniform(0, self.max_offset_y))


def setup_log():
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename= logfile
    )


def translate_pos(client, longitude, latitude):
    url = "http://api.map.baidu.com/geocoder/v2/"
    location = "%s,%s" % (latitude, longitude)
    data = {
        "ak" : "Es0Zdh4LrqUwnh8ylnxCXd44oNFZhcxA",
        "location": location,
        "output": "json",
        "pois": 1
    }
    resp, body = client.get(url, params=data)
    return body["result"]["pois"][0]["name"]


def sign(client, groupId, userName, userId, address, longitude, latitude):
    url = "http://iyouqu.com.cn:8080/app/group/service.do"
    position = "在%s签到啦！" % address.encode('utf-8')
    longitude = round(longitude, 6)
    latitude = round(latitude, 6)
    data = {
        "groupId": groupId,
        "userName": userName,
        "userId": userId,
        "msgId": "APP086",
        "position": position,
        "longitude": longitude,
        "latitude": latitude
    }
    text = jsonutils.dumps(data, sort_keys=False, separators=(',', ':'),
                        ensure_ascii=False)
    params = {"text": text}
    resp, body = client.post(url, data = params)
    LOG.info("%s%s, 坐标: (%s, %s), GroupID: %s" %
             (userName, position, longitude, latitude, groupId))
    return resp, body


def main():
    setup_log()
    time.sleep(random.randint(0, 10))
    client = Client()
    longitude, latitude = genarate_pos().get_random_pos()
    address = translate_pos(client, longitude, latitude)
    sign_resp, sign_body = sign(client, groupId, userName, userId,
                                address, longitude, latitude)
    LOG.info("%s",  jsonutils.dumps(sign_body, encoding='utf-8',
                                    ensure_ascii=False))


if __name__ == "__main__":
    sys.exit(main())

