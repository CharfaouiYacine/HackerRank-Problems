english = int(input())
english_students = set(map(int, input().split()))
french = int(input())
french_students = set(map(int, input().split()))

print(len(english_students.union(french_students)))