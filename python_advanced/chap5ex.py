import winsound
import itertools


class MusicNotes:
    def __init__(self):
        self.notes = [
            [55, 110, 220, 440, 880],
            [61.74, 123.48, 246.96, 493.92, 987.84],
            [65.41, 130.82, 261.64, 523.28, 1046.56],
            [73.42, 146.84, 293.68, 587.36, 1174.72],
            [82.41, 164.82, 329.64, 659.28, 1318.56],
            [87.31, 174.62, 349.24, 698.48, 1396.96],
            [98, 196, 392, 784, 1568],
        ]
        self.current_note = 0
        self.current_octave = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_octave >= len(self.notes[0]):
            raise StopIteration

        note = self.notes[self.current_note][self.current_octave]

        self.current_note += 1
        if self.current_note >= len(self.notes):
            self.current_note = 0
            self.current_octave += 1

        return note


def check_id_valid(id_number):
    id_str = str(id_number).zfill(9)
    sum_digits = sum((int(digit)*2 if i%2 else int(digit))//10 + (int(digit)*2 if i%2 else int(digit))%10 for i, digit in enumerate(id_str))
    return sum_digits % 10 == 0


class IDIterator:
    def __init__(self, id_number):
        self.id_ = id_number

    def __iter__(self):
        return self

    def __next__(self):
        self.id_ += 1
        while not check_id_valid(self.id_):
            self.id_ += 1
            if self.id_ > 999999999:
                raise StopIteration
        return self.id_


def id_generator(id_number):
    id_ = id_number
    while id_ < 999999999:
        id_ += 1
        if check_id_valid(id_):
            yield id_




def main():
    # freqs = {
    #     "la": 220,
    #     "si": 247,
    #     "do": 261,
    #     "re": 293,
    #     "mi": 329,
    #     "fa": 349,
    #     "sol": 392,
    # }
    #
    # notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"
    #
    # split_notes = notes.split('-')
    # print(type(split_notes))
    # print(dir(split_notes))
    #
    # # for each note-duration pair in the split_notes list
    # for note_duration in split_notes:
    #     #פיצול בין התו למשך הזמן
    #     note, duration = note_duration.split(',')
    #     # קבלת תדירות
    #     frequency = freqs[note]
    #     # הפיכת משך הזמן למספר שלם
    #     duration = int(duration)
    #     # נגן
    #     winsound.Beep(frequency, duration)

    # numbers = iter(list(range(1, 103)))
    # for i in numbers:
    #     next(numbers)
    #     next(numbers)
    #     print(i)

    # bills = [20] * 3 + [10] * 5 + [5] * 2 + [1] * 5
    # unique_combinations = set()
    # for r in range(1, len(bills) + 1):
    #     for combination in itertools.combinations(bills, r):
    #         if sum(combination) == 100:
    #             unique_combinations.add(frozenset(combination))
    #
    # for combination in unique_combinations:
    #     print([bill for bill in combination])
    #
    # print(len(unique_combinations))

    # notes_iter = iter(MusicNotes())
    # for freq in notes_iter:
    #     print(freq)

    # print(check_id_valid(123456780))
    # print(check_id_valid(123456782))

    id_number = int(input("Enter ID: "))
    choice = input("Generator or Iterator? (gen/it)? ")

    if choice == 'it':
        id_iter = iter(IDIterator(id_number))
        for _ in range(10):
            print(next(id_iter))
    elif choice == 'gen':
        id_gen = id_generator(id_number)
        for _ in range(10):
            print(next(id_gen))

    return 0


if __name__ == '__main__':
    main()
