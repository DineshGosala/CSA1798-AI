from itertools import permutations
def solve_cryptarithmetic(puzzle):
    letters = set([char for char in puzzle if char.isalpha()])
    if len(letters) > 10:
        return "Invalid puzzle - Too many letters"
    for perm in permutations('0123456789', len(letters)):
        mapping = dict(zip(letters, perm))
        if mapping[puzzle[0]] =='0'or mapping[puzzle[len(puzzle)//2+1]] =='0':
            continue
        equation = puzzle.translate(str.maketrans(mapping))
        if eval(equation):
            return {letter: int(mapping[letter]) for letter in letters}
    return "No solution found"
puzzle = "MOON + SOON + JUNE"
solution = solve_cryptarithmetic(puzzle)
if isinstance(solution, dict):
    print("Solution found:")
    for key, value in solution.items():
        print(f"{key} = {value}")
else:
    print(solution)
