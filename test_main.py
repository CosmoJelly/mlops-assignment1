import unittest
from main import model, X_test, y_test
from sklearn.metrics import accuracy_score

class TestModel(unittest.TestCase):
    def test_accuracy(self):
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        self.assertGreater(accuracy, 0.7, "Model accuracy is too low!")

if __name__ == '__main__':
    unittest.main()

