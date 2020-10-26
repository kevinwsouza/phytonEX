import sys

def validNumber (number):
  if number < 0 or number > 1:
    return False
  return True 

def selectWinner (alice, beta, clara):
  if(alice != beta and alice != clara):
    return print('A')
  elif(beta != clara and beta!= alice):
    return print('B')
  elif(clara != alice and clara != beta):
    return print('C')
  else:
    return print('*')

def main ():
  try:
    line = sys.stdin.readline()
    splitLine = line.split(' ')
    numberAlice = splitLine[0]
    numberBeta = splitLine[1]
    numberClara = splitLine[2]
    if(validNumber(int(numberAlice)) and validNumber(int(numberBeta)) and validNumber(int(numberClara))):
      selectWinner(int(numberAlice), int(numberBeta), int(numberClara))
    else:
      print('Erro')
  except:
    return 'Erro'
main()