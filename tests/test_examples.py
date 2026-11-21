"""Regression checks for the runnable portfolio examples."""
import importlib.util
import math
from pathlib import Path
import sqlite3
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


def example(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'examples' / f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class DrawdownTests(unittest.TestCase):
    def test_known_line_and_generator(self):
        points = ((t, 3000 - 40 * math.log10(t)) for t in (1, 2, 5, 10))
        slope, intercept = example('drawdown').fit(points)
        self.assertAlmostEqual(slope, -40)
        self.assertAlmostEqual(intercept, 3000)

    def test_rejects_invalid_measurements(self):
        fit = example('drawdown').fit
        for points in ([], [(1, 2)], [(1, 2), (1, 3)], [(0, 2), (1, 3)],
                       [(math.nan, 2), (1, 3)], [(1, math.inf), (2, 3)],
                       [(1, 2), (2, math.nan)]):
            with self.subTest(points=points), self.assertRaises(ValueError):
                fit(points)


class ExampleContracts(unittest.TestCase):
    def test_contrast_command_exit_codes(self):
        for fg, bg, code, output in [('000000', 'FFFFFF', 0, '21.00:1'),
                                     ('777777', 'FFFFFF', 1, '4.48:1'),
                                     ('bad-color', 'FFFFFF', 2, '')]:
            with self.subTest(fg=fg):
                result = subprocess.run([sys.executable, str(ROOT / 'examples/contrast.py'), fg, bg],
                                        capture_output=True, text=True)
                self.assertEqual(result.returncode, code)
                self.assertEqual(result.stdout.strip(), output)

    def test_provider_failure_preserves_other_sections(self):
        module = example('briefing')
        result = module.briefing({'Weather': module.offline_weather, 'Inbox': lambda: '3 unread'})
        self.assertEqual(result, 'Weather: Temporarily unavailable\nInbox: 3 unread')

    def test_sql_examples(self):
        with sqlite3.connect(':memory:') as db:
            db.executescript((ROOT / 'examples/attendance.sql').read_text())
            self.assertEqual(db.execute('SELECT COUNT(*) FROM attendance').fetchone()[0], 3)
            self.assertEqual(db.execute('SELECT COUNT(DISTINCT member_id) FROM attendance').fetchone()[0], 2)
        with sqlite3.connect(':memory:') as db:
            db.executescript((ROOT / 'examples/handoffs.sql').read_text())
            self.assertEqual(db.execute("SELECT next_step FROM handoff WHERE project = 'demo' ORDER BY id DESC LIMIT 1").fetchone()[0], 'Add semester reach to the report.')
        with sqlite3.connect(':memory:') as db:
            statements = (ROOT / 'examples/agenda.sql').read_text().strip().rstrip(';').rsplit(';', 1)
            db.executescript(statements[0])
            self.assertEqual(db.execute(statements[1]).fetchall(),
                             [('Submit abstract', 'todo'), ('Prepare field notes', 'doing')])


if __name__ == '__main__':
    unittest.main()
