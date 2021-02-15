#!/usr/bin/env python
# coding: utf-8

# In[3]:


import unittest2
import func

class TestClass(unittest2.TestCase):

    def test_add(self):
        result = func.add(10, 5)
        self.assertEqual(result, 15)
        self.assertEqual(func.add(10, 1), 11)

    def test_subtract(self):
        result = func.subtract(10, 5)
        self.assertEqual(result, 5)

    def test_divide(self):
        self.assertEqual(func.divide(10, 2), 5)

        with self.assertRaises(ValueError):
            func.divide(10, 0)
    def test_multiply(self):
        self.assertEqual(func.multiply(12, -3), -36)

if __name__ == "__main__":
    unittest2.main()


# In[ ]:




