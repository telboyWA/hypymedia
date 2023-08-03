# A list of all of the HTML elements supported by modern browsers.
from pathlib import Path

tags = [
    ("a",),
    ("abbr",),
    ("address",),
    ("area", True),
    ("article",),
    ("aside",),
    ("audio",),
    ("base", True),
    ("blockquote",),
    ("body",),
    ("br", True),
    ("button",),
    ("canvas",),
    ("caption",),
    ("circle",),
    ("cite",),
    ("code",),
    ("col", True),
    ("colgroup",),
    ("data",),
    ("datalist",),
    ("dd",),
    ("del_",),
    ("details",),
    ("dialog",),
    ("div",),
    ("dl",),
    ("dt",),
    ("ellipse",),
    ("em",),
    ("embed", True),
    ("fieldset",),
    ("figcaption",),
    ("figure",),
    ("footer",),
    ("form",),
    ("h1",),
    ("h2",),
    ("h3",),
    ("h4",),
    ("h5",),
    ("h6",),
    ("head",),
    ("header",),
    ("hr", True),
    ("html",),
    ("iframe",),
    ("img", True),
    ("input_", True),
    ("kbd",),
    ("label",),
    ("legend",),
    ("li",),
    ("link", True),
    ("main_",),
    ("map_",),
    ("mark",),
    ("menu",),
    ("meta", True),
    ("meter",),
    ("nav",),
    ("noscript",),
    ("ol",),
    ("optgroup",),
    ("option",),
    ("output",),
    ("p",),
    ("picture",),
    ("polygon",),
    ("portal",),
    ("pre",),
    ("progress",),
    ("param", True),
    ("q",),
    ("rect",),
    ("s",),
    ("samp",),
    ("script",),
    ("section",),
    ("select",),
    ("slot",),
    ("small",),
    ("source", True),
    ("span",),
    ("strong",),
    ("style",),
    ("sub",),
    ("summary",),
    ("sup",),
    ("svg",),
    ("table",),
    ("tbody",),
    ("td",),
    ("template",),
    ("text",),
    ("textarea",),
    ("tfoot",),
    ("th",),
    ("thead",),
    ("time",),
    ("title",),
    ("tr",),
    ("track", True),
    ("u",),
    ("ul",),
    ("var",),
    ("video",),
    ("wbr", True),
]


def create_elements(html_list: set) -> None:
    tags = []
    for html_element in html_list:
        el, *tag = html_element
        end_tag = False if tag else True
        tags.append(f'("{el}", {end_tag})')
        # print(f'("{el}", {end_tag}),')

    output_text = f'tags = [{",".join([tag for tag in tags])}]'

    output_file = Path().cwd() / "hypymedia" / "html_list.py"

    with open(output_file, "w") as py_file:
        py_file.write(output_text)


def list_elements_for_export(html_list: set) -> None:
    elements = []
    for html_element in html_list:
        el, *_ = html_element
        elements.append(el)

    output_text = f'from .main import ({",".join([element for element in elements])})'

    output_file = Path().cwd() / "hypymedia" / "__init__.py"

    with open(output_file, "w") as py_file:
        py_file.write(output_text)


for tag in tags:
    if tag[0].endswith("_"):
        continue
    tag_end = ""
    if len(tag) > 1:
        tag_end = tag[1]
    tag = f"({tag[0]}_,{tag_end}),"
    print(tag)


# # Update HTML elements
# create_elements(tags)
# list_elements_for_export(tags)
