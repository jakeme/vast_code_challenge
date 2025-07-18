class MiningClock:
    """Clock object to keep track of the simulation time"""

    def __init__(self):
        self._time = 0  # Use only single underscore so we can manipulate this for tests

    def increment_time(self):
        self._time += 1

    @property
    def time(self):
        return self._time
