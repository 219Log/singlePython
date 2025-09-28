from urllib import request, error
from bs4 import BeautifulSoup

def fetch_bytes(url: str) -> tuple[bytes, str, str] | tuple[None, None, None]:
    """Fetches the URL with headers. Returns (data, final_url, content_type)."""
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/rss+xml, application/xml;q=0.9, text/xml;q=0.8, */*;q=0.1",
    }
    req = request.Request(url, headers=headers)
    try:
        with request.urlopen(req, timeout=10) as resp:
            data = resp.read()
            final_url = resp.geturl()
            content_type = resp.headers.get("Content-Type", "")
            return data, final_url, content_type
    except Exception:
        return None, None, None


candidate_urls = [
    "https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108",
    "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108",
    # * Try new primary domain if migrated
    "https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108",
    "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108",
]

data = final_url = content_type = None
for u in candidate_urls:
    data, final_url, content_type = fetch_bytes(u)
    if not data:
        continue
    text = data.decode("utf-8", "ignore")
    if "<rss" in text or "<channel" in text:
        # * Likely RSS/XML
        soup = BeautifulSoup(data, "xml")
        locations = soup.select("location")
        if locations:
            for location in locations:
                print("도시:", location.select_one("city").string)
                print("날씨:", location.select_one("wf").string)
                print("최저기온:", location.select_one("tmn").string)
                print("최고기온:", location.select_one("tmx").string)
                print()
            break
    # * Not RSS or no locations; try next candidate
else:
    # * All candidates failed or returned non-RSS HTML; try to discover an RSS link in HTML
    if data:
        text = data.decode("utf-8", "ignore")
        soup_html = BeautifulSoup(text, "html.parser")
        rss_link = None
        for a in soup_html.select("a[href]"):
            href = a.get("href", "")
            if not href:
                continue
            lower = href.lower()
            if "rss" in lower or "mid-term-rss" in lower or "rss3.jsp" in lower:
                rss_link = href
                break

        if rss_link:
            from urllib.parse import urljoin

            rss_url = urljoin(final_url or "", rss_link)
            rss_bytes, rss_final, rss_ct = fetch_bytes(rss_url)
            if rss_bytes and (b"<rss" in rss_bytes or b"<channel" in rss_bytes):
                soup = BeautifulSoup(rss_bytes, "xml")
                locations = soup.select("location")
                if locations:
                    for location in locations:
                        print("도시:", location.select_one("city").string)
                        print("날씨:", location.select_one("wf").string)
                        print("최저기온:", location.select_one("tmn").string)
                        print("최고기온:", location.select_one("tmx").string)
                        print()
                else:
                    print("RSS를 찾았으나 location 태그가 없습니다. URL:", rss_final or rss_url)
            else:
                print("HTML에서 RSS 링크를 발견했으나 유효한 RSS가 아닙니다. 링크:", rss_url)
        else:
            print("location 태그를 찾지 못했습니다. 페이지 구조가 변경되었을 수 있습니다.")
            print("최종 URL:", final_url)
            print("Content-Type:", content_type)
            print("응답 앞부분:")
            print(text[:300])
    else:
        print("요청이 모두 실패했습니다. 네트워크 또는 서버 접근 문제가 있을 수 있습니다.")