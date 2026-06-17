# 速算对决 / Math Duel

一个使用 Python 标准库实现的控制台速算游戏。玩家需要连续解答算术题，支持提示、跳过、中英双语、难度设置、音效、音量、排行榜和自动化测试。

A pure Python standard-library console arithmetic game. Solve a sequence of math problems with optional hints and skips. Includes bilingual zh/en UI, difficulty settings, terminal sound, volume control, score history, and automated tests.

## 功能 / Features

- 纯 Python 标准库，无第三方依赖 / Pure Python stdlib, no third-party dependencies
- 加、减、乘、整除题目 / Addition, subtraction, multiplication, exact integer division
- 中英双语界面，可在设置中切换 / Bilingual zh/en UI with language toggle
- 三档难度：easy / normal / hard / Three difficulty levels
- `hint` 提供答案奇偶和大小提示，得分减半 / `hint` gives parity and size clue with half points
- `skip` 跳过当前题 / `skip` gives up the current problem
- 连对加分 / Streak bonus scoring
- JSON 持久化设置和排行榜 / JSON-persistent settings and top scores
- 终端铃声音效，音量 0-3 / Terminal bell sound with volume 0-3
- 自动化测试覆盖核心逻辑、菜单、设置、音效和分数 / Automated tests for core logic, menus, settings, sound, and scores

## 快速开始 / Quick start

```bash
cd ~/games/math-duel
python3 game.py
```

## 操作 / Controls

主菜单 / Main menu:

| 输入 / Input | 作用 / Action |
|---|---|
| `p` | 开始游戏 / play |
| `h` | 查看帮助 / help |
| `s` | 设置语言、音效、音量、难度 / settings |
| `c` | 查看排行榜 / scores |
| `q` | 退出 / quit |

游戏中 / During a round:

| 输入 / Input | 作用 / Action |
|---|---|
| 整数 / integer | 提交答案 / submit answer |
| `hint` | 查看提示并让本题得分减半 / show clue and halve points |
| `skip` | 跳过本题 / skip current problem |
| `q` | 退出本轮 / quit round |

## 难度与计分 / Difficulty and scoring

| 难度 / Difficulty | 题数 / Rounds | 数字范围 / Max number | 运算 / Ops | 基础分 / Base |
|---|---:|---:|---|---:|
| easy | 8 | 20 | `+ -` | 10 |
| normal | 10 | 50 | `+ - *` | 15 |
| hard | 12 | 99 | `+ - * /` | 25 |

正确得分 / Correct answer points:

```text
base + (streak - 1) * 5
```

如果使用提示，本题得分减半。
If a hint is used, points for that problem are halved.

比赛评级 / Result rating:

- 正确率 >= 75%：胜利 / win
- 正确率 >= 50%：平局 / draw
- 否则：失败 / loss

## 测试 / Tests

```bash
cd ~/games/math-duel
python3 -m py_compile game.py math_duel.py i18n.py settings.py score.py sound.py
python3 tests/run_tests.py
```

当前测试数量 / Current test count: 59.

## 文件结构 / Project layout

```text
math-duel/
├── game.py          # 主菜单与交互流程 / menus and gameplay
├── math_duel.py     # 核心题目与计分逻辑 / core problem and scoring logic
├── i18n.py          # 中英文本 / bilingual strings
├── settings.py      # 设置保存 / settings persistence
├── score.py         # 排行榜 / scoreboard
├── sound.py         # 终端音效 / terminal sound
└── tests/
    ├── test_core.py
    ├── test_game.py
    ├── test_modules.py
    └── run_tests.py
```
