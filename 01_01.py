filepath = "01_01_Data.txt"

# read split whole file by paragraph (each list element is now a paragraph:
with open(filepath) as f:
    paragraphs = f.read().split("\n\n")

all_elf_totals = []

for n, paragraph in enumerate(paragraphs[0: None]):  # enumerate returns both value itself and also position.
    elf_total = 0

    for number in paragraph.split("\n"):
        if number != '':
            elf_total += int(number) #  += instead of  elf_total = elf total +
    all_elf_totals.append(int(elf_total))

print("Elf with biggest total:", (max(all_elf_totals)))
