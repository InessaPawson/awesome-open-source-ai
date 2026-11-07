"""Offline tests for Landscape mapping, counts, and Plotly graph construction."""
import unittest

from catalog import Project
from landscape import build_landscape, category_counts, landscape_nodes


class LandscapeTests(unittest.TestCase):
    def setUp(self):
        self.projects = [
            Project("Same Name", "https://github.com/example/one", "First", "Area", "A", "Listed"),
            Project("Same Name", "https://github.com/example/two", "Second", "Area", "B", "Listed"),
            Project("Third", "https://github.com/example/three", "Third", "Area", "B", "Listed"),
            Project("Other", "https://github.com/example/four", "Other", "Other Area", "A", "Listed"),
        ]

    def test_counts_only_selected_area(self):
        nodes, edges = landscape_nodes(self.projects, "Area")
        self.assertEqual(len(nodes), 1 + 2 + 3)
        self.assertEqual(len(edges), 2 + 3)
        self.assertEqual(category_counts(self.projects[:3]), {"A": 1, "B": 2})
        self.assertTrue(all("four" not in node["id"] for node in nodes))

    def test_duplicate_names_use_distinct_repository_urls(self):
        nodes, edges = landscape_nodes(self.projects, "Area")
        self.assertEqual(len({node["id"] for node in nodes}), len(nodes))
        self.assertIn(("category:Area:A", "project:https://github.com/example/one"), edges)
        self.assertIn(("category:Area:B", "project:https://github.com/example/two"), edges)
        self.assertNotIn(("category:Area:A", "project:https://github.com/example/two"), edges)

    def test_plot_renders_with_highlight(self):
        fig = build_landscape(self.projects, "Area", "B")
        self.assertGreater(len(fig.data), 0)
        project_traces = [trace for trace in fig.data if trace.name == "Project"]
        self.assertEqual(len(project_traces), 1)
        self.assertEqual(len(project_traces[0].customdata), 3)


if __name__ == "__main__":
    unittest.main()
