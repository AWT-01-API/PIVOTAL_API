from unittest import TestCase
from src.util.ReadCfg import ReadCfg


class TestReadCfg(TestCase):
    def test_get_value(self):
        self.assertEqual("hapsneeze", ReadCfg.get_value("user1"))

    def test_get_and_not_found(self):
        with self.assertRaises(Exception) as context:
            ReadCfg.get_value("NotOncfg.ini")
        self.assertTrue('NotOncfg.ini not found on cfg.ini' in context.exception)
