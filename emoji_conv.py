text = 'i love😄'
emoji_dict = {
    '😄':'\U0001f604'
}
for emoji, code_point in emoji_dict.items():
    text = text.replace(emoji, code_point)
    print(text)


