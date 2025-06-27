---
title: "Principle 1: Data in transit protection"
principle: 1
summary: "User data transiting networks should be adequately protected against tampering and eavesdropping."
source: "https://www.ncsc.gov.uk/collection/cloud/the-cloud-security-principles/principle-1-data-in-transit-protection"
ogl: "Contains public sector information licensed under the Open Government Licence v3.0. https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/"
---

# Principle 1: Data in transit protection

> User data transiting networks should be adequately protected against tampering and eavesdropping.

Data in transit protection should be achieved through a combination of:

- encryption– denying your attacker the ability to read or modify data
- network protection– denying your attacker the ability to intercept data
- authentication– denying your attacker the ability to impersonate the service

## Goals

###### You should be sufficiently confident that:

- data is protected in transit between your end user device(s) and the service
- data is protected in transit as it flows between internal components within the service
- data is protected in transit where exposed to other external services, such as via an API

###### You should prefer a cloud provider that:

- encrypts all customer-data in transit by default
- pre-configures data in transit encryption, and defaults to the latest industry standards
- uses standardised, well-understood algorithms and protocols (such as TLS and IPsec) to protect data
- makes it easy to implement good data in transit protections in your application

## Suggested implementation approaches

##### Encryption and authentication

Encryption is usually implemented to provide additional confidentiality and integrity of data over and above that provided by network layer protections. All approaches should include encryption between endpoints and components of the cloud service.

If relying on a protocol that uses TLS, such as HTTPS, ensure that it is configured according to ourTLS guidance.

Alternatively, the service could expose a TLS or IPsec VPN gateway to encapsulate unencrypted protocols. VPNs should be configured to support a strong cryptographic protocol. See our advice onusing IPsecorTLSto protect data, and our advice onVPNsto ascertain whether the gateway supports a good profile.

Some services implement data in transit protections using other protocols, which may include using non-standard or customised versions of standard protocols. Where there is an option, you should choose standard protocols and configurations, as described above.

Where standard implementations are not available, cryptographic expertise will usually be required for you to be confident in the effectiveness of an approach, particularly where a protocol is bespoke. Expertise will also need to validate that the available approach provides an equivalent amount of protection to standards such as those described above.

Your cloud provider should be responsible for the encryption and key management used to protect data in transit. For example, terminating the TLS connection and managing the certificates (and the corresponding private keys) used to authenticate the service. We discuss why a cloud provider can be trusted to take responsibility for key management in ourcloud key management servicesguidance.

The cloud provider should give you assurances that data is protected in transit within their service, as well as when it is accessed via external interfaces. This includes where data is moved between physical data centres. Statements made in independently audited certifications such asCSA STAR,SOC2, andISO 27017:2015can give assurance that this is in place.

##### Network protections

Public cloud providers are accessible directly over the internet. You should ensure that all data flows between clients and the cloud service are encrypted as described above.

Your data will usually need to flow across the cloud provider’s network between different components of the cloud service, and between physical servers. Cloud platforms usually allow you to create virtual networks, which use dynamic routing rules on the underlying network to ensure that packets can only flow between your hosted resources. You can usually also apply data flow rules at the application layer (usually called an Application Layer Network). You should ensure that you understand how these controls are enforced and how to use them to ensure that your data flows cannot be accessed or tampered with by another customer of the service.

Data flows between physical data centres or availability zones usually rely on network connectivity that does not fall within the scope of the cloud provider’s usual physical security measures (such as those described inPrinciple 2.2: data centre security). You will need to ensure that the cloud provider encrypts all data that is transiting between data centres as described above. This includes data flows initiated by your application and those initiated by the underlying cloud platform, including application data, database synchronisations, backup remote storage and log aggregation.

Some services can be accessed via software-defined private networks (SD-WAN). Privacy between different customers of such services is usually implemented by a combination of routing protocols and encryption. Most SD-WAN implementations have options to encrypt traffic using IPsec, and you should ensure that this encryption provides end-to-end protection and is configured using a good profile, as described inour IPsec guidance.

Some services can be accessed via bonded fibre-optic connections, or private WAN circuits offered by a telecommunications provider. These connections do not normally provide adequate cryptographic protections, and so you should always ensure data is also encrypted using TLS or IPsec and configured using a good profile. See ourIPsecandTLS guidancefor details.

##### Authentication

All accesses made to your cloud service should be authenticated. Most public cloud providers are accessible directly over the internet. If doing so, you should ensure that all data flows are authenticated and encrypted as described above. Both parties should be authenticated, but you don’t have to use the same method for both cases. For example, services often authenticate to the customer with a TLS certificate. Customers often authenticate to the service with a username, password, and MFA, as described inPrinciple 10: identity and authentication.

You can also use TLS to support end-user authentication and access controls within applications. TLS can also be used to connect to a service’s management interfaces, to help meet the goals inPrinciple 10: Identity and authentication.

## Additional considerations

##### Points of attack

To compromise data in transit, an attacker would need access to the infrastructure over which the data transits. This could be physical access, or logical access if the attacker has compromised software components within the service.

It is more likely that attackers will have access to infrastructure between the user and the service than to infrastructure within the service. However, the impact of an attacker accessing communications internal to the service would be significantly greater.

##### Bulk data transfers

On-boarding and off-boarding of customers and workloads may involve the transfer of bulk data into or out of the service. In this scenario, you should consider the protection of data during transit using one of the approaches described above.

- If transferring large amounts of personal data, you should also refer to ourProtecting Bulk Personal Data guidance.
- If storage media is being used to transfer data, this should be protected in line withPrinciple 2.3: Data at rest protection.
