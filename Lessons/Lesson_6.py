# @staticmethod
# def action()



def simple_decorator(func):
    def wrapper():
        print("До выполнения!!")
        func()
        print("После выполнения!!")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello world!!")

# say_hello()

def greeting_decorator(func):
    def wrapper(data):
        print(f"Hi {data}!!")
        func(data)
    return wrapper

@greeting_decorator
def test(name):
    print(f"How are you {name}?")

# test("Ardager")

def repeat_decorator(n):
    def decorator(func):
        def wrapper(name):
            for i in range(n):
                func()
        return wrapper
    return decorator

@repeat_decorator(10)
def hi(name):
    print('Hi')

# hi()


def class_decorator(cls):
    class NewClass(cls):
        def action(self):
            print('New action!!')
    return NewClass

@class_decorator
class OldClass:
    def action(self):
        print('Old action!!')

test_obj = OldClass()

# test_obj.action()

# print(type(test_obj))


def is_admin(func):
    def wrapper(user):
        if user.role == "admin":
            func()
        else:
            print("Вы не админ!!")
        return wrapper



# def binary_search(array, target):
#     left, right = 0, len(array) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         print(f"MID: {mid}")
#         if array[mid] == target:
#             return print("OK")
#         elif array[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     print("не нашли!!")
# my_list = [1,2,3,4,5,6,7,8,9,10]
# binary_search(my_list, 10)


# my_list = [2,7,11,15]
target = 9
def two_sum(array, num):
    num_map = {
    #     2:0
    }
    for i in range(len(array) -1):
        print(f" I = {i}")
        current_num = array[i]
        complement = num - current_num
        if complement in num_map:
            return print(f"нашли {[num_map[complement], i]}")
        num_map[current_num] = i

    return print("Не нашли!!")

# two_sum(my_list, target)

my_tuple = (1,2,3,4)
# 4
my_tuple_2 = (1,2,3,4)
my_list = [1,2,3,4] # 4
my_list_2 = [1,2,3,4] # 4

# print(my_tuple is my_tuple_2)
# print(my_tuple_2 is my_list)

# test_1 = 0.1 + 0.2
# test_2 = 0.3
#
# print(test_1 == test_2)