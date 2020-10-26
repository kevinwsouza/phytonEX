import sys

def main ():
  numberLines = sys.stdin.readline()
  numbers = []
  typeList = ''
  numberLines = int(numberLines)
  if(numberLines % 2 == 0):
    typeList = 'pair'
  else:
    typeList = 'odd'
  while(numberLines > 0):
    newNumber = sys.stdin.readline()
    numbers.append(newNumber)
    numberLines = numberLines - 1 
  ordenedArray = sorted(numbers)
  if(typeList == 'odd'):
    numberMedian = (len(ordenedArray) // 2)
    print(ordenedArray[numberMedian])
  else:
    indexMedian = (len(ordenedArray) // 2) + 1
    indexMediaTwo = (len(ordenedArray) // 2) 
    numberMedian = ((int(ordenedArray[indexMedian] + int(ordenedArray[indexMediaTwo])) / 2)
    print(numberMedian)



main()
