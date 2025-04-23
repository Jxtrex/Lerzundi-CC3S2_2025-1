import unittest

class Username:
    def __init__(self, name):
        self.name = name

    def as_lowercase(self):
        return self.name.lower()

class TestUsername(unittest.TestCase):
    
    def test_converts_to_lowercase(self):
        # Arrange
        username = Username("SirJakington35179")
        
        # Act
        actual = username.as_lowercase()
        
        # Assert
        self.assertEqual(actual, "sirjakington35179")

if __name__ == "__main__":
    unittest.main()