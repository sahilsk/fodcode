'''
Sales Path
The car manufacturer Honda holds their distribution system in the form of a tree (not necessarily binary). The root is the company itself, and every node in the tree represents a car distributor that receives cars from the parent node and ships them to its children nodes. The leaf nodes are car dealerships that sell cars direct to consumers. In addition, every node holds an integer that is the cost of shipping a car to it.

Take for example the tree below:

                                           +----+
                                           |    |
                                           | 0  |
                     +---------------------+-+--+----------------------+
                     |                       |                         |
                +----v-+                 +---v--+                  +---v---+
                |      |                 |      |                  |       |
                | 5    |                 |  3   |                  |  6    |
      +---------+------+         +-------+------+---+              +--+----+-------------+
      |                          |                  |                 |                  |
+-----v-+                        |                  |                 |                  |
|       |                    +---v---+           +--v----+         +--v----+             |
|  4    |                    |       |           |       |         |  1    |         +---v---+
|       |                    |  2    |           |  0    |         +-------+         |  5    |
+-------+                    |       |           |       |                           +-------+
                         +---+-------+           +---+---+                          
                         |                           |
                      +--v---+                   +---v--+
                      |  1   |                   |   10 |
                      +------+                   +------+           
                        |                
                        |
                    +----v---+
                    |    1   |
                    +--------+

A path from Honda’s factory to a car dealership, which is a path from the root to a leaf in the tree, is called a Sales Path. The cost of a Sales Path is the sum of the costs for every node in the path. For example, in the tree above one Sales Path is 0→3→0→10, and its cost is 13 (0+3+0+10).

Honda wishes to find the minimal Sales Path cost in its distribution tree. Given a node rootNode, write a function getCheapestCost that calculates the minimal Sales Path cost in the tree.

Implement your function in the most efficient manner and analyze its time and space complexities.

For example:

Given the rootNode of the tree in diagram above

Your function would return:

7 since it’s the minimal Sales Path cost (there are actually two Sales Paths in the tree whose cost is 7: 0→6→1 and 0→3→2→1→1)

Constraints:

[time limit] 5000ms

[input] Node rootNode

0 ≤ rootNode.cost ≤ 100000
[output] integer

'''

from logging import root


def get_cheapest_cost(rootNode):
  '''
  0 -> 5 3 6
     5 -> 4
      3 6 4
     -
  '''
  dfs = [ rootNode.children]
  path = []
  
  while len(dfs) > 0:
    child = dfs.pop(-1) # 5
    
    if len(child.children) > 0:
      # parent node
      dfs = dfs + child.children
    else:
      # leaf node
      print(child.cost)
    

########################################## 
# Use the helper code below to implement #
# and test your function above           #
##########################################

# A node 
class Node:

  # Constructor to create a new node
  def __init__(self, cost):
    self.cost = 
    self.children = []
    self.parent = None
 


def getCheapestCost(rootNode):
    n = rootNode.numberOfChildren()

    if (n == 0):
        return rootNode.cost
    else:
        # initialize minCost to the largest integer in the system
        minCost = MAX_INT
        for i from 0 to n-1:
            tempCost = getCheapestCost(rootNode.child[i])
            if (tempCost < minCost):
                minCost = tempCost

    return minCost + rootNode.cost
