---
title: "Principle 12: Secure service administration"
principle: 12
summary: "Cloud providers should recognise the high value of administration systems."
source: "https://www.ncsc.gov.uk/collection/cloud/the-cloud-security-principles/principle-12-secure-service-administration"
ogl: "Contains public sector information licensed under the Open Government Licence v3.0. https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/"
---

# Principle 12: Secure service administration

> Cloud providers should recognise the high value of administration systems.

The design, implementation, and management of the cloud provider’s administration systems used by your cloud provider should follow enterprise good practice, whilst recognising their high value to attackers.

Systems used by the vendor for administration of their cloud services will have highly privileged access to that service. Their compromise would have significant impact, including the means to bypass security controls and steal or manipulate large volumes of data.

#### Goals

###### You should be sufficiently confident that your provider:

- builds and maintains trust in the devices it uses to administer the service, with regular and thorough, security assessments
- protects its administration interfaces
- risk-manages its administration using tiers
- uses privilege access management, including ‘just in time’ and ‘just enough’ administration
- uses administration interfaces that produce detailed audit information, which is checked regularly for anomalous or unexpected behaviour

###### You should prefer a cloud provider that:

- uses layered controls and processes to manage service administration, avoiding thebrowse-upanti-pattern

These concepts are covered in more detail in the NCSC’sSecure system administration guidance.

#### Suggested implementation approaches

Secure service administration makes compromise of administration interfaces less likely, and lateral movement by an attacker more difficult. Combined withPrinciple 6.2: technical controls for service administration, the administration of the service will resist both external and internal attackers and minimise the impact of compromise.

Privileged accesses should be performed using internal APIs which record appropriately detailed audit information (seePrinciple 13.1: Audit information). These APIs should require any change to be tied to either an internal change request or a customer support ticket, so that the reason for an access can be tracked and audited. This is much easier for the provider to secure and monitor than interactive access to systems through management protocols like SSH and RDP.

Highly privileged accesses, such as those providing access to customer data, should be particularly carefully managed. For example, access to raw customer data could require authorisation from multiple nominated personnel and involve phishing-resistantmulti-factor authentication (MFA).

Particularly privileged APIs may also be restricted toprivileged access workstations (PAWs)located on company premises andrequire the caller to actively request higher privileges first. These approaches make both accidental misuse and deliberate attack more difficult, while helping to produce a robust audit trail of privileged activity.
