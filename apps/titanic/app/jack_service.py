from .walter_reader import WalterReader
from .rose_model import RoseModel

class JackService:
    def __init__(self):
        self.walter = WalterReader()
        self.rose = RoseModel()
        
    def get_model(self) -> str:
        return self.rose.get_model()

    def get_accuracy(self) -> float:
        return self.rose.get_accuracy()

    def get_tree(self) -> str:
        return self.rose.get_tree()

    def get_data(self):
        return self.walter.get_data()

    def get_count(self):
        return self.walter.get_count()

    def get_survived(self):
        return self.walter.get_survived()

    def get_dead(self):
        return self.walter.get_dead()