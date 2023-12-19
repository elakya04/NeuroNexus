import re

def student_teacher_chatbot(user_input):
    # Define rules and responses for student-teacher interaction
    rules = [
        {'pattern': r'hi|hello|hey', 'response': 'Hello! How can I assist you with your studies today?'},
        {'pattern': r'how are you', 'response': "I'm here and ready to help with any academic questions you have."},
        {'pattern': r'what is your name', 'response': 'I am your virtual assistant for academic queries.'},
        {'pattern': r'bye|goodbye', 'response': 'Goodbye! If you have more questions, feel free to ask.'},
        {'pattern': r'exam|test|assignment', 'response': 'If you have questions about exams, tests, or assignments, please provide more details.'},
        {'pattern': r'help', 'response': 'I can help you with questions related to your studies, exams, assignments, or any academic concerns you may have.'},
        {'pattern': r'subject|course', 'response': 'If you have specific questions about a subject or course, let me know which one you need assistance with.'},
        {'pattern': r'grade|grading', 'response': 'If you have questions about grading, please provide more details about the specific issue.'},
        # Add more rules as needed
    ]

    # Check user input against rules
    for rule in rules:
        if re.search(rule['pattern'], user_input, re.IGNORECASE):
            return rule['response']

    # Default response if no rules match
    return "I'm sorry, I didn't understand that. Can you please provide more details or ask a specific academic question?"

# Interactive chat for student-teacher interaction
print("Teacher Assistant: Hello! How can I assist you with your studies today? Type 'exit' to end the conversation.")
while True:
    user_input = input("Student: ")
    if user_input.lower() == 'exit':
        print("Teacher Assistant: Goodbye! If you have more questions, feel free to ask.")
        break
    response = student_teacher_chatbot(user_input)
    print("Teacher Assistant:", response)
