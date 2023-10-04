from src import utils


def main():
    data = utils.load_operations('operations.json')
    data = utils.find_completed_operations(data)
    data = utils.sort_by_date(data)
    data = utils.get_formatted_data(data)
    for pay in data:
        print(pay)


if __name__ == '__main__':
    main()

