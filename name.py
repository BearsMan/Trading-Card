import random


class NameSelector:

  def __init__(self):
    self.first_name = ["John", "Christopher", "Darius", "Lola", "Christinna", "Tracy", "Sonic", "Shadow", "Ashley", "Tammy"]

    self.last_name = ["The ,Hedgehog", "Howell", "Ronkowitz", "Rose", "The Cat", "Helvetica", "Branham", "Bear", "Tiger", "Magician"]

  def get_name(self):
    return self.first_name[random.randint(0, len(self.first_name) -1)] + ""+ self.last_name[random.randint(0, len(self.last_name) -1)]
