text = "Das ist ein Test. Das ist nur ein Test."
text = text.replace(".", "").lower()  # Sonderzeichen entfernen und in Kleinbuchstaben umwandeln
words = text.split()  # Zerlegen in Wörter

word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print("Häufigkeiten:")
for word, count in word_counts.items():
    print(word.capitalize() + ":", count)

# Wie funktioniert split bei anderen Listen?