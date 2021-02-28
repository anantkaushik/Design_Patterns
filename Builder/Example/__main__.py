from director import Director
from computer_builder import MyComputerBuilder

computer_builder = Director(MyComputerBuilder())
computer_builder.build_computer()
computer = computer_builder.get_computer()
computer.display()
