"""列宿（LIESU）算子单测：名帖完整、行为达标、只增不覆盖。"""
import unittest

from liesu import Liesu


class TestLiesu(unittest.TestCase):
    def setUp(self):
        self.op = Liesu()

    def test_describe(self):
        d = self.op.describe()
        self.assertEqual(d["repo"], "liesu")
        self.assertEqual(d["code"], "LIESU")
        self.assertTrue(d["anchor"].startswith("Ω₀⊂⊙∞⊂Ω"))
        self.assertTrue(d["mingwen"])

    def test_allocate(self):
        op = Liesu(config={"capacity": 1})
        slot = op.allocate("任务一")
        self.assertTrue(slot.startswith("XC-"))
        with self.assertRaises(RuntimeError):
            op.allocate("任务二")

    def test_report_capacity(self):
        cap = self.op.report_capacity()
        self.assertEqual(cap, {"total": 4, "used": 0, "free": 4})


if __name__ == "__main__":
    unittest.main()
