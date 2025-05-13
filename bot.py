import nltk
from nltk.chat.util import Chat, reflections

# Download required NLTK data
nltk.download('punkt')

# Define chatbot pairs
pairs = [
    [r"hi|hey|hello", ["Hello!", "Hi there!", "Hey! How can I help you today?"]],
    
    [r"my name is (.*)", ["Hello %1, nice to meet you! How can I assist you today?"]],
    
    [r"how are you ?", ["I'm just a bunch of code, but I'm functioning as expected!"]],
    
    [r"what is your name ?", ["I'm your friendly AI chatbot."]],
    
    [r"who created you ?", ["I was created by an aspiring engineer as part of an internship project."]],
    
    [r"what can you do ?", ["I can answer simple questions, chat with you, and make your day better!"]],
    
    [r"can you help me with (.*)", ["Sure! I can try to help you with %1. Tell me more."]],
    
    [r"what is natural language processing ?", [
        "Natural Language Processing (NLP) is a field of AI that helps computers understand and process human language."
    ]],
    
    [r"what is machine learning ?", [
        "Machine Learning is a branch of AI where computers learn from data without being explicitly programmed."
    ]],
    
    [r"what is artificial intelligence ?", [
        "Artificial Intelligence is the simulation of human intelligence in machines."
    ]],
    
    [r"tell me a joke", [
        "Why did the computer show up late to work? It had a hard drive!"
    ]],
    
    [r"what is the time now ?", [
        "Sorry, I can't access the current time yet, but your device can!"
    ]],
    
    [r"thank you|thanks", ["You're welcome!", "Glad I could help!"]],
    
    [r"sorry (.*)", ["No worries!", "It's all good."]],
    
    [r"bye|exit|quit", ["Goodbye! Have a great day!", "See you later!"]],
    
    [r"(.*)", ["I'm sorry, I didn't understand that. Could you rephrase it?"]]
]


# Create chatbot instance
chatbot = Chat(pairs, reflections)

def get_response(user_input):
    return chatbot.respond(user_input)
[
    r"what (.*) your favorite color?",
    ["I like all colors equally!"]
],
[
    r"who (.*) you?",
    ["I'm a chatbot created using NLTK!"]
],
[
    r"can you help me with (.*)",
    ["Sure, I can help you with %1. Tell me more."]
]
