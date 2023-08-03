# A list of all of the HTML elements supported by modern browsers.
from pathlib import Path

tags = [
    ("a_",),
    ("abbr_",),
    ("address_",),
    ("area_", True),
    ("article_",),
    ("aside_",),
    ("audio_",),
    ("base_", True),
    ("blockquote_",),
    ("body_",),
    ("br_", True),
    ("button_",),
    ("canvas_",),
    ("caption_",),
    ("circle_",),
    ("cite_",),
    ("code_",),
    ("col_", True),
    ("colgroup_",),
    ("data_",),
    ("datalist_",),
    ("dd_",),
    ("del_",),
    ("details_",),
    ("dialog_",),
    ("div_",),
    ("dl_",),
    ("dt_",),
    ("ellipse_",),
    ("em_",),
    ("embed_", True),
    ("fieldset_",),
    ("figcaption_",),
    ("figure_",),
    ("footer_",),
    ("form_",),
    ("h1_",),
    ("h2_",),
    ("h3_",),
    ("h4_",),
    ("h5_",),
    ("h6_",),
    ("head_",),
    ("header_",),
    ("hr_", True),
    ("html_",),
    ("iframe_",),
    ("img_", True),
    ("input_", True),
    ("kbd_",),
    ("label_",),
    ("legend_",),
    ("li_",),
    ("link_", True),
    ("main_",),
    ("map_",),
    ("mark_",),
    ("menu_",),
    ("meta_", True),
    ("meter_",),
    ("nav_",),
    ("noscript_",),
    ("ol_",),
    ("optgroup_",),
    ("option_",),
    ("output_",),
    ("p_",),
    ("picture_",),
    ("polygon_",),
    ("portal_",),
    ("pre_",),
    ("progress_",),
    ("param_", True),
    ("q_",),
    ("rect_",),
    ("s_",),
    ("samp_",),
    ("script_",),
    ("section_",),
    ("select_",),
    ("slot_",),
    ("small_",),
    ("source_", True),
    ("span_",),
    ("strong_",),
    ("style_",),
    ("sub_",),
    ("summary_",),
    ("sup_",),
    ("svg_",),
    ("table_",),
    ("tbody_",),
    ("td_",),
    ("template_",),
    ("text_",),
    ("textarea_",),
    ("tfoot_",),
    ("th_",),
    ("thead_",),
    ("time_",),
    ("title_",),
    ("tr_",),
    ("track_", True),
    ("u_",),
    ("ul_",),
    ("var_",),
    ("video_",),
    ("wbr_", True),
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


# Update HTML elements
create_elements(tags)
list_elements_for_export(tags)
