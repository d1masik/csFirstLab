import os, sys, gzip
from math import log2

if __name__ == "__main__" :
    try:
        textFile = sys.argv[1]
        fileName = os.path.basename(textFile)

        print(f"File Name: {fileName}\n")

        def avgEntropy(alphabet, text, length):
            result = 0

            for char in alphabet:
                frequency = text.count(char) / length
                result += -frequency * log2(frequency)
                print(f"Frequency of appearence for charachter '{char}': {frequency}")

            return result

        if ("gz" in fileName):
            with gzip.open(textFile, "rb") as compressedFile:
                inputText = str(compressedFile.read())
                alphabet = set(list(inputText))
                charAmount = len(inputText)
                fileSize = os.stat(textFile).st_size

                entropy = avgEntropy(alphabet, inputText, charAmount)
                entropyFileSize = entropy * charAmount / 8

                print(f"\nAverage entropy for alphabet: {entropy}\n",
                    f"Amount of information: {entropyFileSize}\n",
                    f"File size: {fileSize} bytes")
        else:
            with open(textFile) as analyzedFile:
                inputText = analyzedFile.read()
                alphabet = set(list(inputText))
                charAmount = len(inputText)
                fileSize = os.stat(textFile).st_size

                entropy = avgEntropy(alphabet, inputText, charAmount)
                entropyFileSize = entropy * charAmount / 8

                print(f"\nAverage entropy for alphabet: {entropy}\n",
                    f"Amount of information: {entropyFileSize}\n",
                    f"File size: {fileSize} bytes")

    except IOError:
        print("Error: file not found")