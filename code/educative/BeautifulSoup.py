# Importing the Libraries
from bs4 import BeautifulSoup

# Creating the Soup Object from the HTML page
html_page = """
<!DOCTYPE html>
<html>
   <head>
      <title>Data Science Course</title>
      <style></style>
   </head>
   <body>
      <h1 class="my-heading"> This is a Heading Tag </h1>
      <p id="my-paragraph"> This is a paragraph in Data Science Course </p>
      <em> This is an emphasis tag in Data Science Course </em>
      <b> This is a tag for Bold Text </b>
      <i> This is a tag for italic text </i>
      <small> This is a tag for small text </small>
      <u> This is a tag for underlined text </u>
      <a href="https://www.educative.io/"> This is a link to Educative Home Page </a>
      <a href="https://www.facebook.com/"> This is a link to Facebook Home Page </a>
      <a href="https://twitter.com/"> This is a link to Twitter Home Page </a>

      <script></script>
   </body>
</html>
"""

soup = BeautifulSoup(html_page)

# Getting the title tag of Html
print("The <title> tag in the corresponding HTML is \n")
print(soup.title)
print("\n")

# Getting the head tag of Html
print("The <head> tag in the corresponding HTML is \n")
print(soup.head)
print("\n")

# Getting the name of the title tag
print("The name of the <title> tag is \n")
print(soup.title.name)
print("\n")

# Getting the name of the head tag
print("The name of the <head> tag is \n")
print(soup.head.name)
print("\n")

# Getting the Text inside the title tag
print("The text inside the <title> tag is \n")
print(soup.title.string)
print("\n")

# Getting the Text inside the head tag
print("The text inside the <head> tag is \n")
print(soup.head.string)
print("\n")

# Displaying all the anchor tags in the HTML
print("Anchor tags present in the HTML are")
print(soup.find_all('a'))
print("\n")

# Display the links being used in the anchor tag
for link in soup.find_all('a'):
    print("Link URL: {}".format(link.get('href')))
    print("Anchor Text: {}".format(link.text))
    print("\n")