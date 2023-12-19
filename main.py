from search.algorithms import CBS, CBSState, State
from search.map import Map

# Function to read problem instances from a file
def read_instances(test_instances):
    problems = []
    with open(test_instances, 'r') as file:
        for line in file:
            starts_instances = []
            goals_instances = []

            # Split the line into components using comma as a delimiter
            list_instance = line.split(",")
            cost = None
            for i in range(0, len(list_instance), 4):
                if i == len(list_instance) - 1:
                    # Last element is the cost, add the problem to the list
                    cost = int(list_instance[i])
                    problems.append((starts_instances, goals_instances, cost))
                    break
                # Create start and goal states and add them to respective lists
                start = State(int(list_instance[i]), int(list_instance[i + 1]))
                goal = State(int(list_instance[i + 2]), int(list_instance[i + 3]))

                starts_instances.append(start)
                goals_instances.append(goal)
    return problems


def main():
    # Load a gridded map from a file
    gridded_map = Map("dao-map/test_map.map")
    
    # Define initial and goal states for two agents
    starts = [State(1, 1), State(5, 1)]
    goals = [State(4, 1), State(2, 1)]
    
    # Create a CBSState object representing the problem
    cbs_state = CBSState(gridded_map, starts, goals)
    
    # Create a CBS object for search
    cbs_search = CBS()
    
    # Perform CBS search and get paths and cost
    paths, cost = cbs_search.search(cbs_state)
    
    # Print the solution paths if found
    if paths is not None:
        print('Solution paths encountered for the easy test: ')
        for agent, path in paths.items():
            print(agent, path)
        print()

    # Load a different map for further testing
    name_map = "dao-map/combat2.map"
    
    # Read problem instances from a file
    test_instances = "test-instances/instances.txt"
    problems = read_instances(test_instances)

    # Iterate over the problems and test CBS search
    for problem in problems:
        # Create a CBSState object for the current problem
        cbs_state = CBSState(gridded_map, problem[0], problem[1])
        
        # Perform CBS search and get paths and cost
        cbs_search = CBS()
        _,
