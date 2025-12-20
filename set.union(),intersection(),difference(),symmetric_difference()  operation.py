#Union() elements that belongs to A or B (because it is a set we won't count a number twice)
english = int(input())
english_students = set(map(int, input().split()))
french = int(input())
french_students = set(map(int, input().split()))

print(len(english_students.union(french_students)))

# intersection() elements that belongs to A and B
english1 = int(input())
english_students1 = set(map(int, input().split()))
french1 = int(input())
french_students1 = set(map(int, input().split()))
print(len(english_students1.intersection(french_students1)))

# Difference() elements that belongs to A and are not in B
english2 = int(input())
english_students2 = set(map(int, input().split()))
french2 = int(input())
french_students2 = set(map(int, input().split()))
print(len(english_students2.difference(french_students2)))

# Symmetric_Difference() elements belongs to A or B but not Both
english3 = int(input())
english_students3 = set(map(int, input().split()))
french3 = int(input())
french_students3 = set(map(int, input().split()))
print(len(english_students3.symmetric_difference(french_students3)))