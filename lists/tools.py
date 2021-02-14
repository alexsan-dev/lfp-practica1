# APLANAR LISTA
flatten = lambda *n: (e for a in n
                      for e in (flatten(*a) if isinstance(a, (tuple, list)) else (a,)))


def strip_data(data):
    return list(map(lambda field: int(
        field.strip()) if field.strip().isnumeric() else list(map(lambda key: int(key) if key.isnumeric() else key, [words for words in field.strip().split(' ') if words != ''])), data))

# OBTENER POSICIÓN DE LA PRIMERA INSTRUCCIÓN


def get_word_index(list):
    index = 0
    keyword_index = []
    keywords = []

    # RECORRER
    for item in list:
        # BUSCAR INSTRUCCIONES
        if isinstance(item, str):
            # AGREGAR
            keyword = item if item == 'ORDENAR' else [item, list[index + 1]]
            keywords.append(keyword)
            keyword_index.append(index)

        index += 1

    # RETORNAR INSTRUCCIONES
    return [keyword_index[0], keywords]


# OBTENER INDEX DE LIST
def get_items_index(list, element):
    index = 0
    indexes = []

    # RECORRER
    for item in list:
        # AGREGAR
        if item == element:
            indexes.append((index + 1))

        index += 1

    # RETORNAR
    return "NO ENCONTRADO" if len(indexes) == 0 else ", ".join(map(str, indexes))
