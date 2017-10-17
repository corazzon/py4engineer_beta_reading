# 클로저 예제
a = 3
def fetch_a():
    return a

if __name__ == "__main__":
    a = 5
    print(fetch_a())
