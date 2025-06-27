---
title: "Principle 10: Identity and authentication"
principle: 10
summary: "Access to service interfaces should be constrained to authenticated and authorised individuals."
source: "https://www.ncsc.gov.uk/collection/cloud/the-cloud-security-principles/principle-10-identity-and-authentication"
ogl: "Contains public sector information licensed under the Open Government Licence v3.0. https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/"
---

# Principle 10: Identity and authentication

> Access to service interfaces should be constrained to authenticated and authorised individuals.

Services and data should only be accessible to an authenticated and authorised identity, which may be either a user or a service identity.

To apply effective access control as described in Principle 9: secure user management, you must have confidence in the authentication method used to determine the identity performing the access.

Weak authentication to these interfaces may enable unauthorised access to your systems, resulting in the theft or modification of your data, changes to your service, or a denial of service. Importantly, authentication should occur over secure channels, as described in Principle 1: data in transit protection.

### Goals

### You should be sufficiently confident that:

- you understand how access to external interfaces is authenticated
- the cloud provider has a modern password policy and requires multi-factor authentication (MFA) for user accesses
- the cloud provider performs equally robust authentication of service identities as it does for users
- authentication of users will integrate with your processes for managing joiners, movers, and leavers
- processes are available for managing the lifecycle of service credentials

### You should prefer a cloud provider that:

- takes active measures to identify and revoke breached credentials
- gives users of the service confidence that they are connecting to the authentic service
- prompts administrators to re-verify themselves using MFA when performing high privilege actions

### Suggested implementation approaches

When authenticating either a user or a service identity, a successful authentication needs to result in a specific identity, to which access control can then be applied (see Principle 9).

### Contextual authentication

Authentication of users should consider various factors, such as whether the password has appeared in common or breached password lists, the strength of the MFA used, and other risk factors associated with the access.

Authenticating service identities should involve checking an appropriate cryptographic assertion, such as a cryptographic signature from a private key, or a secure key exchange, along with any other risk factors of the access. For example, service identities assigned to workloads inside the cloud environment should be rejected and considered breached if used from outside the cloud environment.

### Credential lifecycles

User credentials should follow a lifecycle as new people join the organisation, move within it, or leave. This should integrate with existing processes to reduce the likelihood of leavers retaining functional credentials.

If a user’s credentials are identified as having been breached, they should be revoked as quickly as possible. An account recovery process should then be used to ensure the new credentials are only provided to the legitimate user.

Your provider should have processes for automatically changing ('rotating') and revoking service credentials so that no service credential remains valid indefinitely and breached credentials can be revoked.

### Defending authentication

The cloud provider should take active measures to defend against authentication attacks, like password sprays and common weak passwords, as described in Principle 11 – External interface protection. Similarly, the provider should supply security alerts (see Principle 13.2) if they are discovered in common public locations, like code hosting repositories or breach data sharing sites. Ideally, these should be accompanied with an option to remediate the issue.

The cloud provider should endeavour to make authentication as user-friendly as possible, to avoid discouraging the use of strong authentication methods. This includes:

- making password managers easy to use
- making MFA easy to use through all external interfaces
- enabling the user to maintain a single identity throughout their session

### Single sign-on

We recommend you implement single sign-on (SSO) to federate your users’ identities to a corporate identity directory. This gives you the security benefits of implementing and monitoring robust authentication in a single place. It also allows you to integrate with your existing joiners/movers/leavers processes more easily.

You should understand the dependencies that your services will have on each other, as the failure of the authentication mechanism will impact the availability of your access to cloud services.

We recommend implementing a well-monitored ‘break-glass’ administrator account that you can use to restore access to cloud services that have implemented SSO.

### Identifying the service

You should be confident that, when you access the cloud service through your web browser, or when using an app to use the service, the service authenticates itself. This ensures that copycat services and malfeasant-in-the-middle attacks cannot steal your data. This is typically done using standard security protocols, such as TLS.
