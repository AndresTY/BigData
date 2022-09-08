import unittest
import function


class MyTestCase(unittest.TestCase):
    def test_function(self):
        self.assertEqual(function.data_to_csv("""[\n  [\n    \"1662123624000\",\n    \"4450\"\n  ],\n  [\n    \"1662141599000\",\n    \"4466.5743\"\n  ]\n]\n"""),"1662123624000\t4450\n1662141599000\t4466.5743\n")  # add assertion here
        self.assertEqual(function.data_to_csv("""[[12,8],[12,88]]"""),"12\t8\n12\t88\n")
        self.assertEqual(function.data_to_csv("""[[8,1],[1,8],[199,456]]"""),"8\t1\n1\t8\n199\t456\n")

if __name__ == '__main__':
    unittest.main()
