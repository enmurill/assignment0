# -------------------------------------------------------
# code template for assignment 0
# This code doesn't do anything meaningful;
# Just find and remove the bugs to make the final result True
# -------------------------------------------------------

def matches():
    with open('output.txt', 'r') as file1:
        with open('baseline.txt', 'r') as file2:

            line1, line2 = file1.readline(), file2.readline()

            while line1 and line2:
                if line1 != line2:
                    return True
                line1, line2 = file1.readline(), file2.readline()
    return False

def aGenerator(aLimit):
    i = 0
    while i < aLimit:
        yield i
        i += 1

def doSomethingElse(anOutputFile):
    # emit text to the output file...
    anOutputFile.write("doSomethingElse\n")

    theGen = aGenerator(10)

    anOutputFile.write("word %s\n" % next(theGen))
    anOutputFile.write("word %s\n" % next(theGen))
    anOutputFile.write("word %s\n" % next(theGen))
    anOutputFile.write("words %s\n" % "blah" * next(theGen))

    return True

def doSomething(anOutputFile):
    anOutputFile.write("doSomething\n")
    return doSomethingElse(anOutputFile)

# -------------------------------------------------------

if __name__ == "__main__":

    #This code runs the self-test. This code works fine, so you can ignore it...
    with open('output.txt', 'w') as theOutputFile:
        doSomething(theOutputFile)

    print("matches ", matches())
