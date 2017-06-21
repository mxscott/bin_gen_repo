class BinGenerator(object):
  def __init__(self, file_path, ideal_bin_size=None, max_gap_size=None):
   self.ideal_bin_size = ideal_bin_size
   self.max_gap_size = max_gap_size
   self.start = None
   self.stop = None
   self.reference_name = None
   self.bed_info = []
   self.file = open(file_path)       #open input file
   self.file.readline()     #read past the BED file header
  

  def __iter__(self):
   next_line = self.file.readline.split('\t')           #copy next input line to next_line
   line_num = 1                                         #tracks how many input lines have been evaluated
   while (True):
      self.reference_name = int(curr_line[0])
      self.start = int(next_line[1])
      self.stop = int(next_line[2])
      self.bed_info.append(line_num)
      if (self.stop - self.start < self.ideal_bin_size):   #compare current bin size to ideal_bin_size
         next_line = self.file.readline.split('\t')       #copy next line of input to next_line
         line_num += 1
         if ((int(next_line[1]) - self.stop < max_gap_size) and (int(self.reference_name) == int(next_line[0]))):     #check refrence and gap distance
            self.stop = int(next_line[2])
            self.bed_info.append(line_num)
         else:
            yield Bin(self.start, self.stop, self.reference_name, self.bed_info)
            next_line = self.file.readline.split('\t')       #copy next input line to next_line
            line_num += 1
            self.bed_info[:] = []

      else:
          yield Bin(self.start, self.stop, self.reference_name, self.bed_info)
          next_line = self.file.readline.split('\t')       #copy next input line to next_line
          line_num += 1
          self.bed_info[:] = []


  def __str__(self):
   return "{}: ({}, {}, {}) {} regions".format(self.__class__, self.reference_name, self.start, self.stop, len(self.bed_info))
