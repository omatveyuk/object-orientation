"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   Abstraction:
    As a developer I don't need to know how a particular class is implemented.
    I just use it.
    Encapsulation:
    All attributes and methods, which describe class and it work, are packaged
    in one place
    Polymorphism:
    During the execution of a program if program doesn't see nessecary atrributes or
    methods in the derived class the program will use methods from the base class.

2. What is a class?
    in object oriented programming a class represents a structure of common
    atrributes and functions.

3. What is an instance attribute?
    Atribute of a concreate object already initialized

4. What is a method?
    Operations which performs action with attributes of class or abstract
    action related to a class

5. What is an instance in object orientation?
    if class is plan of a house and direction how to build a house, live
    in a house, use a hoouse, the instance will represent a real house.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   Class attribute is stored inside the class and is used unless an initialized
   object overwrites it.
   Instance attribute is created when an object is initialized.

"""


# Parts 2 through 5:
# Create your classes and class methods
class Student(object):
    """Information about student"""
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """Representation of a question and answer"""
    def __init__(self, question, answer):
        self.question = question
        self.correct_answer = answer

    def ask_and_evaluate(self):
        """Ask and evaluate answer.

            Print the question to the console and prompt the user for the answer.
            Return True if the answer is correct.
            Otherwise return False.
        """
        response = raw_input(self.question + " > ")
        return response.lower() == self.correct_answer.lower()


class Exam(object):
    """Representation questions for an exam"""
    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        """Make question and add it in list of questions for the exam"""
        self.questions.append(Question(question, correct_answer))

    def administer(self):
        """Administer all of the exam's questions and return the user score"""
        score = 0

        if len(self.questions) != 0:

            for question in self.questions:
                if question.ask_and_evaluate():
                    score += 1
            score = float(score) / len(self.questions)

        print score
        return score
