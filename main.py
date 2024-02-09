markdown = """# I am Rakshit
## Hi"""

dict = {'#': 'h1', '##': 'h2', '###': 'h3', '####': 'h4', '#####': 'h5', '######': 'h6'}

for i in markdown.split('\n'):
    # Get first word
    first_word = i.split(' ')[0]
    other_word = ' '.join(i.split(' ')[1:])
    a_html = f'<{dict[first_word]}>{other_word}</{dict[first_word]}>'
    print(a_html)
