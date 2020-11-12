# 0x15. Javascript - Web JQuery

### 0. No jQuery mandatory
Write a Javascript script that updates the text color of the HTML tag HEADER to red (#FF0000):

You must use document.querySelector to select the HTML tag
You can’t use the jQuery API
Please test with this HTML file in your browser:

guillaume@ubuntu:~/0x15$ cat 0-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

### 1. With jQuery mandatory
Write a Javascript script that updates the text color of the HTML tag HEADER to red (#FF0000):

You can’t use document.querySelector to select the HTML tag
You must use the jQuery API
Please test with this HTML file in your browser:

### 2. Click and turn red mandatory
Write a Javascript script that updates the text color of the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#red_header:

You can’t use document.querySelector to select the HTML tag
You must use the jQuery API
Please test with this HTML file in your browser:

###  3. Add `.red` class mandatory
Write a Javascript script that adds the class red to the HTML tag HEADER when the user clicks on the tag DIV#red_header

You can’t use document.querySelector to select the HTML tag
You must use the jQuery API
Please test with this HTML file in your browser:

### 4. Toggle classes mandatory
Write a Javascript script that toggles the class of the HTML tag HEADER when the user clicks on the tag DIV#toggle_header:

The HEADER tag must always have one class: red or green, never both in the same time, never empty.
If the current class is red, when the user click on DIV#toggle_header, the class must be updated to green ; and the reverse.
You can’t use document.querySelector to select the HTML tag
You must use the jQuery API
Please test with this HTML file in your browser:

### 5. List of elements mandatory
Write a Javascript script that adds a LI element to a list when the user clicks on the tag DIV#add_item:

The new element must be: <li>Item</li>
The new element must be added to UL.my_list
You can’t use document.querySelector to select the HTML tag
You must use the jQuery API
Please test with this HTML file in your browser:


### 6. Change the text mandatory
Write a Javascript script that updates the text of the HTML tag HEADER to “New Header!!!” when the user clicks on DIV#update_header

You can’t use document.querySelector to select the HTML tag
You must use the jQuery API
Please test with this HTML file in your browser:

### 7. Star wars character mandatory
Write a Javascript script that fetches the name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json

The name must be displayed in the HTML tag DIV#character
You can’t use document.querySelector to select the HTML tag
You must use the jQuery API
Please test with this HTML file in your browser:

### 8. Star Wars movies mandatory
Write a Javascript script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json

All movie titles must be list in the HTML tag UL#list_movies
You can’t use document.querySelector to select the HTML tag
You must use the jQuery API
Please test with this HTML file in your browser:

9. Say Hello! mandatory
Write a Javascript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML’s tag DIV#hello.

The translation of “hello” must be displayed in the HTML tag DIV#hello
You can’t use document.querySelector to select the HTML tag
You must use the jQuery API
Your script must work when it is imported from the HEAD tag
Please test with this HTML file in your browser: