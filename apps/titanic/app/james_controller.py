from titanic.app.jack_service import JackService


class JamesController:
    def __init__(self):
        self.jack = JackService()

    def get_model_name(self):
        return self.jack.get_model()

    def get_tree(self):
        return self.jack.get_tree()

    def get_accuracy(self):
        return self.jack.get_accuracy()

    def get_data(self):
        return self.jack.get_data()

    def get_count(self):
        return self.jack.get_count()

    def get_survived(self):
        return self.jack.get_survived()

    def get_dead(self):
        return self.jack.get_dead()