# author: Kuznetsov Mikhail

from itertools import permutations

N = 4

# Filter 1: Генерация всех положений королев (сразу ичключая одинаковые строки и столбцы)
def queens_all_positions_filer():
    return permutations(range(N))

# Filter 2: Фильтрация из всех решений положения королев на общих диагоналях
def is_valid_solution(perm):
    for i in range(N):
        for j in range(i + 1, N):
            if abs(perm[i] - perm[j]) == abs(i - j):
                return False
    return True

def solutions_validation_filter(solutions):
    validated_solutions = []
    for solution in solutions:
        if is_valid_solution(solution):
            validated_solutions.append(solution)

    return validated_solutions

# Filter 3: Отображение решений
def print_solutions(solutions):
    print("Solutions cound:", len(solutions))
    for i, sol in enumerate(solutions):
        print("Solution:", i, "->", sol)
        for r in sol:
            print(' '.join(['Q' if i == r else '_' for i in range(N)]))

# Pipes
if __name__ == "__main__":
    positions = queens_all_positions_filer()
    valid_solutions = solutions_validation_filter(positions)
    print_solutions(valid_solutions)
