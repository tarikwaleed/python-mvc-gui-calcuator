from view import View
from model import Model
class Contoller:
    def __init__(self):
        self.view = View(self)
        self.model = Model()

    def main(self):
        self.view.main()


if __name__ == "__main__":
  controller=Contoller()
  controller.main()
