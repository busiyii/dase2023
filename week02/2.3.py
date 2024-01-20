def is_valid_state(state):
    farmer, wolf, sheep, cabbage = state
    # 检查狼是否吃羊或者羊是否吃草
    if (wolf == sheep and farmer != wolf) or (sheep == cabbage and farmer != sheep):
        return False
    return True

def is_final_state(state):
    return state == (0, 0, 0, 0)

def generate_next_states(current_state):
    farmer, wolf, sheep, cabbage = current_state
    next_states = []
    # 农夫带自己过河
    new_state = (1 - farmer, wolf, sheep, cabbage)
    if is_valid_state(new_state):
        next_states.append(new_state)
    # 农夫带狼过河
    new_state = (1 - farmer, 1 - wolf, sheep, cabbage)
    if is_valid_state(new_state):
        next_states.append(new_state)
    # 农夫带羊过河
    new_state = (1 - farmer, wolf, 1 - sheep, cabbage)
    if is_valid_state(new_state):
        next_states.append(new_state)
    # 农夫带草过河
    new_state = (1 - farmer, wolf, sheep, 1 - cabbage)
    if is_valid_state(new_state):
        next_states.append(new_state)
    return next_states

def dfs(current_state, path):
    if is_final_state(current_state):
        print(path)
        return
    for next_state in generate_next_states(current_state):
        if next_state not in path:
            path.append(next_state)
            dfs(next_state, path)
            path.pop()

initial_state = (1, 1, 1, 1) 
path = [initial_state]
dfs(initial_state, path)