from tron import colision

def test_colision():
    assert colision(1,2,8) == False
    assert colision(1,3,2) == True
    assert colision(4,1,2) == True
    assert colision(6,3,6) == True
    assert colision(6,0,0) == True
    assert colision(7,3,2) == False
    assert colision(5,10,7) == True
    assert colision(10,5,7) == True