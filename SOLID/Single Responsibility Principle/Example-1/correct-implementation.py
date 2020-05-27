class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)


# By separating the functionality of saving and loading 
# the journal we're maintaining the SRP.
class PersistenceManager:
    def save_to_file(self, journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug.")
print(f"Journal entries:\n{j}\n")

p = PersistenceManager()
file = 'journal.txt'
p.save_to_file(j, file)

print("Inside Journal File")
with open(file) as fh:
    print(fh.read())
