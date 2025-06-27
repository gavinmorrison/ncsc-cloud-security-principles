---
title: "Principle 6: Personnel security"
principle: 6
summary: "Audit and constrain the actions of service provider personnel."
source: "https://www.ncsc.gov.uk/collection/cloud/the-cloud-security-principles/principle-6-personnel-security"
ogl: "Contains public sector information licensed under the Open Government Licence v3.0. https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/"
---

# Principle 6: Personnel security

> Audit and constrain the actions of service provider personnel.

Where service provider personnel have access to your data and systems, you need to have enough confidence in their trustworthiness, and the technical measures in place that audit and constrain the actions of those personnel.

Effective personnel controls should be a balance of:

- the provider demonstrating how they gain enough confidence in their people
- technical controls that minimise the likelihood and impact of accidental or malicious compromise by service provider personnel

## Principle 6.1: people and security culture

The service provider should subject personnel to security screening and regular security training, appropriate to their role and privileges. Providers should make clear how they screen and manage personnel within privileged roles.

### Goals

You should be confident that:

- the minimum number of people have access to your data, or could affect your use of the service
- the provider has implemented a positive security culture across their organisation
- the level of security screening conducted on service provider staff or contractors that have access to your data, or have the ability to affect your service, is appropriate

### Suggested implementation approaches

Your provider should be able to explain how they build and sustain a positive security culture in their workforce and partnerships. You can read more about the benefits of doing this in in CPNI’s Data Centre guidance. Security training pathways can benefit staff in all roles, but they are most beneficial to staff in privileged roles when there is any dependency on them following procedural controls.

### The provider should be able identify groups of people that:

- could have access to your data, such as second or third line support engineers
- are in a role that could directly affect the operation or integrity of the service, such as someone that can approve code check-in to production

Your cloud provider should be able to explain how they gain sufficient trust in their staff, and the staff of their outsourcers. This will usually include verifying their identity, their right to work, and identifying any unspent criminal convictions.

They may choose to perform more personnel screening of personnel with access to your data or the ability to modify your service. You will need to make a judgement over how much screening is sufficient for people that have privileged accesses to the underlying cloud platform and the data stored on it.

BS 7858:2019 sets out a more thorough standard for personnel screening. Many multinational companies will perform background checks that cover the requirements of this standard.

Note that it is not possible to perform all of the checks in some countries, and some organisations may be unwilling to perform personnel screening checks.

## Principle 6.2: technical controls for service administration

Personnel security should combine background checks and procedural controls with technical measures designed to detect and minimise the impact of a malicious insider.

### Goals

You should be confident that:

- an administrator accessing your data, or making changes that affect your use of the service, will be reliably logged and monitored
- you will be alerted if the provider’s personnel perform an action on the cloud service that could (accidentally or otherwise) expose them to your data

You should prefer a cloud provider that employs technical controls to reduce the likelihood of accidental or malicious compromise by service provider personnel.

### Controls should include:

- administrators and privileged users are only given minimal administrative capabilities temporarily, in response to a specific issue (additional privileges should be requested when necessary)
- requests for additional privileges are tied either to a customer support ticket, or an internal change request
- access to systems or interfaces that could provide access to customer data is only granted if the customer has given explicit time-limited permission for that access (this applies on a case-by-case basis)

### Suggested implementation approaches

Role Based Access Control (RBAC) can be configured so that the cloud provider’s personnel can only perform actions that are directly related to their role. The role of RBAC in how your cloud provider administers its service is covered in more detail in Principle 12: secure service administration.

Your provider should log and audit all accesses made to production systems and the customer data hosted on them. They should be able to explain how they do this, and how they use the logs to ensure that:

- procedural controls are being followed
- privileged accesses are not being misused

Logging is more reliable on cloud services that are administered via a managed API, and hard to do reliably on systems that allow administrators to log onto an interactive session. You should therefore prefer a cloud provider that prevents all interactive logon to servers and services by the cloud service’s personnel. Attempts to use such interfaces – even if prevented – should be raised as a priority security incident.

You should understand which logs relevant to your data and service are made available to you as a customer, as discussed in Principle 13: audit information and alerting for customers.
