"""Tests for LightCubeEngine."""

import pytest
from app.engine import LightCubeEngine
from app.models import RunMode, RunRequest


class TestLightCubeEngine:
    """Test cases for LightCubeEngine."""

    @pytest.fixture
    def engine(self):
        """Create a LightCubeEngine instance."""
        return LightCubeEngine()

    @pytest.fixture
    def run_request_shape(self):
        """Create a basic shape mode request."""
        return RunRequest(
            project_name="test-project",
            mode=RunMode.SHAPE,
            idea="AI-powered meal planning app for busy professionals",
            context="Mobile first, subscription model",
        )

    @pytest.fixture
    def run_request_audit(self):
        """Create an audit mode request."""
        return RunRequest(
            project_name="test-project",
            mode=RunMode.AUDIT,
            url="https://example.com",
        )

    @pytest.mark.asyncio
    async def test_engine_initialization(self, engine):
        """Test engine initializes with all adapters."""
        assert engine.scrapling is not None
        assert engine.oasis is not None
        assert engine.mirofish is not None
        assert engine.paperclip is not None

    @pytest.mark.asyncio
    async def test_run_shape_mode(self, engine, run_request_shape):
        """Test run with shape mode produces decision pack."""
        pack, export = await engine.run(run_request_shape)

        assert pack is not None
        assert pack.run_id is not None
        assert pack.mode == RunMode.SHAPE
        assert pack.executive_summary is not None
        assert len(pack.signal_brief) > 0
        assert len(pack.problem_map) > 0
        assert len(pack.conditional_validation_stack) == 5
        assert pack.strategy_memo is not None
        assert pack.prd is not None
        assert pack.roadmap is not None
        assert len(pack.tasks) > 0

    @pytest.mark.asyncio
    async def test_run_audit_mode(self, engine, run_request_audit):
        """Test run with audit mode produces decision pack."""
        pack, export = await engine.run(run_request_audit)

        assert pack is not None
        assert pack.mode == RunMode.AUDIT

    @pytest.mark.asyncio
    async def test_decision_pack_has_required_fields(self, engine, run_request_shape):
        """Test decision pack has all required fields."""
        pack, _ = await engine.run(run_request_shape)

        # Check required fields
        assert hasattr(pack, 'run_id')
        assert hasattr(pack, 'mode')
        assert hasattr(pack, 'executive_summary')
        assert hasattr(pack, 'signal_brief')
        assert hasattr(pack, 'problem_map')
        assert hasattr(pack, 'conditional_validation_stack')
        assert hasattr(pack, 'strategy_memo')
        assert hasattr(pack, 'prd')
        assert hasattr(pack, 'roadmap')
        assert hasattr(pack, 'tasks')

    @pytest.mark.asyncio
    async def test_validation_stack_has_five_layers(self, engine, run_request_shape):
        """Test validation stack has exactly 5 layers."""
        pack, _ = await engine.run(run_request_shape)

        assert len(pack.conditional_validation_stack) == 5
        for i, layer in enumerate(pack.conditional_validation_stack, 1):
            assert layer.layer == i

    @pytest.mark.asyncio
    async def test_strategy_memo_has_required_keys(self, engine, run_request_shape):
        """Test strategy memo has required keys."""
        pack, _ = await engine.run(run_request_shape)
        memo = pack.strategy_memo

        assert 'target_user' in memo
        assert 'wedge' in memo
        assert 'core_problem' in memo
        assert 'core_flow' in memo

    @pytest.mark.asyncio
    async def test_prd_has_required_fields(self, engine, run_request_shape):
        """Test PRD has required fields."""
        pack, _ = await engine.run(run_request_shape)
        prd = pack.prd

        # PRD is a dict, check keys
        assert 'title' in prd
        assert 'objective' in prd
        assert 'primary_user' in prd
        assert 'must_have_features' in prd
        assert 'non_goals' in prd
        assert 'success_metrics' in prd
