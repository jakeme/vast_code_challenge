import random

from statemachine import StateMachine, State

from mining_sim import MiningClock
from mining_sim.constants import (
    MINING_TIME_MINIMUM,
    MINING_TIME_MAXIMUM,
    UNLOADING_TIME,
    DRIVING_TIME,
)


class MiningTruck(StateMachine):
    driving_to_mine = State()
    mining = State(
        initial=True
    )  # From the prompt: Assume all trucks are empty at a mining site when the simulation starts.
    driving_to_unload = State()
    unloading = State()  # Includes wait time while queued for an unload station

    cycle = (
        driving_to_mine.to(mining, cond="state_end_time_ok")
        | mining.to(driving_to_unload, cond="state_end_time_ok")
        | unloading.to(driving_to_mine, cond="state_end_time_ok")
    )
    start_unloading = driving_to_unload.to(unloading, cond="state_end_time_ok")

    def __init__(self, name: str, clock: MiningClock):
        self.name = name
        self.state_end_time = None
        self.clock = clock
        super().__init__(self)
        self.waiting_time = 0  # Cumulative waiting time over the simulation

    def on_enter_mining(self):
        self.state_end_time = self.clock.time + random.randrange(
            MINING_TIME_MINIMUM, MINING_TIME_MAXIMUM
        )

    def on_enter_driving_to_unload(self):
        self.state_end_time = self.clock.time + DRIVING_TIME

    def on_enter_driving_to_mine(self):
        self.state_end_time = self.clock.time + DRIVING_TIME

    def on_enter_unloading(self):
        self.state_end_time = self.clock.time + UNLOADING_TIME

    def increment_waiting_time(self, wait_time):
        self.waiting_time += wait_time

    def state_end_time_ok(self):
        # Validates that the state has been completed according to the timer
        return self.clock.time >= self.state_end_time


if __name__ == "__main__":
    # Note - must install https://graphviz.org/
    from statemachine.contrib.diagram import DotGraphMachine

    graph = DotGraphMachine(MiningTruck("Mining Truck State Diagram", MiningClock()))
    dot = graph()
    dot.write_png("truck_sm.png")
