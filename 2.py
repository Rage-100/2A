import random  
import re 
def simple_chatbot():  
    responses = { "hello": ["Hi there!", "Hello!", "Greetings!"], "hi": ["Hi there!", "Hello!", 
                "Greetings!"], 
              "how are you": ["I'm a bot, I'm doing great!", "I'm functioning optimally."], 
              "what is your name": ["You can call me PyBot.", "I respond to 'Hey you!'"], 
              "bye": ["Goodbye!", "See you later!", "Have a great day!"], 
              "exit": ["Goodbye!", "See you later!", "Have a great day!"] } 
    default_responses = [ 
    "Sorry, I didn't understand that.", 
    "Could you please rephrase that?", 
    "I'm not sure how to respond to that." 
    ] 
    print("PyBot: Hi! Type 'bye' or 'exit' to end.") 
 
    while True: 
        user_input = re.sub(r'[^\w\s]', '', input("You: ").lower()) 
         
        if user_input in ["bye", "exit"]: 
            print(f"PyBot: {random.choice(responses[user_input])}") 
            break 
         
        matched = False 
        for key in responses: 
            if key in user_input: 
                print(f"PyBot: {random.choice(responses[key])}") 
                matched = True 
                break 
         
        if not matched: 
            print(f"PyBot: {random.choice(default_responses)}") 
  
if __name__ == "__main__": 
    simple_chatbot()
