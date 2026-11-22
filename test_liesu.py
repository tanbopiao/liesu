"""列宿（LIESU）算子骨架单测：名帖完整、桩位齐整、只增不覆盖。"""
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

    def test_allocate_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.allocate(None)

    def test_report_capacity_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.report_capacity()


if __name__ == "__main__":
    unittest.main()
