from app import app, celsius_to_fahrenheit
def test_celsius_to_fahrenheit_logic():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212

def test_api_endpoints():
    client = app.test_client()
    res_home = client.get("/")
    assert res_home.status_code == 200
    res_conv = client.get("/convert/c2f?celsius=0")
    assert res_conv.status_code == 200
    assert res_conv.json["fahrenheit"] == 32
