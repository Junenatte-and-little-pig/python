# -*- encoding: utf-8 -*-

import hashlib
import hmac

pwd = "123asd"
print(hashlib.algorithms_guaranteed)

md5 = hashlib.md5()
md5.update(pwd.encode())
print(md5.hexdigest())

hm = hmac.new(md5.digest(), pwd.encode(), digestmod='MD5')
print(hm.hexdigest())
