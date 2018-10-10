import time

nomen_num = {0: 'zero', 
     1: 'one', 
     2: 'two', 
     3: 'three', 
     4: 'four', 
     5: 'five', 
     6: 'six', 
     7: 'seven', 
     8: 'eight', 
     9: 'nine'}

class RangeException(Exception):
  def __init__(self,text):
        RangeException.txt = text

def first_task(x, y=''):
  """
Вход:2 аргумента (1 опционален)
Выход: название числа (1 аргумент)
Условие: if 2 аргумент type = bin, oct, hex, то 
преобразование числа в выбранную систему счисления. 
Прим: фиксируется момент времени начала выполнения и наличие исключения
Форма: данные записываются в файл 
  """
  start_time = time.ctime(time.time())
  logger = []
  logger.append("Time of start: " + start_time)
  
  nomen_sys = {'bin': bin(x),
       'oct': oct(x),
       'hex': hex(x)}

  result = ['Null']
    
  if x in nomen_num.keys():
    result.clear()
    result.append(nomen_num.get(x))
    if y in nomen_sys.keys():
        result.append(nomen_sys.get(y))
    elif y != '':
        print('Select number system: hex/bin/oct')
        logger.append("ConvertTypeException")
      
  else:
     print('Enter the number from 0 to 9')
     logger.append("RangeException")

  if len(logger) == 1:   
     logger.append("Not found!")
  try:
    with open('newfile.txt', 'a') as f:
      f.write(str(logger) + "\n")
  except IOError:
    print("Read/write file error") 
  return result

def tests():
  assert first_task(9,'hex') == ['nine','0x9'], 'Not in order'
  assert first_task(0) == ['zero'], 'No match for expected'

if __name__ == "__main__":
   x = int(input('Enter the first argument:'))
   y = input('Enter the second argument(optional):')
   # tests() 
   print(first_task(x,y))
