from tkinter import *

def eval(input):
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
      output.append(float(element))
    else:
      while operator_stack and has_greater_precedence(element,operator_stack[-1]):
        output.append(operator_stack.pop())
      operator_stack.append(element)
  while operator_stack:
      output.append(operator_stack.pop())

  answer = []
  for element in output:
    if isinstance(element,float):
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
  return answer[-1]

window = Tk()

(width,height) = (180,160)
window.geometry(f"{width}x{height}")

txt = Entry(window,width=10)
txt.grid(column=0, row=0,columnspan=4)

def add_to_entry(value):
  txt.insert(len(txt.get()),  value)

def eval_all():
  res = eval(txt.get())
  txt.delete(0,'end')
  txt.insert(0,res)

btns = [['7','8','9','<<'],['6','5','4',' * '],[' - ','3','2','1'],['=',' + ','/','0']]

for x in range(1,5):
  for y in range(4):
    if x == 4 and y == 0:
      btn = Button(window,width=2, text=btns[x-1][y], command=lambda: eval_all())
    else if x == 1 and y == 3:
      btn = Button(window,width=2, text=btns[x-1][y], command=lambda v=btns[x-1][y]: add_to_entry(v))
    else:
      btn = Button(window,width=2, text=btns[x-1][y], command=lambda v=btns[x-1][y]: add_to_entry(v))
    btn.grid(column=y, row=x)

window.mainloop()
