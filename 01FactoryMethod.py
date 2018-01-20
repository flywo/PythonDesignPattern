#!/usr/bin/env python3
#coding:utf8

'''
工厂方法

意图：

定义一个用于创建对象的接口，让子类决定实例化哪一个类。Factory Method 使一个类的实例化延迟到其子类。

适用性：

当一个类不知道它所必须创建的对象的类的时候。

当一个类希望由它的子类来指定它所创建的对象的时候。

当类将创建对象的职责委托给多个帮助子类中的某一个，并且你希望将哪一个帮助子类是代理者这一信息局部化的时候。

'''

class ChinaGetter:
    def __init__(self):
        self.trans = dict(dog=u'小狗', cat=u'小猫')

    def get(self, msgid):
        try:
            return self.trans[msgid]
        except KeyError:
            return str(msgid)

class EnglistGetter:
    def get(self, msgid):
        return str(msgid)

#该方法就是工厂方法
def get_localizer(language='English'):
    languages = dict(English=EnglistGetter, China=ChinaGetter)
    return languages[language]()

e,g = get_localizer('English'), get_localizer('China')

for msgid in 'dog parrot cat bear'.split():
    print(e.get(msgid), g.get(msgid))