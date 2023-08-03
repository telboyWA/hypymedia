import pytest
from hypymedia.html_list import tags
from hypymedia.main import create_element, create_tag_function


def test_create_element_with_empty_attributes():
    result = create_element("div")
    assert result == "<div></div>"


def test_create_element_with_attributes():
    result = create_element("div", attributes={"class": "test", "id": "mydiv"})
    assert result == '<div class="test" id="mydiv"></div>'


def test_create_element_with_boolean_attributes():
    result = create_element("div", attributes={"class": "test", "disabled": True})
    assert result == '<div class="test" disabled></div>'


def test_create_element_without_end_tag():
    result = create_element("input", end_tag=False)
    assert result == "<input>"


def test_create_element_with_content_str():
    result = create_element("p", content="Hello World")
    assert result == "<p>Hello World</p>"


def test_create_element_with_content_list():
    result = create_element("p", content=["Hello", " ", "World"])
    assert result == "<p>Hello World</p>"


def test_create_element_with_underscore_in_tag():
    result = create_element("p_", content="Hello World")
    assert result == "<p>Hello World</p>"


def test_create_element_with_mixed_parameters():
    result = create_element(
        "div", content=["Hello", "World"], attributes={"class": "test"}, end_tag=False
    )
    assert result == '<div class="test">HelloWorld'


def test_create_tag_function():
    p_ = create_tag_function("p")
    result = p_("Hello World", {"class": "text"})
    assert result == '<p class="text">Hello World</p>'


@pytest.mark.parametrize("tag_name,end_tag", tags)
def test_tags_creation(tag_name, end_tag):
    # Get the function from the global scope
    tag_function = globals()[tag_name] = create_tag_function(tag_name, end_tag=end_tag)

    content = "Content" if end_tag else None
    attributes = {"class": "test"}
    result = tag_function(content=content, attributes=attributes)

    # Removing trailing underscore from the tag name
    actual_tag_name = tag_name[:-1]  # Stripping the last character

    # Formatting attributes
    attributes_str = " ".join(f'{k}="{v}"' for k, v in attributes.items())

    if end_tag:
        expected = f"<{actual_tag_name} {attributes_str}>Content</{actual_tag_name}>"
    else:
        expected = f"<{actual_tag_name} {attributes_str}>"

    assert result == expected.strip()
