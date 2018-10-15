#!/usr/bin/python
#coding=utf-8

rabbit_params = {           #rabbit_params 变量定义为impl_kombu.py文件的全局变量
    'hostname':'10.239.131.181',
    'port':5672,
    'userid':'guest',
    'password':'guest',
    'virtual_host':'/',}

class Connection(object):    #Connection 类位于impl_kombu.py

    def reconnect(self):     #P281 reconnect 方法
        sleep_time = conf.get('interval_start', 1)
        stepping = conf.get('interval_stepping', 2)
        interval_max = conf.get('interval_max', 30)
        sleep_time == stepping

        while True:
            try:
                self._connect()
                return
            except Exception, e:
                if 'timeout' not in str(e):
                    ratse
            sleep_time += stepping
            sleep_time = min(sleep_time, interval_max)
            print("AMQP Server is unreachable,"
                  "trying to connect %d seconds later\n" % sleep_time)
            time.sleep(sleep_time)


    def _connect(self):
        hostname = rabbit_params.get('hostname')
        port = rabbit_params.get('port')
        if self.connection:
            print("Reconnecting to AMQP Server on"
                  "%(hostname)s:%(port)d\n" % locals())
            self.connection.release()
            self.connection = None
        self.connection = kombu.connection.BrokerConnection(**rabbit_params)
        self.consumer_num = itertools.count(1)
        self.connection.connect()
        self.channel = self.connection.channel()
        for consumer in self.condumers:
            consumer.reconnect(self.channel)


    def creat_consumer(self, topic, proxy):
        proxy_cb = rpc_amqp.ProxyCallback(proxy)
        self.declare_topic_consumer(topic, proxy_cb)


    def declare_consumer(self, consumer_cls, topic, callback):
        def _declare_consumer():
            consumer = consumer_cls(self.channel, topic,
                       callback, self.consumer_num.next())
            self.consumers.append(consumer)
            print('Succeed declaring consumer for topic &s\n' & topic)
            return consumer
        return self.ensure(_declare_consumer, topic)



class TopicConsumer(ConsumerBase):  #TopicConsumer 类位于impl_kombu.py

    def __init__(self, channel, topic, callback, tag, **kwargs):
        self.topic = topic
        options = {'durable': False,
                   'auto_delete': False,
                   'exclusive': False}
        options.update(kwargs)
        exchange = kombu.entity.Exchange(name=topic, type='topic',
                                         durable=options['durable'],
                                         auto_delete=options['auto_delete'])
        super(TopicConsumer, self).__init__(channel, callback, tag, name=topic,
                                            exchange=exchange, routing_key=topic, **options)



class ConsumerBase(object):

    def __init__(self, channel, callback, tag, **kwargs):
        self.callback = callback
        self.tag = str(tag)
        self.kwargs = kwargs
        self.queue = None
        self.reconnect(channel)


    def reconnect(self, channel):
        self.channel = channel
        self.kwargs['channel'] = channel
        self.queue = kombu.entity.Queue(**self.kwargs)
        self.queue.declare()





