def test(function):
    # * Decorator that logs before/after and returns the wrapped function
    def wrapper(*args, **kwargs):
        print("인사가 시작되었습니다.")
        result = function(*args, **kwargs)
        print("인사가 종료되었습니다.")
        return result
    return wrapper

@test
def hello():
    print("hello")

hello()