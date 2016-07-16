#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
if sys.version_info >= (3, 0):
    import imp
    imp.reload(sys)
else:
    reload(sys)
    sys.setdefaultencoding('utf8')
sys.dont_write_bytecode = True

from pixivpy3 import *

_USERNAME = "usersp"
_PASSWORD = "passsp"
_TEST_WRITE = False

_REQUESTS_KWARGS = {
  'proxies': {
    'https': 'http://192.168.88.167:8888',
  },
  'verify': False,       # PAPI use https, an easy way is disable requests SSL verify
}

def get_qs(url):
  import urlparse
  query = urlparse.urlparse(url).query
  return dict([(k,v[0]) for k,v in urlparse.parse_qs(query).items()])


def main():
  api = PixivAppAPI()
  # api = PixivAppAPI(**_REQUESTS_KWARGS)
  api.login(_USERNAME, _PASSWORD)

  response = api.illust_recommended()
  illust = response.illusts[0]
  print illust.title, illust.image_urls.medium

  # next page
  qs = api.parse_qs(response.next_url)
  response = api.illust_recommended(**qs)
  illust = response.illusts[0]
  print illust.title, illust.image_urls.medium


if __name__ == '__main__':
    main()
