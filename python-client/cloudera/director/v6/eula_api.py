# coding: utf-8

"""
Licensed to Cloudera, Inc. under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  Cloudera, Inc. licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cloudera.director.common.client import ApiClient


class EulaApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get(self, **kwargs):  # noqa: E501
        """Get the EULA  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_call=True
        >>> thread = api.get(async_call=True)
        >>> result = thread.get()

        :param async bool
        :return: Eula
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_call'):
            return self.get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_with_http_info(self, **kwargs):  # noqa: E501
        """Get the EULA  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_call=True
        >>> thread = api.get_with_http_info(async_call=True)
        >>> result = thread.get()

        :param async bool
        :return: Eula
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_call')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v6/eula', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Eula',  # noqa: E501
            auth_settings=auth_settings,
            async_call=params.get('async_call'),
            model_package="cloudera.director.v6.models",
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update(self, eula, **kwargs):  # noqa: E501
        """Update the EULA  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_call=True
        >>> thread = api.update(eula, async_call=True)
        >>> result = thread.get()

        :param async bool
        :param Eula eula: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_call'):
            return self.update_with_http_info(eula, **kwargs)  # noqa: E501
        else:
            (data) = self.update_with_http_info(eula, **kwargs)  # noqa: E501
            return data

    def update_with_http_info(self, eula, **kwargs):  # noqa: E501
        """Update the EULA  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_call=True
        >>> thread = api.update_with_http_info(eula, async_call=True)
        >>> result = thread.get()

        :param async bool
        :param Eula eula: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['eula']  # noqa: E501
        all_params.append('async_call')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'eula' is set
        if ('eula' not in params or
                params['eula'] is None):
            raise ValueError("Missing the required parameter `eula` when calling `update`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'eula' in params:
            body_params = params['eula']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v6/eula', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_call=params.get('async_call'),
            model_package="cloudera.director.v6.models",
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
