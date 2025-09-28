from flask import Flask
from bs4 import BeautifulSoup
from urllib import request

app = Flask(__name__)

@app.route("/")
def hello():
    # * Fetches the RSS with headers and timeout
    try:
        req = request.Request(
            "https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108",
            headers={"User-Agent": "Mozilla/5.0"},
        )
        with request.urlopen(req, timeout=10) as resp:
            data = resp.read()
    except Exception as fetch_error:
        return f"<p>데이터 요청 실패: {fetch_error}</p>", 502

    # * Try XML parser first; fallback to HTML if needed
    soup = None
    try:
        soup = BeautifulSoup(data, "xml")
        locations = soup.select("location")
        if not locations:
            raise ValueError("No location in XML")
    except Exception:
        soup = BeautifulSoup(data, "html.parser")
        locations = soup.select("location")

    if not locations:
        return "<p>예상한 데이터 구조(location)가 없습니다.</p>", 502

    # * Safely extract fields
    parts = []
    for location in locations:
        city = location.select_one("city")
        wf = location.select_one("wf")
        tmn = location.select_one("tmn")
        tmx = location.select_one("tmx")

        city_text = city.string if city and city.string else "-"
        wf_text = wf.string if wf and wf.string else "-"
        tmn_text = tmn.string if tmn and tmn.string else "-"
        tmx_text = tmx.string if tmx and tmx.string else "-"

        parts.append(
            "".join([
                f"<h3>{city_text}</h3>",
                f"<p>날씨: {wf_text}</p>",
                f"<p>최저/최고 기온: {tmn_text}/{tmx_text}</p>",
                "<hr />",
            ])
        )

    return "".join(parts)

if __name__ == "__main__":
    app.run(debug=True)