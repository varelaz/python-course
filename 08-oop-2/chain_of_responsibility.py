from urllib.parse import urlparse, parse_qsl, quote


class CheckDomain:
    def __init__(self, domain):
        self.domain = domain

    def check_domain(self, url):
        parsed_url = urlparse(url)

        if parsed_url.netloc == self.domain:
            return True

        if parsed_url.netloc.endswith('.' + self.domain):
            return True

        return False

    def resolve(self, url):
        return None


class ResolveByUrlParam(CheckDomain):
    def __init__(self, domain, params):
        super().__init__(domain)
        self.params = params

    def resolve(self, url):
        if not self.check_domain(url):
            return None

        u = urlparse(url)
        q = dict(parse_qsl(u.query))
        if not q:
            return None

        for item in self.params:
            if item in q:
                res = q[item]
                if res and res.startswith('http'):
                    print('Resolve [%s] for [%s] domain. Result: [%s]' % (url, self.domain, res))
                    return res
        return None


class ResolveUrl:
    def __init__(self):
        self.processors = [
            ResolveByUrlParam('ads.google.com', ['url']),
            ResolveByUrlParam('ads.yahoo.com', ['rdest']),
        ]

    def resolve_one_step(self, url):
        for item in self.processors:
            result = item.resolve(url)

            if result is not None and result != url:
                return result

        return url

    def resolve(self, url):
        resolved_url = self.resolve_one_step(url)

        while resolved_url != url:
            url = resolved_url
            resolved_url = self.resolve_one_step(url)
        return resolved_url


click_url = 'http://r1.ads.google.com/redirect?url=http%3A//a.ads.yahoo.com/redirect%3Frdest%3Dhttp%253A//www.example.com%253Fa%253Db%26price%3D0.01&arg=123'

r = ResolveUrl()
print(r.resolve(click_url))