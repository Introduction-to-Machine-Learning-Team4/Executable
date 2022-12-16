## Action Space
Continuous Action: 0 <br />
Discrete Action: 1 <br />
- Branch size: 5 <br />
0: No Movement/1: Front/2: Back/3: Left/4: Right

## Observation Space
Total size: 49 <br />
49 feature observed <br />
Grid of observation
- -1: Player
- 0: Safe Spot
- 1: Car
- 2: water

Observation Vector (of one): <br/>
\[(-3,-3),(-2,-3),(-1,-3),(0,-3),(1,-3),(2,-3),(3,-3)<br />
(-3,-2),(-2,-2),(-1,-2),(0,-2),(1,-2),(2,-2),(3,-2) ......<br />\]

## Reward
Dead: Set -0.8 * score <br />
Beating Highest score: Set 1<br />
Stucking On Wall: Add -0.5 <br />
Moving before first 15 seconds:
- Foward : Add 0.2
- Backward: Add -0.1

MovingAfter first 15 seconds:
- Not Beating Highscore in 5 second: Add -0.0001 * time interval (cap at -0.001)

Episode end if not beating the highscore in 30 second or Died