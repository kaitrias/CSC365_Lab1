
def parse_input(input_string):
   parsed = input_string.split(' ')
   return parsed

def main():
   entry = "q"
   while entry != "Q:" and  entry != "Quit:":
      user_input = input ("Input a search command: ")
      parsed_input = parse_input(user_input)
      entry = parsed_input[0]
      if (entry == "S:" or entry == "Student:"):
         print ('S')
         break
      elif (entry == 'T' or entry == "Teacher"):
         print ('T')
         break
      elif (entry == 'B' or entry == "Bus"):
         print('B')
         break
      elif (entry == 'G' or entry == "Grade"):
         print('G')
         break
      elif (entry == 'A' or entry == "Average"):
         print('A')
         break
      elif (entry == 'I' or entry == "Info"):
         print('I')
         break
   return

if __name__ == '__main__':
   main()
