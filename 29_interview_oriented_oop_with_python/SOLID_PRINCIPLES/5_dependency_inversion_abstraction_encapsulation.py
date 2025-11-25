'''
Dependency Inversion Principle (DIP) - Higher order classes/entities should
not be dependent upon lower order classes.

Following also highlights, Encapsulation & Abstraction.
'''

from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass


class MySQLDB(Database):
    def save(self, data):
        print(f'saving data {data} in MySQL')


class UserService:
    def __init__(self, db: Database):
        self.db = db

    def save_user(self, user):
        self.db.save(user)


service = UserService(MySQLDB())
service.save_user('shadabsk')
