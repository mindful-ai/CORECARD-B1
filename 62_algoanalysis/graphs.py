graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

'''
This is a simple function to determine a path between two nodes. It takes a graph and the start and end nodes as arguments. 
It will return a list of nodes (including the start and end nodes) comprising the path. When no path can be found, 
it returns None. The same node will not occur more than once on the path returned (i.e. it won't contain cycles). 
The algorithm uses an important technique called backtracking: it tries each possibility in turn until it finds a solution.

'''

def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not start in graph.keys():
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None

'''
It is simple to change this function to return a list of all paths (without cycles) 
instead of the first path it finds
'''

def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not start in graph.keys():
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths


if __name__ == '__main__':

    print(find_path(graph, 'A', 'D'))
    print(find_all_paths(graph, 'A', 'D'))
    
