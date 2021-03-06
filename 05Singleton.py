#!/usr/bin/env python3
#coding:utf8

'''
单例

意图：

保证一个类仅有一个实例，并提供一个访问它的全局访问点。

适用性：

当类只能有一个实例而且客户可以从一个众所周知的访问点访问它时。

当这个唯一实例应该是通过子类化可扩展的，并且客户应该无需更改代码就能使用一个扩展的实例时。
'''


class Singleton(object):
    __instance = None
    def __init__(self):
        pass
    def __new__(cls, *args, **kwargs):
        if Singleton.__instance is None:
            Singleton.__instance = object.__ne__(cls, *args, **kwargs)
        return Singleton.__instance

if __name__ == '__main__':
    class SingleSpam(Singleton):
        def __init__(self, s):
            self.s = s
        def __str__(self):
            return self.s

    s1 = SingleSpam('spam')
    print(id(s1), s1)
    s2 = SingleSpam('spa')
    print(id(s2), s2)
    print(id(s1), s1)
