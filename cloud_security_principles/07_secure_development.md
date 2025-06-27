---
title: "Principle 7: Secure development"
principle: 7
summary: "Cloud services should be designed, developed and deployed in a way that minimises and mitigates threats to their security."
source: "https://www.ncsc.gov.uk/collection/cloud/the-cloud-security-principles/principle-7-secure-development"
ogl: "Contains public sector information licensed under the Open Government Licence v3.0. https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/"
---

# Principle 7: Secure development

> Cloud services should be designed, developed and deployed in a way that minimises and mitigates threats to their security.

Cloud services which aren’t designed, developed and deployed in a secure way may be vulnerable to security issues which could compromise your data, cause loss of service, or enable other malicious activity.

### Goals

### You should be sufficiently confident that:

- the provider uses a software development lifecycle in line with our secure software development and deployment guidance, at a standard appropriate for the sensitivity of your data
- the provider has built a culture of secure development, including secure development training, code review of all deployed changes, and curation of well-understood libraries for solving security-critical problems
- the provider automates the integration and deployment pipeline used to deliver their cloud services, to enforce security, consistency, and a detailed audit trail
- the provider clearly separates their production environment from testing or development environments
- the provider risk-manages the supply chain of internal and third-party software libraries used in their code, only using supported external software
- the provider monitors the external software’s security advisories and pulls in any security fixes promptly
- configuration and secrets management processes are in place to ensure the integrity of the cloud service throughout development, testing and deployment
- the provider maintains their services over time and responds to new and evolving threats

### Suggested implementation approaches

Security should be considered throughout the design and development of the service. For example, during development of new features, potential attacks should be evaluated, and effective mitigations designed to address them. Care must be taken to balance security, cost and usability.

### Automation

Software deployed by the cloud vendor should be built and tested using an automated build pipeline and infrastructure as code, so that security requirements can be enforced, and an audit trail produced.

These measures help to deter and detect malicious insiders interfering with the software. Automation also increases the consistency of the deployment process, which aids patching, incident response, and general security health of the software. The provider should be able to trace all software it deploys back to the source code that produced it.

Secure development does not mean that all development must be done in-house, at secure facilities or by highly vetted personnel. Whilst these approaches may be appropriate for specialised components, extensive automation in the build pipeline should be the primary way of gaining confidence in the development process.

### Standards and certification

Security standards are available with certification mechanisms. These can be used to gain confidence in the effectiveness of the vendor’s software development lifecycle. These include ISO/IEC 27034, ISO/IEC 30111:2019 and CSA CCM v3.0.1.

### Third party code

You should ensure that, when your provider purchases services, software components or development services from third parties, the development practices of the supplier are suitably secure. This should be achieved through the cloud provider’s supply chain process (see Principle 8 ).

Similarly, the cloud provider’s use of third-party software dependencies should be tracked and risk-managed, according to their supply chain process. As with all software, these third-party dependencies need to be kept up to date, have security fixes applied, and continue to be actively maintained.
