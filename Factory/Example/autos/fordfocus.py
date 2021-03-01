from abs_auto import AbsAuto


class FordFocus(AbsAuto):

    def start(self):
        print(f"{self.name} is running smoothly.")

    def stop(self):
        print(f"{self.name} is shutting down.")
