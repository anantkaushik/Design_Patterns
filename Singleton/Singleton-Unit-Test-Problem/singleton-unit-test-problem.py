import unittest
import os

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        self.population = {}

        f = open(os.path.join(os.getcwd(), 'capitals.txt'), 'r')
        lines = f.readlines()
        for i in range(0, len(lines), 2):
            self.population[lines[i].strip()] = int(lines[i + 1].strip())
        f.close()


class SingletonRecordFinder:
    def total_population(self, cities):
        result = 0
        for c in cities:
            result += Database().population[c]
        return result


class SingletonTests(unittest.TestCase):
    def test_is_singleton(self):
        db = Database()
        db2 = Database()
        self.assertEqual(db, db2)

    def test_singleton_total_population(self):
        """ This tests on a live database :( """
        rf = SingletonRecordFinder()
        names = ['Seoul', 'Mexico City']
        tp = rf.total_population(names)
        self.assertEqual(tp, 17500000 + 17400000)  # what if these change?


if __name__ == '__main__':
    unittest.main()