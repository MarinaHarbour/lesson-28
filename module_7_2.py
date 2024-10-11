def custom_write(file_name, strings):
    string_position = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        line_number = 1

        for string in strings:
            position = file.tell()
            file.write(string + '\n')
            key = (line_number, position)
            value = strings
            string_position[key] = value
            line_number += 1

    return string_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
