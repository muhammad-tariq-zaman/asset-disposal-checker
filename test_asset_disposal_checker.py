import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import check


def row(s, m, cert="yes"):
    return {"asset": "a", "sensitivity": s, "wipe_method": m, "certificate": cert}


class TestDisposal(unittest.TestCase):
    def test_high_destroy_ok(self):
        self.assertEqual(check(row("high", "destroy"))[0], "COMPLIANT")

    def test_high_wipe_is_gap(self):
        self.assertEqual(check(row("high", "wipe-3pass"))[0], "GAP")

    def test_missing_certificate_is_gap(self):
        self.assertEqual(check(row("low", "wipe-1pass", "no"))[0], "GAP")

    def test_medium_3pass_ok(self):
        self.assertEqual(check(row("medium", "wipe-3pass"))[0], "COMPLIANT")
