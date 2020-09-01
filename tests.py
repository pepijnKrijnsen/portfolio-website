import unittest
import datetime
import main

class tests(unittest.TestCase):
    
#    def testOne(self):
#        self.assertEqual(main.core.storeNewBofr("new_title", "new_body"), {"title": "new_title", "body": "new_body",})

    def testPassingVariablesWorks(self):
        nt = "A bug is eating me!"
        nb = "Please send help"
        dt = datetime.datetime.now()
        fd = dt.strftime("%Y%m%d")
        self.assertEqual(main.core.storeNewBofr(nt, nb), {"title": nt, "body": nb, "stamp": fd,})


if __name__ == "__main__":
    unittest.main()
