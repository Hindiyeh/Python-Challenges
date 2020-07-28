#Product Inventory Project - Create an application 
# which manages an inventory of products. Create a 
# product class which has a price, id, and quantity 
# on hand. Then create an inventory class which keeps
#  track of various products and can sum up the inventory
#  value.

#attributes
# ID (automatically), Size (w,h, d=0) , Year of Make (xxxx)
# Name of Painting (=No Title) , Medium (one of finite attributes)
# Location () - Sub-Location (), Price ($...)
# prints edition (texts) , Notes (txt = '')
# automatically filled genre, colour
# Name of Artist, DOB - DOD , Country of Origin, Description ('txt')
# if Artist is Alive
class Artist():
    def __init__(self, artist_id, date_of_birth,
    date_of_death, country_of_origin, description):
        self.artist_id = artist_id
        self.date_of_birth = date_of_birth
        self.date_of_death = date_of_birth
        self.country_of_origin = country_of_origin
        self.description = description
    
    def artist_alive(self):
        if self.date_of_death is '':
            return 'Alive'
        else:
            return 'Passed Away in' + str(self.date_of_death)


class Artwork(Artist):
    inventory = 0
    
    def __init__(self, artwork_id, width, height, depth,
    year_of_make, name_of_painting, medium,
    location, sub_location, price,
    prints_edition , notes, artist_id
    , date_of_birth, date_of_death, 
    country_of_origin, description):
        super().__init__(artist_id, date_of_birth, 
        date_of_death, country_of_origin, description)
        self.artwork_id = artwork_id
        self.width = width
        self.height = height
        self.depth = depth
        self.size = (self.width , self.height, self.depth) 
        self.depth = depth
        self.year_of_make = year_of_make
        self.name_of_painting = name_of_painting
        self.medium = medium
        self.location = location
        self.sub_location = sub_location
        self.price = price
        self.prints_edition = prints_edition
        self.notes = notes
        Artwork.inventory += 1

    def print_size(self):
        if self.size == 0: 
            print(f'{self.size[0]} cm and {self.size[1]} cm')
        else:
            print(f'{self.size[0]} cm and {self.size[1]} cm and {self.size[2]}')

y = Artwork(1,10,20,30,1999,'bitch ass nigger', 'Acrylic on Canvas', 'Museum', 'second floor', 200, '' , 'nothing to right', 11, 1970, 2000, 'Amman', 'nothing' )
y.print_size()
print(Artwork.inventory)