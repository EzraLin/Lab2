import statistics


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    number=input('Enter some numbers seperated by commas: ')
    print(number)
    splitter=number.split(",")
    print(splitter)
    num_list=[]
    for x in splitter:
        num_list.append(float(x))
    print(num_list)
    return num_list

def calc_average_temperature(num):
    total=sum(num)
    num_of_elements=len(num)
    average=total/num_of_elements
    print("The average value is " + str(average))

def calc_min_max_temperature(num):
    smallest=min(num)
    largest=max(num)
    print("The largest value is " + str(smallest))
    print("The smallest value is " + str(largest))

def calc_median_temperature(num):

    print("The median value is " + str(statistics.median(num)))


def main():
    num_list=get_user_input()
    calc_average_temperature(num_list)
    calc_min_max_temperature(num_list)
    calc_median_temperature(num_list)


if __name__ == "__main__":
    main()