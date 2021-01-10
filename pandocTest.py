import pypandoc

print(pypandoc.get_pandoc_formats())

# output = pypandoc.convert_file(
#     r"C:\Users\Tilman\Documents\GitHub\convert\test.csv", "docx", outputfile="somefile.docx", format="csv")

# output = pypandoc.convert_file('somefile.md', 'docx', outputfile="somefile.docx")
