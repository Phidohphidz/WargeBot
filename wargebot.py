# To run this code:
# Just pip install sentence-transformers scikit-learn

# U can make your own dataset, that it's format should look like the dialogs.txt or the self.data variable
# U can contact me 0981254727 on whatsApp if, U want to understand a little bit more.

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import time

class WargeBot:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def load_dataset(self, data_file="dialogs.txt"):

                self.data = [
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

                with open(data_file, "r") as f:
                    self.lines = f.readlines()

                for line in self.lines:
                    parts = line.strip().split("\t")
                    if len(parts) >= 2:
                        self.data.append((parts[0], parts[1]))

                self.questions = [q for q, a in self.data]
                self.answers = [a for q, a in self.data]

                self.questions_embeddings =  self.model.encode(self.questions)

    def type_text(self,text, delay=0.08):
        for c in text:
            print(c,end="",flush=True)
            time.sleep(delay)

    def get_response(self,user_input):
        user_embedding = self.model.encode([user_input])

        similarities = cosine_similarity(user_embedding, self.questions_embeddings)
        best_index = np.argmax(similarities)
        best_score = similarities[0][best_index]

        if best_score < 0.3:
            return "I don't understand that yet."
        
        return self.answers[best_index]


bot = WargeBot()
bot.load_dataset()
print("WargeBot: Hello! Ask me anything (type 'exit' to quit)")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        bot.type_text("WargeBot: Goodbye ^__^")
        break

    response = bot.get_response(user_input)

    print("WargeBot: ", end="")
    bot.type_text(response)