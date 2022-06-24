def sum(a,b):
  if type(a) != type(b):
    print("더하기를 할 수 없습니다.")
  else:
    return a + b


# mod2.py 모듈에서 이 부분은 .py 파일만 실행 시켰을 때 main method가 실행될 때 어떤것을 해라 라는 의미 이다
# 우클릭하고 run python file in terminal 실행
if __name__ == "__main__":
  print(sum(10,20))