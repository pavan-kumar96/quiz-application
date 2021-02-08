from User import super_user,Candidate
from zauto import run_quiz_easy, questions
# from admin import admin_Question, questions
### Taking the Super_user Details(handling on;y 3 questions):



def user_details():
    name = input("please Enter the  name of the candidate\n")
    id = input("please Enter the id of the candidate\n")
    cad1 = Candidate(name, id)
    # print("Mr.{} with id {}".format(name, id))
    cad1.run_test()
    print("Mr.{} with id {}".format(name, id))

name = input("Please Enter the superuser name\n")
id = int(input("Please enter the super_user id\n"))
# password = input("please enter the Password")

if name == 'admin':
    # print("Mr.{} with id {}".format(name, id))

    run_quiz_easy(questions)
    print("Mr.{} with id {}".format(name, id))

else:
    test1 = super_user(name, id)
    print(test1)
    test1.addQuestion("Fruits and Colors","easy")
    test1.addQuestion("Fruits and Colors","easy")
    test1.addQuestion("Python","medium")
    test1.displayAllQuestions()
    user_details()



    


# c1=Candidate("S",2)
# print(c1)
# c1.viewTopics()
# c1.run_test()
