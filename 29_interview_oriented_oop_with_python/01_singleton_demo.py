class SingletonBasicDemo():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SingletonBasicDemo, cls).__new__(cls)

        return cls._instance


first_instance = SingletonBasicDemo()
second_instance = SingletonBasicDemo()


print(id(first_instance))
print(id(second_instance))


print(first_instance is second_instance)
