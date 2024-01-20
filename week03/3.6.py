score = int(input())

if score < 60:
    grade = "不合格"
elif score >= 60 and score <= 74:
    grade = "合格"
elif score >= 75 and score <= 89:
    grade = "良好"
else:
    grade = "优秀"

print(grade)
