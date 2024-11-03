import inspect


def introspection_info(obj):
    info = {
        'type': type(obj).__name__,
        'attributes': [],
        'methods': [],
        'module': getattr(obj, '__module__', None)
    }

    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)

        if callable(attr):
            info['methods'].append(attr_name)
        else:
            info['attributes'].append(attr_name)

    return info


class Example:
    def __init__(self, value):
        self.value = value

    def example_method(self):
        return f"Value is {self.value}"


example_obj = Example(42)
result = introspection_info(example_obj)
print(result)
