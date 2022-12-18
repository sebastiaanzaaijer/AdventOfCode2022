from collections import defaultdict,namedtuple
from heapq import heapify,heappop,heappush
from itertools import combinations

def shortest_paths(start,nodes,edges):
    visited = {start:0}
    to_visit = [(_,edges[(start,_)]["length"]) for _ in nodes[start]["connections"]]
    while to_visit:
        visit_next = []
        for node,dist in to_visit:
            if not node in visited:
                visited[node] = dist
                for next_node in nodes[node]["connections"]:
                    to_visit.append((next_node,edges[(node,next_node)]["length"]+dist))
            else:
                visited[node] = min(visited[node],dist)
        to_visit = visit_next
    return visited

def simplify_graph(nodes,edges):
    nodes_for_simplification = [_ for _ in nodes if nodes[_]["flowrate"] == 0 and len(nodes[_]["connections"]) == 2]
    new_nodes = {_:nodes[_] for _ in nodes if _ not in nodes_for_simplification}
    new_edges = dict(edges)
    for node in nodes_for_simplification:
        connection1, connection2 = nodes[node]["connections"]
        nodes[connection1]["connections"].remove(node)
        nodes[connection1]["connections"].append(connection2)
        nodes[connection2]["connections"].remove(node)
        nodes[connection2]["connections"].append(connection1)
        old_edge1 = (min(node,connection1),max(node,connection1))
        old_edge2 = (min(node,connection2),max(node,connection2))
        new_edge = (min(connection1,connection2),max(connection1,connection2))
        new_edge_length = new_edges[old_edge1]["length"]+new_edges[old_edge2]["length"]
        new_edges.pop(old_edge1,None)
        new_edges.pop(old_edge2,None)
        new_edges[new_edge] = {"length": new_edge_length}

    return new_nodes,new_edges

def release(flowrate,start):
    return max(0,(26-start)*flowrate)

def solve_puzzle(puzzle_input):
    nodes = defaultdict(lambda: {"flowrate":0, "connections": []})
    edges = defaultdict(lambda: {"length":0})
    for line in puzzle_input.splitlines():
        node_info,connection_info = line.split(";")
        node = node_info.split()[1]
        flowrate = int(node_info.split()[-1].split("=")[-1])
        connections = [_.split()[-1] for _ in connection_info.split(", ")]
        nodes[node]["flowrate"] = flowrate
        for connection in connections:
            edges[(min(node,connection),max(node,connection))]["length"] = 1
            nodes[node]["connections"].append(connection)

    nodes,edges = simplify_graph(nodes,edges)

    # make graph directional
    for edge in list(edges.keys()):
        edges[(edge[1],edge[0])] = dict(edges[edge])
    
    # introduce ghost nodes for valve operation
    ghost_nodes = {}
    for node in nodes:
        if nodes[node]["flowrate"] > 0:
            ghost_node = node+"_V"
            ghost_nodes[ghost_node] = {"flowrate": nodes[node]["flowrate"], "connections": [node]}
            nodes[node]["connections"].append(ghost_node)
            edges[(ghost_node,node)] = {"length" : 0}
            edges[(node,ghost_node)] = {"length" : 1}
            nodes[node]["flowrate"] = 0

    nodes.update(ghost_nodes)
    # for node in nodes:
    #     print(f"{node}({nodes[node]})")
    # for edge in edges:
    #     n1,n2 = edge
    #     l = edges[edge]["length"]
    #     print(f"{n1}({nodes[n1]['flowrate']}) {n2}({nodes[n2]['flowrate']}) {l}")

    valve_distances = {}
    for node in nodes:
        if node.endswith("_V") or node == "AA":
            shortest = shortest_paths(node,nodes,edges)
            for to_node in shortest:
                if to_node.endswith("_V") or to_node == "AA":
                    valve_distances[(node,to_node)] = shortest[to_node]

    valves = {_:nodes[_]["flowrate"] for _ in nodes if _.endswith("_V")}
    
    QueueItem = namedtuple("QueueItem", "time released visited")
    queue = []
    heapify(queue)
    best_release = 0
    for v1,v2 in combinations(valves, 2):
        visited1 = ["AA",v1]
        visited2 = ["AA",v2]
        time1 = valve_distances[tuple(visited1[-2:])]
        time2 = valve_distances[tuple(visited2[-2:])]
        potential = sum(release(valves[v],min(time1,time2)) for v in valves if not v in visited1+visited2)
        released1 = release(valves[v1],time1)
        released2 = release(valves[v2],time2)
        best_release = max(released1+released2,best_release)
        heappush(queue,(-potential-released1-released2,QueueItem(time1,released1,visited1),QueueItem(time2,released2,visited2)))

    best = None
    count = 0
    while len(queue) > 0:
        potential,item1,item2 = heappop(queue)
        if (item1.released + item2.released) > best_release:
            best_release = item1.released + item2.released
            best = count,potential,item1,item2,best_release
        if -potential <= best_release:
            return best_release 
        if item1.time < 26 or item2.time < 26:
            for v1,v2 in combinations(valves, 2):
                if v1 not in item1.visited+item2.visited and v2 not in item1.visited+item2.visited:
                    visited1 = item1.visited[:]+[v1]
                    visited2 = item2.visited[:]+[v2]
                    time1 = item1.time + valve_distances[tuple(visited1[-2:])]
                    time2 = item2.time + valve_distances[tuple(visited2[-2:])]
                    potential = sum(release(valves[v],min(time1,time2)) for v in valves if not v in visited1+visited2)
                    released1 = item1.released + release(valves[v1],time1)
                    released2 = item2.released + release(valves[v2],time2)
                    heappush(queue,(-potential-released1-released2,QueueItem(time1,released1,visited1),QueueItem(time2,released2,visited2)))
            for v2,v1 in combinations(valves, 2):
                if v1 not in item1.visited+item2.visited and v2 not in item1.visited+item2.visited:
                    visited1 = item1.visited[:]+[v1]
                    visited2 = item2.visited[:]+[v2]
                    time1 = item1.time + valve_distances[tuple(visited1[-2:])]
                    time2 = item2.time + valve_distances[tuple(visited2[-2:])]
                    potential = sum(release(valves[v],min(time1,time2)+min(valve_distances[(v1,v)],valve_distances[(v2,v)])) for v in valves if not v in visited1+visited2)
                    released1 = item1.released + release(valves[v1],time1)
                    released2 = item2.released + release(valves[v2],time2)
                    heappush(queue,(-potential-released1-released2,QueueItem(time1,released1,visited1),QueueItem(time2,released2,visited2)))
        count += 1
        # if count % 1000 == 0:
        #     print(count,best)

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))