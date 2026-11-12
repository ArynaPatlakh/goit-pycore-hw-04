from pathlib import Path 

def total_salary(path):

    path = Path(__file__).parent / path

    print(path)
    total = 0
    employee = 0
    try: 
        with open(path, encoding="utf-8") as f:

            for line in f:

                name, salary = line.strip().split(",")
                total += int(salary)
                employee += 1
            
            if employee == 0:
                return (0, 0)
        
        return (total, round(total / employee, 2), )

    except (OSError, ValueError):
        return (0, 0,)

total, average = total_salary('salary.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
