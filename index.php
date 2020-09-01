<!DOCTYPE html>
<html lang="en">
<head>
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Slab&display=swap" rel="stylesheet"> 
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="style.css">
    <title>Document</title>
</head>
<body>
    <header>
       <div id="logowanie"> 
        <ol>
          <ul>logowanie
            <li>login:</br><input type="text" size="15"></li>
            <li>password:</br><input type="password" size="15"></li>
            <li><button type="submit">loguj</button></li>
          </ul>
          <ul>rejestracja
            <li>login:</br><input type="text" size="15"></li>
            <li>password:</br><input type="password" size="15"></li>
            <li>password:</br><input type="password" size="15"></li>
            <li><button type="submit">rejestruj</button></li>
          </ul>
        </ol>
      </div>
      <div id="menu">
          <ol>
            <li><a href="#logowanie">Start</a></li>
            <li><a href="#bestsellery">Bestsellery</a></li>
            <li>Nasze książki</li>
            <li>Kontakt</li>
          </ol>
      </div>
      <div id="media">
        <ul>
          <a href="https://web.facebook.com/" target="_blank"><li><i class="fab fa-facebook-f"></i></li></a>
          <a href="https://twitter.com/?lang=pl" target="_blank"><li><i class="fab fa-twitter"></i></li></a>
          <a href="https://www.instagram.com/" target="_blank"><li><i class="fab fa-instagram"></i></li></a>
          </ul>
      </div>
    </header>
    <div class="obraz">
      
    </div>
    <div class="opis">
      
      <div class="box1">
        <div class="w3-content w3-display-container">
          <img class="mySlides" src="books.jpg">
          <img class="mySlides" src="header.jpg">
          <img class="mySlides" src="kwiat.jpg">
          <img class="mySlides" src="droga.jpg">

          <button class="button" onclick="plusDivs(-1)">&#10094;</button>
          <button class="button" onclick="plusDivs(1)">&#10095;</button>
        </div>
      </div>
      
      <div class="box2">
        <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ultricies dui sapien, quis ullamcorper sem sollicitudin quis. Aliquam erat volutpat. Vivamus placerat est vitae congue auctor. Maecenas eros velit, vulputate eu congue varius, ultrices ut purus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Mauris lectus lorem, porttitor vitae purus in, efficitur rutrum purus. Morbi gravida dui ligula, vitae facilisis risus consequat non. Aenean mauris magna, porttitor non rutrum in, accumsan non ex. In nec odio pulvinar, sagittis ligula ac, pellentesque libero. Nulla nulla nibh, imperdiet non lorem id, bibendum luctus orci.

        Etiam faucibus est sed libero tincidunt pellentesque. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nunc posuere turpis quam, at vehicula risus varius eu. Sed ultrices ut purus ac pharetra. Cras congue commodo risus ac sodales. Suspendisse elementum ante metus, rutrum lobortis arcu interdum id. Interdum et malesuada fames ac ante ipsum primis in faucibus.
        Etiam faucibus est sed libero tincidunt pellentesque. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nunc posuere turpis quam, at vehicula risus varius eu. Sed ultrices ut purus ac pharetra. Cras congue commodo risus ac sodales.


        </p>
      </div> 
    
    </div>
    <div id="bestsellery">
      <div class="one">
        <div class="overlay">
          <div class="text">Hello World</div>
        </div>
      </div>
      <div class="two">
      <div class="overlay">
    <div class="text">Hello World</div>
  </div>
      </div>
      <div class="three">
      <div class="overlay">
    <div class="text">Hello World</div>
  </div>
      </div>
      <div class="four">
      <div class="overlay">
    <div class="text">Hello World</div>
  </div>
      </div>
      <div class="five">
      <div class="overlay">
    <div class="text">Hello World</div>
  </div>
      </div>
    </div>

    <div id="books">
      <p>kappa</p>
    
    </div>
</body>
</html>
<script>
var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
  showDivs(slideIndex += n);
}

function showDivs(n) {
  var i;
  var x = document.getElementsByClassName("mySlides");
  if (n > x.length) {slideIndex = 1}
  if (n < 1) {slideIndex = x.length}
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
  x[slideIndex-1].style.display = "block";  
}
function myFunction(id) {
  var x = document.getElementById(id);
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
  } else { 
    x.className = x.className.replace(" w3-show", "");
  }
}
</script>