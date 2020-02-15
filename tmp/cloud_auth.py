#!/usr/bin/python
# -*- coding: utf-8 -*-

import adal
from msrestazure.azure_active_directory import AdalAuthentication
from msrestazure.azure_cloud import AZURE_PUBLIC_CLOUD
import requests

# subscriptionID
Subscription_ID = 'cca68b79-c062-4cdb-9de9-2c44614fa6b2'

# Tenant ID for your Azure Subscription
TENANT_ID = '645c70b5-548c-4ea5-bb99-8572b486014c'

# Your Service Principal App ID
CLIENT = '1341b2c9-a257-493d-87f4-23576d91d25b'

# Your Service Principal Password
KEY = 'oQP1a@_A8IKSucOwyVu@:yHoRuryoL21'

LOGIN_ENDPOINT = AZURE_PUBLIC_CLOUD.endpoints.active_directory
RESOURCE = AZURE_PUBLIC_CLOUD.endpoints.active_directory_resource_id

context = adal.AuthenticationContext(LOGIN_ENDPOINT + '/' + TENANT_ID)
credentials = AdalAuthentication(
    context.acquire_token_with_client_credentials,
    RESOURCE,
    CLIENT,
    KEY
)


url = 'https://management.azure.com/subscriptions/' + Subscription_ID + \
    '/providers/Microsoft.Compute/skus?api-version=2019-04-01'
req = requests.request('GET', url)
print req
