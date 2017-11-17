class Phonebook:
    def __init__(self):
        self._entries = dict()
        self._is_consistent = True

    def add(self, name, number):
        self._check_consistency_of_added_number(number)
        self._entries[name] = number

    def _check_consistency_of_added_number(self, number):
        self._check_duplicate_number(number)
        self._check_prefix_number(number)

    def _check_duplicate_number(self, number):
        if number in self._entries.values():
            self._is_consistent = False

    def _check_prefix_number(self, new_number):
        for existing_number in self._entries.values():
            if new_number.startswith(existing_number) or existing_number.startswith(new_number):
                self._is_consistent = False

    def lookup(self, name):
        return self._entries[name]

    def is_consistent(self):
        return self._is_consistent
