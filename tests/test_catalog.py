"""Quick offline smoke tests: python -m unittest discover -s tests -v"""
import unittest
from pathlib import Path

from catalog import parse_projects, search_projects


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        text = Path(__file__).resolve().parents[1].joinpath('README.snapshot.md').read_text()
        cls.projects = parse_projects(text)

    def test_catalog_parses(self):
        self.assertGreater(len(self.projects), 50)
        self.assertGreater(len(set(p.area for p in self.projects)), 3)

    def test_search(self):
        results = search_projects(self.projects, 'agent')
        self.assertGreater(len(results), 0)
        self.assertTrue(all('agent' in f'{p.name} {p.description} {p.area} {p.category}'.lower() for p in results))


if __name__ == '__main__':
    unittest.main()
