## Action Space
Continuous Action: 0 <br />
Discrete Action: 1 <br />
- Branch size: 5 <br />
0: No Movement/1: Front/2: Back/3: Left/4: Right

## Observation Space
Total size: 30 <br />
- size 2: Player Coordinate(X,Z)
- size 4: The type of line which relative to player(previous,current,next two)<br />
type 0: Grass, 1: Road, 2: Water
- size 2: The Obstacles Coordinate(X,Z)<br />
3 obstacle observed per line. 6 feature per line. Total 24 feature.<br /> 

Observation Vector (of one): <br/>
[Player.x, Player.z, Line -1 Type, Obstacles_-1_1.x, Obstacles_-1_1.z, Obstacles_-1_2.x, Obstacles_-1_2.z, Obstacles_-1_3.x, Obstacles_-1_3.z, Line 0 Type, ...]

## Reward
Dead: -1 <br />
Beating Highest score: 1 <br />
Moving before first 15 seconds:
- Foward : 0.1
- Other than stop : -0.1

After first 15 seconds:
- Not Beating Highscore in 5 second: -0.0001 * time interval (cap at -0.01)

Episode end if reward < -5 or Died
