const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');


    const subMenu = document.querySelector('.sub-menu-1');
    const categoryContainers = document.querySelectorAll('.category-container');

    burger.addEventListener('click', ()=> {
        nav.classList.toggle('nav-active');
        // Burger Animation 
        burger.classList.toggle('toggle');

        // If media query matches
        subMenu.classList.toggle('collapsible');
        categoryContainers.forEach( element => {
            element.classList.toggle('collapsible')
        });
    });
}

// not working
const currentSection = () => {
    let mainNavLinks = document.querySelectorAll('nav ul li a');
    console.log(mainNavLinks)

    window.addEventListener('scroll', event => {
        let fromTop = window.screenY;

        mainNavLinks.forEach(link => {
            let section = document.querySelector(link.hash);

            if(
                section.offsetTop <= fromTop && 
                section.offsetTop + section.offsetHeight > fromTop
            ){
                link.classList.add('current')
            }else{
                link.classList.remove('current');
            }

        });

    });

}


var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}


navSlide();