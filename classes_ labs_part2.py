class Student:
    def __init__(self, first, last, age, current_class):
        self.first = first
        self.last = last
        self.age = age
        self.current_class = current_class
        self.test_scores = []

    def fullname(self):
        return self.first + " " + self.last

    def add_test_score(self, score):
        self.test_scores.append(score)

    def calculate_average_test_score(self):
        if not self.test_scores:
            return 0
        return sum(self.test_scores) / len(self.test_scores)

student1 = Student("Dan", "Smith", 10, "Math")

student1.add_test_score(85)
student1.add_test_score(90)
student1.add_test_score(88)

print("Average test score for {}: {}".format(student1.fullname(), student1.calculate_average_test_score()))
