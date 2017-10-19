# StoleYourCookies
This is a rather simple XSS payload generator used to steal session cookies from authenticated users. Currently this tool will only work on a local network for demonstration purposes.

# Usage
```
python2 StoleYourCookie.py <Local IP Address> <Port> <Redirection URL>
```

# To Do:
- Allow access from external networks
- Implement payloads to bypass Content Security Policy (CSP)
- Implement payloads to bypass Web Application Firewalls
- Create a password protected administrator panel to display information about stolen cookies.
- Implement E-Mail alerts

# Ethics
Only use this tool in an ethical manner. Hijacking a users session without permission is illegal.
