import requests
import folium

# Function to get geolocation based on the user's IP
def get_geolocation():
    try:
        # Fetching the geolocation using ipinfo.io API
        response = requests.get('https://ipinfo.io/3.165.198.15/json?token=880e7a29236aed')
        data = response.json()
        
        # Extracting location details
        location = data['loc'].split(',')
        latitude = float(location[0])                     
        longitude = float(location[1])
        city = data.get('city', 'N/A')
        region = data.get('region', 'N/A')
        country = data.get('country', 'N/A')
        
        print(f"Location: {city}, {region}, {country}")
        print(f"Latitude: {latitude}, Longitude: {longitude}")
        
        return latitude, longitude, city, region, country
    except Exception as e:
        print(f"Error fetching geolocation: {e}")
        return None, None, None, None, None

# Function to display the location on a map
def display_map(lat, lon, city, region, country):
    if lat is None or lon is None:
        print("Unable to fetch geolocation.")
        return
    
    # Create a map centered around the user's location
    user_map = folium.Map(location=[lat, lon], zoom_start=12)
    
    # Add a marker for the user's location
    folium.Marker(
        [lat, lon], 
        popup=f"{city}, {region}, {country}",
        tooltip="Your Location"
    ).add_to(user_map)
    
    # Save the map to an HTML file and open it
    user_map.save("user_location_map.html")
    print("Map has been saved as user_location_map.html")

# Main function
if __name__ == "__main__":
    latitude, longitude, city, region, country = get_geolocation()
    display_map(latitude, longitude, city, region, country)
