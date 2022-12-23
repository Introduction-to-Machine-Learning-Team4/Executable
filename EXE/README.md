## Action Space
Continuous Action: 0 <br />
Discrete Action: 1 <br />
- Branch size: 5 <br />
0: No Movement/1: Front/2: Back/3: Left/4: Right

## Observation Space
Total size: 147 <br />
Grid size: 7*21 (7 row , 21 grid on row) <br />
Grid of observation
- -1: Player (In the middle)
- 0: Safe Spot
- 1: Car
- 2: water



## Reward
Dead: Set -0.2 * score (cap at -5.0) <br />
Beating Highest score: Set 1<br />
Stucking On Wall: Add -0.5 <br />

MovingAfter first 15 seconds:
- Not Beating Highscore in 15 second: Add -0.0001 * time interval (cap at -0.001)

Episode end if not beating the highscore in 45 second or Died