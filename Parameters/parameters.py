def testScore(numCorrect, total = 100):
    return numCorrect / total * 100

print("Test Score:", testScore(87, 93))
print("Unspecified Test Score:", testScore(87))
print("Specified Paraneter:", testScore(87, total = 90))