def counter(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        result = func(count, *args, **kwargs)  # Передаем текущий count в функцию
        return
    return wrapper

@counter
def example_function(count):
    print(f"Function has been called {count} times")

# Примеры вызова
example_function()
example_function()
example_function()