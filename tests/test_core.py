"""Tests for Math Duel core."""
import os
import random
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import math_duel as core


class TestProblem(unittest.TestCase):
    def test_config_default(self):
        self.assertEqual(core.config("bad"), core.config("normal"))

    def test_make_problem_has_answer(self):
        problem = core.make_problem("easy", random.Random(0))
        self.assertIn("answer", problem)
        self.assertEqual(problem["answer"], core.OPS[problem["op"]](problem["a"], problem["b"]))

    def test_make_subtraction_non_negative(self):
        for seed in range(50):
            p = core.make_problem("easy", random.Random(seed))
            self.assertGreaterEqual(p["answer"], 0)

    def test_make_division_exact(self):
        seen = False
        for seed in range(100):
            p = core.make_problem("hard", random.Random(seed))
            if p["op"] == "/":
                seen = True
                self.assertEqual(p["a"] // p["b"], p["answer"])
                self.assertEqual(p["a"] % p["b"], 0)
        self.assertTrue(seen)

    def test_format_problem(self):
        self.assertEqual(core.format_problem({"a": 2, "op": "+", "b": 3}), "2 + 3 = ?")


class TestAnswers(unittest.TestCase):
    def test_parse_answer(self):
        self.assertEqual(core.parse_answer(" 42 "), 42)
        self.assertEqual(core.parse_answer("-5"), -5)

    def test_parse_invalid(self):
        self.assertIsNone(core.parse_answer("x"))

    def test_is_correct(self):
        p = {"answer": 7}
        self.assertTrue(core.is_correct(p, "7"))
        self.assertFalse(core.is_correct(p, "8"))


class TestScoring(unittest.TestCase):
    def test_points_easy(self):
        self.assertEqual(core.points_for("easy", 1), 10)
        self.assertEqual(core.points_for("easy", 3), 20)

    def test_points_hint_halves(self):
        self.assertEqual(core.points_for("easy", 2, True), 7)

    def test_points_unknown(self):
        self.assertEqual(core.points_for("bad", 1), 15)

    def test_hint_even_small(self):
        self.assertEqual(core.hint_for({"answer": 8}), ("even", "small"))

    def test_hint_odd_medium(self):
        self.assertEqual(core.hint_for({"answer": 15}), ("odd", "medium"))

    def test_hint_large(self):
        self.assertEqual(core.hint_for({"answer": 50}), ("even", "large"))

    def test_final_rating_win(self):
        self.assertEqual(core.final_rating(8, 10), "win")

    def test_final_rating_draw(self):
        self.assertEqual(core.final_rating(5, 10), "draw")

    def test_final_rating_loss(self):
        self.assertEqual(core.final_rating(4, 10), "loss")

    def test_final_rating_zero(self):
        self.assertEqual(core.final_rating(0, 0), "loss")


if __name__ == "__main__":
    unittest.main()
