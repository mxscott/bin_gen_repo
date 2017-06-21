class BinGenerator(object):
  def __init__(self, file_path, max_gap_size=None, ideal_bin_size=None):
   self.ideal_bin_size = ideal_bin_size
   self.max_gap_size = max_gap_size
   self.start = None
   self.stop = None
   self.reference_name = None
   self.bed_info = []
   self.file = open(file_path)       #open input file
   self.file.readline()     #read past the BED file header


  def __iter__(self):
   num_bins = 0
   total_bin_size = 0
   size = 0
   next_line = self.file.readline()                       #copy next input line to next_line
   next_line = next_line.split('\t')                      #splits line into list around tabs
   line_num = 1
   self.reference_name = next_line[0]
   self.start = int(next_line[1])
   self.stop = int(next_line[2])
   self.bed_info.append(line_num)                                            #tracks how many input lines have been evaluated


   while (True):

      if (self.stop - self.start < self.ideal_bin_size):   #compare current bin size to ideal_bin_size
         next_line = self.file.readline()                 #copy next line of input to next_line
         if (next_line == ""):                             #checks for EOF
             yield self
             num_bins += 1
             total_bin_size += (self.stop - self.start)
             return
         next_line = next_line.split('\t')

         line_num += 1
         if ((int(next_line[1]) - self.stop < self.max_gap_size) and (self.reference_name == next_line[0])):     #check refrence and gap distance
            self.stop = int(next_line[2])
            self.bed_info.append(line_num)
         else:

            yield self
            num_bins += 1
            total_bin_size += (self.stop - self.start)
            self.bed_info[:] = []
            self.reference_name = next_line[0]
            self.start = int(next_line[1])
            self.stop = int(next_line[2])
            self.bed_info.append(line_num)


      else:

          yield self
          num_bins += 1
          total_bin_size += (self.stop - self.start)
          next_line = self.file.readline()             #copy next input line to next_line
          if (next_line == ""):
              return 
          next_line = next_line.split('\t')

          line_num += 1
          self.bed_info[:] = []
          self.reference_name = next_line[0]
          self.start = int(next_line[1])
          self.stop = int(next_line[2])
          self.bed_info.append(line_num)


  def __str__(self):
   return "{}: ({}, {}, {}) {} regions".format(self.__class__, self.reference_name, self.start, self.stop, len(self.bed_info))
