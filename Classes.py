#class Tree
class TreeNode:
  def __init__(self, value, height, astar, parent=[]):
    self.value = value #state as a list
    self.parent = parent
    self.children = []# references to other nodes
    self.height = height
    self.astar = astar
    

  def add_child(self, child_node):
    # creates parent-child relationship
    self.children.append(child_node) 
    
  def remove_child(self, child_node):
    # removes parent-child relationship
    self.children = [child for child in self.children 
                     if child is not child_node]


  #may delete
  def traverse(self):
    # moves through each node referenced from self downwards
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children    