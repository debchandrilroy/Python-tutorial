import requests

print("\t\tWelcome to the Weather Forecaster!\n\n")
city_name = input("Enter the name of the City: ")

def Gen_report(city):
    url = f"https://wttr.in/{city}"
    try:
        data = requests.get(url)
        report = data.text
    except:
        report = "Error Occurred"
    print(report)

Gen_report(city_name)
