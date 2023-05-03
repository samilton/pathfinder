from __future__ import annotations

from mypy.test.helpers import Suite, assert_equal

from pathfinder.ai.openai import OpenAI


class OpenAiSuite(Suite):
    def setUp(self) -> None:
        self.ai = OpenAI()

    def test_configure(self) -> None:
        configuration = self.ai.configure("abc")
        assert_equal("abc", configuration)
