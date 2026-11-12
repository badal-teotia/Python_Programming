# Store numerical and float value of the same number

# 1. Store one representation as a string.
# 2. Store values with labels in a set.

values = {9, "9.0"}
labelled_values = {
    ("float", 9.0),
    ("int", 9)
}

print(values,"\n", labelled_values)
