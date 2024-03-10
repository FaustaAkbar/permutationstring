def generatePermutations(string):
    permutations = []
    recursivePermute(string, "", permutations)
    return permutations

def recursivePermute(remainingString, currentPermutation, permutations):
    if len(remainingString) == 1:
        permutations.append(currentPermutation + remainingString)
    else:
        for char in remainingString:
            nextPermutation = currentPermutation + char
            nextRemaining = remainingString.replace(char, '', 1)
            recursivePermute(nextRemaining, nextPermutation, permutations)

# Contoh penggunaan
input_string = input("Masukkan kata :")
permutations = generatePermutations(input_string)
for perm in permutations:
    print(perm)
