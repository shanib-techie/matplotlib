import matplotlib.pyplot as plt
# hour_studies = [1,2,3,4,5,6,7,8]
# exam_score = [50,54,33,15,88,66,55,45]
# plt.scatter(hour_studies,exam_score,color="green",marker="^",label = "student data")#mark="o","s","^","+","d"

# plt.xlabel("hour_studies")
# plt.ylabel("exam_score")

# plt.title("relationship between study_hours & marks_score")
# plt.legend()
# plt.grid()
# plt.show()


# make scatter graph for compare two section

plt.scatter([1,2,3],[50,30,12],color="orange",label="class A")
plt.scatter([1,2,3],[40,22,10],color="pink",label="class B")
plt.xlabel("hour_studies")
plt.ylabel("exam_score")
plt.title("RELATION BETWEEN TWO SECTION",color="orange")
plt.legend()
plt.grid()
plt.show()
