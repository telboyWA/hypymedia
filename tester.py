from hypymedia import html_, body_, h1_, div_, p_


def html_view(heading: str):
    return html_(
        [
            body_(
                [
                    h1_(heading),
                    div_(
                        p_("My first paragraph."),
                    ),
                ],
                {"hx-boost": "true"},
            )
        ]
    )


print(html_view("Testyboi"))
