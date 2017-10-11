#!/usr/bin/env python

# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Note: This file is auto generated. Do not edit manually.

class TimeSeriesResponseList:

    def __init__(self, **kwargs):
        self.swaggerTypes = {
            'responses': 'list[cloudera.director.v10.models.TimeSeriesResponse]',
            'rows': 'list[cloudera.director.v10.models.TimeSeriesRow]'

        }


        #Responses
        self.responses = kwargs.get('responses',[]) # list[cloudera.director.v10.models.TimeSeriesResponse]
        #Rows
        self.rows = kwargs.get('rows',[]) # list[cloudera.director.v10.models.TimeSeriesRow]
        
