message = '''Bien sûr, voici un exemple simple de code Python qui affiche "Bonjour, monde!" dans la console:\n\n\n```\nbash`print("Bonjour, monde!")`\n```\n\n\nCe code utilise la fonction `print()` pour afficher le texte "Bonjour, monde!" dans la console Python.'''

result = ''
get = 0
one_previous = ''
two_previous = ''
ignore = False
for caractère in message:
    if caractère == '\n':
        caractère == 'passe à la ligne'
    print('caractère: ' + caractère + ' | caractère précédent: ' + one_previous + ' | caractère précédent du caractère précédent: ' + two_previous )
    # Si on trouve 3 backsticks, on ignore les caractères suivants et on incremente get
    if caractère == '`' and one_previous == '`' and two_previous == '`' and get == 0:
        print('ok1')
        ignore = True
        get += 1
        result += caractère
        one_previous = caractère
        two_previous = one_previous
        pass
    # Si on trouve un backstick et que get vaut 1, on arrete d'ignorer les caractères et on incremente get
    elif caractère == '`' and get == 1:
        print('ok2')
        ignore = False
        get += 1
        result += caractère
        one_previous = caractère
        two_previous = one_previous
        pass
    # Si on trouve un backstick et que get vaut 3, on ignore les caractères suivants et on incremente get
    elif caractère == '`' and get == 3:
        print('ok3')
        ignore = True
        get += 1
        result += caractère
        one_previous = caractère
        two_previous = one_previous
        pass
    # Si on trouve 3 backsticks et que get vaut 4, on arrete d'ignorer les caractères et on incremente get
    elif caractère == '`' and one_previous == '`' and two_previous == '`' and get == 4:
        print('ok4')
        ignore = False
        get += 1
        result += caractère
        one_previous = caractère
        two_previous = one_previous
        pass
    # Si ignore est vrai, on ignore les caractères
    elif ignore == True:
        print('ok5')
        pass
    # Si ignore est faux, on ajoute le caractère à result
    else:
        print('ok6')
        if caractère == 'passe à la ligne':
            result += '\n'
        else:
            result += caractère
        one_previous = caractère
        two_previous = one_previous
        # Si get vaut 5, on remet get à 0
        if get == 5:
            get = 0
    
    

print (result)