from mining_sim import MiningClock
from mining_sim.constants import UNLOADING_TIME


class UnloadStationQueue:
    def __init__(self, clock: MiningClock, num_unload_stations):
        self.clock = clock
        # Unload stations list shall be a list of stations
        # Each station is a list of times when a truck leaves. An empty station has no trucks in queue.
        # There is no reference that shows which truck is which in the queue (not needed - truck objects track their own time spent there).
        self.unload_stations_list = [[] for _ in range(num_unload_stations)]
        self.dwell_time_list = [0 for _ in range(num_unload_stations)]

    def clean_up_queue(self):
        """Remove trucks from the lists that are done unloading and accumulate dwell time"""
        for i in range(len(self.dwell_time_list)):
            has_queue = len(self.unload_stations_list[i]) > 1
            if has_queue:
                self.dwell_time_list[i] += 1
        for station_queue in self.unload_stations_list:
            if station_queue:
                if station_queue[0] <= self.clock.time:
                    station_queue.pop(0)

    def add_to_queue(self) -> (int, 0):
        """
        Adds a truck to an unload station.
        If no unload station is ready, adds the truck to the queue at the station with the least wait time.

        Returns a tuple:
            (time done unloading, wait time)
        """
        for station_queue in self.unload_stations_list:
            if not station_queue:
                exit_time = self.clock.time + UNLOADING_TIME
                station_queue.append(exit_time)
                return exit_time, 0
        # If there are no free stations, find the one with the shortest wait time
        station_ready_time = float("inf")
        station_ready_index = None
        for i in range(len(self.unload_stations_list)):
            station_queue = self.unload_stations_list[i]
            if station_queue[-1] < station_ready_time:
                station_ready_time = station_queue[-1]
                station_ready_index = i
        assert station_ready_index is not None
        exit_time = station_ready_time + UNLOADING_TIME
        wait_time = station_ready_time - self.clock.time

        self.unload_stations_list[station_ready_index].append(exit_time)
        return exit_time, wait_time
