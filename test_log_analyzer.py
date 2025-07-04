import unittest

from log_analyzer import LogEntry

class TestMonsterTown(unittest.TestCase):

    def setUp(self):

        self.e1 = LogEntry("2001-12-01 00:18:38 UTC","223.248.203.131","20","FTP - Data","Allow","186","223.57.223.121","US","United States")
        self.e2 = LogEntry("2022-04-01 04:32:51 UTC","0.133.38.22","21","FTP - Control","Allow","92","0.213.122.173", "US","United States")
    def testLogEntryInitializer(self):
        self.assertEqual(self.e1.event_time.year, 2001)
        self.assertEqual(self.e1.event_time.month, 12)
        self.assertEqual(self.e2.event_time.year, 2022)
        self.assertEqual(self.e2.event_time.day, 1)
        
    def testipv4_class(self):
        self.assertEqual(self.e1.ipv4_class, "C")
       
if __name__ == '__main__':
    unittest.main()