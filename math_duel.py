"""Core logic for Math Duel."""
import operator
import random

DIFFICULTY_CONFIG = {
    "easy": {"rounds": 8, "max_num": 20, "ops": ("+", "-"), "base": 10},
    "normal": {"rounds": 10, "max_num": 50, "ops": ("+", "-", "*"), "base": 15},
    "hard": {"rounds": 12, "max_num": 99, "ops": ("+", "-", "*", "/"), "base": 25},
}
OPS = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv}


def config(difficulty):
    return DIFFICULTY_CONFIG.get(difficulty, DIFFICULTY_CONFIG["normal"])


def make_problem(difficulty, rng=None):
    rng = rng or random
    cfg = config(difficulty)
    op = rng.choice(cfg["ops"])
    if op == "/":
        answer = rng.randint(2, cfg["max_num"] // 2)
        b = rng.randint(2, 12)
        a = answer * b
    else:
        a = rng.randint(1, cfg["max_num"])
        b = rng.randint(1, cfg["max_num"])
        if op == "-" and b > a:
            a, b = b, a
        answer = OPS[op](a, b)
    return {"a": a, "b": b, "op": op, "answer": answer}


def format_problem(problem):
    return f"{problem['a']} {problem['op']} {problem['b']} = ?"


def parse_answer(text):
    try:
        return int(text.strip())
    except ValueError:
        return None


def is_correct(problem, answer_text):
    return parse_answer(answer_text) == problem["answer"]


def points_for(difficulty, streak, used_hint=False):
    base = config(difficulty)["base"]
    points = base + max(0, streak - 1) * 5
    if used_hint:
        points //= 2
    return max(1, points)


def hint_for(problem):
    ans = problem["answer"]
    if ans % 2 == 0:
        parity = "even"
    else:
        parity = "odd"
    if ans < 10:
        size = "small"
    elif ans < 50:
        size = "medium"
    else:
        size = "large"
    return parity, size


def final_rating(correct, rounds):
    if rounds <= 0:
        return "loss"
    ratio = correct / rounds
    if ratio >= 0.75:
        return "win"
    if ratio >= 0.5:
        return "draw"
    return "loss"
