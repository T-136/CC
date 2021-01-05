import pypandoc

output = pypandoc.convert_file('test.xlsx', 'rst')

# output = pypandoc.convert_file('somefile.md', 'docx', outputfile="somefile.docx")
# assert output == ""