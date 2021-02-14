from lists.tools import flatten, get_word_index, strip_data
from lists.text import set_order_str, set_searched_str


def parse_lines(lines, filtered_keyword):
    solved_lines = []

    for line in lines:
        # SEPARAR VALORES POR =
        values = line.split('=')

        # OBTENER ID Y DATOS
        line_id = values[0].strip()
        data = values[1].strip().split(',')

        # CORTAR ESPACIOS
        data_stripted = strip_data(data)
        data_flated = list(flatten(data_stripted))

        # LISTA ORIGINAL
        keywords = get_word_index(data_flated)
        origin_list = data_flated[0:keywords[0]]

        # RECORRER INSTRUCCIONES
        for keyword in keywords[1]:
            # ORDENAR
            if isinstance(keyword, str):
                set_order_str(filtered_keyword, origin_list,
                              solved_lines, line_id)

            # BUSCAR
            else:
                set_searched_str(filtered_keyword, origin_list,
                                 solved_lines, line_id, keyword)

        # LINEA DE SEPARACION
        solved_lines.append('')

    # IMPRIMIR EN PANTALLA
    final_text = '\n'.join(solved_lines)
    print(final_text)
    return final_text
