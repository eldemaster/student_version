from search_problem import SearchProblem

class PathFinding(SearchProblem):
    def __init__(self, world, init, goal):
        actions = ['N','S','W','E']
        cost = [(a,1) for a in actions]
        super().__init__(init, goal, actions, world, cost)    

    def getSuccessors(self, state) -> set:
        succ = list()
        for a in self.actions:
            if a == 'S':
                next_state = (state[0], state[1]-1)
            elif a == 'N':
                next_state = (state[0], state[1]+1)
            elif a == 'W':
                next_state = (state[0]-1, state[1])
            elif a == 'E':
                next_state = (state[0]+1, state[1])
            if next_state not in self.world.walls and self.isInTheLimits(next_state):
                succ.append((a,next_state))
                
        return succ
    
    def isGoal(self,state):
        return state[0] == self.goal[0] and state[1] == self.goal[1]
    class World():
        def __init__(self, x_lim, y_lim,walls):
            self.x_lim=x_lim
            self.y_lim=y_lim
            self.walls=walls
        def __str__(self) -> str:
            pass




