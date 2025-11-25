class ClassInstanceCountDemo():
    cur_class_instance_count = 0

    def __new__(cls, *args, **kwargs):
        cls.cur_class_instance_count += 1
        return super(ClassInstanceCountDemo, cls).__new__(cls)


first_instance = ClassInstanceCountDemo()
second_instance = ClassInstanceCountDemo()

print(ClassInstanceCountDemo.cur_class_instance_count)

# Using global count

class_instance_count = 0


class ClassInstanceCountDemoWithGlobalCount():
    def __new__(cls, *args, **kwargs):
        global class_instance_count
        class_instance_count += 1
        return super(
            ClassInstanceCountDemoWithGlobalCount, cls
        ).__new__(cls)


first_instance = ClassInstanceCountDemoWithGlobalCount()
second_instance = ClassInstanceCountDemoWithGlobalCount()

print(class_instance_count)
