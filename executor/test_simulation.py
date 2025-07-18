import pytest
import logging

from statistics import mean

from mining_sim.main import mining_sim

logger = logging.getLogger()
SIMULATION_TIME = 72 * 60  # 72 hours in minutes


@pytest.mark.parametrize(
    "num_trucks, num_unload_stations", [(10, 1), (50, 1), (50, 2), (100, 5)]
)
def test_mining_sim(num_trucks, num_unload_stations):
    truck_list, unload_station_queue = mining_sim(
        num_trucks, num_unload_stations, SIMULATION_TIME
    )

    logger.info(f"Simulation with {num_trucks=} and {num_unload_stations=} :")
    for truck in truck_list:
        delay_pct = truck.waiting_time / SIMULATION_TIME * 100.0
        logger.info(f"\tTruck {truck.name} delayed {delay_pct:.1f}% of the time")
    for i in range(len(unload_station_queue.dwell_time_list)):
        delay_pct = unload_station_queue.dwell_time_list[i] / SIMULATION_TIME * 100.0
        logger.info(f"\tUnload Station {i} had a queue {delay_pct:.1f}% of the time")
    mean_truck_delay = mean([x.waiting_time for x in truck_list])
    logger.info(
        f"Average truck delay: {mean_truck_delay} minutes (out of sim time {SIMULATION_TIME} mins)"
    )
