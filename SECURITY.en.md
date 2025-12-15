# Security Policy

## Supported Versions

We release patches for security vulnerabilities. Currently supported versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take the security of our project seriously. If you discover a security vulnerability, please follow these steps:

### 1. Do Not Publicly Disclose

Please do not publicly disclose the vulnerability until we have had a chance to address it.

### 2. Contact Us

Report security vulnerabilities by:
- Opening a GitHub Security Advisory
- Sending an email to the maintainers through GitHub

### 3. Provide Details

Include the following information:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

### 4. Response Timeline

- **Initial Response:** Within 48 hours
- **Status Update:** Within 7 days
- **Fix Timeline:** Depends on severity
  - Critical: Within 7 days
  - High: Within 14 days
  - Medium: Within 30 days
  - Low: Best effort

## Security Best Practices

When using this project:

1. **Keep Dependencies Updated:** Regularly update all dependencies
2. **Use Virtual Environments:** Isolate project dependencies
3. **Review Code:** Always review code before running
4. **API Security:** Use HTTPS in production, implement rate limiting
5. **Environment Variables:** Never commit secrets or API keys
6. **Input Validation:** Always validate user inputs
7. **Docker Security:** Use specific version tags, not `latest`

## Security Features

This project includes:

- ✅ Security scanning with Bandit
- ✅ Dependency security checks with Safety
- ✅ Code quality checks with flake8
- ✅ Type checking with mypy
- ✅ Automated CI/CD security checks
- ✅ Minimal GITHUB_TOKEN permissions
- ✅ Input validation with Pydantic

## Responsible Disclosure

We appreciate responsible disclosure and will acknowledge contributors who report vulnerabilities, unless they prefer to remain anonymous.

Thank you for helping keep this project secure!
