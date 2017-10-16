''' Question 1
Given two strings s and t, determine whether some anagram of t is a substring
of s. For example: if s = "udacity" and t = "ad", then the function returns
True. Your function definition should look like: question1(s, t) and return
a boolean True or False.'''

def question1(s, t):
    if (t == None or s == None):
        return "Anagram is not possible"
    if not t or not s and (not t and not s):
        return "Anagram is not possible"    
    if len(t) > len(s):
        return "Anagram is not possible"

    s = s.lower()
    t = t.lower()
    
    def c_dict(strg):
        str_dict = {}
        for i in strg:
            if i in str_dict:
                str_dict[i] += 1
            else:
                str_dict[i] = 1
               
        return str_dict

    t_dict = c_dict(t)
    s_dict = c_dict(s)
    for j in t_dict:
        if j not in s_dict:
            return False
        
        if s_dict[j] < t_dict[j]:
            return False 
	 
    return True

     
print "\nQuestion1 Answers"
print question1('udacity', 'ad')
print question1(None, 'ad')
print question1('udacity', None)


''' Question 2
Given a string a, find the longest palindromic substring contained in a.
Your function definition should look like question2(a), and return a string.'''

def question2(a):
    ans = []
    if a == ' ':
        return "Error Input"
    for i in range(0, len(a)):
        for l in range(0,i):
            strg = a[l:i+1]
            if strg == strg[::-1]:
                ans.append(strg)
                
    if ans==[]:
        return "No palindromic substring in the given string"
    else:
        return max(ans, key=len)

print "\nQuestion2 Answers"
print question2(' ')
print question2('banana')
print question2('tomato')



'''Question 4
Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is
the farthest node from the root that is an ancestor of both nodes. For example, the root is a common ancestor
of all nodes on the tree, but if both nodes are descendents of the root's left child, then that left child might
be the lowest common ancestor. You can assume that both nodes are in the tree, and the tree itself adheres to
all BST properties. The function definition should look like question4(T, r, n1, n2), where T is the tree
represented as a matrix, where the index of the list is equal to the integer stored in that node and a 1
represents a child node, r is a non-negative integer representing the root, and n1 and n2 are non-negative
integers representing the two nodes in no particular order. For example, one test case might be

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
and the answer would be 3.'''

def question4(T, r, n1, n2):
    parentnode = []
    while n1 != r:
        n1 = parent(T, n1)
        parentnode.append(n1)
    if len(parentnode) == 0:
        return -1
    while n2 != r:
        n2 = parent(T, n2)
        if n2 in parentnode:
            return n2
    return -1
    
    
def parent(T, n):
    noofrows = len(T)
    for i in range(0, noofrows):
        if T[i][n] == 1:
            return i
    return -1

print "\nQuestion4 Answers"
print question4([[0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
                 3,
                 1,
                 4)
print question4([[0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 1, 0],
                 [0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]],
                 4,
                 2,
                 1)

print question4([[0, 1, 0, 0, 0],
                 [0, 0, 1, 0, 0],
                 [0, 0, 0, 1, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
                 0,
                 3,
                 4)

'''Question 5
Find the element in a singly linked list that's m elements from the end. For example, if a linked list has
5 elements, the 3rd element from the end is the 3rd element. The function definition should look like
question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end".
You should copy/paste the Node class below to use as a representation of a node in the linked list.
Return the value of the node at that position.'''

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
def question5(ll, m):
    maxlen = 1
    current = head = ll
    while current.next:
            current = current.next
            maxlen += 1

    remainlen = (maxlen - m) + 1
    current = head
    for i in range(1, remainlen):
        current = current.next
    return current.data
      
    

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)


# Start setting up a LinkedList
ll = LinkedList(n1)
ll.append(n2)
ll.append(n3)
ll.append(n4)

print "\nQuetion5 Answers"
print question5(n1,3)
print question5(n1,1)
print question5(n1,4)


''' Question 3
Given an undirected graph G, find the minimum spanning tree within G.
A minimum spanning tree connects all vertices in a graph with the smallest
possible total weight of edges. Your function should take in and return an
adjacency list structured like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}
Vertices are represented as unique strings. The function definition
should be question3(G). '''

class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        
        edge_list = []
        for edge_object in self.edges:
            edge = (edge_object.value, edge_object.node_from.value, edge_object.node_to.value)
            edge_list.append(edge)
        return edge_list

    def get_node_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        node_list = []
        for node in self.nodes:
            node = (node.value)
            node_list.append(node)
        return node_list

    def make_set(self, vertex, parent, rank):
        parent[vertex] = vertex
        rank[vertex] = 0

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, v1, v2):
        v1root = self.find(parent, v1)
        v2root = self.find(parent, v2)

        
        if rank[v1root] < rank[v2root]:
            parent[v1root] = v2root
        elif rank[v1root] > rank[v2root]:
            parent[v2root] = v1root
        else :
            parent[v1root] = v2root
            rank[v2root] += 1


def question3(graph)
   
    A = {}

    nodes = graph.get_node_list()
    
    parent = {}
    rank = {}

    for i, node in enumerate(nodes):
        graph.make_set(node, parent, rank)

    edges = sorted(graph.get_edge_list())

    for w, v1, v2 in edges:
        root1 = graph.find(parent, v1)
        root2 = graph.find(parent, v2)
        if root1 != root2:
            if bool(A.has_key(v1)):
                A[v1].append((v2,w))
                graph.union(parent, rank, root1, root2)
            else:
                A[v1] = [(v2,w)]
                graph.union(parent, rank, root1, root2)
    return A
            

print "\nQuetion3 Answers"
G = Graph()
G.insert_edge(2, 'A', 'B')
G.insert_edge(2, 'B', 'A')
G.insert_edge(5, 'B', 'C')
G.insert_edge(5, 'C', 'B')

print question3(G)

