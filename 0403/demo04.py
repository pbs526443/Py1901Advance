def renameattr(classname,parentclass,addrs):
    # print(classname)
    # print(parentclass)
    # print(addrs)
    # print(classname.lower()[0]+'_')
    newattr = {}
    for k,v in addrs.items():
        # print(k,v)
        if not k.startswith('__'):
            # print(classname.lower()[0]+'_'+k)
            k = classname.lower()[0] + '_' + k
            newattr[k] = v
    return type(classname,parentclass,newattr)


class Good( metaclass = renameattr ):
    id = None
    name = None

g = Good()
print(g)
print(Good)
print(hasattr(Good,'name'))
print(hasattr(g,'g_name'))
print(g.__dir__())