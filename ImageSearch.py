# Importing modules
import urllib.request
from bs4 import BeautifulSoup

# Required base url for image search
googleImageSearchBaseUrl = "https://www.google.com/search?hl=EN&tbm=isch&q="
searchEngineBaseUrl = googleImageSearchBaseUrl

# Save the image in the file
def SaveImage(url, filename):
    # Open the file the user want the image data to be saved
    imagefile = open(filename + ".jpeg", "wb")
    # Write the image data in the file
    imagefile.write(urllib.request.urlopen(url).read())
    # Close the file
    imagefile.close()

# Fetch the image Url
def FetchImageUrl(url, query):
    # Fetch url
    thepage = urllib.request.urlopen(url)
    # Pull data of the page
    soupdata = BeautifulSoup(thepage, "html.parser")

    # Iterate over all images in the page
    for img in soupdata.findAll('img'):
        # If they are equal to the keyword
        if query in img.get('alt'):
            # Return it's url
            temp = img.get('src')
            return temp

# Get the keyword to be searched by the user
query = input("Enter keyword to be searched: ")

# Generating required url
url = searchEngineBaseUrl + query.replace(" ", "+")

# Fetching the Image
imageUrl = FetchImageUrl(url, query)

# Saving the Image
SaveImage(imageUrl, "ant")