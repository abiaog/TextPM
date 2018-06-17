import sys
import csv, codecs, cStringIO

class TextPM(object):
    ''' 
    model
    view
    controller
    '''

    def __init__(self):
        pass



class UTF8Recoder:
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next().encode("utf-8")

class UnicodeReader:
    """
    A CSV reader which will iterate over lines in the CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)

    def next(self):
        row = self.reader.next()
        return [unicode(s, "utf-8") for s in row]

    def __iter__(self):
        return self

def main():
    filename = 'backlog.csv'
    with open(filename, 'rb') as f:
      reader = UnicodeReader(f)
      for i in range(0, 50):
        print("{} {}".format(reader.next(),"\n"))


"""
   textpm = TextPM() 
"""

if __name__ == '__main__':
    main()


