def initialize_map(f_name):
    map,v_map,shadow_frontier = dict(),dict(),dict()
    dimension,start,goal = [0]*2,[0]*2,[0]*2
    row_num = -1
    with open(f_name,'rU') as f:
        lines = f.readlines()
        for line in lines:
            if row_num == -1:
                l = line.split(" ")
                dimension[0] = l[0]
                dimension[1] = l[1]
            else:
                row_dic, true_row_dic, stack_row_dic = dict(), dict(), dict()
                col_num = 0
                for tile in line:
                    row_dic[col_num] = tile
                    true_row_dic[col_num] = 0
                    stack_row_dic[col_num] = 0
                    if tile == "S":
                        start[0],start[1] = row_num,col_num
                    if tile == "G":
                        goal[0],goal[1] = row_num,col_num
                    col_num = col_num + 1
                map[row_num] = row_dic
                v_map[row_num] = true_row_dic
                shadow_frontier[row_num] =stack_row_dic
            row_num = row_num + 1
        return [map,v_map,shadow_frontier,dimension,start,goal]

def create_node(coordinate, h_cost, health):
    node = (coordinate,) + (h_cost, ) + (health, )
    return node

def calculate_heuristic_cost (current_position,goal_position):
    row_diff = abs(goal_position[0] - current_position[0])
    col_diff = abs(goal_position[1] - current_position[1])
    return (row_diff + col_diff)

def calculate_health(current_position,map,health,dimension):
    i, j = current_position[0], current_position[1]
    factor = 1
    if map[i][j] == '*':
        factor = 3
    direction= gen_validate_children(current_position,dimension)
    for z in direction:
        if(check_tower(z, map)):
            health = health - 1 * factor
    return health

def check_tower(current_position,map):
    if map[current_position[0]][current_position[1]] == 'O':
        return True
    return False
def gen_validate_children(current_position,dimension):
    children = []
    i,j = current_position[0],current_position[1]
    max_i,max_j = dimension[0],dimension[1]
    if (i > 0):
        children.append([i-1,j])
    if (j > 0):
        children.append([i,j-1])
    if (j < int(max_j) -1):
        children.append([i,j+1])
    if (i < int(max_i) -1):
        children.append([i+1,j])

    return children

def validate_child(coordinate,health,map):
    if health <=0:
        return False;
    i,j = coordinate[0],coordinate[1]
    if map[i][j] == 'X' or map[i][j] == 'O':
        return False
    return True


def check_duplicate(q,node):
    n =list(node)
    for nn in q:
        t_n = list(nn)
        if t_n[0][0] == n[0][0] and t_n[0][1] == n[0][1] and int(t_n[2])== int(n[2]):
            return True
    return False

def gbfs():
    f_name = "large_map2.txt"
    res = initialize_map(f_name)
    map,v_map,shadow_frontier,dimension,start,goal = res[0],res[1],res[2],res[3],res[4],res[5]
    qualified_node_list = list()
    parent = dict()
    start_node = create_node(start,calculate_heuristic_cost(start,goal),5)
    frontier = list()
    frontier.append(start_node)
    qualified_node_list.append(start_node)
    count = 0
    goal_health = 0
    while len(frontier) > 0:
        node = frontier[0]
        p_coordinate, p_health = list(node[0]),int(node[-1])
        count = count + 1
        if p_health <= 0:
            frontier.remove(node)
        else:
            if map[p_coordinate[0]][p_coordinate[1]] == 'G':
                goal_health = p_health
                print "Reach Goal\n"
                break
            else:
                children = gen_validate_children(p_coordinate,dimension)
                for child in children:
                    health = calculate_health(child, map, p_health, dimension)
                    if validate_child(child,health,map):
                        h_cost = calculate_heuristic_cost(child, goal)
                        new_node = create_node(child, h_cost, health)
                        if not check_duplicate(qualified_node_list,new_node):
                            frontier.append(new_node)
                            qualified_node_list.append(new_node)
                            parent[tuple(child) + (health,)] = tuple(p_coordinate) + (p_health,)
                frontier = sorted(frontier,key=lambda x:(x[1],x[0][0],x[0][1],-x[-1]))
            frontier.remove(node)

    node_visited_count = count
    path = ""
    path_cost = 0
    p = tuple(goal) +(goal_health,)

    while p != None:
        c = list(p)
        path_cost = path_cost + get_cost(c, map)
        if p in parent:
            p = parent[p]
            if p[0] == c[0] and p[1] == c[1] + 1:
                path = 'W' + path
            elif p[0] == c[0] and p[1] == c[1] - 1:
                path = 'E' + path
            elif p[0] == c[0] - 1 and p[1] == c[1]:
                path = 'S' + path
            elif p[0] == c[0] + 1 and p[1] == c[1]:
                path = 'N' + path
        else:
            p = None

    print "Greedy Solution for " + f_name + ":\n"
    print "Path:"
    print path
    print ""
    print "Path length: " + str(len(path))
    print "Path Cost: " + str(path_cost)
    print "# Nodes Examined: " + str(node_visited_count)



def get_cost(node,map):
    tile = map[node[0]][node[1]]
    if tile == ' ':
        return 1
    elif tile == '*':
        return 3
    elif tile == 'S':
        return 1
    else:
        return 0

def show_stack(ss):
    s = list(ss)
    res = ""
    while len(s) > 0:
        print str(s.pop())
         #res = str(s.pop()) + "" + res;
    #return res

def main():
    gbfs()

if __name__ == '__main__':
    main()
