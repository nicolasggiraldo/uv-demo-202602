import requests

def main():
    response = requests.get("https://api.github.com")
    print(response.status_code)
    print(response.content)

if __name__ == "__main__":
    main()
