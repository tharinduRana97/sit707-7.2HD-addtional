import unittest

# Mock definitions for demonstration
class MockCustomer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class App:
    def __init__(self, database):
        if 'complex' in database:
            self.customers = [MockCustomer("バナナ", "10 Red Road, Akihabara, Tokyo") for _ in range(9999)]
            self.customers.append(MockCustomer("バナナ", "10 Red Road, Akihabara, Tokyo"))
        else:
            self.customers = [MockCustomer("Org XYZ", "10 Red Road, Reading") for _ in range(100)]

    def get_customer(self, id):
        return self.customers[id]

# Test suite
class TestBasic(unittest.TestCase):
    def setUp(self):
        self.app = App(database='fixtures/test_basic.json')

    def test_customer_count(self):
        self.assertEqual(len(self.app.customers), 100)

    def test_existence_of_customer(self):
        customer = self.app.get_customer(id=10)
        self.assertEqual(customer.name, "Org XYZ")
        self.assertEqual(customer.address, "10 Red Road, Reading")

class TestComplexData(unittest.TestCase):
    def setUp(self):
        self.app = App(database='fixtures/test_complex.json')

    def test_customer_count(self):
        self.assertEqual(len(self.app.customers), 10000)

    def test_existence_of_customer(self):
        customer = self.app.get_customer(id=9999)
        self.assertEqual(customer.name, "バナナ")
        self.assertEqual(customer.address, "10 Red Road, Akihabara, Tokyo")

if __name__ == '__main__':
    unittest.main()
