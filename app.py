from langchain_google_genai import ChatGoogleGenerativeAI
# import tools
from langchain_core.tools import tool


print("installation successful")
def add(a, b):
    return a + b

def divide(a, b):
    return a / b

@tool
def get_weather(city: str) -> str:
    """Get the weather of a city"""
    return f"The weather of {city} is sunny"
output = get_weather.invoke("New York")
print(output)

 