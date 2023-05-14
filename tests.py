from main import f_dict

def test_y():
    assert f_dict({}) == {}
def test_two():
    assert f_dict({'a': 1}) == {'a': 1}
def test_i():
    assert f_dict({'a':{'b':{'c':2}}})=={'a.b.c':2}
def test_one():
    assert f_dict({'a': 1,'b':{'c':2,'d':{'e':3,'r':{'t':4}}},'y':{'u':5},'i':0}) == {'a': 1, 'b.c': 2, 'b.d.e': 3, 'b.d.r.t': 4, 'y.u': 5, 'i': 0}


