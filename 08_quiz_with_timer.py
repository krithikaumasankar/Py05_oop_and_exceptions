import random
import time

# Custom Exception
class InvalidOptionError(Exception):
    pass

class Quiz:
    def __init__(self):
        # Questions with answers together (tuple)
        self.questions = [
            ("1. Largest planet?\nA. Earth\nB. Mars\nC. Jupiter", 'C'),
            ("2. 5 + 3 = ?\nA. 6\nB. 8\nC. 10", 'B'),
            ("3. Capital of India?\nA. Mumbai\nB. Delhi\nC. Chennai", 'B'),
            ("4. Water chemical formula?\nA. H2O\nB. CO2\nC. O2", 'A'),
            ("5. Sun rises in?\nA. West\nB. East\nC. North", 'B'),
            ("6. 10 * 2 = ?\nA. 20\nB. 15\nC. 25", 'A'),
            ("7. Fastest land animal?\nA. Lion\nB. Cheetah\nC. Tiger", 'B'),
            ("8. National animal of India?\nA. Lion\nB. Tiger\nC. Elephant", 'B')
        ]

        self.score = 0
        self.time_limit = 10  # seconds per question

    def start_quiz(self):
        # Randomize questions
        random.shuffle(self.questions)

        for q, ans in self.questions:
            while True:
                try:
                    print("\n" + q)
                    print(f"(You have {self.time_limit} seconds)")

                    start_time = time.time()
                    user_ans = input("Enter option (A/B/C): ").upper()
                    end_time = time.time()

                    # Check time
                    if end_time - start_time > self.time_limit:
                        print("⏰ Time's up! Moving to next question.")
                        break

                    if user_ans not in ['A', 'B', 'C']:
                        raise InvalidOptionError("Invalid option selected!")

                    if user_ans == ans:
                        print("Correct!")
                        self.score += 1
                    else:
                        print("Wrong!")

                    break

                except InvalidOptionError as e:
                    print(e)

    def display_score(self):
        print("\nQuiz Completed!")
        print(f"Your final score is: {self.score} / {len(self.questions)}")


# Run the quiz
q = Quiz()
q.start_quiz()
q.display_score()
