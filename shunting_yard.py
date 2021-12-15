input           = "3 + 3 * 3 - 3"
operator_stack  = []
output          = []

def has_greater_precedence(a,b):
  match a:
    case "+":
      return True if b in ["/","*","^","+","-"] else False
    case "-":
      return True if b in ["/","*","^","+","-"] else False
    case "*":
      return True if b in ["^"] else False
    case "/":
      return True if b in ["^"] else False

for element in input.split(" "):
  if element.isdigit():
    output.append(int(element))
  else:
    while operator_stack and has_greater_precedence(element,operator_stack[-1]):
      output.append(operator_stack.pop())
    operator_stack.append(element)

while operator_stack:
    output.append(operator_stack.pop())

answer = []
for element in output:
  if isinstance(element,int):
    answer.append(element)
  else:
    match element:
      case "-":
        pop1 = answer.pop()
        pop2 = answer.pop()
        answer.append(pop2 - pop1)
      case "+":
        pop1 = answer.pop()
        pop2 = answer.pop()
        answer.append(pop2 + pop1)
      case "*":
        pop1 = answer.pop()
        pop2 = answer.pop()
        answer.append(pop2 * pop1)
      case "/":
        pop1 = answer.pop()
        pop2 = answer.pop()
        answer.append(pop2 / pop1)
print("answer:" + str(answer))
