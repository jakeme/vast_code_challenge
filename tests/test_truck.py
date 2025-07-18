import pytest

from statemachine.exceptions import TransitionNotAllowed

from mining_sim.constants import MINING_TIME_MAXIMUM, DRIVING_TIME


def test_truck_states(mining_clock, mining_truck):
    assert mining_truck.mining.is_active

    mining_clock.increment_time()
    with pytest.raises(TransitionNotAllowed):
        mining_truck.cycle()

    assert mining_truck.mining.is_active
    # Move clock time forward to allow state to transition
    # Can use class variables here (less toil if the variables change) or type "300 minutes" directly (catch accidental change)
    mining_clock._time += MINING_TIME_MAXIMUM

    mining_truck.cycle()
    assert mining_truck.driving_to_unload.is_active

    mining_clock._time += DRIVING_TIME - 1
    with pytest.raises(TransitionNotAllowed):
        mining_truck.start_unloading()
    assert mining_truck.driving_to_unload.is_active

    mining_clock._time += 1
    mining_truck.start_unloading()
    assert mining_truck.unloading.is_active

    # Could test the rest of the loop...


def test_truck_queues():
    # Same test as above but using the waiting_to_unload state
    ...
