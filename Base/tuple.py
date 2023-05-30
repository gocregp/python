ab = {'Swaroop': 'swaroop@swaroopch.com',
      'Larry': 'larry@wall.org',
      'Matsumoto': 'matz@ruby-lang.org',
      'Spammer': 'spammer@hotmail.com'
      }


def show_contacts():
    for name, mail in ab.items():
        print(f'Имя: {name} --------- почта: {mail}', sep='\n')
        print(f'в адресной книге {count} контактов')

ab['one_contact'] = 'one@contact.rf'
ab['new_contact'] = 'list@test.ru'
count = len(ab)
show_contacts()
