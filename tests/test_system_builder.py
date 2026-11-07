import unittest

from catalog import parse_projects
from pathlib import Path
from system_builder import RECIPES, architecture, blueprint_json, blueprint_markdown, candidates, defaults


class BuilderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.projects = parse_projects(Path(__file__).resolve().parents[1].joinpath('README.snapshot.md').read_text())

    def test_every_recipe_has_grounded_candidates(self):
        for title, recipe in RECIPES.items():
            with self.subTest(title=title):
                self.assertGreater(len(recipe.stages), 3)
                self.assertTrue(all(candidates(stage, self.projects) for stage in recipe.stages))

    def test_missing_catalog_project_is_not_recommended(self):
        stage = RECIPES['Document Q&A (RAG)'].stages[0]
        self.assertEqual(candidates(stage, []), [])

    def test_blueprints_are_exportable_and_have_gaps(self):
        title = 'Tool-using AI agent'
        plan = architecture(title, self.projects, defaults(RECIPES[title], self.projects), {'goal': 'Workflows', 'deployment': 'Private cloud'})
        self.assertEqual(len(plan['stages']), len(RECIPES[title].stages))
        self.assertIn('Workflows', blueprint_markdown(plan))
        self.assertIn('gaps', blueprint_json(plan))
        self.assertTrue(all(s['repository'].startswith('https://github.com/') for s in plan['stages'] if s['repository']))

    def test_unselected_stage_is_explicit(self):
        title = 'Local private assistant'
        plan = architecture(title, self.projects, {}, {})
        self.assertTrue(all(s['tool'] is None for s in plan['stages']))
        self.assertIn('Needs decision', blueprint_markdown(plan).replace('needs decision', 'Needs decision'))

    def test_reject_unknown_recipe(self):
        with self.assertRaises(ValueError):
            architecture('unknown', self.projects, {}, {})

if __name__ == '__main__':
    unittest.main()
