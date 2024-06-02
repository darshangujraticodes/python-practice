# Table Of Content

1. [Heading](https://github.com/darshangujraticodes/python-practice/blob/main/Markdown-Syntax.md#heading)
2. [Text Style Effect](https://github.com/darshangujraticodes/python-practice/blob/main/Markdown-Syntax.md#text-style-effect)
3. [Insert Text Link ](https://github.com/darshangujraticodes/python-practice/blob/main/Markdown-Syntax.md#insert-link-in-text)
4. [Insert Image](https://github.com/darshangujraticodes/python-practice/blob/main/Markdown-Syntax.md#insert-image)
5. [Alert Message Box](https://github.com/darshangujraticodes/python-practice/blob/main/Markdown-Syntax.md#alert-message)
6. [Ordered and Unoredered List](https://github.com/darshangujraticodes/python-practice/blob/main/Markdown-Syntax.md#ordered-and-unordered-list)
7. [Text Higlighter](https://github.com/darshangujraticodes/python-practice/blob/main/Markdown-Syntax.md#text-highlighter)
8. [Code Block](https://github.com/darshangujraticodes/python-practice/blob/main/Markdown-Syntax.md#code-block)
9. [DropDown Arrow](https://github.com/darshangujraticodes/python-practice/blob/main/Markdown-Syntax.md#dropdown-arrow)

<br>

# Heading

### Heading Syntax :

```
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
```

### Output :

# Heading 1

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

<br>

# Text Style Effect

### Text Style Syntax :

```
Text **Bold** Effect in Readme file
Text *Italic* Effect in Readme File
Text ***Bold and Italic*** in Readme File
Text ~~Strike Effect~~ in Readme File
Emoji in Text :+1:
```

For a full list of available emoji and codes, see the [Emoji-Cheat-Sheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md).

### Text Style Output :

Text **Bold** Effect in Readme file <br>
Text _Italic_ Effect in Readme File <br>
Text **_Bold and Italic_** in Readme File <br>
Text ~~Strike Effect~~ in Readme File <br>
Emoji in Text :+1:

<br>

# Insert Link in Text

### Insert Link Syntax :

```
syntax : [Text Title](Url Link)
eg : [CS Techtube Youtube Channel](https://www.youtube.com/@cstechtube/videos)
```

### Insert Link Output :

[CS Techtube Youtube Channel](https://www.youtube.com/@cstechtube/videos)

<br>

# Insert Image

### Insert Image Syntax :

```
syntax : ![Alt Text](Image Url Link)
eg : ![CS Techtube](https://cstechtube.com/wp-content/uploads/2023/07/Copy-of-xs-1.png)
```

### Insert Image Output :

![CS Techtube](https://yt3.googleusercontent.com/VV55wfKSKiYJsixkcFDq4mlRWbUtcMg596xEfQ8UvQdCDdCqZbRdeAPng7Ekos94TeT5ypdSRCw=s176-c-k-c0x00ffffff-no-rj)

<br>

# Alert Message

### Alert Message Syntax :

```
> Simple Text Quote

> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.
```

### Alert Message Output :

> Simple Text Quote

> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.

<br>

# Ordered and Unordered List

### Ordered List Syntax :

```
1. Item 1
2. Item 2
3. Item 3
```

### Ordered List Output :

1. Item 1
2. Item 2
3. Item 3

### Unordered List Syntax :

It can be created by using any of this three symbol (\*, -, and +)

```
- Item 1
* Item 2
+ Item 3
```

### Unordered List Output :

- Item 1

* Item 2

- Item 3

### Unordered List using HTML Syntax :

```
<ul>
  <li> Item 1</li>
  <li> Item 2</li>
  <li> Item 3</li>
</ul>
```

### Output :

<ul>
  <li> Item 1</li>
  <li> Item 2</li>
  <li> Item 3</li>
</ul>

<br>

# Text Highlighter

Helpful to highlight text in paragraph also with can help to mention color code, or any important point using single backtick
text should be wrapped inside single backtick (`)

Also useful for color highlighter

### Highlighter Syntax :

```
The core purpose of the CSTechtube Channel to make students skillful with both
`Hard skill` and `softskill` to become Industry Ready Professional and Teach them
Skills based on Production and Industry Relevant Methods.

Also useful for color showcase Yellow `#fed700`
```

### Highlighter Output :

The core purpose of the CSTechtube Channel to make students skillful with both `Hard skill` and `softskill` to become Industry Ready Professional and Teach them Skills based on Production and Industry Relevant Methods.

Also useful for color showcase Yellow `#fed700`
<br>

<br>

# Code Block

To Showcase code it need to be wrapped inside 3 Backticks (```)

### Code Block Input Syntax :

````
```
  <html>
    <head>
      <title>Hello World !!</title>
    </head>
    <body>
      <h1>Welcome to CS TechTube Channel</h1>
    </body>
  </html>
```
````

### Code Block Output :

```
  <html>
    <head>
      <title>Hello World !!</title>
    </head>
    <body>
      <h1>Welcome to CS TechTube Channel</h1>
    </body>
  </html>
```

<br>

# Dropdown Arrow

To Showcase dropdown wrapped your code inside details tag (`<details> </details>`)

### DropDown Input Syntax :

Summary define the head part of Dropdown and info out of summary tag are the value which will be showcase in opening drop down

````
```
<details>
  <summary>
  1. Print the Sum of Input number in Python
  </summary>

  Python Code :

  input_val = int(input('Enter your number = '))

  def sum_of_num(number):
      sum = 0
      while (number > 0):
          rem = int(number % 10)
          sum = sum + rem
          number = int(number / 10)

      return sum

  print('Sum of Input Number = ', sum_of_num(input_val))

</details>
```
````

### DropDown Output :

<details>
  <summary>
  1. Print the Sum of Input number in Python
  </summary>

Python Code :

```
input_val = int(input('Enter your number = '))

def sum_of_num(number):
    sum = 0
    while (number > 0):
        rem = int(number % 10)
        sum = sum + rem
        number = int(number / 10)

    return sum

print('Sum of Input Number = ', sum_of_num(input_val))
```

</details>
