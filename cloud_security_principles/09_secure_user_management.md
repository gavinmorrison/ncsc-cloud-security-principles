---
title: "Principle 9: Secure user management"
principle: 9
summary: "Providers should make tools available to securely manage your use of their service."
source: "https://www.ncsc.gov.uk/collection/cloud/the-cloud-security-principles/principle-9-secure-user-management"
ogl: "Contains public sector information licensed under the Open Government Licence v3.0. https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/"
---

# Principle 9: Secure user management

> Providers should make tools available to securely manage your use of their service.

Your provider should make the tools available for you to securely manage your access to their service, preventing unauthorised access and alteration of your resources, applications and data.

### Goals

### You should be sufficiently confident that:

- there is a single, well-defined user account model
- you understand the mechanisms used to authorise access to your data and services, including accesses to management interfaces
- you are aware of all of the mechanisms by which the service provider would accept management or support requests from you (telephone, web portal, email etc.)
- you can apply granular access control, according to the ‘principle of least privilege’, enabling both ‘standard’ and ‘administrative’ user accounts
- other customers cannot access, modify or otherwise affect your service configuration

### You should prefer a cloud provider that:

- makes access control easy to manage at scale, throughout your organisation
- makes it easy to see the access permissions applied to all resources
- uses one access control mechanism for all authorisation decisions
- helps you to remove permissions that are not being used
- lets you apply time-bounded permissions for highly privileged accesses

### Suggested implementation approaches

Access control should be based on individual permissions applied to a human or machine identity, as happens under role-based access control (RBAC). In this model, a role (the identity) is given a set of fine-grained permissions, each scoped to one or more resources. This enables you to design roles which have only the necessary permissions on the necessary resources required to meet the role’s purpose.

### Minimising permissions

Your cloud provider should supply tools to help you maintain the identities you use, so that they have only the permissions necessary for each purpose. This should include tooling to help identify the smallest set of additional permissions necessary to allow an identity to conduct a new task, and to help identify and remove permissions no longer needed. This helps to keep permission sets as small as possible over time, reducing risk and the impact of compromise.

Your cloud provider should offer curated permission sets for common purposes, to simplify access control management. It should be possible to scope these permission sets to individual resources, while still enabling the cloud provider to maintain them over time, as capabilities are removed or added.

### One access control mechanism

Your cloud provider should use a single, coherent access control mechanism. This will help it to be well understood and managed. If multiple independent mechanisms are used, discrepancies between them can result in confusion or unexpected accesses.

### Time-bounded permissions

As described in our secure system administration guidance , time-bounded permissions are an effective technique for reducing the risks around highly privileged identities.

For example, global or super-administrator identities should not be used for routine tasks, but may be needed to respond to incidents. Enabling those privileges only for the duration of an incident helps to prevent their use (accidentally or otherwise) after the incident has ended.
