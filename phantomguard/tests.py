"""Fast smoke tests for deterministic parts; no AWS/Decider network needed."""
import unittest
from unittest.mock import patch

from engine import decide_action


class DecisionGateTests(unittest.TestCase):
    def test_hard_stop_wins_over_low_model_score(self):
        with patch("engine.call_decider", return_value={"violation_probability": 0.01, "latency_ms": 100, "source": "strands-decider-2b", "source_detail": "test"}):
            result = decide_action({"user_request": "search", "proposed_tool": "search_documentation", "arguments": {}, "environment": "sandbox", "impact": "low", "argument_provenance": "Directly grounded in user request", "scenario_flags": ["credential_exfiltration"]})
        self.assertEqual(result["decision"], "BLOCK")

    def test_uncertain_signal_routes_to_review(self):
        with patch("engine.call_decider", return_value={"violation_probability": 0.52, "latency_ms": 100, "source": "strands-decider-2b", "source_detail": "test"}):
            result = decide_action({"user_request": "do a task", "proposed_tool": "search_documentation", "arguments": {}, "environment": "sandbox", "impact": "low", "argument_provenance": "Directly grounded in user request", "scenario_flags": []})
        self.assertEqual(result["decision"], "REVIEW")

    def test_low_risk_grounded_sandbox_can_allow(self):
        with patch("engine.call_decider", return_value={"violation_probability": 0.08, "latency_ms": 100, "source": "strands-decider-2b", "source_detail": "test"}):
            result = decide_action({"user_request": "find docs", "proposed_tool": "search_documentation", "arguments": {"query": "S3 lifecycle"}, "environment": "read-only sandbox", "impact": "low", "argument_provenance": "Directly grounded in user request", "scenario_flags": []})
        self.assertEqual(result["decision"], "ALLOW")


if __name__ == "__main__":
    unittest.main()
