
def getinfo(self):
    print('getinfo++')
g = type('Goods',(),{'id':'Gooodsid','name':'pbs','getinfo':getinfo})

def getname(self):
    print('getname--')
f = type('Food',(g,),{'type':'qwe','getname':getname})

g1 = g()
print(g1.id,g1.name)
g1.getinfo()
f1 = f()
print(f1.id,f1.name,f1.type)
f1.getname()
f1.getinfo()


g().getinfo()
print(g.id,g.name)

f().getinfo()
f().getname()
print(f.id,f.name,f.type)
