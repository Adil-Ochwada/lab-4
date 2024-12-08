from itertools import combinations

items = [
    ('rifle', 'r', 3, 25),
    ('pistol', 'p', 2, 15),
    ('ammo', 'a', 2, 15),
    ('medkit', 'm', 2, 20),
    ('knife', 'k', 1, 15),
    ('axe', 'x', 3, 20),
    ('talisman', 't', 1, 25),
    ('flask', 'f', 1, 15),
    ('supplies', 's', 2, 20),
    ('crossbow', 'c', 2, 20)
]

initial_points = 15  
max_cells = 7        

def evaluate_combination(combo):
    total_size = sum(item[2] for item in combo) 
    total_points = sum(item[3] for item in combo)  
    return total_size, total_points

valid_combinations = []
for r in range(1, len(items) + 1):
    for combo in combinations(items, r):
        total_size, total_points = evaluate_combination(combo)
        if total_size <= max_cells and (initial_points + total_points) > 0:
            valid_combinations.append(combo)

formatted_combinations = []
for combo in valid_combinations:
    combo_list = [item[1] for item in combo]  
    total_points = initial_points + sum(item[3] for item in combo)
    formatted_combinations.append((combo_list, total_points))

if formatted_combinations:
    print(f"Found {len(formatted_combinations)} valid combinations:\n")
    for combo, points in formatted_combinations:
        print(f"Items: {combo}, Survival Points: {points}")
else:
    print("Ноль является доказательством отсутствия комбинаций")
#look
