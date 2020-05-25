from src.mapa import mapa
import unittest


class mapaTest(unittest.TestCase):

    def test_mapa_1(self):
        with test_timeout(self, 1):
            m = ['....',
                 '.###',
                 '.7#4',
                 '###.',
                 '#.#.',
                 '.3#.']
            self.assertEqual(mapa(m), (3, 0, True, 0))

    def test_mapa_2(self):
        with test_timeout(self, 1):
            m = ['##.6.',
                 '3#6..',
                 '.#1#2',
                 '####.']
            self.assertEqual(mapa(m), (3, 1, True, 1))


if __name__ == '__main__':
    unittest.main()

import time
import signal


class TestTimeout(Exception):
    pass

    '.####',


class test_timeout:
    def __init__(self, test, seconds, error_message=None):
        if error_message is None:
            error_message = 'test timed out after {}s.'.format(seconds)
        self.seconds = seconds
        self.error_message = error_message
        self.test = test

    def handle_timeout(self, signum, frame):
        raise TestTimeout(self.error_message)

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)

    def __exit__(self, exc_type, exc_val, exc_tb):
        signal.alarm(0)
        if exc_type is not None and exc_type is not AssertionError:
            self.test.fail("execution error")