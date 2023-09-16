# 🚀 Hypymedia 

`Hypymedia` is a Python package that significantly simplifies the process of creating dynamic HTML content programmatically. Featuring a rich library of functions, each corresponding to a specific HTML tag, it empowers users to craft HTML elements with dynamic content and attributes seamlessly. 

---

## 🛠 Installation 

Installing the `Hypymedia` package is as easy as running a single command:

```sh
pip install hypymedia
```

---

## 💡 Usage 

`Hypymedia` boasts a user-friendly and intuitive interface. Simply import the desired functions, representing HTML tags, and you are ready to design HTML content dynamically. 

The attributes for tags can be declared through dictionaries, and the content can be customized using additional arguments. 


### 🌟 Basic Usage 

```python
from hypymedia import div_, p_

# Creating a div element with a class attribute containing a p element
html_content = div_({'class': 'example'}, p_('Hello, World!'))
```

Output:

```html
<div class="example">
    <p>Hello, World!</p>
</div>
```

### 🌟 Using Attributes 

Adding attributes to your HTML tags is straightforward, simply pass a dictionary with the elements you need.

```python
from hypymedia import a_

# Crafting a link with href and title attributes
link = a_({'href': 'https://www.example.com', 'title': 'Example'}, 'Click here')
```

Output:

```html
<a href="https://www.example.com" title="Example">Click here</a>
```
where you have an attribute that doesn't have a value (e.g., `disabled`), you can pass `None` as the value:

```python
from hypymedia import button_
button = (button_({"disabled": None}, "Click here"))
```

Output:
```html
<button disabled>Click here</button>
```

### 🌟 Handling Self-closing Tags 

With `Hypymedia`, you can effortlessly create self-closing tags such as `<img>` and `<br>`:

```python
from hypymedia import img_, br_

# Creating an img element with src and alt attributes
image = img_({'src': 'image.jpg', 'alt': 'An example image'})
```

Output:

```html
<img src="image.jpg" alt="An example image"/>
```

---

## 🎨 Examples 

Dive into the potential of `Hypymedia` with these illustrative examples:



### Unordered List

```python
from hypymedia import ul_, li_

# Define the list items
items = ["Item 1", "Item 2", "Item 3"]

# Utilize a list comprehension to develop the list items
list_items = [li_(item) for item in items]

# Create the unordered list
unordered_list = ul_(*list_items)
```

Output:
    
```html
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ul>
```


### Using Python Functions to Build a Table with a List and a List Comprehension 

Constructing a table with lists and list comprehensions is a breeze with `Hypymedia`:

```python
from hypymedia import table_, tr_, th_, td_

# Define the data set for the table
data = [
    ["Name", "Age", "City"],
    ["John Doe", 30, "New York"],
    ["Jane Doe", 28, "Los Angeles"],
    ["Jim Doe", 32, "Chicago"],
]

# Utilize a list comprehension to develop the table rows
rows = [tr_(*[td_(item) for item in row]) for row in data]

# Create the table by unpacking...
table = table_(*rows)

```

Output:

```html
<table>
    <tr>
        <td>Name</td>
        <td>Age</td>
        <td>City</td>
    </tr>
    <tr>
        <td>John Doe</td>
        <td>30</td>
        <td>New York</td>
    </tr>
    <tr>
        <td>Jane Doe</td>
        <td>28</td>
        <td>Los Angeles</td>
    </tr>
    <tr>
        <td>Jim Doe</td>
        <td>32</td>
        <td>Chicago</td>
    </tr>
</table>
```

### Building a Simple Webpage 

Here's how you can assemble a simple webpage utilizing `Hypymedia`:

```python
from hypymedia import html_, head_, title_, body_, h1_, p_, div_, a_, img_

# Define the webpage's title
title = title_("My Simple Webpage")

# Construct the webpage's header
header = h1_("Welcome to My Simple Webpage")

# Create a paragraph for the webpage
paragraph = p_("This is a simple webpage crafted with `Hypymedia`.")

# Design a link for the webpage
link = a_({'href': 'https://www.example.com'}, 'Visit Example.com')

# Develop an image for the webpage
image = img_({'src': 'image.jpg', 'alt': 'An example image'})

# Combine all elements to form the webpage's body
body = body_(header, paragraph, link, image)

# Merge the title and body to craft the complete HTML document
html_document = html_(head_(title), body)
```
Output:
```html
<html>
    <head>
        <title>My Simple Webpage</title>
    </head>
    <body>
        <h1>Welcome to My Simple Webpage</h1>
        <p>This is a simple webpage crafted with `Hypymedia`.</p>
        <a href="https://www.example.com">Visit Example.com</a>
        <img src="image.jpg" alt="An example image"/>
    </body>
</html>
```

## Hypymedia and HTMX

For web libraries like HTMX, utilizing the `Hypymedia` library to generate and return partial HTML content offers numerous advantages. Firstly, it promotes network and server efficiency by only transmitting and processing the necessary data, which invariably enhances the user experience through faster load times and more responsive interactions. 

Moreover, developers gain granular control over content updates, which allows for a more interactive and dynamic web application design. This not only simplifies the codebase but also facilitates easier integration into existing applications without the need for a complete overhaul. 

Furthermore, this approach maintains the benefits of SEO optimization, unlike heavy single-page applications that rely predominantly on client-side rendering, potentially enhancing the visibility of the web content in search engine rankings. Overall, adopting partial content returns with `Hypymedia` can accelerate development cycles, foster a seamless user experience, and cultivate a more streamlined and efficient web application environment.

## Hypymedia or Jinja?
In the ever-evolving landscape of web development, `Hypymedia` emerges as a potent alternative to the well-established Jinja templating engine, particularly for developers vested in Python. 
`Hypymedia` facilitates a Pythonic approach to HTML content generation, allowing developers to leverage Python's syntax and structures seamlessly, thereby potentially reducing the learning curve and boilerplate code often associated with Jinja. Moreover, it integrates effortlessly with modern frontend technologies like HTMX and FastAPI, offering a streamlined pathway to creating dynamic, interactive web applications.

## Simple FastAPI and HTMX Example

```python
from fastapi import FastAPI, HTMLResponse
from hypymedia import html_, head_, body_, div_, p_, a_, img_

app = FastAPI()

def index_view():
    head_view = head_(
            script_({
                "src": "https://unpkg.com/htmx.org@1.9.5", 
                "integrity": "sha384-xcuj3WpfgjlKF+FXhSQFQ0ZNr39ln+hwjN3npfM9VBnUskLolQAcN80McRIVOPuO", 
                "crossorigin": "anonymous"
            })
        )
    
    body_view = body_(
            div_(
                p_("Welcome to our website!"),
                a_({"href": "/image", "hx-get": "/image"}, "Click here to see an image."),
            )
        )

    return html_(head_view, body_view)

@app.get("/", response_class=HTMLResponse)
def read_root():
    return index_view()


@app.get("/image", response_class=HTMLResponse)
def read_image():
    return img_({"src": "logo.png", "alt": "logo"})

```



---

## 📜 License 

This project is licensed under the terms of the MIT License.

