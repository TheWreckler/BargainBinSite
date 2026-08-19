import json

pages = [
    ('json/cards.json',          '_site/index.html',                          '<!-- Static cards -->'),
    ('json/earthdawn_cards.json','_site/Earthdawn/index.html',                '<!-- Earthdawn cards -->'),
    ('json/maps_cards.json',     '_site/Earthdawn/Earthdawn/Maps/index.html',  '<!-- Maps cards -->')
    ('json/wiki_cards.json',     '_site/Earthdawn/Wiki/index.html',  '<!-- Maps cards -->'),
]

def build_cards(data):
    text = ""
    for i in data["cards"]:
        text += f"""
    <div class="card">
        <h1>{i["name"]}</h1>
        <p>{i["description"]}</p>
        <div class="buttons">
            <a href="{i["link"]}"><button class="button">{i["button_text"]}</button></a>
        </div>
    </div>"""
    return text

for json_file, html_file, placeholder in pages:
    with open(json_file) as f:
        data = json.load(f)
    with open(html_file) as f:
        html = f.read()
    html = html.replace(placeholder, build_cards(data))
    with open(html_file, 'w') as f:
        f.write(html)