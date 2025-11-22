# Simple Turing Test Program

# Questions + Answers + Who wrote them
qa_pairs = [
    ("Why do people smile?", "People smile when they feel happiness and joy. And also when they try to hide their pain and sadness they smile at people.", "human"),
    ("What would you do if it started raining suddenly?", "Often when it rains, I like to get wet in the rain and it gives me a different kind of feeling and vibe. But most of the time when it rains, I avoid getting wet so that I don’t get sick.", "human"),
    ("What's something people do that you find annoying?", "I get bothered when people are constantly late without letting anyone know. It feels like they don't respect other people's time, and it can mess up plans. I think a quick message or call to explain would make a big difference.", "ai"),
    ("Explain how the internet works in simple terms.", "The internet is a global network that connects computers and devices using cables, satellites, and wireless signals. When you visit a website, your computer sends a request through your internet service provider to a server where that website is stored. The server sends back the website's data, which your browser displays.", "ai"),
    ("How would you plan a trip?", "Choose where to go, book transport and hotels, plan places to visit, pack your things, and get ready to travel.", "ai"),
    ("Can you describe your perfect weekend?", "My perfect weekend would start with sleeping in late, then having a relaxed breakfast. I'd spend the afternoon outside, maybe visiting a park or meeting friends, and end the day watching a movie or reading a book at home.", "ai"),
    ("Describe how it feels to wait for exam results.", "Waiting for exam results feels stressful and nervous. You keep imagining all the possible outcomes and refresh the results page over and over. But once you get the results, there's a big relief, whatever the outcome.", "ai"),
    ("Why do we need sleep?", "Sleep is a necessary activity for humans. Humans need 6-8 hours of sleep a day to keep their body and mental health in check. Lack of sleep can cause dizziness and hallucinations and can cause health and brain damage which can sometimes be permanent.", "human"),
    ("What is the difference between a smartphone and a laptop?", "The difference between a smartphone and a laptop is that you can carry and hold your smartphone in your hand. Laptop is more preferable to use on a desk or in lap thus the name laptop.", "human"),
    ("Describe a tradition in your family.", "In my family, during Eid, we prepare a big meal and invite relatives and neighbors. Everyone wears new clothes, shares food, and spends the day together celebrating. It feels very special.", "ai")
]

# Score counters
ai_as_human = 0
human_as_ai = 0

print("\n<<<<<< Simple Turing Test >>>>>>\n")

# Ask each question
for i, (q, a, author) in enumerate(qa_pairs, start=1):
    print(f"\nQuestion {i}: {q}")
    print(f"Answer: {a}\n")

    guess = input("Do you think this is Human (h) or AI (a)? ").lower()

    if guess.startswith("h") and author == "ai":
        ai_as_human += 1
    elif guess.startswith("a") and author == "human":
        human_as_ai += 1

# Show results
print("\n====== Turing Test Result ======")
print(f"AI answers mistaken as Human: {ai_as_human}")
print(f"Human answers mistaken as AI: {human_as_ai}")
print("================================\n")
