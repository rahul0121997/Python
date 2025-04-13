import requests  # This script fetches a random Chuck Norris joke from an API and prints it to the console.
import json # This script fetches a random Chuck Norris joke from an API and prints it to the console.
# It handles potential errors such as network issues or JSON parsing errors.

def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        data = response.json()
        joke = data.get('value')
        
        if joke:
            print("Here's a joke for you:")
            print(joke)
        else:
            print("Oops! The joke is missing in the response.")
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching joke: {e}")
    except ValueError:
        print("Error parsing JSON response")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    get_chuck_norris_joke()