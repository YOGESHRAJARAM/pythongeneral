import random
num="12345678"
wor="gjduiejdgyur"
total=num+wor
srt1=""
for i in range (8):
    pas_word=random.choice(total)
    srt1+=pas_word
print(srt1)