from assignment import Vehicle, Animal, Plant, Tree

# Test Vehicle class
def test_vehicle():
    v = Vehicle()
    assert v.name == 'Ferrari'
    assert v.speed == 200
    assert v.mileage == 10000
    v.change_speed(220)
    assert v.speed == 220
    assert v.get_speed() == 220

# Test Animal class
def test_animal():
    a = Animal()
    assert a.name == 'Lion'
    assert a.age == 10
    assert a.species == 'Carnivore'
    a.change_age(11)
    assert a.age == 11
    assert a.get_age() == 11

# Test Plant class
def test_plant():
    p = Plant()
    assert p.name == 'Rose'
    assert p.height == 1
    assert p.species == 'Flower'
    p.change_height(1.5)
    assert p.height == 1.5
    assert p.get_height() == 1.5

# Test Tree class (Inheritance)
def test_inheritance():
    t = Tree()
    assert t.name == 'Oak'
    assert t.height == 20
    assert t.species == 'Tree'
    assert t.age == 100
    t.change_height(22)
    assert t.height == 22
    assert t.get_height() == 22
    t.change_age(101)
    assert t.age == 101
    assert t.get_age() == 101
