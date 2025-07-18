import logging

from mining_sim import MiningClock, MiningTruck, UnloadStationQueue


def mining_sim(num_trucks, num_unload_stations, sim_time_minutes):
    logger = logging.getLogger("sim")
    logging.basicConfig()

    sim_clock = MiningClock()
    truck_list = [MiningTruck(str(i), sim_clock) for i in range(num_trucks)]
    unload_station_queue = UnloadStationQueue(sim_clock, num_unload_stations)

    for t in range(sim_time_minutes):
        sim_clock.increment_time()
        unload_station_queue.clean_up_queue()
        for truck in truck_list:
            if truck.current_state in (
                MiningTruck.mining,
                MiningTruck.driving_to_mine,
                MiningTruck.unloading,
            ):
                if truck.state_end_time_ok():
                    truck.cycle()
                continue
            if truck.driving_to_unload.is_active:
                if truck.state_end_time_ok():
                    exit_time, wait_time = unload_station_queue.add_to_queue()
                    truck.start_unloading()
                    truck.state_end_time = exit_time
                    truck.increment_waiting_time(wait_time)
                    logger.debug(
                        f"Truck {truck.name} has reached an unloading station, dwell time {wait_time} minutes"
                    )
                continue
            raise AssertionError("error in the simulation")

    return truck_list, unload_station_queue
