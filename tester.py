from hypymedia import (
    a_,
    aside_,
    body_,
    div_,
    footer_,
    h1_,
    head_,
    header_,
    html_,
    li_,
    main_,
    meta_,
    nav_,
    p_,
    script_,
    section_,
    title_,
    ul_,
)


def html_view(heading: str):
    doctype = "<!DOCTYPE html>"

    # HEAD
    head_view = head_(
        [
            meta_(None, {"charset": "UTF-8"}),
            meta_(None, {"http-equiv": "X-UA-Compatible", "content": "IE=edge"}),
            meta_(
                None,
                {
                    "name": "viewport",
                    "content": "width=device-width, initial-scale=1.0",
                },
            ),
            title_("Hypermediacy"),
            script_(None, {"src": "https://unpkg.com/htmx.org@1.8.0"}),
        ]
    )

    # BODY

    # Header
    header_view = header_(
        [
            h1_(a_(f"{heading}", {"href": "#"})),
            nav_(
                ul_(
                    li_(a_("home", {"href": "#"}), {"class": "active"}),
                )
            ),
        ],
        {"id": "banner", "class": "body"},
    )

    # Main
    main_view = main_(
        [
            section_(
                div_("Sign In", {"hx-get": "views/index/signin.html"}),
                {"id": "content", "class": "body"},
            ),
            section_(p_("User is not logged in"), {"id": "notify"}),
        ]
    )

    # Aside
    aside_view = aside_("Extra Content")

    # Footer
    footer_view = footer_("Footer")

    # HTML
    final_html = html_(
        [
            head_view,
            body_(
                [
                    header_view,
                    main_view,
                    aside_view,
                    footer_view,
                ],
                {"id": "index", "class": "home"},
            ),
        ],
        {"lang": "en"},
    )

    return f"{doctype}\n{final_html}"


print(html_view("Testyboi"))
