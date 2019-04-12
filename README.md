
#Dependencies

It should be run on server that executes python2 files
The server needs to be installed with two modules: 
                  module math - for square root function 
                  module requests - to handle the http requests to GET data through API
                  
To run the script, execute the command 'Python myAirport.py'


#Inputs

The script asks for 
    user's Latitude,
    Latitude range user is searching in (+ and -),
    user's Longitute, 
    Longitude range user is searching in (+ and -) 
    
For example if the user is at latitude = 5 and searching for range between 0 to 10: 
    User inputs latitude >> 5
    Latitude range (+/-) >> 5
                          range = (5 - 5) = 0 and (5 + 5)= 10
    
The Script only takes Floating numbers as input. If any other data type is entered, it keeps promting to enter a float value until a decimal or interger is entered. To exit, hit CTRL+C.


#Output

When entered the right data-type values, the script outputs the number of airports available in the given range.
It returns 25 airports (fetched from API).
These Airports are then arranged in ascending order of the distances from the User's co-ordinates.
          The distance is calculated as the distance between two points in geometry.


#Note

1) Some test inputs returned aiports with same name and same geo-lation cordinates. Even though, logically, 
the script should output unique set of airports, I left it as it is since the assignment didnt ask for it.

2) The radius is decided on the range of latitude and logitude input by the user as:
      The API's parameters are defined by range
      The latitudes and longitudes form gird not circle
