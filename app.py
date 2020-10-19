print("Title of program: Helping you find the best CCA for your secondary school life!")
print()
print("Welcome to DHS! Please answer the following questions truthfully such that we can suggest the beter CCA option for you!")
print("Please respond with a number 1 - 5, where 1 is strongly disagree and 5 is strongly agree.")
print()


music1 = input("I am able to play a musical instrument well.")

tech1 = input("I enjoy constructing and fixing things.")

outdoor1 = input("I'll be mad if I do not go out of house for the whole day .")

music2 = input("I can visualise different colours when i hear music.")

tech2 = input("I know how to make my own online apps and websites.")

outdoor2 = input("I enjoy exercising.")

music3 = input(" I enjoy watchig concerts.")

outdoor3 = input("NAPFA is easy to pass.")

tech3 = input("I enjoy coding.")


tech_final = int(tech1) + int(tech2) + int(tech3)
outdoor_final = int(outdoor1) + int(outdoor2) + int(outdoor3)
music_final = int(music1)+ int(music2) + int(music3)

print()

if tech_final > outdoor_final and tech_final > music_final:
  print("You should join Infocomm club!")
elif outdoor_final > music_final:
  print("A sport CCA is the best choice for you!")
else:
  print("Band or Chinese Ochestra would be the better choice for you!")
