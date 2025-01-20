n, m = map(int, input().split())
melody = list(map(int, input().split()))
count_m = 0
note = set()
len_note = 0
count = 0
for i in range(n):
    if melody[i] not in note:
        note.add(melody[i])
        len_note += 1
    if len_note == m:
        note.clear()
        len_note = 0
        count += 1
print(count + 1)