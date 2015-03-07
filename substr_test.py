text = "X-DSPAM-Confidence:    0.8475";
pos = text.find('.')
numbr = text[pos:pos+5]
print(float(numbr))
