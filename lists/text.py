from .sort import merge_sort
from .tools import get_items_index


def set_order_str(filtered_keyword, origin_list, solved_lines, line_id):
    # ORDENAR
    if filtered_keyword == 'ORDENAR' or len(filtered_keyword) == 0:
        data_sorted = merge_sort(origin_list)
        solved_lines.append(
            f'{line_id}: LISTA ORDENADA = {", ".join(map(str, data_sorted))}')


def set_searched_str(filtered_keyword, origin_list, solved_lines, line_id, keyword):
    # BUSCAR
    if filtered_keyword == 'BUSCAR' or len(filtered_keyword) == 0:
        solved_lines.append(
            f'{line_id}: POSICIONES DE {keyword[1]} = {get_items_index(origin_list, keyword[1])}')
