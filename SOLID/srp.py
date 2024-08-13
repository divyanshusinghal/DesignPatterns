# single responsibility principle
# also called separation of concerns

# if you load a single class with too many functionalities, you end up creating an anti-pattern
# also called God Object
# SRP prevents us from creating a God Object

class Journal:
    "Primary purpose of Journal is to add and remove entries"
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count+=1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        # deletes the entry from the corresponding position
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    # we break srp by giving additional responsibilities
    # (saving and loading)

    def save(self, filename):
        file = open(filename, 'w')
        file.write(str(self))
        file.close()

    def load(self, filename):
        pass


class PersistanceManager:
    """We have created a new central class to save journal entries.
    This ensures that we do not need to create save functionality in each and every file.
    We can manage in centrally. """
    @staticmethod
    def save_to_files(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


if __name__ == "__main__":
    j = Journal()
    j.add_entry("My name is James Bond")
    j.add_entry("I live in London")
    print(f'Journal entries: \n{j}')

    file = r"C:\Users\singh\PycharmProjects\DesignPatterns\SOLID\journal_entries.txt"
    PersistanceManager.save_to_files(j, file)

    print("Reading from the file now: \n")
    with open(file) as fh:
        print(fh.read())