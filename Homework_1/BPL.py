
from typing import Literal


class BPL_Verifier:
    def __init__(self) -> None:
        self.total_left = 0
        self.total_right = 0
        self.always_false = False

    def reset(self):
        self.total_left = 0
        self.total_right = 0
        self.always_false = False

    def __call__(self, input_string):
        for i, c in enumerate(input_string):
            result = self.eval_step(c)
            print("\tStep {}: {}".format(i, result))
        self.reset()
        return result

    def eval_step(self, char):
        step_result = False
        if self.always_false:
            step_result = False
            return step_result
        x_t = self.interpret_char(char)
        lgr = self.total_left > self.total_right
        ler = self.total_left == self.total_right
        if x_t == 1 and lgr == False and ler == False:
            step_result = False
            self.always_false = True
            return step_result
        if ler:
            step_result = True
            return True
        return step_result

    def interpret_char(self, char):
        if char == "(":
            x_t = 0
            self.total_left = self.total_left + 1
        elif char == ")":
            x_t = 1
            self.total_right = self.total_right + 1
        else:
            raise Exception(
                "Unknown character. Language only contains '(' or ')'.")
        return x_t


test_strings = ["()", "()()", "(()(()))", "(", ")", ")(())"]
bplv = BPL_Verifier()

for i, t in enumerate(test_strings):
    result = bplv(t)
    print("String {}: {}".format(i, result))
    print("")
