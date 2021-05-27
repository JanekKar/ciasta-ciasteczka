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
 * [x] Slogan
 * [x] Some vague information about company
  
### About Us
 * [x] Info about company
 * [ ] Pictures of kitchen??

### Contact
 * [x] Phone
 * [x] Facebook link (or page plugin [link](https://developers.facebook.com/docs/plugins/page*plugin/))
 * [x] Instagram Link
 * [x] Google map with location pined ([link](https://support.google.com/maps/answer/144361?co=GENIE.Platform%3DDesktop&hl=en))
 * [x] Address


## menu.html
* [x] Grid with products
* [ ] Filters


## how-to-order.html
* [x] Step by step instruction

## Product Page
* [x] Same category items ❓️
* [x] Slideshow
* [x] Product name
* [x] Description
* [x] Prices based on sizes


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
- Parent [Torty, Ciasta, Inne Słodkości]
- Name
- Description

Jeden tort może mieć więcej niż jedną kategorię❗️❗️


Disclaimer:
- Waga tortu może się różnić, wygląd może się różnić
- Alergeny
- Skład



Jak zamawiać


Rozmiary:
6szt, 12szt
Mały tort, Średni, Średni-większy, Duży

Średnica == Ilością osób (jest równoznaczna)



Models:
* [x] product
* [x] type
* [x] category
* [x] size
* [x] product_photo

