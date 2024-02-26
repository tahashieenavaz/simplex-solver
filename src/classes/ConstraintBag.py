from classes.Table import Table


class ConstraintBag:
    def __init__(self) -> None:
        self.value = Table()

    def add(self, *args):
        self.value.add_row(*args)
