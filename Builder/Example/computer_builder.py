from abs_builder import AbsBuilder


class MyComputerBuilder(AbsBuilder):

    def get_case(self):
        self._computer.case = "Coolermaster N300"

    def build_mainboard(self):
        self._computer.mainboard = "MSI 970"
        self._computer.cpu = "Intel Core i7"
        self._computer.memory = "Corsair Vengeance 16GB"

    def install_mainboard(self):
        pass

    def install_hard_drive(self):
        self._computer.hard_drive = "Seagate 2TB"

    def install_video_card(self):
        self._computer.video_card = "GeForce GTX 1070"
