from tkinter import *

def evaluate(input_string):
  operator_stack  = []  #  this is where we will store the operators
  output          = []  #  here we will build the result

  def has_greater_precedence(operator_a,operator_b):#returns if operator_a has a higher precedence than operator_b
    match operator_a:
      case "+":
        return True if operator_b in ["/","*","^","+","-"] else False
      case "-":
        return True if operator_b in ["/","*","^","+","-"] else False
      case "*":
        return True if operator_b in ["^"] else False
      case "/":
        return True if operator_b in ["^"] else False

  for element in input_string.split(" "): # splits the input in to a list of numbers and operators, e.g. "1+2" into ["1","+","2"] and loop over every element in that list
    if element.isdigit():
      output.append(float(element))  #  add it to the output stack
    else:  #  if the current element is not a digit (it must be an operator)
      while operator_stack and has_greater_precedence(element,operator_stack[-1]):  #  as long as there are elements in the operator stack, and the current element has higher precedence than the element on top of the stack
        output.append(operator_stack.pop())  #  remove the last element from the operator stack to the output stack
      operator_stack.append(element)  #  push the current element to the operator stack
  #we're done! push all the remaining elements still in the operator stack to the output stack
  while operator_stack:
      output.append(operator_stack.pop())
  #at this point the elements in the output stack are in reverse polish notation, and we can easily evaluate the input expression this way
  answer = []
  for element in output:#loop over elements in the output stack
    if isinstance(element, float):#if that element is a float
      answer.append(element)#add it to the answer queue
    else:#if not (meaning, it's an operator)
      match element:#check which type of operator it is
        case "-":#if it's a minus, get the top two numbers form the answer stack
          pop1 = answer.pop()
          pop2 = answer.pop()
          answer.append(pop2 - pop1)#after that, push back the result to the answer stack
        case "+":#the other cases do the same as the minus
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
  return answer[-1]#after this, the answer is at the top of the answer stack

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
