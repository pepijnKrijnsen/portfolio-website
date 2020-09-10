import unittest
import datetime
import main
import random

class tests(unittest.TestCase):
    

#    def testPassingVariablesWorks(self):
#        nt = "A bug is eating me!"
#        nb = "Please send help"
#        dt = datetime.datetime.now()
#        fd = dt.strftime("%Y%m%d")
#        self.assertEqual(main.core.storeNewBofr(nt, nb), {"title": nt, "body": nb, "stamp": fd,})

    def testPresenterReceivesNewTicketData(self):
        json_data = {"title": "nt", "body": "nb",}
        for i in range(80):
            main.presenter.newTicket(json_data)
        f = open("lib/UIDs.csv")
        UIDs = f.read()
        print(UIDs)
        f.close()

if __name__ == "__main__":
    unittest.main()
