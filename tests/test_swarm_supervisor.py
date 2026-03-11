import unittest

from ai_os.swarm_supervisor import _is_idle, _is_rate_limited, _next_backoff


class SwarmSupervisorTests(unittest.TestCase):
    def test_rate_limit_detection_matches_common_codex_and_http_patterns(self) -> None:
        self.assertTrue(_is_rate_limited("429 Too Many Requests"))
        self.assertTrue(_is_rate_limited("Rate limit hit, try again later"))
        self.assertFalse(_is_rate_limited("Heartbeat completed successfully"))

    def test_idle_detection_matches_clean_exit_language(self) -> None:
        self.assertTrue(_is_idle("No assigned issues were found, exit cleanly."))
        self.assertFalse(_is_idle("Implemented the requested change."))

    def test_backoff_schedule_caps_after_one_hour(self) -> None:
        self.assertEqual(_next_backoff(1), 300)
        self.assertEqual(_next_backoff(2), 900)
        self.assertEqual(_next_backoff(3), 1800)
        self.assertEqual(_next_backoff(4), 3600)
        self.assertEqual(_next_backoff(8), 3600)


if __name__ == "__main__":
    unittest.main()
