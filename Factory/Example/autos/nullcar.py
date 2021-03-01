from abs_auto import AbsAuto


class NullCar(AbsAuto):

    def start(self):
        print(f"{self.name} car")

    def stop(self):
        pass
