def generate_html(content):
    html = f'<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Document</title></head><body><p>{content}</p></body></html>'
    file = open('./index.html', "w")
    file.write(html)
    file.close()
