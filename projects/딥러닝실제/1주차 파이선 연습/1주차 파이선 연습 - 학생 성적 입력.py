STUDENT = 5

scores = []
scoreSum = 0

for i in range(STUDENT):
  value = int(input("성적을 입력하시오: "))
  scores.append(value)
  scoreSum += value

scoreAvg = scoreSum / len(scores)

highScoreStudents = 0
for i in range(len(scores)):
  if score[i] >= 80:
    high