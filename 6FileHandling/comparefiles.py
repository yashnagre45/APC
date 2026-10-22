file1 = open("file1.txt", "r")
lines1 = file1.readlines()
file1.close()

file2 = open("file2.txt", "r")
lines2 = file2.readlines()
file2.close()

if lines1 == lines2:
    print("Both files are identical")
else:
    print("Files are different")

    for i in range(max(len(lines1), len(lines2))):
        line1 = lines1[i] if i < len(lines1) else None
        line2 = lines2[i] if i < len(lines2) else None

        if line1 != line2:
            print("First difference at line:", i + 1)
            print("File 1:", line1)
            print("File 2:", line2)
            break