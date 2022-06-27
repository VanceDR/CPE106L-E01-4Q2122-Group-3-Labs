"""
File: student.py
Resources to manage a student's name and test scores.
"""

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

    def __eq__(self,other):
        return self.name == other.name
   
    def __lt__(self,other):
        return self.name < other.name
 
    def __ge__(self,other):
        return self.name >= other.name

def main():
   # First student
  student = Student("Ezra", 5)
  print(student)
  print("\nList populated..")
  for i in range(1, 6):
    student.setScore(i, 100)
  print(student)

  # Second student
  student2= Student("Phoebe",5)
  print(student2)
  print("\nList populated..")
  for i in range(1, 6):
    student2.setScore(i, 100)
  print(student2)

  # Checking comparisons
  print("\nEquality Method: ")
  print(student==student2)

  print("\nLess than Method: ")
  print(student<student2)

  print("\nGreater than or Equal Method: ")
  print(student>=student2)

# Calling main
if __name__ == "__main__":

  main()