class Tree:
  def __init__(self, root=None):
    self.root = root

  def get_element_by_id(self, id):
    # Check if the current node matches the desired ID
    if self.root['id'] == id:
      return self.root

    # Iterate through the child nodes and recursively call get_element_by_id
    for child in self.root['children']:
      result = Tree(child).get_element_by_id(id)
      if result:
        return result

    # If no matching node is found, return None
    return None