import os

end_tag = "<!--end-->"

source = ""
with open('index.html', mode="r", encoding="utf-8") as index:
    source = index.read()


def make_degrees():
    global source  
    for category in os.listdir("degrees"):
        begin_tag = "<!--begin degrees/" + category + "-->"
        start = source.index(begin_tag)
        if start < 0:
            raise "Could not found where to put the degrees of: " + category;
        end = source.index(end_tag, start + len(begin_tag))
        if end < 0:
            raise "Could not found where to end the degrees of: " + category;
        made = "";
        for degree in sorted(os.listdir("degrees/" + category), reverse=True):
            made += "\n              <div><a href='link'>" + degree + "</a></div>";
        made += "\n              "
        source = source[:start+len(begin_tag)] + made + source[end:]


def save():
    with open('index_new.html', mode="w", encoding="utf-8") as index_new:
        index_new.write(source)

if __name__ == '__main__':
    make_degrees()
    save()