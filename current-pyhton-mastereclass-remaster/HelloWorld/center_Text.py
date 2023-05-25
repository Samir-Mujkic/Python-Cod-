def centre_text(*args):
   text = "-".join([str()])
   left_margin = (80 - len(text)) // 2
   print(" " * left_margin, text)

centre_text("spam and eggs")
centre_text("spam, spam and eggs")
centre_text(12)
centre_text("spam, spam, spam and spam")

centre_text("first", "second", 3, 4, "spam")

print(centre_text())