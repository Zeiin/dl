from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Pietro

class Pietro(Adv):
#    comment = 'unsuitable resist'
    
    a1 = ('cd',0.13)

    conf = {}
    conf['slots.a'] = RR()+Breakfast_at_Valerios()
    conf['slots.frostbite.a'] = Primal_Crisis()+His_Clever_Brother()
    conf['slots.d'] = Nimis()
    conf['acl'] = """
        `dragon
        `s3, not self.s3_buff
        `s1
        `fs, x=5
        """
    coab = ['Tiki', 'Xander', 'Dagger']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)