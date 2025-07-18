from mining_sim.main import mining_sim
from mining_sim.constants import UNLOADING_TIME


def test_simulation(mocker):
    """Test a very basic scenario where two trucks hit the one unloading site at the same time"""
    # Speed up the simulation
    mocker.patch("mining_sim.truck.MINING_TIME_MINIMUM", 0)
    mocker.patch("mining_sim.truck.MINING_TIME_MAXIMUM", 1)
    mocker.patch("mining_sim.truck.DRIVING_TIME", 1)

    # Simulate just long enough for both trucks to start unloading
    truck_result_list, unload_station_queue = mining_sim(2, 1, 4)

    assert truck_result_list[0].waiting_time == 0
    assert truck_result_list[1].waiting_time == UNLOADING_TIME
    assert (
        unload_station_queue.dwell_time_list[0] >= 2
    )  # It's a little random due to the random mining time - could mock/patch this randomness out during testing


def test_simulation_queueing(mocker):
    # A good thing to test is the most tenuous relationship in my code:
    # That the amount of trucks in the "unloading" state is always equal to
    # the sum of sum([len(x) for x in unload_stations_list]) in the queue manager
    ...
