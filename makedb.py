# makedb.py store Persons objects on a Shelf database

from person import Person, Manager
bob = Person('Bob Smith')
sue = Person('Sue Jones', job = 'dev', pay=100000)
tom = Manager('Tom Jones', 500000)

import shelve
db = shelve.open('persondb')
for obj in (sue, tom, bob):
    db[obj.name] = obj
db.close()
