class UCSAgent:
    """
    function UNIFORM-COST-SEARCH(problem) returns a solution node, or failure
        return BEST-FIRST-SEARCH(problem, PATH-COST)

    function BEST-FIRST-SEARCH(problem, f) returns a solution node, or failure
        node <- NODE(problem.INITIAL)
        frontier <- a priority queue ordered by f, with node as an element
        reached <- a lookup table, with one entry with key problem.INITIAL and value node

        while not EMPTY(frontier) do
            node <- POP(frontier)
            if problem.IS-GOAL(node.STATE) then return node
            for each child in EXPAND(problem, node) do
                s <- child.STATE
                if s not in reached or child.PATH-COST < reached[s].PATH-COST then
                    reached[s] <- child
                    add child to frontier
        return failure
    """
    pass
