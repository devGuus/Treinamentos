# 3 valores com uma casa decimal, de dupla precisão (double).
A = float(input())
B = float(input())
C = float(input())
# A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5. (cada nota pode ir de 0 até 10.0)
media = ((A*2)+(B*3)+(C*5))/10
print("MEDIA = {:.1f}" .format(media))

