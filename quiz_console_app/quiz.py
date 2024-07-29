print("Welcome to Computer Quiz!!")

player = input("Do you want to play? ")

if player.lower() != "yes":
    quit()
else:
    print("Let's start!\n")

score = 0

questions = [
    {"question": "What is the full form of CPU?", "answer": "central processing unit"},
    {"question": "What is the full form of GUI?", "answer": "graphical user interface"},
    {"question": "What is the full form of RAM?", "answer": "random access memory"},
    {"question": "What is the full form of ROM?", "answer": "read only memory"},
    {"question": "Who Developed Windows?", "answer": "microsoft"},
    {"question": "What is the full form of HTTP?", "answer": "hypertext transfer protocol"},
    {"question": "What is the full form of FTP?", "answer": "file transfer protocol"},
    {"question": "What is the full form of PNG?", "answer": "portable network graphics"},
    {"question": "What is the full form of SMS?", "answer": "short message service"},
    {"question": "What is the full form of OS?", "answer": "operating system"},
]

for q in questions:
    answer = input(q["question"] + " ").lower()
    if answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Sorry, the correct answer is {q['answer']}\n")

print(f"You got {score} questions correct!")
print(f"Your score is {(score / len(questions)) * 100}%")