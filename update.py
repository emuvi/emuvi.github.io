import os
import urllib.parse

end_tag = "<!--end-->"

source = ""
with open('index.html', mode="r", encoding="utf-8") as index:
    source = index.read()


def make_degrees():
    global source  
    for category in os.listdir("degrees"):
        begin_tag = f"<!--begin degrees/{category}-->"
        try:
            start = source.index(begin_tag)
        except ValueError:
            raise ValueError(f"Could not find where to put the degrees of: {category}")
        
        try:
            end = source.index(end_tag, start + len(begin_tag))
        except ValueError:
            raise ValueError(f"Could not find where to end the degrees of: {category}")
        
        made = ""
        for degree in sorted(os.listdir(f"degrees/{category}"), reverse=True):
            encoded_name = urllib.parse.quote(degree)  # Codifica o nome do arquivo
            link_path = f"degrees/{category}/{encoded_name}"  # Constrói o caminho do link
            made += f"\n              <div><a href='{link_path}'>{degree}</a></div>"
        made += "\n              "
        source = source[:start + len(begin_tag)] + made + source[end:]


def save():
    with open('index_new.html', mode="w", encoding="utf-8") as index_new:
        index_new.write(source)


if __name__ == '__main__':
    make_degrees()
    save()
    print("Done!")
