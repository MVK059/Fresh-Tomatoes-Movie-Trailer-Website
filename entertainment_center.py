""" Movie details to be displayed on the website """
import media, fresh_tomatoes

# Create movie objects with title, storyline, director, image poster url, youtube video url.
mudbound = media.Movie("Mudbound", 
                    "Two men return home from World War II to work on a farm where they struggle to adjust to life after war", 
                    "Dee Rees",
                    "https://goo.gl/eVib3Z", 
                    "https://www.youtube.com/watch?v=vAZWhFI9lLQ")

okja = media.Movie("Okja",
                    "A young girl risks everything to prevent a multinational company from kidnapping her best friend",
                    "Bong Joon-ho",
                    "https://goo.gl/tZV55c",
                    "https://www.youtube.com/watch?v=AjCebKn4iic")


beasts = media.Movie("Beasts of No Nation", 
                    "A drama based on the experiences of a child soldier fighting in the civil war of an African country", 
                    "Cary Fukunaga",
                    "https://goo.gl/h9gZef",
                    "https://www.youtube.com/watch?v=2xb9Ty-1frw")

geralds_game = media.Movie("Gerald's Game", 
                        "While trying to spice up their marriage, Jessie must fight to survive when her husband dies unexpectedly", 
                        "Mike Flanagan",
                        "https://goo.gl/KxL8Em", 
                        "https://www.youtube.com/watch?v=twbGU2CqqQU")

mute = media.Movie("Mute", 
                    "A mute bartender goes up against his city's gangsters to find out what happened to his missing partner.",
                    "Duncan Jones",
                    "https://goo.gl/8gSGyh",
                    "https://www.youtube.com/watch?v=ma8te7ywEio")

thirteenth = media.Movie("13th", 
                        "An in-depth look at the prison system in the United States and how it reveals the history of racial inequality.",
                        "Ava DuVernay",
                        "https://goo.gl/pNSN5A",
                        "https://www.youtube.com/watch?v=V66F3WU2CKk")

# create a list of movie objects
movies = [mudbound, okja, beasts, geralds_game, mute, thirteenth]

# Create the webpage with the data inside movies list 
fresh_tomatoes.open_movies_page(movies)