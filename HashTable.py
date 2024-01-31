class HashTable:
  def __init__(self):
    self.size = 41
    self.hash_table = [None] * self.size

  def _get_hash(self, key):
    return key % self.size
  
  def add(self, key, value):
    key_hash = self._get_hash(key)
    key_value = [key, value]

    if self.hash_table[key_hash] is None:
      self.hash_table[key_hash] = key_value

  def get(self, key):
    if self.hash_table[key] is not None:
      return self.hash_table[key][1]

  def delete(self, key):
    key_hash = self._get_hash(key)
    if self.hash_table[key_hash] is None:
      return False
    if self.hash_table[key_hash][0] == key:
      self.hash_table.pop(key_hash)
      return True

  def print(self):
    for item in self.hash_table:
      if item is not None:
        print(str(item))