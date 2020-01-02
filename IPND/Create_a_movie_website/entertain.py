import media
import fresh_tomatoes
#Creating instance for individual movies and series
kaala = media.Movie("Kaala",
                    "http://t3.gstatic.com/images?q=tbn:ANd9GcToH2_QC0mp0PLOW-dEEyXd9DkF8woFmkb1a4bSePveYn5PYAUX",
                    "https://www.youtube.com/watch?v=mMCEvr3VWqQ",
                    "152 mins")

mersal = media.Movie("Mersal",
                    "https://st1.bollywoodlife.com/wp-content/uploads/2017/06/DC3XFWIVYAAeF_6.jpg",
                    "https://www.youtube.com/watch?v=ifmBVkQH5AM",
                    "172 mins")

tamil_padam = media.Movie("Tamilzh Padam 2",
                            "http://t1.gstatic.com/images?q=tbn:ANd9GcQ-1ywvuO113C_zoTmH4GEGtZjFaV4BSIieQrilxcWz21kfSPAO",
                            "https://www.youtube.com/watch?v=vFWlCsjWFMw",
                            "155 mins")

mi4 = media.Movie("MI: Ghost Protocal",
                    "http://t3.gstatic.com/images?q=tbn:ANd9GcS09yEMdQ7R-Bb60EAWZeGICXMkteXzI2kxLGseaQhSKZ6AOJ6q",
                    "https://www.youtube.com/watch?v=hR-0po0hzDQ",
                    "147 mins")

intersteller = media.Movie("Intersteller",
                    "http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mker2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB",
                    "https://www.youtube.com/watch?v=egkvnEYewMs",
                    "169 mins")

ff8 = media.Movie("The Fate of the Furious",
                        "http://t1.gstatic.com/images?q=tbn:ANd9GcQh2MCGCzxmCq4ei68-i6ELtRB18nFS4iHKBnHxffrLHkouoN-4",
                        "https://www.youtube.com/watch?v=uisBaTkQAEs",
                        "138 mins")

atypical = media.Series("Lost in Space",
                        "https://upload.wikimedia.org/wikipedia/en/f/ff/Lost_in_Space_2018_series_Logo.jpg",
                        "https://www.youtube.com/watch?v=fzmM0AB60QQ",
                        "10 episodes")

altered_carbon = media.Series("Altered Carbon",
                        "https://upload.wikimedia.org/wikipedia/en/a/a0/Altered_Carbon_title.jpg",
                        "https://www.youtube.com/watch?v=dhFM8akm9a4",
                        "10 episodes")

b_the_begining = media.Series("B The Beginning",
                        "https://upload.wikimedia.org/wikipedia/en/4/42/B_the_Beginning_Main_Visual.jpg",
                        "https://www.youtube.com/watch?v=ReXY28B7FgQ",
                        "12 episodes")


movies = [kaala, mersal, tamil_padam, mi4, intersteller, ff8]
series = [atypical, altered_carbon, b_the_begining]
#Both movies and series sent as argument to create HTML code
fresh_tomatoes.open_movies_page(movies, series)
