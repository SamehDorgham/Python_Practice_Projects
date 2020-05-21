
class person:
    def Say_Hello(self):
        print('hello to python')

p = person()
p.Say_Hello()

# -----------------------------------------

class person1:
    def Person_Info(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
        print('i am {} and i`m {} years old and i work as {} developer'.format(name,age,job))

A = person1()
A.Person_Info('Sameh Dorgham',43,'Python')


class calc():

    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        return self.n1 + self.n2
    
    def mult(self):
        return self.n1 * self.n2

    def div(self):
        return self.n1 / self.n2
    
class scientific(calc):
    def power(self):
        return self.n1 ** self.n2

x = scientific(20,10)
print(x.add())
print(x.mult())
print(x.div())
print(x.power())



class animal:
    def __init__(self,name):
        self.name = name
    
class dog(animal):
    def __init__(self,name):
        super(dog, self).__init__(name)
        self.food = 'fish'

d = dog('misho')
print(d.food)
d.food = 'meat'
print(d.food)




