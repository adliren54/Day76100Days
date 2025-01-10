from flask import Flask
import datetime # import the datetime library

app = Flask(__name__, static_url_path="/static")

@app.route('/')
def index(): 
  page = f"""<html><body>
  <p><a href = "/linktree">Go to linktree</a></p>
  <p><a href = "/portfolio">Go to portfolio</a></p>
  </body>
  </html>"""
  return page

@app.route('/portfolio')
def portfolio():
  page = """
  <html>
  <head>
    <title>My Portfolio</title>
    <link 
      href = "static/portfolio.css"
      rel = "stylesheet"
      type = "text/css"
      />
  </head>
  <body>
  <h1>My Portolio</h1>
  <h2>Welcome to my website!</h2>
  <p>This is a website that shows 5 selected portfolio from my work in Replit 100 Days Code in Python. These are selected portfolion where I find the concept was harder than usual or interesting to implement in other projects, and I plan to back to these challenges again once I finished the whole 100 days.</p>

  <h2>Day 39</h2>
  <p>Before this challenge, I have no idea what hangman is. I heard about it before but have not played it enought to understand what to build. The programming concept was pretty straightforward though.</p>

  <img src="static/images/day39.png" width = 70%>
  <p><a href = "https://replit.com/@tjikini1/Day39100Days">Day 39.</a></p>

  <h2>Day 43</h2>
  <p>Just like in day 39, before this challenge, I have no idea what bingo is. I heard about it before but have not played it enought to understand what to build.</p>

  <img src="static/images/day43.png" width = 70%>
  <p><a href = "https://replit.com/@tjikini1/Day43100Days">Day 43.</a></p>

  <h2>Day 44</h2>
  <p>This is a continuation of day 43 challenge, and still related to Bingo. However, I also found the dynamic 2D list concept harder to digest. Definitely need to back to this challenge again to understand the concept better.</p>

  <img src="static/images/day44.png" width = 70%>
  <p><a href = "https://replit.com/@tjikini1/Day44100Days">Day 44.</a></p>

  <h2>Day 56</h2>
  <p>This project was interesting because I thought to implement it as part of my web scrapping project for textbook. It would be nice to do it based on author or publisher.</p>

  <img src="static/images/day55.png" width = 70%>
  <p><a href = "https://replit.com/@tjikini1/Day56100Days">Day 56 (wrong picture from day 55).</a></p>

  <h2>Day 71</h2>
  <p>Before this challenge, I have no idea what hangman is. I heard about it before but have not played it enought to understand what to build. The programming concept was pretty straightforward though.</p>

  <img src="static/images/day71.png" width = 70%>
  <p><a href = "https://replit.com/@tjikini1/Day71100Days">Day 71.</a></p>

    <p><a href="baldies2.html">Go to page 2</a></p>

  </body>
  </html>
  """
  return page

@app.route('/linktree')
def linktree():
  page = f"""
  <html>

  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Linktree</title>
    <link href="linktree.css" rel="stylesheet" type="text/css" />
  </head>

  <body>
    <img src="static/images/picture.jpg" width=10%>
    <h1>Renhoren</h1>
    <p class="blurb">Trying to complete Replit 100 Days of Coding</p>
    <h2>Socials</h2>
    <h3><a href = "https://x.com/Tjikini1">Twitter (@Tjikini1)</a></h3>
    <h3><a href = "https://arenhoren.substack.com/">Substack (@arenhoren)</a></h3>
    <h3><a href = "https://replit.com/@tjikini1">Replit (@tjikini1)</a></h3>

    <script src="script.js"></script>

  </body>

  </html>
  """
  return page

app.run(host='0.0.0.0', port=81)