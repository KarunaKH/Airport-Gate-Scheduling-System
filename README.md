# Airport-Gate-Scheduling-System

Airport Gate Scheduling System is an automatic assignment of Landing time and Take-off time for each of the airplanes based on various constraints so that no two planes have schedule conflict.

NOTATIONS:
- N = Number of airplanes flying over the airport, waiting to land, unload passengers, board new passengers, and take off again.
- R = The max number of minutes a plane can stay in the air before its fuel runs out.
- M = The number of minutes required by the plane to reach its landing gate.
- S = The number of minutes required by the crew of the plane to unload passengers, refuel and board new passengers, before it is ready to take off again.
- C = The max minutes a plane can stay at the gate before passengers start complaining.
- O = The max number of minutes required by the plane to fully take off and for the inflight beverages to be served.
- L = Number of Landing runways,that is the max number of planes allowed to land at the same time.
- T = Number of Take-off runways,that is the max number of planes allowed to take-off at the same time.
- G = Number of Gates,that is the max number of planes occupying the gates at the same time.

EXAMPLE:
N=1 R=0 M=10 S=50 O=20 C=70
- There is only 1 flight that needs to be scheduled.
- The flight can wait upto 5 minutes before its out of fuel(R=5), so Landing procedure needs to start between 0-5 mins.
- The flight requires 10 minutes to land(M=10), so if the flight started landing at 0 mins, it will finish its landing and reach one of the gates at 15 mins.
- The flight requires 50 mins for maintenance and servicing(S=10), so the flight will be serviced from 15-65 mins.
- The flight can stay at the gate for 70 mins max(C=70), so we need to begin take-off between 65-85 mins before customers start complaining since we utilised 50 mins at the gate for servicing, we have only 20 mins left.
- The flight will take 20 mins to fully take-off and be in the air(O=20), so if we take off at 65, we can begin serving inflight beverages at 85 mins.

CONSTRAINTS:
1. A plane must begin its Landing procedure before its fuel is exhausted.
2. A plane utilises all of its M minutes in landing.
3. A plane must move to the gate immediately after it finished its landing. No extra minutes are assigned for the plane to move from Landing runway to gate!
4. Each plane must have a gate to stay before its time to take off again.
5. A plane utilises all of its S minutes for servicing.
6. A plane can spend atmost C minutes at the gate.
Once the plane leaves the gate, it takes all of the O minutes to fully take-off.

GOAL: Assign each plane in the air a time when it should begin landing procdeure and a time when it should begin its take-off procedure.

INPUT:
- The first line of the input states 3 numbers in order: L, G, T.
- The second line = N.
- From line 3 to end: R,M,S,O,C description(in order) of N planes.

OUTPUT:
N lines of Start_Landing and Start_Takeoff time for each of the N planes, in order.
