import re



file = 'paragraph_2.txt'
newlines=[]
sentence_count=0
word_count=0
sum_word_length=0
with open(file, 'r') as text:

    lines = text.read()
    sentence_count = lines.count(".")
    newlines=re.sub('[.,]','',lines)
    newlines=re.split('\s', newlines)
    word_count=len(newlines)
    
    for word in newlines:
        sum_word_length += len(word)
    

    print(f'Paragraph Analysis')
    print(f'-------------------')
    print(f'Approximate Word Count is: {word_count}')
    print(f'Approximate Sentence Count is: {sentence_count}')
    print(f'Average Word Length in letters: {round((sum_word_length/word_count),0)}')
    print(f'Average Sentence Lenth in words: {round(word_count/sentence_count)}')


bankfile = open("PyParagraph2.out", 'w')
bankfile.write("Paragraph Analysis\n")
bankfile.write("------------------\n")
bankfile.write('Approximate Word Count is: '+ str(word_count)+"\n")
bankfile.write('Approximate Sentence Count is: '+ str(sentence_count)+"\n")
bankfile.write('Average Word Length in letters: '+ str(round((sum_word_length/word_count),0))+"\n")
bankfile.write('Average Sentence Lenth in words: '+ str(round(word_count/sentence_count))+"\n")