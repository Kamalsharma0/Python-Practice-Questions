"""6. Count Vowels in a String
Question: Write a program to count the number of vowels in the word "education".
Input: education
Expected Output: 5
Hint: Check if each character in the string is a vowel and keep
a count."""

def count_vow(input):
    first_vow = input.count('a')
    second_vow = input.count('e')
    third_vow = input.count('i')
    fourth_vow = input.count('o')
    fifth_vow = input.count('u')
    print(f"Occurence of a = {first_vow}\nOccurence of e = {second_vow}\nOccurence of i = {third_vow}\nOccurence of o = {fourth_vow}\nOccurence of u = {fifth_vow}")
    
count_vow("education")