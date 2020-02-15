#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

tentid = "645c70b5-548c-4ea5-bb99-8572b486014c"
clientid = "1341b2c9-a257-493d-87f4-23576d91d25b"

subscriptionId = "cca68b79-c062-4cdb-9de9-2c44614fa6b2"
url = 'https://management.azure.com/subscriptions/' + subscriptionId + \
    '/providers/Microsoft.Compute/skus?api-version=2019-04-01'
req = requests.request('GET', url)
print url
