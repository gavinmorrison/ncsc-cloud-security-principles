# NCSC Cloud Security Principles

This repository contains a static export of the [NCSC Cloud Security Principles](https://www.ncsc.gov.uk/collection/cloud/the-cloud-security-principles) as individual, well-formatted Markdown files, suitable for reference, documentation, or further processing.

## Version Information

- **Published:** 17 November 2018
- **Reviewed:** 7 June 2023
- **Version:** 2.1

## Index of Principles

1. [Data in transit protection](principles/01_data_in_transit_protection.md)
2. [Asset protection and resilience](principles/02_asset_protection_and_resilience.md)
3. [Separation between customers](principles/03_separation_between_customers.md)
4. [Governance framework](principles/04_governance_framework.md)
5. [Operational security](principles/05_operational_security.md)
6. [Personnel security](principles/06_personnel_security.md)
7. [Secure development](principles/07_secure_development.md)
8. [Supply chain security](principles/08_supply_chain_security.md)
9. [Secure user management](principles/09_secure_user_management.md)
10. [Identity and authentication](principles/10_identity_and_authentication.md)
11. [External interface protection](principles/11_external_interface_protection.md)
12. [Secure service administration](principles/12_secure_service_administration.md)
13. [Audit information and alerting for customers](principles/13_audit_information_and_alerting_for_customers.md)
14. [Secure use of the service](principles/14_secure_use_of_the_service.md)

## Directory Structure

- `principles/` — Contains one Markdown file per principle, with YAML frontmatter and clean GitHub-flavored formatting.
- `download_ncsc.py` — Script to fetch and regenerate the Markdown files from the NCSC API (optional, not required for static use).

## Usage

You can browse or use the Markdown files directly. To regenerate or update the files, run:

```sh
python download_ncsc.py
```

## License

This repository is a static export for reference and research. The content is subject to the [Open Government Licence v3.0 (OGL 3.0)](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/). Please refer to the [NCSC website](https://www.ncsc.gov.uk/) for the latest official guidance and licensing information.
