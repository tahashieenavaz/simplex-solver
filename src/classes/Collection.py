class Map:
    def __init__(self, target: list) -> None:
        self.target = target

    def using(self, callback) -> list:
        return list(map(callback, self.target))

    def pipe(self, callback):
        return Map(map(callback, self.target))

    def get(self):
        return list(self.target)
