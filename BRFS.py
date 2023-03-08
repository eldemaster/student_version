from search_algorithm import SearchAlgorithm
from queue import Queue
from search_algorithm import Node

class BrFS(SearchAlgorithm):
    """Breath First Search

    Args:
        Solver (_type_): This is an implementation for the Solver class
    """
    def solve(self, problem) -> list:
        frontier = Queue()
        explored = set()
        start_node = Node(problem.__init__())
        frontier.put(start_node)
        
        while not frontier.empty():
            node = frontier.get()
            
            if problem.goal_test(node.state):
                return self.trace_path(node)
            
            explored.add(node.state)
            
            for action, state, cost in problem.get_successors(node.state):
                if state not in explored:
                    new_node = Node(state, node, action, node.g + cost)
                    frontier.put(new_node)
                    explored.add(state)
                    
        return None