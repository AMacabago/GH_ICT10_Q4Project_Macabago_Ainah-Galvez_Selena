from pyscript import display, HTML

\
# Your data
items = [
    ("Christmas Party", "img1.jpg"),
    ("CAT Graduation", "img2.jpg"),
    ("Christmas Party w/ sir Perez", "img3.jpg"),
    ("Halloween", "img4.jpg"),
    ("Intrams", "img5.jpg"),
    ("CAT Practice", "img6.jpg")
]

# Build the HTML string
html_out = ""
for name, img in items:
    html_out += f"""
    <div class="col-6 col-md-4 mb-4">  <div class="card h-100 shadow-sm">
            <img src="{img}" class="card-img-top" style="height: 200px; object-fit: cover;">
            <div class="card-body">
                <h6 class="fw-bold mb-1">{name}</h6>
            </div>
        </div>
    </div>
    """

# Target the specific ID
display(HTML(html_out), target="grid-target")