import csv
import json

# from pprint import pprint


def show_teams():
    """
    This function output to console hierarchy of teams
    :return:
    """
    with open('./HW2/Corp_Summary.csv', 'r') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        hierarchy = {}
        for row in reader:
            if row[1] not in hierarchy:  # row[1] is a department
                hierarchy[row[1]] = [row[2]]  # row[2] is a team
            else:
                hierarchy[row[1]].append(row[2])

    for department, teams in hierarchy.items():
        hierarchy[department] = list(set(teams))

    print(json.dumps(hierarchy, indent=4, sort_keys=True, ensure_ascii=False).encode('utf8').decode())
    print()
    # pprint(hierarchy)


def depart_report(output: bool) -> dict:
    """
    This function output to console the information about each department.
    :param output: flag affecting printing
    :return: dict with the info
    """
    with open('./HW2/Corp_Summary.csv', 'r') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        departments = []
        for row in reader:
            if row[1] not in departments:
                departments.append(row[1])

        departs_info = dict.fromkeys(departments)
        for department in departments:
            departs_info[department] = {'number': 0,
                                        'min_salary': 1000000,
                                        'max_salary': 0,
                                        'average_salary': 0}

        f.seek(0)  # jump to the beginning
        next(reader)
        for row in reader:
            departs_info[row[1]]['number'] += 1
            departs_info[row[1]]['average_salary'] += int(row[5])
            if int(row[5]) < departs_info[row[1]]['min_salary']:
                departs_info[row[1]]['min_salary'] = int(row[5])
            if int(row[5]) > departs_info[row[1]]['max_salary']:
                departs_info[row[1]]['max_salary'] = int(row[5])

        for department in departments:
            if departs_info[department]['number'] != 0:
                avr = departs_info[department]['average_salary'] / departs_info[department]['number']
                departs_info[department]['average_salary'] = round(avr, 2)

        if output:
            for department in departs_info:
                print(f'{department}:')
                print(f'\tЧисленность - {departs_info[department]["number"]}')
                print(f'\tМинимальная зарплата - {departs_info[department]["min_salary"]}')
                print(f'\tМаксимальная зарплата - {departs_info[department]["max_salary"]}')
                print(f'\tСредняя зарплата - {departs_info[department]["average_salary"]}\n')

        return departs_info


def save_report(filename: str):
    """
    This function creates csv-file with the report of the second option of the menu.
    :param filename: string with name of the file
    :return:
    """
    departs_info = depart_report(output=False)
    fieldnames = ('Название', 'Численность', 'Минимальная зарплата', 'Максимальная зарплата', 'Средняя зарплата')

    with open(f'{filename}.csv', 'w') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(fieldnames)
        for department, parameters in departs_info.items():
            writer.writerow((
                department,
                parameters['number'],
                parameters['min_salary'],
                parameters['max_salary'],
                parameters['average_salary']
            ))


def start():
    """
    This function shows the menu and calls up the selected option.
    :return:
    """
    menu = (
        'Выберите пункт из меню:\n'
        '\t1. Вывести в понятном виде иерархию команд, т.е. департамент и все команды, которые входят в него\n'
        '\t2. Вывести сводный отчёт по департаментам: название, численность, "вилка" зарплат в виде мин – макс, '
        'среднюю зарплату\n'
        '\t3. Сохранить сводный отчёт из предыдущего пункта в виде csv-файла. При этом необязательно вызывать сначала '
        'команду из п.2\n'
        '\t4. Выход\n'
    )

    print(menu)
    item = input()
    while item != '4':
        if item == '1':
            show_teams()
        elif item == '2':
            depart_report(output=True)
        elif item == '3':
            print('Введите название csv-файла: ', end='')
            filename = input()
            save_report(filename=filename)
            print('Файл успешно сохранён.\n')
        elif item == '4':
            break
        else:
            print('Данный пункт отсутствует.')

        print(menu)
        item = input()


if __name__ == '__main__':
    start()
