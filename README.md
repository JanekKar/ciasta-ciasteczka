# Ciasta Ciasteczka
Repository for development of web page for Ciasta, Ciasteczka company

# Pages

## index.html
* [x] responsive navbar
* [x] responsive footer

### Home
 * [x] Slide show
   * [x] Indicators
   * [x] Automatic slideshow
   * [x] Arrows for next and previous
 * [ ] Slogan
 * [ ] Some vague information about company
  
### About Us
 * [ ] Info about company
 * [ ] Pictures of kitchen??

### Contact
 * [x] Phone
 * [ ] Facebook link (or page plugin [link](https://developers.facebook.com/docs/plugins/page*plugin/))
 * [ ] Instagram Link
 * [x] Google map with location pined ([link](https://support.google.com/maps/answer/144361?co=GENIE.Platform%3DDesktop&hl=en))
 * [x] Address


## menu.html
* [ ] Grid with products
* [ ] Filters


## how-to-order.html
* [ ] Step by step instruction

## Product Page
* [ ] Same category items ❓️
* [ ] Slideshow
* [ ] Product name
* [ ] Description
* [ ] Prices based on sizes


## Html Templates 
* base-template
  * Top bar
  * Footer
* product-template
  * name
  * base price
  * category


# Objects

Product:
- ID
- Name
- Description
- Price
- Type
- Category
- Ingredients
- Allergens
- Photos
- Hidden



Size: - torty
- Product_ID
- Weight
- Amount of people
- Diameter

Type
  Tort - 4 rozmiary - (torty) zł/szt
  Ciasta - 3 Rozmiary - (ciasta) zł/szt
  Monoporcja - po 6 szt. lub 12 szt. (babeczki) zł/6szt

Category:
- Parent [Torty, Ciasta, Inne Słotkości]
- Name
- Description

Jeden tort może mieć wiecje niż jedną kategorię❗️❗️


Disclaimer:
- Waga tortu może się różnić, wygląd możę się różńić
- Alergeny
- Skład



Jak zamawiać


Rozmiary:
6szt, 12szt
Mały tort, Średni, Średni-większy, Duży

Średnia == Ilością osób (jest równoznaczna)



Models:
* [ ] product
* [ ] type
* [ ] category
* [ ] size
* [ ] product_photo

