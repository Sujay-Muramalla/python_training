import dns.resolver
import re

def get_spf_records(domain, visited=None):
    """
    Recursively resolve SPF records for a domain.
    Extract ip4, ip6, and include mechanisms.
    """
    if visited is None:
        visited = set()

    if domain in visited:
        return []

    visited.add(domain)
    ip_ranges = []

    try:
        answers = dns.resolver.resolve(domain, 'TXT')
    except Exception as e:
        print(f"[!] Could not resolve TXT for {domain}: {e}")
        return []

    for rdata in answers:
        record = b"".join(rdata.strings).decode()

        # Only process SPF records
        if not record.startswith("v=spf1"):
            continue

        # Extract ip4 and ip6 ranges
        ip_ranges.extend(re.findall(r"ip4:([\w./]+)", record))
        ip_ranges.extend(re.findall(r"ip6:([\w:/]+)", record))

        # Extract include: mechanisms
        includes = re.findall(r"include:([\w\.\-_]+)", record)

        for inc in includes:
            ip_ranges.extend(get_spf_records(inc, visited))

    return ip_ranges


if __name__ == "__main__":
    domain = input("Enter domain (e.g., paypal.com): ").strip()

    print(f"\n[+] Gathering SPF-authorized IP ranges for: {domain}\n")

    results = get_spf_records(domain)

    if not results:
        print("No SPF IPs found or domain does not use SPF.")
    else:
        print(f"[+] Found {len(results)} authorized IP ranges:\n")
        for ip in sorted(set(results)):
            print("  -", ip)

        print("\n[+] Done.")
