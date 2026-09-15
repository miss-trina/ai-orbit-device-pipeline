from urllib.parse import urlparse

class DataCleaner:
    """Normalizes URLs, derives official logos, and deduplicates records."""

    @staticmethod
    def clean_url(url: str) -> str:
        if not url:
            return ""
        url = url.strip()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url
        parsed = urlparse(url)
        return f"{parsed.scheme}://{parsed.netloc}{parsed.path}".rstrip("/")

    @staticmethod
    def get_clearbit_logo(domain: str) -> str:
        """Derives verified official logo link using Clearbit standard."""
        if not domain:
            return ""
        domain = domain.replace("https://", "").replace("http://", "").split("/")[0]
        return f"https://logo.clearbit.com/{domain}"

    def deduplicate(self, records: list) -> list:
        seen = set()
        unique_records = []
        for r in records:
            key = r.get("Device Name", "").strip().lower()
            if key and key not in seen:
                seen.add(key)
                unique_records.append(r)
        return unique_records
