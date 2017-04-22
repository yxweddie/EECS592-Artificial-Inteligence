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

def create_node(coordinate, p_cost,h_cost, health):
    total_cost = p_cost + h_cost
    node = (coordinate,) + (total_cost,) + (p_cost,) + (h_cost,) + (health,)
    return node

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
    if health <= 0:
        return False;
    i,j = coordinate[0],coordinate[1]
    if map[i][j] == 'X' or map[i][j] == 'O':
        return False
    return True


def check_duplicate(q,node):
    n =list(node)
    for nn in q:
        t_n = list(nn)
        if t_n[0][0] == n[0][0] and t_n[0][1] == n[0][1] and int(t_n[4])== int(n[4]):
            return True
    return False

def update_total_cost(queue,node_coordinate,t_cost,health,p_coordinate,p_health,parent):
    for i in range(0, len(queue)):
        n = list(queue[i])
        if int(n[0][0]) == int(node_coordinate[0]) and int(n[0][1]) == int(node_coordinate[1]) and health == int(n[4]):
            if t_cost < int(n[1]):
                new_node = list(n)
                new_node[1] = t_cost
                queue.remove(tuple(n))
                queue.append(tuple(new_node))
                #parent[tuple(node_coordinate) + (health,)] = tuple(p_coordinate) + (p_health,)
                break
    #return False
def calculate_heuristic_cost_zero(current_position,goal_position):
    return 0

def a_star_zero(f_name):
    res = initialize_map(f_name)
    map,v_map,shadow_frontier,dimension,start,goal = res[0],res[1],res[2],res[3],res[4],res[5]
    qualified_node_list = list()
    parent = dict()
    start_node = create_node(start,0,calculate_heuristic_cost_zero(start,goal),5)
    frontier = list()
    frontier.append(start_node)
    qualified_node_list.append(start_node)
    count = 0
    goal_health = 0
    while len(frontier) > 0:
        count = count + 1
        node = frontier[0]
        p_coordinate, p_pcost,p_health = list(node[0]),int(node[2]),int(node[-1])
        if p_health <= 0:
            frontier.remove(node)
        else:
            frontier.remove(node)
            if map[p_coordinate[0]][p_coordinate[1]] == 'G':
                goal_health = p_health
                print "Reach Goal\n"
                break
            else:
                children = gen_validate_children(p_coordinate,dimension)
                for child in children:
                    health = calculate_health(child, map, p_health, dimension)
                    if validate_child(child,health,map):
                        c_cost = p_pcost + get_cost(p_coordinate, map)
                        h_cost = calculate_heuristic_cost_zero(child, goal)
                        new_node = create_node(child, c_cost, h_cost, health)
                        if not check_duplicate(qualified_node_list,new_node):
                            frontier.append(new_node)
                            qualified_node_list.append(new_node)
                            parent[tuple(child) + (health,)] = tuple(p_coordinate) + (p_health,)
                        else:
                            update_total_cost(frontier,child,c_cost+h_cost,health,p_coordinate,p_health,parent)
                frontier = sorted(frontier,key=lambda x:(x[1],x[0][0],x[0][1],-x[-1]))
    return count

def calculate_heuristic_cost_mahattan(current_position,goal_position):
    row_diff = abs(int(goal_position[0]) - int(current_position[0]))
    col_diff = abs(int(goal_position[1]) - int(current_position[1]))
    return (row_diff + col_diff)

def a_star_manhattan(f_name):
    res = initialize_map(f_name)
    map,v_map,shadow_frontier,dimension,start,goal = res[0],res[1],res[2],res[3],res[4],res[5]
    qualified_node_list = list()
    parent = dict()
    start_node = create_node(start,0,calculate_heuristic_cost_mahattan(start,goal),5)
    frontier = list()
    frontier.append(start_node)
    qualified_node_list.append(start_node)
    count = 0
    while len(frontier) > 0:
        count = count + 1
        node = frontier[0]
        #print show_stack(frontier)
        p_coordinate, p_pcost, p_health = list(node[0]),int(node[2]),int(node[-1])

        if p_health <= 0:
            frontier.remove(node)
        else:
            if map[p_coordinate[0]][p_coordinate[1]] == 'G':
                print "Reach Goal\n"
                break
            else:
                children = gen_validate_children(p_coordinate,dimension)
                for child in children:
                    health = calculate_health(child, map, p_health, dimension)
                    if validate_child(child,health,map):
                        h_cost = calculate_heuristic_cost_mahattan(child, goal)
                        c_cost = p_pcost + get_cost(p_coordinate, map)
                        new_node = create_node(child, c_cost, h_cost, health)
                        if not check_duplicate(qualified_node_list,new_node):
                            frontier.append(new_node)
                            qualified_node_list.append(new_node)
                            parent[tuple(child) + (health,)] = tuple(p_coordinate) + (p_health,)
                        else:
                            update_total_cost(frontier, child, c_cost + h_cost, health, p_coordinate, p_health, parent)
                frontier = sorted(frontier,key=lambda n:(n[1],n[0][0],n[0][1],-n[-1]))
            frontier.remove(node)
    return count

def calculate_heuristic_cost_east(current_position,goal_position):
    row_diff = abs(goal_position[0] - current_position[0]) * (1/4)
    col_diff = abs(goal_position[1] - current_position[1])
    return (row_diff + col_diff)

def a_star_east(f_name):
    res = initialize_map(f_name)
    map,v_map,shadow_frontier,dimension,start,goal = res[0],res[1],res[2],res[3],res[4],res[5]
    qualified_node_list = list()
    parent = dict()
    start_node = create_node(start,0,calculate_heuristic_cost_east(start,goal),5)
    frontier = list()
    frontier.append(start_node)
    qualified_node_list.append(start_node)
    count = 0
    goal_health = 0
    while len(frontier) > 0:
        count = count + 1
        node = frontier[0]
        p_coordinate, p_pcost,p_health = list(node[0]),int(node[2]),int(node[-1])
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
                        h_cost = calculate_heuristic_cost_east(child, goal)
                        c_cost = p_pcost + get_cost(p_coordinate, map)
                        new_node = create_node(child, c_cost, h_cost, health)
                        if not check_duplicate(qualified_node_list,new_node):
                            frontier.append(new_node)
                            qualified_node_list.append(new_node)
                            parent[tuple(child) + (health,)] = tuple(p_coordinate) + (p_health,)
                        else:
                            update_total_cost(frontier, child, c_cost + h_cost, health, p_coordinate, p_health, parent)
                frontier = sorted(frontier,key=lambda x:(x[1],x[0][0],x[0][1],-x[-1]))
            frontier.remove(node)

    return count

def calculate_heuristic_cost_wall(current_position,goal_position,dimension,map):
    c_i,c_j = int(current_position[0]),int(current_position[1])

    if map[c_i][c_j+1] == ' ' or map[c_i][c_j+1] == '*':
        return calculate_heuristic_cost_mahattan(current_position,goal_position)
    elif (map[c_i-1][c_j] == 'X' or map[c_i-1][c_j] == 'O') and (map[c_i+1][c_j] == 'X' or map[c_i+1][c_j] == 'O'):
        return  calculate_heuristic_cost_mahattan(current_position,goal_position)
    elif int(c_j) == int(goal_position[1]):
        return calculate_heuristic_cost_mahattan(current_position,goal_position)
    elif find_fist_east_tile('N',current_position,dimension,goal_position,map) == -1 and \
                    find_fist_east_tile('S',current_position,dimension,goal_position,map) == -1:
        return calculate_heuristic_cost_mahattan(current_position,goal_position)
    else:
        north,south = 1000,1000

        n_i = find_fist_east_tile('N',current_position,dimension,goal_position,map)
        s_i = find_fist_east_tile('S',current_position,dimension,goal_position,map)

        if n_i != -1 :
            north = abs(c_i - n_i) + calculate_heuristic_cost_mahattan([n_i,c_j],goal_position)
        if s_i != -1:
            south = abs(c_i - s_i) + calculate_heuristic_cost_mahattan([s_i,c_j],goal_position)

        return min(north,south)


def find_fist_east_tile(direction,start,dimension,goal_position,map):
    max_i,max_j = int(dimension[0]),int(dimension[1])
    start_i, start_j = int(start[0]),int(start[1])

    find_east = False
    if direction == 'N':
        while start_i > 0:
            if map[start_i-1][start_j] == ' ' or map[start_i-1][start_j] == '*':
                start_i = start_i -1
                if map[start_i][start_j+1] == ' ' or map[start_i][start_j+1] == '*':
                    find_east = True
                    break
            else:
                break

        if find_east :
            return int(start_i)

    elif direction == 'S' :
        while start_i < int(max_i):
            if map[start_i + 1][start_j] == ' ' or map[start_i+1][start_j] == '*':
                start_i = start_i +1
                if map[start_i][start_j+1] == ' ' or map[start_i][start_j+1] == '*':
                    find_east = True
                    break
            else:
                break
        if find_east :
            return int(start_i)

    return -1

def a_star_wall(f_name):
    res = initialize_map(f_name)
    map,v_map,shadow_frontier,dimension,start,goal = res[0],res[1],res[2],res[3],res[4],res[5]
    qualified_node_list = list()
    parent = dict()
    start_node = create_node(start,0,calculate_heuristic_cost_wall(start,goal,dimension,map),5)
    frontier = list()
    frontier.append(start_node)
    qualified_node_list.append(start_node)
    count = 0
    while len(frontier) > 0:
        node = frontier[0]
        p_coordinate, p_pcost, p_health = list(node[0]),int(node[2]),int(node[-1])
        count = count + 1
        if p_health <= 0:
            frontier.remove(node)
        else:
            if map[p_coordinate[0]][p_coordinate[1]] == 'G':
                print "Reach Goal\n"
                break
            else:
                children = gen_validate_children(p_coordinate,dimension)
                for child in children:
                    health = calculate_health(child, map, p_health, dimension)
                    if validate_child(child,health,map):
                        h_cost = calculate_heuristic_cost_wall(child, goal, dimension, map)
                        c_cost = p_pcost + get_cost(p_coordinate, map)
                        new_node = create_node(child, c_cost, h_cost, health)
                        if not check_duplicate(qualified_node_list,new_node):
                            frontier.append(new_node)
                            qualified_node_list.append(new_node)
                            parent[tuple(child) + (health,)] = tuple(p_coordinate) + (p_health,)
                        else:
                            update_total_cost(frontier, child, c_cost + h_cost, health, p_coordinate, p_health, parent)
                frontier = sorted(frontier,key=lambda x:(x[1],x[0][0],x[0][1],-x[-1]))
            frontier.remove(node)
    return count


def get_cost(node,map):
    tile = map[int(node[0])][int(node[1])]
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
        #print str(s.pop())
        res =  str(s.pop()) + res
    return res

def main():
    f_name = "large_map2.txt"
    count_zero = a_star_zero(f_name)
    count_manh = a_star_manhattan(f_name)
    count_east = a_star_east(f_name)
    count_wall = a_star_wall(f_name)

    print "Heuristic Solution for " + f_name + ":\n"
    #print "# Nodes Examined: "
    print "1 Zero: " + str(count_zero)
    print "2 Manh: " + str(count_manh)
    print "3 East: " + str(count_east)
    print "4 Wall: " + str(count_wall)

if __name__ == '__main__':
    main()
