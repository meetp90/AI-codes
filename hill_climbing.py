import random

def generate_states(state):
    queen = random.randint(0,len(state) - 1)
    new_pos = random.randint(0,len(state) - 1)
    new_state = state.copy()
    new_state[new_pos] = queen
    return new_state

def cost(state):
    attack = 0
    for i in range(len(state)):
        for j in range(i+1,len(state)):
            if state[i] == state[j]:
                attack += 1
            elif abs(i - j) == abs(state[i] - state[j]):
                attack += 1
    return attack

def hill_climbing(f,initial_state,max_iterations = 1000):
    state = initial_state
    for _ in range(max_iterations):
        new_state = generate_states(state)
        if f(new_state) < f(state):
            state = new_state
    return state

N = 8
initial_state = [random.randint(0,N-1) for _ in range(N)]
solution = hill_climbing(cost,initial_state)
print(cost(initial_state))
print(solution)
print(cost(solution))