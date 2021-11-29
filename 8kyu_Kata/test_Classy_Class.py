import unittest as test

test.describe("Basic tests")
names=["john","matt","alex","cam"]
ages=[16,25,57,39]
for i in range(4):
    name,age=names[i],ages[i]
    person=Person(name,age)
    test.it("Testing for %s and %s" %(repr(name),age))
    test.assert_equals(person.info, name+"s age is "+str(age))












