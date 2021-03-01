from abs_auto import AbsAuto


class ChevySpark(AbsAuto):

    def start(self):
        print("Chevy Spark is running cheaply.")

    def stop(self):
        print("Chevy Spark shutting down.")


class ChevyCamaro(AbsAuto):

    def start(self):
        print("Chevy Camaro roaring and ready to go.")

    def stop(self):
        print("Chevy Camaro shutting down.")


class CadillacCTS(AbsAuto):

    def start(self):
        print("Cadillac CTS running smoothly.")

    def stop(self):
        print("Cadillac CTS shutting down.")
