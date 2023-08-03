from hypymedia import html, body, h1, p, div


def html_view(heading: str):
    return html(
        [
            body(
                [
                    h1(heading),
                    div(
                        p("My first paragraph."),
                    ),
                ],
                {"hx-boost": "true"},
            )
        ]
    )


print(html_view("Testyboi"))
