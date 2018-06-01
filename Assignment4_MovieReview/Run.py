from Movie_Review import *
import time


def submain(x):
    print("analyzing the trainingsets...")
    time.sleep(1)
    preader=Reader("C:/Users/Dennis/Downloads/data(2)/data/subset/train/pos",x,2)
    nreader=Reader("C:/Users/Dennis/Downloads/data(2)/data/subset/train/neg",x,2)

    preader.read()
    nreader.read()
    nreader.analyze(preader)
    preader.analyze(nreader)

    tester=Tester(preader,nreader,x)
    tester.classify("C:/Users/Dennis/Downloads/data(2)/data/subset/test/neg", 'neg')
    tester.classify("C:/Users/Dennis/Downloads/data(2)/data/subset/test/pos", 'pos')
    time.sleep(1)
    print("process finished")

submain(3)
print()
submain(2)
print()
submain(0)
print()

def allmain(x):
    print("analyzing the actual sets")
    preader=Reader("C:/Users/Dennis/Downloads/data(2)/data/alle/train/pos",x,2)
    nreader=Reader("C:/Users/Dennis/Downloads/data(2)/data/alle/train/neg",x,2)

    preader.read()
    nreader.read()
    nreader.analyze(preader)
    preader.analyze(nreader)

    tester=Tester(preader,nreader,x)
    tester.classify("C:/Users/Dennis/Downloads/data(2)/data/alle/test/neg", 'neg')
    tester.classify("C:/Users/Dennis/Downloads/data(2)/data/alle/test/pos", 'pos')
    time.sleep(1)
    print("process finished")

allmain(3)
print()
allmain(2)
print()
allmain(0)

