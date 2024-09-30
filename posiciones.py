class KnowledgeBase:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def evaluate(self, guess, secret):
        exact_matches = 0
        secret_copy = secret.copy()

        # Contar los colores que son correctos y están en la posición correcta
        for i in range(4):
            if guess[i] == secret[i]:
                exact_matches += 1
                secret_copy[i] = None  # Marcar el color como contado en la combinación secreta

        return exact_matches

    def check_rules(self, guess):
        feedback = []
        for i, color in enumerate(guess):
            # Verificar si el color está en la combinación secreta
            color_found = False
            position_correct = False
            
            for rule in self.rules:
                if rule[0] == color:
                    color_found = True
                    if rule[1] == i:
                        position_correct = True
                    break
            
            if not color_found:
                feedback.append(f"{color} no se encuentra en la combinación secreta.")
            elif position_correct:
                feedback.append(f"{color} está en su posición correcta.")
            else:
                feedback.append(f"{color} se encuentra en la combinación pero no en su posición correcta.")

        return feedback


class SimpleMastermind:
    def __init__(self):
        self.colors = ["red", "blue", "green", "yellow"]  # Solo 4 colores
        self.secret_combination = []
        self.kb = KnowledgeBase()
        self.max_attempts = 10

    def setup_game(self):
        print("Set up the secret combination by answering the following questions:")
        # Preguntar sobre la posición de cada color
        for color in self.colors:
            for position in range(4):
                answer = input(f"Is {color} in position {position}? (yes/no): ").strip().lower()
                if answer == 'yes':
                    self.secret_combination.append(color)
                    self.kb.add_rule((color, position))  # Guardar la regla de posición

        print("Secret combination has been set. Try to guess it!")

    def play(self):
        self.setup_game()
        attempts = 0

        while attempts < self.max_attempts:
            print(f"\nAttempt {attempts + 1}/{self.max_attempts}")
            proposal = []

            # Obtener propuesta del jugador
            while len(proposal) < 4:
                color = input(f"Enter color {len(proposal) + 1} (choose from {self.colors}): ").strip().lower()
                if color not in self.colors:
                    print("Invalid color. Choose from the available colors.")
                elif color in proposal:
                    print("Color already used in this proposal. Please choose a different color.")
                else:
                    proposal.append(color)

            # Evaluar la propuesta usando la base de conocimientos
            exact_matches = self.kb.evaluate(proposal, self.secret_combination)
            feedback = self.kb.check_rules(proposal)

            # Mostrar feedback
            for msg in feedback:
                print(msg)

            print(f"You got {exact_matches} exact matches.")

            if exact_matches == 4:
                print("Congratulations! You guessed the correct combination.")
                break

            attempts += 1

        if attempts == self.max_attempts:
            print(f"Game over! The correct combination was {self.secret_combination}.")

if __name__ == "__main__":
    game = SimpleMastermind()
    game.play()
