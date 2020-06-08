class Singleton(object):
    ans = None

    @staticmethod
    def instance():
        """
        This method is used to instantiate class object.
        It'll make sure class will have only one object.
        """
        if '_instance' not in Singleton.__dict__:
            Singleton._instance = Singleton()
        return Singleton._instance
    
s1 = Singleton.instance()
s2 = Singleton.instance()

assert s1 is s2

s1.ans = 42

assert s2.ans == s1.ans
print("Assertions passed.")