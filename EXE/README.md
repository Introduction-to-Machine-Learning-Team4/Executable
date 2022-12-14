## Action Space
Continuous Action: 0 <br />
Discrete Action: 1 <br />
- Branch size: 5 <br />
0: No Movement/1: Front/2: Back/3: Left/4: Right

## Observation Space
Total size: 67 <br />
67 feature obsered 
- size 2: Player Coordinate(X,Z)
- size 5: The type of line which relative to player(-1~3)<br />
type 0: Grass, 1: Road, 2: Water
- size 4: The Obstacles Type, Coordinate(X,Z), Width<br />
3 obstacle observed per line. 12 feature per line. Total 36 feature.<br /> 
pad the x,z with (-10 + random) if observation is missed

Observation Vector (of one): <br/>
[Player.x, Player.z, Line -1 Type,Obstacles_-1_1.type, Obstacles_-1_1.x, Obstacles_-1_1.z, Obstacles_-1_1.width,...]

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