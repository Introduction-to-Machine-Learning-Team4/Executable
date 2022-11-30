## Action Space
Continuous Action: 0 <br />
Discrete Action: 1 <br />
- Branch size: 5 <br />
0: No Movement/1: Front/2: Back/3: Left/4: Right

## Observation Space
Total size:3 <br />
3 feature obsered and with 1 stacked vector.
- size 3: Player Coordinate(X,Y,Z)

Observation Vector (of one): <br/>
[Player.x, Player.y ,Player.z]

## Reward
Dead: -1 <br />