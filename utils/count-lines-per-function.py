import inspect
import guess_max_4
def main():
    functions = inspect.getmembers(guess_max_4, inspect.isfunction)
    for name, fn in functions:
        print(f"{name}: {len(inspect.getsourcelines(fn)[0])}")

if __name__ == '__main__':
    main()
