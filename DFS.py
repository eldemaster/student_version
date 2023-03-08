from search_algorithm import SearchAlgorithm
from queue import LifoQueue
from search_algorithm import Node

class DFS(SearchAlgorithm):
    """Depth First Search

    Args:
        Solver (_type_): This is an implementation for the Solver class
    """

    def solve(self, problem) -> list:
        # Create an empty stack for DFS
        stack = LifoQueue()

        # Create a set to store visited nodes
        visited = set()

        # Create a root node for the search tree
        root = Node(problem.init)

        # Push the root node onto the stack
        stack.put(root)

        while not stack.empty():
            # Pop the next node off the stack
            current_node = stack.get()

            # Check if the current node is a goal state
            if problem.isGoal(current_node.state):
                # If it is, return the solution path
                return current_node.extract_solution()

            # Add the current node to the set of visited nodes
            visited.add(current_node.state)

            # Expand the current node
            child_states = problem.getSuccessors(current_node.state)
            for child_state in child_states:
                if child_state not in visited:
                    # Create a child node for the current node
                    child_node = Node(child_state, current_node)

                    # Push the child node onto the stack
                    stack.put(child_node)

        # If the stack is empty and no goal state was found, return None
        return None

