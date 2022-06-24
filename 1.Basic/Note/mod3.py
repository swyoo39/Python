# 변수 선언
PI = 3.141592

# 클래스 선언
class Math:
  # 함수 선언 - 클래스 안에 함수 선언시 self를 추가해야 함(현재 모듈 안에 있는 변수를 사용하겠다는 의미)
  def solve(self, r):
    return PI * (r ** 2)
  
  def sum(self, a, b):
    return a + b

if __name__ == "__main__":
  print(PI)
  a = Math()
  print(a.solve(2))
  print(a.sum(PI,4.4))