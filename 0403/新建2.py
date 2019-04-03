
def ref( classname,parentclass,addrs ):
    print(classname)
    print(parentclass)
    print(addrs)
    newaddr = {}
    for k,v in addrs.items():
        # print(k,v)
        if not k.startswith('__'):
            k  = k +'attr'
            print(k,v)
            newaddr[k] = v
    return type('new'+classname,parentclass,newaddr)
class Good(metaclass=ref):
    id = None
    name = None

g = Good()
print(g)
print(g.__dir__())