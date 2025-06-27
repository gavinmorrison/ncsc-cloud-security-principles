---
title: "Principle 8: Supply chain security"
principle: 8
summary: "Third party supply chains should support all of the security principles which the service claims to implement."
source: "https://www.ncsc.gov.uk/collection/cloud/the-cloud-security-principles/principle-8-supply-chain-security"
ogl: "Contains public sector information licensed under the Open Government Licence v3.0. https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/"
---

# Principle 8: Supply chain security

> Third party supply chains should support all of the security principles which the service claims to implement.

Cloud services rely upon third party products and services. Consequently, if this principle is not implemented, supply chain compromise can undermine the security of the service and affect the implementation of other security principles.

### Goals

### You should be sufficiently confident that you understand:

- how your data is shared with (or made accessible to) third party suppliers and their supply chains, including the circumstances under which that data is shared
- which customer data, and metadata derived from that data, is shared with, or made accessible to third party supplies and their supply chains
- how the service provider’s hardware and software procurement processes place security requirements on third party suppliers
- how the service provider manages security risks from third party suppliers
- how the service provider manages the conformance of their suppliers with security requirements

These concepts are covered in more detail in the NCSC’s Supply chain guidance.

### Suggested implementation approaches

Cloud services are often built on top of third-party IaaS or PaaS products. This is a valuable opportunity to re-use trusted components, but it’s important to identify which party is responsible for implementing which security functions.

### Separation

These layered services may result in a more complex situation when it comes to understanding separation. For example, a community SaaS may separate different users with application software controls. However, it may have been built on top of a public cloud IaaS offering, where the separation controls are implemented in the hypervisor. Thus, the actual controls may be different in practice to what they first appear.

### Sensitive data

If your application or data is particularly sensitive, you will need to consider the entire underlying stack of services as part of any security assessment. It will be difficult to gain a high degree of confidence in the security of any service built on foundations you do not understand.

### Data sharing

Cloud services often describe data sharing relationships with third parties in their terms of service, or a separate privacy policy. You should also be able to find out how they specifically share personal data (or data derived from it) as part of a GDPR compliance statement.

### Additional considerations

If you buy or outsource the operation of your cloud services to a third party such as a Managed Service Provider (MSP), they and their supply chains will also be part of your supply chain.

It is common for an MSP and their suppliers to retain privileged access to your cloud service. We discuss the considerations you should make in the MSP section of the cloud shared responsibility model.
