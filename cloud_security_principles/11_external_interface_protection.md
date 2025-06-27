---
title: "Principle 11: External interface protection"
principle: 11
summary: "All external or less trusted interfaces to the service should be identified and defended."
source: "https://www.ncsc.gov.uk/collection/cloud/the-cloud-security-principles/principle-11-external-interface-protection"
ogl: "Contains public sector information licensed under the Open Government Licence v3.0. https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/"
---

# Principle 11: External interface protection

> All external or less trusted interfaces to the service should be identified and defended.

External interfaces may include application programming interfaces (APIs), web consoles, command line interfaces (CLIs), or direct connect services. Also, the cloud provider’s administration interfaces, the interfaces you use to access the service, and any interfaces to your services built on top of the cloud service.

If some of the interfaces exposed are private (such as management interfaces) then the impact of compromise may be more significant. You can use different models to connect to cloud services which expose your enterprise systems to varying levels of risk.

### Goals

##### You should be sufficiently confident that:

- you understand what physical and logical interfaces to your information exist, and how access to your data is controlled
- the service identifies and authenticates users to an appropriate level over those interfaces (as described in Principle 10 )

##### You should prefer a cloud provider that:

- shows you which interfaces or services are exposed to the internet, highlighting those exposed without authentication
- makes it easy to understand which defences are in place to protect each external interface to your data or your use of the service
- provides easy to use defences against common attacks for the interfaces and components you use to build your service

### Suggested implementation approaches

An internet-connected interface can be attacked from anywhere, but an interface only available to a community or private network can only be attacked from those networks. Network protection methods like MPLS, SD-WAN, and VPNs are described in Principle 1: data in transit protection .

The cloud provider should design every interface of their service to be robust against attack. You should be confident that the service provider has a regime of continuous testing in place to ensure any external interfaces remain secure.

The cloud provider should make it easy to understand how your data and services are exposed more widely and what defences are in place. For example, it should be easy to identify which services are exposed to the internet, and which of those do not have protections against common attacks. This should include denial of service (DoS) attacks, authentication attacks like password sprays, and application-level attacks like HTTP desynchronisation, or SQL injection.

As internet-accessible services are more exposed to attacks, having high confidence in the strength of authentication and access control will be particularly important. Principle 10: Identity and authentication , details common approaches to identification and authentication and explains the risks associated with each. Principle 9: Secure user management covers managing access control to cloud services, including the principle of least privilege.

The cloud provider may support insecure legacy protocols, such as those that do not permit modern approaches to authentication. Those protocols should be disabled by default, and the cloud provider should generate warnings if they are left enabled, as described in Principle 13.2: Security alerts .
