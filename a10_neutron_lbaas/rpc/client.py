# Copyright 2017,  Michael Durrant,  A10 Networks.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

class Client(object):

    def __init__(self, ip_address='127.0.0.1', exchange='openstack', topic='a10_lbaas', version='1.0'):
        self.ip_address = ip_address
        self.exchange = exchange
        self.topic = topic
        self.version = version
        self.transport = oslo_msg.get_transport(cfg.CONF)

    def get_client(namespace):
        target = oslo_msg.Target(server=self.ip_address, excahnge=self.exchange,
                                 topic=self.topic, namespace=namespace, version=self.version)
        return oslo_msg.RPCClient(self.transport, target)

    def msg_constructor(self, **args, **kwargs):
        return dict(args=args, kwargs=kwargs)

    def configure():
        rabbit_host = cfg.IPOpt('rabbit_host', default='127.0.0.1')
        rabbit_port = cfg.PortOpt('rabbit_port', default=5672)
        rabbit_userid = cfg.StrOpt('rabbit_userid', default='guest')
        rabbit_password = cfg.StrOpt('rabbit_password', default='stackqueue')
        rabbit_login_method = cfg.StrOpt('rabbit_login_method', default='AMQPLAIN')
        rabbit_virtual_host = cfg.StrOpt('rabbit_virtual_host', default='/')
        rpc_backend = cfg.StrOpt('rpc_backend', default='rabbit')

        conf = cfg.ConfigOpts()
        conf.register_opt(rabbit_host)
        conf.register_opt(rabbit_port)
        conf.register_opt(rabbit_userid)
        conf.register_opt(rabbit_password)
        conf.register_opt(rabbit_login_method)
        conf.register_opt(rabbit_virtual_host)
        conf.register_opt(rpc_backend)
