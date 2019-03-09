class Episode:
    def __init__(self, players, result, test_inputs, questions, num_questions = 20):
        """ Constructor for Episode (only include episodes that give information about who dropped of)
        Args:
            players (list): The players (string format) that participate in the final test of the episode
            result (Result): The result of the test
            test_inputs (dict): What the players did on the test. The key is the player (string format) and the value
            is a TestInput object
            questions (dict): The questions of the test that were visible for viewers (key is the question number which
             is an int and  The values are Question objects)
            num_questions (int): The total number of questions the test had
        """
        self.players = players
        self.result = result
        self.initialize_test(players, test_inputs)
        self.test_inputs = test_inputs
        self.initialize_questions(questions, num_questions, players)
        self.questions = questions
        self.num_questions = num_questions

    def initialize_test(self, players, test_inputs):
        """ For players not contained in test_inputs do not give any information about questions and use 0 jokers """
        for p in players:
            if p not in test_inputs:
                test_inputs[p] = TestInput()

    def initialize_questions(self, questions, num_questions, players):
        """ If the length of question dict is smaller than num_questions then the questions will be appended with
        standard questions (for every player an answer) """
        for i in range(1, num_questions + 1):
            if i not in questions:
                options = dict()
                for j in range(1, len(players) + 1):
                    options[j] = players[j - 1]
                questions[i] = Question(options)

class Result:
    def __init__(self, drop, players):
        """ Constructor for Result (a Result is what happend after the test)
        Args:
            drop (bool): True means that player(s) did not survive the test, False means that everyone survived the test
            players (list): In case drop is true then this is the list of players (string format) that did not survive
            the test, in case drop is false then this is the list of players that possible would have failed the test
        """
        self.drop = drop
        self.players = players

class Question:
    """ Constructor of Question
    Args:
        options (dict): The different options a player can choose at the question (the key is the option number (int):
        options are numbered from top to bottom, left to right. The value is the list of players (string format) that
        an option targets)
    """
    def __init__(self, options):
        self.options = options

    def option_for_player(self, player):
        """ Get the option in the question that belongs to the player given as argument """
        for key in self.options:
            if player in self.options[key]:
                return key

class TestInput:
    """ Constructo of Test Input (what a player did and filled in on the test)
    Args:
        answered_questions (dict): A dictionary where the key is the question number (int) and the value is the option
        number (int) that the player selected. If a question number is not contained in the dictionary then it is
        unknown what the player filled in at this question
        jokers (int): How much jokers the player used on the test (set equal to num_questions if player had immunity)
    """
    def __init__(self, answered_questions = None, jokers = 0):
        if answered_questions is None:
            answered_questions = dict()
        self.answered_questions = answered_questions
        self.jokers = jokers