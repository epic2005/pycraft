#!/usr/bin/python
# -*- coding: utf-8 -*-

import adal
from msrestazure.azure_active_directory import AdalAuthentication
from msrestazure.azure_cloud import AZURE_PUBLIC_CLOUD

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
