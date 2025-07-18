Run pytest in this folder to actually run the simulation.

I have the results going to console via the logger, but with more time, I'd use matplotlib to show a heatmap
w/ confidence interval for a range of realistic inputs.

One could accomplish this by running several times for each set of variables to get a distribution.

#### Results

Example results follow:
```
============================= test session starts =============================
collecting ... collected 4 items

test_simulation.py::test_mining_sim[10-1] 
test_simulation.py::test_mining_sim[50-1] 
test_simulation.py::test_mining_sim[50-2] 
test_simulation.py::test_mining_sim[100-5] 

============================== 4 passed in 8.65s ==============================

-------------------------------- live log call --------------------------------
2025-07-18 16:32:19 INFO Simulation with num_trucks=10 and num_unload_stations=1 :
2025-07-18 16:32:19 INFO 	Truck 0 delayed 0.1% of the time
2025-07-18 16:32:19 INFO 	Truck 1 delayed 0.1% of the time
2025-07-18 16:32:19 INFO 	Truck 2 delayed 0.2% of the time
2025-07-18 16:32:19 INFO 	Truck 3 delayed 0.4% of the time
2025-07-18 16:32:19 INFO 	Truck 4 delayed 0.1% of the time
2025-07-18 16:32:19 INFO 	Truck 5 delayed 0.1% of the time
2025-07-18 16:32:19 INFO 	Truck 6 delayed 0.0% of the time
2025-07-18 16:32:19 INFO 	Truck 7 delayed 0.1% of the time
2025-07-18 16:32:19 INFO 	Truck 8 delayed 0.4% of the time
2025-07-18 16:32:19 INFO 	Truck 9 delayed 0.2% of the time
2025-07-18 16:32:19 INFO 	Unload Station 0 had a queue 1.5% of the time
2025-07-18 16:32:19 INFO Average truck delay: 7.1 minutes (out of sim time 4320 mins)
PASSED                                                                   [ 25%]
-------------------------------- live log call --------------------------------
2025-07-18 16:32:21 INFO Simulation with num_trucks=50 and num_unload_stations=1 :
2025-07-18 16:32:21 INFO 	Truck 0 delayed 8.3% of the time
<omitted for brevity>
2025-07-18 16:32:21 INFO 	Truck 49 delayed 7.4% of the time
2025-07-18 16:32:21 INFO 	Unload Station 0 had a queue 84.9% of the time
2025-07-18 16:32:21 INFO Average truck delay: 292.34 minutes (out of sim time 4320 mins)
PASSED                                                                   [ 50%]
-------------------------------- live log call --------------------------------
2025-07-18 16:32:23 INFO Simulation with num_trucks=50 and num_unload_stations=2 :
2025-07-18 16:32:23 INFO 	Truck 0 delayed 0.5% of the time
<omitted for brevity>
2025-07-18 16:32:23 INFO 	Truck 49 delayed 0.4% of the time
2025-07-18 16:32:23 INFO 	Unload Station 0 had a queue 9.4% of the time
2025-07-18 16:32:23 INFO 	Unload Station 1 had a queue 5.1% of the time
2025-07-18 16:32:23 INFO Average truck delay: 13.64 minutes (out of sim time 4320 mins)
PASSED                                                                   [ 75%]
-------------------------------- live log call --------------------------------
2025-07-18 16:32:27 INFO Simulation with num_trucks=100 and num_unload_stations=5 :
2025-07-18 16:32:27 INFO 	Truck 0 delayed 0.0% of the time
<omitted for brevity>
2025-07-18 16:32:28 INFO 	Truck 99 delayed 0.0% of the time
2025-07-18 16:32:28 INFO 	Unload Station 0 had a queue 1.2% of the time
2025-07-18 16:32:28 INFO 	Unload Station 1 had a queue 0.9% of the time
2025-07-18 16:32:28 INFO 	Unload Station 2 had a queue 0.6% of the time
2025-07-18 16:32:28 INFO 	Unload Station 3 had a queue 0.4% of the time
2025-07-18 16:32:28 INFO 	Unload Station 4 had a queue 0.2% of the time
2025-07-18 16:32:28 INFO Average truck delay: 1.41 minutes (out of sim time 4320 mins)
PASSED                                                                   [100%]
Process finished with exit code 0
```
