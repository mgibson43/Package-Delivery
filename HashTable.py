class HashTable:
  def _init_(self):
    self.size = 41
    self.hash_table = [None] * self.size

  def _get_hash(self, key):
    return key % self.size
  
  def add(self, key, value):
    key_hash = self._get_hash(key)
    key_value = [key, value]

    if self.hash_table[key_hash] is None:
      self.hash_table[key_hash] = list([key_value])

  def get(self, key):
    if self.hash_table[key] is not None:
      return self.hash_table[key][1]
    
  

  # def _init_(self, size):
  #   self.size = size
  #   self.hash_table = [None] * self.size

  # def _get_hash(self, key):
  #   hash = 0
  #   for char in str(key):
  #     hash += ord(char)
  #   return hash % self.size

  # def add(self, key, value):
  #   key_hash = self._get_hash(key)
  #   key_value = [key, value]

  #   if self.hash_table[key_hash] is None:
  #     self.hash_table[key_hash] = list([key_value])
  #     return True
  #   else:
  #     for pair in self.hash_table[key_hash]:
  #       if pair[0] == key:
  #         pair[1] = value
  #         return True
  #     self.hash_table[key_hash].append(key_value)
  #     return True

  # def get(self, key):
  #   key_hash = self._get_hash(key)
  #   if self.hash_table[key_hash] is not None:
  #     for pair in self.hash_table[key_hash]:
  #       if pair[0] == key:
  #         return pair[1]
  #   return None

  # def delete(self, key):
  #   key_hash = self._get_hash(key)

  #   if self.hash_table[key_hash] is None:
  #     return False
  #   for i in range (0, len(self.hash_table[key_hash])):
  #     if self.hash_table[key_hash][i][0] == key:
  #       self.hash_table[key_hash].pop(i)
  #       return True
  
  # def print(self):
  #   for item in self.hash_table:
  #     if item is not None:
  #       print(str(item))