print("Hello")


def my_func():
    pass


def my_solution():
    print("solution")


def greet(name=None):
    if name is None:
        name = "World"
    print(f"Hello {name}!")


def run_greet():
    greet()
