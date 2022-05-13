#Trees

# Tree Class
class Tree:
    def __init__(self, value, branches=()):
        self.value = value
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.value, branches_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.value) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

    def is_leaf(self):
        return not self.branches



# Q1
def search(t, value):
    """Searches for and returns the Tree whose entry is equal to value if
    it exists and None if it does not. Assume unique entries.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> search(t, 10)
    >>> search(t, 5)
    Tree(5)
    >>> search(t, 1)
    Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> search(t, 7)
    Tree(7)
    """
    


    if (t.value == value):
      return t
  
    result = None
    for branch in t.branches:
        result = search(branch, value)
        if result is not None:
            return result
  
    return None

# Q2
def cumulative_sum(t):
    """Return a new Tree, where each value is the sum of all entries in the
    corresponding subtree of t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative = cumulative_sum(t)
    >>> t
    Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(Tree(1))
    Tree(1)
    """
    lst=[]
    if t.is_leaf():
        return t #if it's only one node then just return the tree itself
    else:
        value=t.value
        for branch in t.branches:
            value = value+ cumulative_sum(branch).value # we need to get the first tree node value
            lst.append(cumulative_sum(branch))
    return Tree(value,lst)


#Q3
def add_d_leaves(t, v):
    """Add d leaves containing v to each node at every depth d.

    >>> t1 = Tree(1, [Tree(3)])
    >>> add_d_leaves(t1, 4)
    >>> t1
    Tree(1, [Tree(3, [Tree(4)])])
    >>> t2 = Tree(2, [Tree(5), Tree(6)])
    >>> t3 = Tree(3, [t1, Tree(0), t2])
    >>> add_d_leaves(t3, 10)
    >>> print(t3)
    3
      1
        3
          4
            10
            10
            10
          10
          10
        10
      0
        10
      2
        5
          10
          10
        6
          10
          10
        10
    """
    def add_leaves(t, d):
      for branch in t.branches:
        add_leaves(branch, d + 1)
      for d in range(d):
        t.branches.append(Tree(v))
    
    add_leaves(t, 0)
    