import json
import tempfile
import unittest
from pathlib import Path

from ai_os.strategy_lab import load_forecast_request, persist_mock_forecast


EXAMPLE_FORECAST = Path(__file__).resolve().parents[1] / "examples/forecast_request.yaml"


class StrategyLabTests(unittest.TestCase):
    def test_mock_forecast_persists_request_and_report(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            request = load_forecast_request(EXAMPLE_FORECAST)

            report_path = persist_mock_forecast(request, repo_root)

            request_path = repo_root / "ops/strategy_lab/requests/q2-growth-forecast.json"
            self.assertTrue(request_path.exists())
            report = json.loads(Path(report_path).read_text(encoding="utf-8"))
            self.assertEqual(report["request_id"], "q2-growth-forecast")
            self.assertIn("staged rollout", report["scenario_summary"])


if __name__ == "__main__":
    unittest.main()
