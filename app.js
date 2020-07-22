// Open navigation slide
const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const subMenu = document.querySelector('.sub-menu');
    //const categoryContainers = document.querySelectorAll('.category-container');

    burger.addEventListener('click', () => {
        nav.classList.toggle('nav-active');
        // Burger Animation 
        burger.classList.toggle('toggle');
        subMenu.classList.remove('sub-menu-active');

        // // If media query matches
        // subMenu.classList.toggle('collapsible');
        // categoryContainers.forEach( element => {
        //     element.classList.toggle('collapsible')
        // });
    });

}

// open submenu in desktop view
const openMenu = () => {
    if (!is_touch_device()) {
        const subMenu = document.querySelector('.sub-menu');
        subMenu.classList.add('active');
    }
}

// close submenu in desktop view
const closeMenu = () => {
    if (!is_touch_device()) {
        const subMenu = document.querySelector('.sub-menu');
        subMenu.classList.remove('active');
    }
}

//close navigation slide
const closeNav = () => {

    const nav = document.querySelector('.nav-links');
    const subMenu = document.querySelector('.sub-menu');
    const burger = document.querySelector('.burger');

    subMenu.classList.remove('menu-active');
    nav.classList.remove('nav-active');
    burger.classList.toggle('toggle');
}


// toggle submenu in mobile view 
const subMenu = () => {
    if (is_touch_device()) {
        const subMenuToggle = document.querySelector('.sub-menu-toggle');
        const subMenu = subMenuToggle.querySelector('.sub-menu-toggle .sub-menu');

        subMenuToggle.addEventListener('click', () => {
            subMenu.classList.toggle('sub-menu-active');
        })
    }
}

// not working
const currentSection = () => {
    let mainNavLinks = document.querySelectorAll('nav ul li a');
    console.log(mainNavLinks)

    window.addEventListener('scroll', event => {
        let fromTop = window.screenY;

        mainNavLinks.forEach(link => {
            let section = document.querySelector(link.hash);

            if (
                section.offsetTop <= fromTop &&
                section.offsetTop + section.offsetHeight > fromTop
            ) {
                link.classList.add('current')
            } else {
                link.classList.remove('current');
            }

        });

    });

}

function set_sticky() {

    const nav = document.querySelector('nav');

    if (!is_touch_device()) {
        nav.classList.add('sticky');
    } else {
        nav.classList.remove('sticky');
    }
}

// check is media query matches mobile or desktop dimensions
function is_touch_device() {

    if ((window.matchMedia("(max-width: 768px)")).matches) {
        return true
    } else {
        var prefixes = ' -webkit- -moz- -o- -ms- '.split(' ');

        var mq = function (query) {
            return window.matchMedia(query).matches;
        }

        if (('ontouchstart' in window) || window.DocumentTouch && document instanceof DocumentTouch) {
            return true;
        }

        // include the 'heartz' as a way to have a non matching MQ to help terminate the join
        // https://git.io/vznFH
        var query = ['(', prefixes.join('touch-enabled),('), 'heartz', ')'].join('');
        return mq(query);

    }
}


set_sticky();
subMenu();
navSlide();


function showSlides(n){
    var i;
    var slides = document.getElementsByClassName("slide");
    var dots = document.getElementsByClassName("dot");
    if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active-dot", "");
    }
    slides[slideIndex-1].style.display = "block";
    dots[slideIndex-1].className += " active-dot";
  }


  window.addEventListener("load",function() {
    showSlides(slideIndex);
    myTimer = setInterval(function(){plusSlides(1)}, 4000);
})


function currentSlide(n){
    clearInterval(myTimer);
    myTimer = setInterval(function(){plusSlides(n + 1)}, 4000);
    showSlides(slideIndex = n);
  }


function plusSlides(n){
    clearInterval(myTimer);
    if (n < 0){
      showSlides(slideIndex -= 1);
    } else {
     showSlides(slideIndex += 1); 
    }
    if (n === -1){
      myTimer = setInterval(function(){plusSlides(n + 2)}, 4000);
    } else {
      myTimer = setInterval(function(){plusSlides(n + 1)}, 4000);
    }
  }

var slideIndex = 0;
// carousel();