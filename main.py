from tkinter import *
import time
import random
from faker import Faker

def generate_random_short_sentence_list(num_sentences):
    fake = Faker()
    short_sentence_list = [fake.sentence(nb_words=random.randint(5, 10))[:-1] + '.' for _ in range(num_sentences)]
    return short_sentence_list

# Example usage:
random_short_sentence_list = generate_random_short_sentence_list(10)

class TypeSpeedTest:
    def __init__(self, master):
        self.master = master
        self.master.title = "Type Speed Test"

        self.random_sentences = random_short_sentence_list

        self.current_sentence = random.choice(self.random_sentences)

        self.title_label = Label(master, text="Type Speed Test", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=10)

        self.random_word_label = Label(master, text=self.current_sentence, font=("Arial", 12))
        self.random_word_label.pack(pady=10)

        self.word_entry = Entry(master, font=("Arial", 12))
        self.word_entry.pack(pady=10)

        self.start_btn = Button(master, text="Start", command=self.check_typing_speed)
        self.start_btn.pack(pady=10)

        self.result_label = Label(master, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def check_typing_speed(self):
        entered_text = self.word_entry.get()
        if entered_text == self.current_sentence:
            elapsed_time = time.perf_counter()
            self.result_label.config(text=f"Your typing speed is: {elapsed_time} seconds")
        else:
            self.result_label.config(text="Incorrect entry, try again!")

if __name__ == "__main__":
    window = Tk()
    test = TypeSpeedTest(window)
    window.mainloop()


# #Timer Class to handle calculating time for input
# class Timer:
#     def __init__(self):
#         self.start_time = None
#         self.end_time = None
#
#     def start(self):
#         self.start_time = time.time()
#         print("start")
#     def stop(self):
#         self.end_time = time.time()
#         print("stop")
#         self.elapsed_time()
#         check_if_valid()
#
#     def elapsed_time(self):
#         if self.start_time is None:
#             raise ValueError('Timer not started')
#         if self.end_time is None:
#             raise ValueError('Timer not stopped')
#         print(self.end_time - self.start_time)
#         total_time = self.end_time - self.start_time
#         return round(total_time, 2)
#         # output_label.config(text=str(total_time))

# def get_random_word(word_list):
#     if len(word_list) < 1:
#         return None  # Return None if the list is empty
#     return random.choice(word_list)
#
# word_list = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'pear', 'cherry', 'strawberry', 'blueberry', 'raspberry']
# random_word = get_random_word(word_list)




# def check_if_valid():
#     if word_entry.get() == random_sentence:
#         output_label.config(text=f"{str(timer.elapsed_time())} seconds!")
#     else:
#         output_label.config(text="WRONG WORD ENTERED")
#
# timer = Timer()
# window = Tk()
# window.title("Type Speed Test")
# window.minsize(500, 500)
# window.config(padx=100, pady=200)
#
# title_label = Label(text="Type Speed Test", font=("Arial", 24, "bold"))
# title_label.grid(column=0, row=0)
# title_label.config(padx=10, pady=10)
#
# random_word_label = Label(text=random_sentence, font=("Arial", 16, "normal"))
# random_word_label.grid(column=0, row=1)
# random_word_label.config(padx=10, pady=10)
#
# word_entry = Entry(width=60)
# word_entry.grid(column=0,row=2)
#
# start_btn = Button(text="Start", command=timer.start)
# start_btn.grid(column=0, row=3)
#
# end_btn = Button(text="End", command=timer.stop)
# end_btn.grid(column=0, row=4)
#
# output_label = Label(text="...", font=("Arial", 16, "normal"))
# output_label.grid(column=0, row=5)
# output_label.config(padx=10, pady=10)










