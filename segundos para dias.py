import sys


def main ():
  line = sys.stdin.readline()
  try :
    line = int(line)
    if (line < 0 or line > 864000):
      print('ERRO')
    else:
      days = line // 86400
      hours = (line % 86400) // 3600
      restHours = (line % 86400) % 3600
      minutes = restHours // 60
      seconds = (restHours % 60)
      print("%02dd%02dh%02dm%02ds" % (days, hours, minutes, seconds))
  except:
    print('ERRO')

main()