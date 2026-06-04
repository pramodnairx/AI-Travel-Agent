"""Unit tests for the Travel Agent"""

import pytest
from src.travel_agent import TravelAgent


class TestTravelAgent:
    """Test suite for TravelAgent class."""

    @pytest.fixture
    def agent(self):
        """Create a TravelAgent instance for testing."""
        return TravelAgent()

    def test_travel_agent_initialization(self, agent):
        """Test TravelAgent initializes correctly."""
        assert agent is not None
        assert agent.destinations == []
        assert agent.itineraries == []

    def test_get_destination_recommendations(self, agent):
        """Test getting destination recommendations."""
        recommendations = agent.get_destination_recommendations()
        assert isinstance(recommendations, list)

    def test_plan_itinerary(self, agent):
        """Test itinerary planning."""
        itinerary = agent.plan_itinerary("Paris", 5)
        assert isinstance(itinerary, dict)

    def test_get_travel_cost(self, agent):
        """Test travel cost estimation."""
        cost = agent.get_travel_cost("Paris", 5)
        assert isinstance(cost, dict)
