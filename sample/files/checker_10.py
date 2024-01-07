import sys

# Получаем пути к файлам.
test_file = sys.argv[1]
solution_result_file = sys.argv[2]
answer_file = sys.argv[3]

delta = 1e-2
task_cost = 10

sol_file = open(solution_result_file, mode="r")
ans_file = open(answer_file, mode="r")
s = sol_file.readlines()
a = ans_file.readlines()

for i in range(len(s)):
    s[i] = s[i].strip()
    a[i] = a[i].strip()

    try:
        s[i] = float(s[i])
        a[i] = float(a[i])
        if not abs(s[i] - a[i]) < delta:
            print(
                f"0 Wrong answer. Your answer {s[i]} differs from {a[i]} by more than {delta}."  # noqa: E501
            )
            sys.exit(1)
    except:  # noqa: E722
        if not s[i].lower() == a[i].lower():
            print(
                f"0 Wrong answer. Your answer {s[i]} differs from {a[i]}."  # noqa: E501
            )
            sys.exit(1)

print(f"{task_cost} OK")
sys.exit(0)
