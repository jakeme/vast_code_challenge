from mining_sim.constants import UNLOADING_TIME

"""
These tests could be parametrized, although at this scale I think it sacrifices readability for not much benefit

Longer tests (that go through the simulation state several times) are a coverage gap here
"""


def test_queue_one_station_one_truck(mining_clock, unload_queue_one_station):
    exit_time, wait_time = unload_queue_one_station.add_to_queue()
    assert exit_time == mining_clock.time + UNLOADING_TIME
    assert wait_time == 0  # No wait time, only one truck

    for i in range(UNLOADING_TIME):
        mining_clock.increment_time()
        unload_queue_one_station.clean_up_queue()

    exit_time, wait_time = unload_queue_one_station.add_to_queue()
    assert exit_time == mining_clock.time + UNLOADING_TIME
    assert wait_time == 0
    assert unload_queue_one_station.dwell_time_list[0] == 0


def test_queue_one_station_two_trucks(mining_clock, unload_queue_one_station):
    exit_time, wait_time = unload_queue_one_station.add_to_queue()
    assert exit_time == mining_clock.time + UNLOADING_TIME
    assert wait_time == 0  # No wait time, only one truck

    exit_time, wait_time = unload_queue_one_station.add_to_queue()
    assert exit_time == mining_clock.time + (2 * UNLOADING_TIME)
    assert wait_time == UNLOADING_TIME


def test_queue_two_stations(mining_clock, unload_queue_two_stations):
    exit_time, wait_time = unload_queue_two_stations.add_to_queue()
    assert exit_time == mining_clock.time + UNLOADING_TIME
    assert wait_time == 0

    exit_time, wait_time = unload_queue_two_stations.add_to_queue()
    assert exit_time == mining_clock.time + UNLOADING_TIME
    assert wait_time == 0

    exit_time, wait_time = unload_queue_two_stations.add_to_queue()
    assert exit_time == mining_clock.time + (2 * UNLOADING_TIME)
    assert wait_time == UNLOADING_TIME


def test_queue_one_station_three_trucks(mining_clock, unload_queue_one_station):
    exit_time, wait_time = unload_queue_one_station.add_to_queue()
    assert exit_time == mining_clock.time + UNLOADING_TIME
    assert wait_time == 0  # No wait time, only one truck

    exit_time, wait_time = unload_queue_one_station.add_to_queue()
    assert exit_time == mining_clock.time + (2 * UNLOADING_TIME)
    assert wait_time == UNLOADING_TIME

    exit_time, wait_time = unload_queue_one_station.add_to_queue()
    assert exit_time == mining_clock.time + (3 * UNLOADING_TIME)
    assert wait_time == 2 * UNLOADING_TIME
