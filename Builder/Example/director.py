class Director:

    def __init__(self, builder):
        self._builder = builder

    def build_computer(self):
        self._builder.new_computer()
        self._builder.get_case()
        self._builder.build_mainboard()
        self._builder.install_mainboard()
        self._builder.install_hard_drive()
        self._builder.install_video_card()

    def get_computer(self):
        return self._builder.get_computer()
