import random


class NameSelector:

  def __init__(self):
    self.first_names = ["John", "Jordon", "Darius", "Lola", "Christinna", "Tracy", "Sonic", "Shadow", "Ashley", "Tammy"]

    self.last_name = ["The ,Hedgehog", "Baker", "Bunny", "Rose", "The Cat", "Helvetica", "Branham", "Bear", "Tiger", "Magician"]

def get_name(self):
  return self.first_names[random.randint(0, len(self.first_names) -1)]
