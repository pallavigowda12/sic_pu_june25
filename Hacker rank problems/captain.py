def process_passes(n, initial_id, passes):
    stack = [initial_id]
    for move in passes:
        if move[0] == 'P':
            stack.append(int(move[1]))
        else:  # 'B'
            stack.pop()
    return f"Player {stack[-1]}"

# Example usage
n = 10
initial_id = 23
passes = [['P', '86'], ['P', '63'], ['P', '60'], ['B'], ['P', '47'], ['B'], ['P', '99'], ['P', '9'], ['B'], ['B']]
print(process_passes(n, initial_id, passes))  # Output: Player 9
