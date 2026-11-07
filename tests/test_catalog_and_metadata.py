"""Quick offline smoke tests: python -m unittest discover -s tests -v"""
import unittest
from pathlib import Path
from unittest.mock import patch

from catalog import parse_projects, search_projects
from metadata import project_metadata


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

    def test_invalid_metadata_repo(self):
        self.assertIn('error', project_metadata('https://example.org/repo'))

    @patch('metadata.github_metadata')
    def test_github_link_parses(self, mock_metadata):
        mock_metadata.return_value = {'language': 'Python'}
        self.assertEqual(project_metadata('https://github.com/numpy/numpy')['language'], 'Python')
        mock_metadata.assert_called_once_with('numpy', 'numpy')


if __name__ == '__main__':
    unittest.main()
