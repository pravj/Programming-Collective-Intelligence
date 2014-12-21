K-mean Clustering
=================

> This assignment apply the `K-mean clustering algorithm` on population density data parameters of different countries.

### Description
This assignment uses the `K-mean clustering algorithm` on provided [dataset](#dataset). Here the value of `k` is 3, which separate available countries into 3 different groups(clusters) according to their position in area and population plane. 

### Dataset
Assignment uses `json` form data, containing object for each country having `country code`, `country name`, `population` and `area` as the parameters. 
Data used in the assignment is scraped from its source. You can check the data file [here](https://github.com/pravj/Programming-Collective-Intelligence/blob/master/Exercise/Discovering%20Groups/Clustering/k-mean/dataset.json).

Dataset don't have all the countries listed on the [source page](http://www.geonames.org/countries/) because it excludes any country with blank parameter value.
> source : [GeoNames](http://www.geonames.org/)

> Code for scraping the data is not provided, because I did this in the native Python console.

### Ingredients & Recipe
* clustering.py
  * contains classes `Cluster` and `KMean`, which helps implementing the `K-mean clustering algorithm`.
* dataset.json
  * dataset file containg data for each country.
* main.py
  * main file, which import required modules and make them work accordingly.
* plotter.py
  * contains class `Plotter` which helps drawing resultant by provided data image using `matplotlib` library.

> `$ python main.py` will process and return results.

> Only external library needed is `matplotlib`.

### Result
This is the resultant clusters image. Running `main.py` should result a similar image.
![Cluster-Image](https://raw.githubusercontent.com/pravj/Programming-Collective-Intelligence/master/Exercise/Discovering%20Groups/Clustering/k-mean/clusters.png?token=ADRywtTSXEpE-aLlJdOLYHromY04clCsks5Unj4twA%3D%3D)

* Cluster-I
  * China
  * India
* Cluster-II
  * Antarctica
  * Australia
  * Brazil
  * Canada
  * Russia
  * United States
* Cluster-III
  * Andorra
  * United Arab Emirates
  * Afghanistan
  * Antigua and Barbuda
  * Anguilla
  * Albania
  * Armenia
  * Angola
  * Argentina
  * American Samoa
  * Austria
  * Aruba
  * Azerbaijan
  * Bosnia and Herzegovina
  * Barbados
  * Bangladesh
  * Belgium
  * Burkina Faso
  * Bulgaria
  * Bahrain
  * Burundi
  * Benin
  * Saint Barthélemy
  * Bermuda
  * Brunei
  * Bolivia
  * Bahamas
  * Bhutan
  * Botswana
  * Belarus
  * Belize
  * Cocos [Keeling] Islands
  * Democratic Republic of the Congo
  * Central African Republic
  * Republic of the Congo
  * Switzerland
  * Ivory Coast
  * Cook Islands
  * Chile
  * Cameroon
  * Colombia
  * Costa Rica
  * Cuba
  * Cape Verde
  * Christmas Island
  * Cyprus
  * Czech Republic
  * Germany
  * Djibouti
  * Denmark
  * Dominica
  * Dominican Republic
  * Algeria
  * Ecuador
  * Estonia
  * Egypt
  * Western Sahara
  * Eritrea
  * Spain
  * Ethiopia
  * Finland
  * Fiji
  * Falkland Islands
  * Micronesia
  * Faroe Islands
  * France
  * Gabon
  * United Kingdom
  * Grenada
  * Georgia
  * French Guiana
  * Guernsey
  * Ghana
  * Gibraltar
  * Greenland
  * Gambia
  * Guinea
  * Guadeloupe
  * Equatorial Guinea
  * Greece
  * South Georgia and the South Sandwich Islands
  * Guatemala
  * Guam
  * Guinea-Bissau
  * Guyana
  * Hong Kong
  * Heard Island and McDonald Islands
  * Honduras
  * Croatia
  * Haiti
  * Hungary
  * Indonesia
  * Ireland
  * Israel
  * Isle of Man
  * British Indian Ocean Territory
  * Iraq
  * Iran
  * Iceland
  * Italy
  * Jersey
  * Jamaica
  * Jordan
  * Japan
  * Kenya
  * Kyrgyzstan
  * Cambodia
  * Kiribati
  * Comoros
  * Saint Kitts and Nevis
  * North Korea
  * South Korea
  * Kuwait
  * Cayman Islands
  * Kazakhstan
  * Laos
  * Lebanon
  * Saint Lucia
  * Liechtenstein
  * Sri Lanka
  * Liberia
  * Lesotho
  * Lithuania
  * Luxembourg
  * Latvia
  * Libya
  * Morocco
  * Monaco
  * Moldova
  * Montenegro
  * Saint Martin
  * Madagascar
  * Marshall Islands
  * Macedonia
  * Mali
  * Myanmar [Burma]
  * Mongolia
  * Macao
  * Northern Mariana Islands
  * Martinique
  * Mauritania
  * Montserrat
  * Malta
  * Mauritius
  * Maldives
  * Malawi
  * Mexico
  * Malaysia
  * Mozambique
  * Namibia
  * New Caledonia
  * Niger
  * Norfolk Island
  * Nigeria
  * Nicaragua
  * Netherlands
  * Norway
  * Nepal
  * Nauru
  * Niue
  * New Zealand
  * Oman
  * Panama
  * Peru
  * French Polynesia
  * Papua New Guinea
  * Philippines
  * Pakistan
  * Poland
  * Saint Pierre and Miquelon
  * Pitcairn Islands
  * Puerto Rico
  * Palestine
  * Portugal
  * Palau
  * Paraguay
  * Qatar
  * Réunion
  * Romania
  * Serbia
  * Rwanda
  * Saudi Arabia
  * Solomon Islands
  * Seychelles
  * Sudan
  * Sweden
  * Singapore
  * Saint Helena
  * Slovenia
  * Svalbard and Jan Mayen
  * Slovakia
  * Sierra Leone
  * San Marino
  * Senegal
  * Somalia
  * Suriname
  * South Sudan
  * São Tomé and Príncipe
  * El Salvador
  * Syria
  * Swaziland
  * Turks and Caicos Islands
  * Chad
  * French Southern Territories
  * Togo
  * Thailand
  * Tajikistan
  * Tokelau
  * East Timor
  * Turkmenistan
  * Tunisia
  * Tonga
  * Turkey
  * Trinidad and Tobago
  * Tuvalu
  * Taiwan
  * Tanzania
  * Ukraine
  * Uganda
  * Uruguay
  * Uzbekistan
  * Vatican City
  * Saint Vincent and the Grenadines
  * Venezuela
  * British Virgin Islands
  * U.S. Virgin Islands
  * Vietnam
  * Vanuatu
  * Wallis and Futuna
  * Samoa
  * Yemen
  * Mayotte
  * South Africa
  * Zambia
  * Zimbabwe
