#This quiz has 3 levels easy, medium and harder and has to fill in the blanks to win it.
quiz_easy_answer = {'__1__':"website", '__2__':"web", '__3__':"Internet", '__4__':"LAN",'__5__':"URL"}
quiz_easy_para = """A __1__ is a collection of related __2__ pages, including multimedia content,
typically identified with a common domain name, and published on at least one
__2__ server. Notable examples are wikipedia.org, google.com, and amazon.com.
Today roughly 380 new websites are created every minute across the World.

A __1__ may be accessible via a public __3__ Protocol (IP) network, such as
the __3__, or a private local area network (__4__), by referencing a
uniform resource locator (__5__) that identifies the site. """

quiz_medium_answer = {'__1__':"css", '__2__':"editor", '__3__':"code", '__4__':"browser", '__5__':"hyper", '__6__':"HTTP"}
quiz_medium_para = """When you're making your first website, there's a lot to do! As well as writing
your HTML and __1__ code. HTML and __1__ are the basic languages of websites.
You'll also need a text __2__ to write your HTML and __1__ code.
A text __2__ is a special program that's designed for writing __3__, rather
than a word processor like Microsoft Word. Each web __4__ renders HTML and CSS
in a different way, so you'll also need to make sure that your website
displays and functions properly in each one. Website are accessed
using __5__ text Protocol (__6__). """

quiz_harder_answer = {'__1__':"interpreted", '__2__':"coding", '__3__':"1991", '__4__':"Rossum", '__5__':"multiple", '__6__':"functional", '__7__':"memory"}
quiz_harder_para = """Python is a high-level, __1__ and general-purpose dynamic programming
language  that focuses on code readability. The syntax in Python helps
the programmers to do __2__ in fewer  steps as compared to Java or C++.
The language founded in the year __3__ by the developer Guido Van __4__
has the programming easy and fun to do. The Python is widely used in bigger
organizations because of its __5__ programming paradigms. They usually involve
imperative and  object-oriented __6__ programming. It has a comprehensive
and large standard library that  has automatic __7__ management and dynamic
features. """
max_attempts = 5
def ans_is_correct(current_answer, true_answer, ans_index):
    #This functio is to check whether given input is correct or not
    for ans in true_answer:
        if current_answer == true_answer[ans_index].lower():#Here we are comparing the user answer with actual answer by lowercasing the answers.
            return true_answer[ans_index] #if the answer is correct this statement returns the actual in correct case.
    return None

def ans_replace(ans_to_replace, field_to_fill, replace_para):
    #This function is to replace the dashes with correct answers
    if ans_to_replace != None:
        replace_para = replace_para.replace(field_to_fill, ans_to_replace) #This statement will replace the blank space with correct answer
        return replace_para
    else:
        print '\n',replace_para,"\n\n","{}\n\nPlease try again with correct choice\n".format('#'*40)
        return replace_para

def ans_check(req_field,answer_para,expected_answer):
    """This fucntion will get the input from the user and it will send the arguments to
    check whether the answer is correct?"""
    no_of_try, ans_pos_retry = 0, 0
    while req_field in answer_para:
        if ans_pos_retry == max_attempts : #if user entered 5 wrong answers game will end without prompting for other answers
            return None
        if no_of_try < max_attempts : # to check if user exceeds 5 attempts
            user_answer = raw_input("\nPlease input for " + req_field + " :").lower() #getting input in lower case
            answer = ans_is_correct(user_answer, expected_answer, req_field) #We are passing 3 arguments to check whether the answer is correct
            answer_para = ans_replace(answer,req_field, answer_para)
            ans_pos_retry += 1
        else:
            return answer_para
        no_of_try += 1
        if (5-ans_pos_retry)!=0:
            print "You have", max_attempts -ans_pos_retry, "more attempts\n\n",'#'*40
    return answer_para

def quiz(quiz_para, quiz_answer, word):#input arguments are based on the level selection
    print "\n{0}\n\nLevel ={1}, Good Luck!!\n\nYou have total 5 attempts\n\n{0}\n".format('#'*40,word)
    print quiz_para
    blank_key=quiz_answer.keys()
    blank_key.sort()
    total_answer_try = 0
    while total_answer_try < max_attempts:
        ans_pos =0
        for field in blank_key: # Here we will pass the blanks to prompt for answer from 1 to 5
            quiz_para = ans_check(field, quiz_para, quiz_answer)
            if quiz_para == None:
                return None #If the answers are wrong game will exit with None
            print "\n",quiz_para,"\n"
            ans_pos += 1
        total_answer_try += 1
        return quiz_para
    return quiz_para

def result(ans_para):
    #This function will display the final result
    if ans_para != None:
        print "{0}\n\nCongratulations! You Won!!!\n\n{0}".format('#'*40)
    else:
        print "{0}\n\nYou exceeded maximum number of attempts\n\n{0}".format('#'*40)

#THis is the main menu displayed in the program execution
print ''' \nPlease select the difficulty level from the below menu:

          1. Easy
          2. Medium
          3. Harder\n'''
main_program_try=0
while main_program_try < max_attempts :
    user_choice = input("please enter your choice in number:")
    if user_choice == 1:
        result(ans_para = quiz(quiz_easy_para, quiz_easy_answer, "Easy"))#Passing quiz question, answer and level
        break
    elif user_choice == 2:
        result(ans_para = quiz(quiz_medium_para, quiz_medium_answer, "Medium"))
        break
    elif user_choice == 3:
        result(ans_para = quiz(quiz_harder_para, quiz_harder_answer, "Harder"))
        break
    else:
        print "\nPlease select the number between 1 to 3"
    main_program_try +=1
print "\n Game Over"
