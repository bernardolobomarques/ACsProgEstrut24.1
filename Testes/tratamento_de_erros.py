def func1():
#   print(5 / 0)
    pass

def func2():
  func1()

def func3():
  func2()

func3()

print("-" * 30)

while True:
  num = None
  try:
    num = int(input("Informe um número: "))
  except (ValueError, KeyboardInterrupt):
    print("Dado inválido! Tente novamente!")
  else:
    break
  finally:
    print("-" * 15)