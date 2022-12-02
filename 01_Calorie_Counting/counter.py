print('Attention Elves, who has the most calories?')

with open('input.txt') as f:
    elf_input = f.readlines()
top_elf = 0
top_elf_number = 0
current_elf = 0
elf_total = 0
for line in elf_input:
    current_elf += 1
    line = line.strip()
    if len(line) > 0:
        elf_total += int(line)
    else:
        if elf_total > top_elf:
            top_elf = elf_total
            top_elf_number = current_elf
            print('Elf', current_elf, 'with an all new high!')
        elf_total = 0
print('Winner is', top_elf_number, 'with', top_elf, 'calories!')