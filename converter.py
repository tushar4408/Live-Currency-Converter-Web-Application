import requests
import pycountry

BASE_URL = "https://open.er-api.com/v6/latest/"

def convert(amount: float, from_cur: str, to_cur: str) -> float:
    url = BASE_URL + from_cur

    try:
        response = requests.get(url, timeout=8)
        response.raise_for_status()
        data = response.json()

    except requests.exceptions.Timeout:
        raise RuntimeError("Request timed out. Please try again.")
    except requests.exceptions.ConnectionError:
        raise RuntimeError("Network error. Check your internet connection.")
    except requests.exceptions.HTTPError:
        raise RuntimeError("API service error.")
    except requests.exceptions.RequestException:
        raise RuntimeError("Unexpected error while connecting to currency service.")

    if data.get("result") != "success":
        raise RuntimeError("Currency API returned an error.")

    rate = data.get("rates", {}).get(to_cur)

    if rate is None:
        raise ValueError(f"Unsupported currency code: {to_cur}")

    return round(amount * rate, 2)


def get_supported_currencies():
    try:
        response = requests.get(BASE_URL + "USD", timeout=8)
        response.raise_for_status()
        data = response.json()

        if data.get("result") != "success":
            return []

        return sorted(data.get("rates", {}).keys())

    except Exception:
        return []


def get_currency_name(code):
    """
    Return full currency name from ISO code using pycountry.
    """
    try:
        currency = pycountry.currencies.get(alpha_3=code)
        return currency.name if currency else code
    except:
        return code
