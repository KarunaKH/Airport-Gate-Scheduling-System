# AIRPORT-GATE-SCHEDULING-SYSTEM

Airport Gate Scheduling System is an automatic assignment of Landing time and Take-off time for each of the airplanes based on various constraints so that no two planes have schedule conflict.

# Notations:
- N = Number of airplanes flying over the airport, waiting to land, unload passengers, board new passengers, and take off again.
- R = The max number of minutes a plane can stay in the air before its fuel runs out.
- M = The number of minutes required by the plane to finish its landing and move to gate.
- S = The number of minutes required by the crew of the plane to unload passengers, refuel and board new passengers, before it is ready to take off again.
- C = The max minutes a plane can stay at the gate before passengers start complaining.
- O = The max number of minutes required by the plane to fully take off and for the inflight beverages to start getting served.
- L = Number of Landing runways,that is the max number of planes allowed to land at the same time.
- T = Number of Take-off runways,that is the max number of planes allowed to take-off at the same time.
- G = Number of Gates,that is the max number of planes occupying the gates at the same time.

# Example:
N=1 R=5 M=10 S=50 O=20 C=70
- There is only 1 flight that needs to be scheduled.
- The flight can wait upto 5 minutes before its out of fuel(R=5), so Landing procedure needs to start between 0-5 mins.
- The flight requires 10 minutes to land(M=10), so if the flight started landing at 5 mins, it will finish its landing and reach one of the gates at 15 mins.
- The flight requires 50 mins for maintenance and servicing(S=50), so the flight will be serviced from 15-65 mins.
- The flight can stay at the gate for 70 mins max(C=70), so we need to begin take-off between 65-85 mins before customers start complaining since we utilised 50 mins at the gate for servicing, we have only 20 mins left.
- The flight will take 20 mins to fully take-off and be in the air(O=20), so if we take off at 65, we can begin serving inflight beverages at 85 mins.

# Constraints:
1. A plane must begin its Landing procedure before its fuel is exhausted.
2. A plane utilises all of its M minutes in landing.
3. A plane must move to the gate immediately after it finished its landing. No extra minutes are assigned for the plane to move from Landing runway to gate!
4. Each plane must have a gate to stay before its time to take off again.
5. A plane utilises all of its S minutes for servicing.
6. A plane can spend **atmost** C minutes at the gate.
7. Once the plane leaves the gate, it takes all of the O minutes to fully take-off.

# Goal:
Assign each plane in the air a time when it should begin landing procdeure and a time when it should begin its take-off procedure.

# Input:
- The first line of the input gives 3 numbers in order: L, G, T.
- The second line = N.
- From line 3 to end: R,M,S,O,C description(in order) of N planes.

# Output:
N lines of Start_Landing and Start_Takeoff times for each of the N planes, in order.

# Logic:
# Attempt #1: Always, The Brute Force Method.
Trying all the possible combinations at each minute!

1. Create arrays of size 1440(number of minutes in a day) for Landing, Gates and Takeoff, each initialized to 0 to keep track of each minute of each of the plane's schedule.
2. For plane 1, assign its landing to first possible min(say l1), and increment the value of corresponding Landing array from l1 to l1+M, Gates array from l1+M to l1+M+S and take off array from l1+M+S to l1+M+S+O mins.
3. Check all the constraints.
-If this assignment is incorrect, move the assignment by 1 min and repeat step 3.
-If this assignment is correct, move onto plane 2 and repeat the process from step 2.
4. Keep doing step 2 and 3 for all the planes until you reach an assignment satisfied by all the planes.
-If you do not have any assignment for any plane at any point in time, go to previous plane assignment and repeat step 2.
5. Check every possible minute of the schedule and you will successfully reach an assignment by the end of the algorithm!

Why this attempt may fail?
This pseudo code doesn't fail in logic but in time! Infact its the best solution because it will give you the most efficient assignment!
But try using this method on 25 planes which have only 1 possible schedule! It will take minutes to reach a solution. In my case, for my particular laptop, it took me 37 minutes to get a solution for N=25(yes, I waited 37 long minutes!).

# Attempt 2: Classic Constraint Satisfaction Problem!
Use domain reduction technique to find the first possible valid assignment.
**Domain of a flight means if a flight has say max 5 mins to wait before its fuel is exhuasted, its possible values can only be 0,1,2,3,4,5.
After these minutes, it cannot have a valid solution, so why even try it!**

1. Start with plane 1 and assign it to the first possible minute.
2. For plane 2, first remove all the values from its domain that might be conflicting with the 1st plane.
3. Now select the first possible value for next flight from the remaining domain value!
**(You see what happened here? lets say L=1 R1=0 M1=10 and R2=10 M2=10, plane 1 can begin its landing at 0 minute but will reach gate at 10 minutes, plane 2 cannot reach the gate before 10 mins, so there is no point in starting its landing at 0th minute! You can maybe start its landing at 10 minute, by that time Plane 1 would've completed its landing. So why do you want to check values from 0-9 and try 10 useless possibilities)**
4. We can use one more exceptionally simple and smart heuristic called MRV(Minimum Remaining Value)
**MRV: Pick that plane first which have minimum number of possible values. Intuition is very simple, if a plane can be assigned only 1 way, it will surely fail if assigned any other way(obvio!) so why not assign it first and then adjust the schedule for other planes accordingly!**
5. Again, Check all the constraints.
-If this assignment is incorrect, move the assignment to next domain value and repeat step 2.
-If this assignment is correct, move onto next plane and repeat the process from step 2.
4. Keep doing above steps for all the planes until you reach an assignment satisfied by all the planes.
-If you do not have any assignment for any plane at any point in time, go to previous plane assignment and repeat step 2.

Why this attempt will succeed?
There are a lot of constraints which is advantageous in this attempt because if you reduce the size of the domain for each of the planes, you can reduce the number of trail and errors!
Also, the tighter the constraints, the quicker the domain values decreases, the faster the algorithm!
This particular algorithm can produce a valid assignment for as high as **N=100 planes under 60 seconds!**
