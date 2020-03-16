# My solution to the Unknown Language Problem
## Problem- Given a sorted list of words of an unknown language, find the order of the alphabets.
## Approach
- Find the critical alphabets between two adjacent words to make the edges in the graph.
  - for two words find the first mismatch of its letters
- Make a directed graph from the edges
  - Adjacency list with the dictionary
- Pick an unvisited node from the graph 
    - if there are nodes connected to the current node
      - recursively call each connected node
      - max position = max of each recursive call
    - if no nodes connected (last alpabet)
      - max position = 0
    - return max position + 1
- After each node is visited, we will have reversed positions of each node in our visited dictionary. (Note- the position of the last node was 0)
- To make the approach feasible (Not sort it) - Everytime we add a position to the visited dictionary, we will store the node in the ans array as ans[pos] = node
- At the end, we return ans in the reverse order

### Follow the solution for more clarification!
### Thank you!
