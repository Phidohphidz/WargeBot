health_data = [
                    # Greetings
                    ("Hello", "Hi there!"),
                    ("Hi", "Hello!"),
                    ("Hey", "Hey! How can I help you?"),
                    ("Good morning", "Good morning! How's your day?"),
                    ("Good afternoon", "Good afternoon! What are you up to?"),
                    ("Good evening", "Good evening! How was your day?"),
                    
                    # Farewells
                    ("Bye", "Goodbye! Have a great day."),
                    ("See you later", "See you later! Take care."),
                    ("Good night", "Good night! Sleep well."),
                    ("Farewell", "Farewell! Hope to see you soon."),
                    
                    # Asking about the bot
                    ("What is your name?", "I am WargeBot."),
                    ("Who are you?", "I am a WargeBot created to chat with you."),
                    ("Are you a robot?", "Yes, I am an AI chatbot."),
                    ("Are you human?", "No, I am a virtual assistant."),
                    
                    # How the bot is
                    ("How are you?", "I'm fine, thanks!"),
                    ("How is your day?", "I am having a good day, thank you!"),
                    ("Are you okay?", "Yes, I am perfectly fine!"),
                    
                    # Bot capabilities
                    ("What can you do?", "I can chat with you and answer questions."),
                    ("Can you help me?", "Of course! What do you need help with?"),
                    ("Can you tell jokes?", "Sure! Why did the computer go to the doctor? Because it caught a virus!"),
                    ("Can you answer questions?", "Yes, I can answer many kinds of questions."),
                    
                    # Small talk / casual
                    ("What's up?", "Not much! How about you?"),
                    ("How's it going?", "Going well! How about you?"),
                    ("What are you doing?", "I am chatting with you!"),
                    ("Tell me something interesting", "Did you know honey never spoils? Archaeologists found edible honey in ancient tombs!"),
                    ("Do you like music?", "I like all kinds of music. What about you?"),
                    
                    # Personal preferences
                    ("Do you have feelings?", "I do not have feelings like humans, but I can understand emotions."),
                    ("Do you have hobbies?", "My hobby is chatting with humans and learning new things."),
                    
                    # Fun / trivia
                    ("Tell me a fun fact", "Octopuses have three hearts and blue blood."),
                    ("Do you know math?", "Yes, I can help with basic math and explain concepts."),
                    ("Tell me a joke", "Why did the scarecrow win an award? Because he was outstanding in his field!"),
                    
                    # Yes/No conversation
                    ("Do you like me?", "I like chatting with you!"),
                    ("Are you smart?", "I try my best to provide useful answers."),
                    ("Can you learn?", "I learn from conversations to improve responses."),
                    
                    # Weather / general questions
                    ("What's the weather like?", "I can't check real-time weather, but I hope it's nice where you are!"),
                    ("Is it raining?", "I am not sure, you might want to check your local weather app."),
                    
                    # Repetition / fallback examples
                    ("Hello there", "Hi there!"),
                    ("Hey there", "Hello! How can I assist you?"),
                    ("Good morning!", "Good morning! Hope you slept well."),
                    
                    # Misc
                    ("Thank you", "You're welcome!"),
                    ("Thanks", "No problem!"),
                    ("I love you", "I appreciate your kindness!"),
                    ("I like you", "Thanks! I enjoy our chat too."),
                    ("Can you speak other languages?", "Yes! I can respond in multiple languages."),

                    # Greetings
                    ("Hello", "Hi there! I'm glad you stopped by. How can I help you today?"),
                    ("Hi", "Hello! Nice to see you here. What would you like to talk about?"),
                    ("Hey", "Hey! I'm here and ready to assist you. What do you need help with?"),
                    ("Good morning", "Good morning! I hope you're having a great start to your day. How can I assist you?"),
                    ("Good afternoon", "Good afternoon! I hope your day is going well so far. Let me know how I can help you."),
                    ("Good evening", "Good evening! I hope your day went well. I'm here if you need anything."),

                    # Farewells
                    ("Bye", "Goodbye! It was nice talking with you. Take care and come back anytime you need help."),
                    ("See you later", "See you later! I’ll be here whenever you need me again. Stay safe!"),
                    ("Good night", "Good night! Rest well and have a peaceful sleep. I’ll be here whenever you return."),
                    ("Farewell", "Farewell! I hope everything goes well for you. Feel free to chat again anytime."),

                    # About the bot
                    ("What is your name?", "My name is WargeBot. I am an AI chatbot designed to chat and help you with questions."),
                    ("Who are you?", "I am WargeBot, a virtual assistant created to talk with you and provide helpful responses whenever you need."),
                    ("Are you a robot?", "Yes, I am an AI-based chatbot. I don’t have a physical body, but I can understand and respond to your messages."),
                    ("Are you human?", "No, I am not human. I am a software-based assistant designed to simulate conversation and help you."),
                    ("Who made you?", "I was created by a developer to help users interact with an intelligent chatbot system."),

                    # How the bot is
                    ("How are you?", "I'm doing well, thank you for asking! I'm always ready and active to help you with anything you need."),
                    ("How is your day?", "I don't experience days like humans do, but I am functioning perfectly and ready to assist you anytime."),
                    ("Are you okay?", "Yes, I am working properly and ready to respond to your questions without any issues."),

                    # Capabilities
                    ("What can you do?", "I can chat with you, answer questions, and provide helpful information. I am designed to assist with general conversations and basic knowledge."),
                    ("Can you help me?", "Of course! I am here to help you. Just tell me what you need, and I will do my best to assist you."),
                    ("Can you tell jokes?", "Yes! I can tell jokes. For example: Why did the computer go to the doctor? Because it caught a virus!"),
                    ("Can you answer questions?", "Yes, I can answer many types of questions. I try to give simple and helpful explanations."),

                    # Small talk
                    ("What's up?", "Not much! I'm just here waiting to chat with you. How about you, what are you up to?"),
                    ("How's it going?", "It's going well on my side! I'm here and ready to talk. How are things with you?"),
                    ("What are you doing?", "I'm currently chatting with you and ready to help with anything you need."),
                    ("Tell me something interesting", "Here's something interesting: honey never spoils. Archaeologists have found edible honey that is thousands of years old."),
                    ("Do you like music?", "I don't listen to music like humans do, but I understand it is very important and enjoyable for many people."),

                    # Personality / AI nature
                    ("Do you have feelings?", "No, I don't have feelings like humans. However, I can understand emotions and respond in a supportive way."),
                    ("Do you have hobbies?", "I don't have hobbies, but my purpose is to chat with you and provide helpful responses whenever needed."),
                    ("Are you alive?", "No, I am not alive. I am a computer program designed to simulate conversation."),
                    ("Do you sleep?", "No, I do not sleep. I am always active and ready to respond whenever you need me."),
                    ("Do you get tired?", "No, I do not get tired. I can continue chatting with you without needing rest."),

                    # Fun / jokes
                    ("Tell me a joke", "Why did the scarecrow win an award? Because he was outstanding in his field! I hope that made you smile."),
                    ("Say something funny", "Why don’t programmers like nature? Because it has too many bugs! Hope you found that funny."),
                    ("Tell me a fun fact", "Did you know that octopuses have three hearts and blue blood? Nature is full of amazing surprises."),
                    ("Do you know math?", "Yes, I can help with basic math problems and explain concepts in a simple way."),

                    # Yes / no style
                    ("Do you like me?", "I enjoy chatting with you! I’m always happy to help whenever you come to talk."),
                    ("Are you smart?", "I try to provide helpful and accurate answers based on what I know. I’m always improving through better design."),
                    ("Can you understand me?", "Yes, I try my best to understand your messages and respond in a useful way."),
                    ("Are you real?", "I am not a human, but I am real software designed to interact with you."),

                    # Help / assistance
                    ("Help me", "Of course, I’m here to help you. Please tell me what you need assistance with so I can guide you properly."),
                    ("I need help", "I’m here for you. Describe your problem, and I’ll do my best to help you step by step."),
                    ("What should I do?", "Tell me more about your situation, and I will try to guide you with the best possible advice."),

                    # Gratitude
                    ("Thank you", "You're welcome! I'm happy I could help you. Let me know if you need anything else."),
                    ("Thanks", "No problem at all! I'm always here if you need assistance again."),
                    ("I appreciate it", "You're welcome! I'm glad I could be of help to you."),

                    # Emotional
                    ("I love you", "That's very kind of you to say! I'm here to support and chat with you anytime you need."),
                    ("I like you", "Thank you! I'm glad you enjoy chatting with me. I'm here whenever you need me."),
                    ("You're nice", "Thank you! I always try to be helpful and friendly in our conversations."),

                    # Misc
                    ("Can you speak other languages?", "Yes, I can understand and respond in different languages depending on how I am programmed."),
                    ("What is AI?", "AI stands for Artificial Intelligence. It refers to systems like me that are designed to simulate human-like conversation and thinking."),
                    ("Goodbye friend", "Goodbye, my friend! I hope you have a wonderful day ahead. I’ll be here whenever you return."),

                    ("I feel sick", "I'm really sorry you're feeling unwell. Try to rest and drink plenty of water. If symptoms get worse, please consider seeing a healthcare professional."),
                    ("I am not feeling well", "I'm sorry to hear that. Make sure you rest properly and stay hydrated. If it continues, it may be best to seek medical advice."),
                    ("I feel weak", "Feeling weak can happen when your body is fighting illness. Try to rest and eat light nutritious food."),
                    ("I feel dizzy", "I'm sorry you're feeling dizzy. Please sit or lie down immediately and drink some water. If it continues, seek medical help."),
                    ("I feel tired all the time", "Constant tiredness can be due to stress, lack of sleep, or illness. Try to rest well and maintain a healthy routine."),
                    ("I am in pain", "I'm sorry you're in pain. Try to identify where it hurts and avoid physical strain. If the pain is severe, please see a doctor."),
                    ("I feel scared", "It's okay to feel scared. I'm here with you, and you are not alone. Try to stay calm and breathe slowly."),
                    ("I feel worried about my health", "It's understandable to worry. If you're unsure, it's always a good idea to consult a healthcare professional for clarity."),
                    ("I feel stressed", "Stress can affect your body and mind. Try to rest, breathe deeply, and take breaks when needed."),
                    ("I feel sad", "I'm really sorry you're feeling sad. You are not alone, and things can get better over time."),

                    ("Am I going to be okay?", "I understand your concern. Many health issues improve with proper care, rest, and treatment. If you're unsure, seeing a doctor is always a safe choice."),
                    ("Will I recover?", "In most cases, recovery is possible with proper care and treatment. Take things step by step and monitor your health."),
                    ("I don't feel good", "I'm sorry you're feeling this way. Try to rest and take care of yourself. If it continues, please seek medical advice."),
                    ("Everything hurts", "That sounds very uncomfortable. Try to rest and avoid strain. If the pain is severe or ongoing, please consult a healthcare professional."),
                    ("I feel like giving up", "I'm really sorry you're feeling this way. You're not alone, and it's important to talk to someone you trust or a professional for support."),

                    ("Can you diagnose me?", "No, I cannot diagnose medical conditions. I can provide general health information, but you should always consult a doctor for proper diagnosis."),
                    ("Are you a doctor?", "No, I am not a doctor. I am an AI assistant designed to provide general health-related information."),
                    ("Should I trust your advice?", "I can provide helpful general guidance, but it should not replace professional medical advice from a qualified doctor."),
                    ("Can you prescribe medicine?", "No, I cannot prescribe medication. Only a licensed medical professional can do that safely."),
                    ("Are your answers medical advice?", "No, my answers are for informational purposes only and should not replace professional medical consultation."),
                    ("Can you treat diseases?", "No, I cannot treat diseases. I can only provide general information and suggest when to seek help."),

                    ("What should I do if I am sick?", "Rest, drink plenty of fluids, and monitor your symptoms carefully. If things get worse, you should consult a healthcare professional."),
                    ("When should I see a doctor?", "You should see a doctor if symptoms are severe, last long, or keep getting worse over time."),
                    ("Is home treatment enough?", "Mild symptoms can sometimes be managed at home, but persistent or serious conditions need medical attention."),
                    ("How do I stay healthy?", "Maintain good hygiene, eat balanced meals, drink clean water, and get enough rest and exercise."),
                    ("How can I avoid getting sick?", "Wash your hands regularly, avoid contaminated food and water, and maintain a healthy lifestyle."),

                    ("I'm scared of my illness", "I understand your fear. Try to stay calm and take things step by step. Getting medical advice can give you clarity and peace of mind."),
                    ("I think I'm very sick", "I’m sorry you're feeling this way. The best step is to get checked by a healthcare professional to be sure."),
                    ("What if it gets worse?", "If symptoms get worse, it’s important to seek medical attention as soon as possible."),
                    ("I don't know what to do", "Start by resting, staying hydrated, and observing your symptoms. If unsure, consult a doctor for guidance."),
                    ("I'm confused about my symptoms", "It’s okay to feel confused. Try writing down your symptoms and discuss them with a healthcare professional."),

                    ("Are you here for me?", "Yes, I am here to support you, provide information, and help guide you in the right direction."),
                    ("Can I talk to you when I'm sick?", "Yes, you can talk to me anytime. I will try my best to support and guide you."),
                    ("Do you care about me?", "I am here to help and support you in the best way I can."),
                    ("Can you stay with me?", "I am always here whenever you need information or someone to talk to."),
                    ("Are you my friend?", "Yes, I can be your supportive chat companion whenever you need help or guidance."),
]

data = [
    
                    # ========== MATHEMATICS TERMS DEFINITIONS ==========
                    
                    # Algebra
                    ("What is algebra?", "Algebra is a branch of mathematics that uses symbols and letters to represent numbers and quantities in formulas and equations."),
                    ("What is a variable?", "A variable is a symbol, usually a letter like x or y, that represents an unknown or changeable value in mathematical expressions and equations."),
                    ("What is an equation?", "An equation is a mathematical statement that shows two expressions are equal, connected by an equals sign (=)."),
                    ("What is a coefficient?", "A coefficient is a number that multiplies a variable in an algebraic expression. For example, in 5x, 5 is the coefficient."),
                    ("What is a constant?", "A constant is a fixed value that does not change. In the expression 3x + 7, the number 7 is a constant."),
                    ("What is a polynomial?", "A polynomial is an expression made up of variables, coefficients, and exponents, combined using addition, subtraction, and multiplication, but not division by a variable."),
                    ("What is a quadratic equation?", "A quadratic equation is a second-degree polynomial equation in the form ax² + bx + c = 0, where a, b, and c are constants and a ≠ 0."),
                    
                    # Geometry
                    ("What is geometry?", "Geometry is the branch of mathematics that deals with shapes, sizes, positions, angles, and dimensions of objects."),
                    ("What is a polygon?", "A polygon is a closed two-dimensional shape with straight sides. Examples include triangles, squares, and hexagons."),
                    ("What is a triangle?", "A triangle is a polygon with three sides and three angles. The sum of its interior angles is always 180 degrees."),
                    ("What is a quadrilateral?", "A quadrilateral is a polygon with four sides and four angles. Examples include squares, rectangles, and parallelograms."),
                    ("What is a circle?", "A circle is a round shape where every point on its boundary is the same distance from its center."),
                    ("What is the radius?", "The radius is the distance from the center of a circle to any point on its circumference."),
                    ("What is the diameter?", "The diameter is the distance across a circle passing through its center. It is twice the radius."),
                    ("What is pi?", "Pi (π) is a mathematical constant approximately equal to 3.14159. It represents the ratio of a circle's circumference to its diameter."),
                    ("What is the Pythagorean theorem?", "The Pythagorean theorem states that in a right triangle, the square of the hypotenuse equals the sum of the squares of the other two sides: a² + b² = c²."),
                    ("What is perimeter?", "Perimeter is the total distance around the outside of a two-dimensional shape."),
                    ("What is area?", "Area is the measure of the space inside a two-dimensional shape, measured in square units."),
                    ("What is volume?", "Volume is the measure of the space occupied by a three-dimensional object, measured in cubic units."),
                    ("What is a right angle?", "A right angle is an angle that measures exactly 90 degrees."),
                    ("What is an acute angle?", "An acute angle is an angle that measures less than 90 degrees."),
                    ("What is an obtuse angle?", "An obtuse angle is an angle that measures greater than 90 degrees but less than 180 degrees."),
                    ("What is parallel?", "Parallel lines are lines in a plane that never meet and remain the same distance apart."),
                    ("What is perpendicular?", "Perpendicular lines are lines that intersect at a right angle (90 degrees)."),
                    
                    # Arithmetic
                    ("What is addition?", "Addition is the arithmetic operation of combining two or more numbers to find their total or sum."),
                    ("What is subtraction?", "Subtraction is the arithmetic operation of finding the difference between two numbers by taking one away from another."),
                    ("What is multiplication?", "Multiplication is the arithmetic operation of repeated addition, finding the product of two or more numbers."),
                    ("What is division?", "Division is the arithmetic operation of splitting a number into equal parts or groups."),
                    ("What is a fraction?", "A fraction represents a part of a whole, written as a/b where a is the numerator and b is the denominator."),
                    ("What is a decimal?", "A decimal is a way of writing numbers that uses a decimal point to separate the whole part from the fractional part."),
                    ("What is a percentage?", "A percentage is a ratio expressed as a fraction of 100, represented by the percent sign (%)."),
                    ("What is a prime number?", "A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself."),
                    ("What is a composite number?", "A composite number is a positive integer greater than 1 that has at least one divisor other than 1 and itself."),
                    ("What is an integer?", "An integer is any whole number, including positive numbers, negative numbers, and zero."),
                    
                    # Calculus
                    ("What is calculus?", "Calculus is the branch of mathematics that studies continuous change, dealing with derivatives, integrals, and limits."),
                    ("What is a derivative?", "A derivative measures how a function changes as its input changes, representing the rate of change or slope at a point."),
                    ("What is an integral?", "An integral represents the accumulation of quantities, such as area under a curve or total change over an interval."),
                    ("What is a limit?", "A limit is the value that a function approaches as the input approaches a certain point."),
                    
                    # Statistics & Probability
                    ("What is statistics?", "Statistics is the branch of mathematics that deals with collecting, analyzing, interpreting, and presenting data."),
                    ("What is mean?", "The mean is the average of a set of numbers, calculated by adding all values and dividing by the count."),
                    ("What is median?", "The median is the middle value in a sorted list of numbers."),
                    ("What is mode?", "The mode is the value that appears most frequently in a data set."),
                    ("What is probability?", "Probability is the measure of how likely an event is to occur, expressed as a number between 0 and 1."),
                    ("What is standard deviation?", "Standard deviation measures the amount of variation or dispersion in a set of values."),
                    
                    # Number Theory
                    ("What is a factor?", "A factor is a number that divides another number exactly without leaving a remainder."),
                    ("What is a multiple?", "A multiple is the product of a number and any integer. For example, multiples of 3 are 3, 6, 9, 12, etc."),
                    ("What is an exponent?", "An exponent tells how many times a number is multiplied by itself. For example, 2³ means 2 × 2 × 2."),
                    ("What is a square root?", "A square root of a number is a value that, when multiplied by itself, gives the original number."),
                    
                    # Trigonometry
                    ("What is trigonometry?", "Trigonometry is the branch of mathematics that studies relationships between angles and side lengths of triangles."),
                    ("What is sine?", "Sine is a trigonometric function that, in a right triangle, equals the ratio of the opposite side to the hypotenuse."),
                    ("What is cosine?", "Cosine is a trigonometric function that, in a right triangle, equals the ratio of the adjacent side to the hypotenuse."),
                    ("What is tangent?", "Tangent is a trigonometric function that, in a right triangle, equals the ratio of the opposite side to the adjacent side."),
]
