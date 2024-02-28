from classes.Table import Table

from utils.functions import panicIfNot
from errors.WrongSimplexAnswerPassed import WrongSimplexAnswerPassed


class SimplexAnswer:
    def check(self):
        panicIfNot(
            all(item >= 0 for item in self.value.row(0)),
            WrongSimplexAnswerPassed
        )

    def record(self, table: Table):
        self.value = table
        self.check()
