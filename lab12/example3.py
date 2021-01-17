class DNA:

  def __init__(self, string):
    self.string = string
  
  def count_nucleotides(self):
    dict_nucleotides = {}
    dict_nucleotides["A"] = self.string.count("A")
    dict_nucleotides["G"] = self.string.count("G")
    dict_nucleotides["C"] = self.string.count("C")
    dict_nucleotides["T"] = self.string.count("T")
    return dict_nucleotides
  
  def calculate_complement(self):
    new_string = ""
    for i in self.string:
      if i == "A":
        new_string += "T"
      elif i == "T":
        new_string += "A"
      elif i == "C":
        new_string += "G"
      elif i == "G":
        new_string += "C"
    return new_string
  
  def count_point_mutations(self, dna):
    distance = 0
    for i in range(len(dna)):
      if self.string[i] != dna[i]:
        distance += 1
    return distance
  
  def find_motif(self, dna):
    locations = []
    for i in range(len(self.string)-len(dna)+1):
      if self.string[i:i+len(dna)] == dna:
        locations.append(i)
    return locations


d1 = DNA("AGGGTAG")
print(d1.count_nucleotides())
print(d1.calculate_complement())
print(d1.count_point_mutations("AGGTTAG"))
print(d1.find_motif("AG"))
