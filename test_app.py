import unittest

import os
import sys
import time
import os.path as op
from functools import partial
from kivy.clock import Clock

from simpleapp import SimpleApp


class Test(unittest.TestCase):

    def pause(*args):
        time.sleep(0.000001)

    # main test function
    def run_test(self, app, *args):
        Clock.schedule_interval(self.pause, 0.000001)

        # Do something
        self.assertEqual(app.text, "Hello World")
        # Comment out if you are editing the test, it'll leave the
        # Window opened.
        app.stop()

    def test_example(self):
        app = SimpleApp()
        p = partial(self.run_test, app)
        Clock.schedule_once(p, 0.000001)
        app.run()


if __name__ == '__main__':
    unittest.main()
