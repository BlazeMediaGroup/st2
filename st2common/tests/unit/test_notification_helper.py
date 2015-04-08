# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest2

from st2common.models.api.notification import NotificationsHelper


class NotificationsHelperTestCase(unittest2.TestCase):

    def test_model_transformations(self):
        notify = {}
        notify['on_complete'] = {
            'message': 'Action completed.',
            'data': {
                'foo': '{{foo}}',
                'bar': 1,
                'baz': [1, 2, 3]
            }
        }
        notify['on_success'] = {
            'message': 'Action succeeded.',
            'data': {
                'foo': '{{foo}}',
                'bar': 1,
            }
        }
        notify_model = NotificationsHelper.to_model(notify)
        self.assertEqual(notify['on_complete']['message'], notify_model.on_complete.message)
        self.assertDictEqual(notify['on_complete']['data'], notify_model.on_complete.data)
        self.assertEqual(notify['on_success']['message'], notify_model.on_success.message)
        self.assertDictEqual(notify['on_success']['data'], notify_model.on_success.data)

        notify_api = NotificationsHelper.from_model(notify_model)
        self.assertEqual(notify['on_complete']['message'], notify_api['on_complete']['message'])
        self.assertDictEqual(notify['on_complete']['data'], notify_api['on_complete']['data'])
        self.assertEqual(notify['on_success']['message'], notify_api['on_success']['message'])
        self.assertDictEqual(notify['on_success']['data'], notify_api['on_success']['data'])
