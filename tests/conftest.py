import pytest
from mining_sim import MiningTruck, MiningClock, UnloadStationQueue


@pytest.fixture()
def mining_clock():
    return MiningClock()


@pytest.fixture()
def mining_truck(mining_clock):
    return MiningTruck("truck", mining_clock)


@pytest.fixture()
def unload_queue_one_station(mining_clock):
    return UnloadStationQueue(mining_clock, 1)


@pytest.fixture()
def unload_queue_two_stations(mining_clock):
    return UnloadStationQueue(mining_clock, 2)
