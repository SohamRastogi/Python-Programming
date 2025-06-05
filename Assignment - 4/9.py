class CustomWrapperException(Exception):
       def __init__(self, original_exception):
        self.original_exception = original_exception
        super().__init__(f"Wrapped Exception: {str(original_exception)}")


class Wrapper:
    def __init__(self, wrapped_class, *args, **kwargs):
        self._wrapped_instance = wrapped_class(*args, **kwargs)  

    def __getattr__(self, attr):
        original_attr = getattr(self._wrapped_instance, attr)  

        if callable(original_attr):  
            def wrapped_method(*args, **kwargs):
                try:
                    return original_attr(*args, **kwargs)  
                except Exception as e:
                    raise CustomWrapperException(e)  

            return wrapped_method  
        return original_attr  

class SampleClass:
    def divide(self, a, b):
        return a / b  

    def raise_error(self):
        raise ValueError("An intentional error occurred!")


wrapped_instance = Wrapper(SampleClass)

try:
    print(wrapped_instance.divide(10, 0)) 
except CustomWrapperException as e:
    print(f"Caught Custom Exception: {e}")

try:
    wrapped_instance.raise_error()  
except CustomWrapperException as e:
    print(f"Caught Custom Exception: {e}")
