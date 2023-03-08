from search_algorithm import SearchAlgorithm
from queue import PriorityQueue
from search_algorithm import Node

class AstarNode(Node):
    def __init__(self, state, parent = None, action = None, g = 0, h = 0) -> None:
        self.h = h
        super().__init__(state, parent, action, g)
        
    def __lt__(self, other):
        return self.g + self.h < other.g + other.h 
    
class AStar(SearchAlgorithm):
    """AStar First Search

    Args:
        Solver (_type_): This is an implementation for the Solver class
    """
    def __init__(self, heuristic = lambda x,y : 0, view = False, w = 1) -> None:
        self.heuristic = heuristic
        self.w = w
        super().__init__(view)

    def solve(self, problem) -> list:
        frontier = PriorityQueue()
        explored = set()
        start_node = AstarNode(problem.get_initial_state(), None, None, 0, self.heuristic(problem.get_initial_state(), problem.goal_state))
        frontier.put(start_node)
        
        while not frontier.empty():
            node = frontier.get()
            
            if problem.goal_test(node.state):
                return self.trace_path(node)
            
            explored.add(node.state)
            
            for action, state, cost in problem.get_successors(node.state):
                if state not in explored:
                    new_g = node.g + cost
                    new_h = self.heuristic(state, problem.goal_state)
                    new_node = AstarNode(state, node, action, new_g, new_h)
                    frontier.put(new_node)
                    
        return None