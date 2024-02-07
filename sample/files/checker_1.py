import sys

# Получаем пути к файлам.
test_file = sys.argv[1]
solution_result_file = sys.argv[2]
answer_file = sys.argv[3]

delta = 1e-2
task_cost = 1

with open(solution_result_file) as sol_file, open(answer_file) as ans_file:
    s = sol_file.readlines()
    a = ans_file.readlines()

if len(a) != len(s):
    print(
        f"0 Wrong answer. Number of lines differs from the answer.\n Your solution contains {len(s)} lines, while the answer contains {len(a)} lines."
    )
    sys.exit(1)

for i in range(len(s)):
    s[i] = s[i].strip()
    a[i] = a[i].strip()

    try:
        if not abs(float(s[i]) - float(a[i])) < delta:
            print(f"0 Wrong answer.\n Your answer {float(s[i])} differs from {float(a[i])} by more than {delta}.")
            sys.exit(1)
    except:  # noqa: E722
        if s[i] != a[i]:
            print(f"0 Wrong answer.\n Your answer {s[i]} differs from {a[i]}")
            sys.exit(1)

print(f"{task_cost} OK")
sys.exit(0)
