Amount=int(input("How much do you want to draw?"))
note_1=Amount//100
note_2=(Amount%100)//50
note_3=((Amount%100)%50)//10
print("note of 100 rupee", note_1)
print("note of 50 rupee", note_2)
print("note of 10 rupee", note_3)
