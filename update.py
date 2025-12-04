import os
import urllib.parse

end_tag = "<!--end-->"

def make(file_name):
    global end_tag
    source = ""

    with open(file_name, mode="r", encoding="utf-8") as index:
        source = index.read()

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
            made += f"\n                            <div><a href='{link_path}'>{degree}</a></div>"
        made += "\n                            "
        source = source[:start + len(begin_tag)] + made + source[end:]

    with open(file_name, mode="w", encoding="utf-8") as index_new:
        index_new.write(source)

    print("Done " + file_name)


if __name__ == '__main__':
    make("index.html")
