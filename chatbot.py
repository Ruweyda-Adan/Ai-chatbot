import random
from textblob import TextBlob
import spacy

# Load spaCy's small English model
nlp = spacy.load("en_core_web_sm")

def get_response(user_input):
    """
    Process user input and generate an intelligent response based on intent, sentiment, and specific school-related issues.
    """
    user_input = user_input.lower()

    # Sentiment analysis
    sentiment = TextBlob(user_input).sentiment.polarity  # Sentiment range: -1 to 1

    # Predefined responses for common situations
    stress_responses = [
        "I'm sorry to hear you're feeling overwhelmed. Take a deep breath and focus on the present moment.",
        "It sounds like you're dealing with a lot right now. Would you like some tips to manage stress?",
        "I understand it can be tough. Take a moment to breathe deeply and ground yourself. Can I help with anything specific?"
    ]

    casual_responses = [
        "I'm here to help! Feel free to ask me anything.",
        "I'm always here for you, what’s on your mind?",
        "How can I support you today?"
    ]

    greeting_responses = [
        "Hey there! How’s it going?",
        "Hello! What can I do for you today?",
        "Hi! How’s your day been so far?"
    ]

    # Greeting response check: If the user input matches any common greetings
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return random.choice(greeting_responses)

    # School-specific responses (more targeted to student concerns)
    if "stress" in user_input or "overwhelmed" in user_input:
        return random.choice(stress_responses)

    if "peer pressure" in user_input or "fitting in" in user_input:
        return "Peer pressure can be really tough, but remember, you don’t have to do things you’re uncomfortable with. It's okay to say no and stick to your values. Surround yourself with supportive people. Don't be afraid to walk away."

    if "homework" in user_input or "studying" in user_input:
        return "Balancing schoolwork with everything else can be stressful. Try breaking tasks into smaller pieces. What are you finding challenging right now?"

    if "friends" in user_input or "lonely" in user_input:
        return "Friendship is important, and it's normal to feel lonely at times. Maybe there's a group or activity at school where you can meet new people."

    if "family" in user_input or "parents" in user_input:
        return "Family dynamics can be complicated. If you're comfortable, talking with your parents about how you're feeling might help."

    if "bullying" in user_input or "harassed" in user_input:
        return "I'm really sorry you're experiencing this. It’s important to talk to a trusted adult or school counselor to get support."

    # Sentiment-based response (positive, negative, neutral)
    if sentiment > 0.2:
        return "I'm glad you're feeling positive! Keep it up!"
    elif sentiment < -0.2:
        return "It sounds like you're going through a tough time. Would you like some tips to help manage your feelings?"
    else:
        return "I hear you. Let's take it one step at a time."

    # Random response for questions or unknown input
    unknown_responses = [
        "That's an interesting question. Let me think about it...",
        "Hmm, I'm not sure about that. Can I help with something else?",
        "Could you tell me more? I’d love to understand better!"
    ]
    
    return random.choice(unknown_responses)
