---
title: "Principle 14: Secure use of the service"
principle: 14
summary: "Providers should make it easy for you to adequately protect your data."
source: "https://www.ncsc.gov.uk/collection/cloud/the-cloud-security-principles/principle-14-secure-use-of-the-service"
ogl: "Contains public sector information licensed under the Open Government Licence v3.0. https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/"
---

# Principle 14: Secure use of the service

> Providers should make it easy for you to adequately protect your data.

Your cloud provider should make it easy for you to meet your responsibility to adequately protect your data.

You should consider:

- whether the service is secure by design and by default
- what help the provider gives you to meet your responsibilities

## Principle 14.1: Security by design and by default

#### Goals

Your service provider should make it easy for you to use their services in a way that is defended against common attacks.

###### You should be sufficiently confident that:

- you know which goals from the Principles 1-13 are met by the service’s default configuration
- you know what you need to do to the service’s configuration to meet the remaining goals
- data and services are not accessible to unauthenticated users, by default
- the provider takes responsibility for improving their service’s default configuration, to respond to new threats (this may include altering the configuration of existing customers, as well as changing the starting point for new customers)

###### You should prefer a cloud service that:

- meets all of the goals described in Principles 1-13 by design, or in its default configuration
- makes configurable security-enhancing features opt-out, and not opt-in
- defends against common network-based attacks (such as DDoS) against the service and your hosted workloads by default, as described in Principle 11: external interface protection

#### Suggested implementation approaches

A cloud service may be designed such that it natively meets all the goals described in this guidance, by design. Where the service provider gives direct responses to Principles 1-13, you should note where the goal is achieved by the design of the service.

Goals described in Principles 1-13 may be met because of a default configuration, that a user or service administrator can choose to override.

If your cloud provider cannot meet all of the goals directly, they may refer you to an ecosystem of third-party providers who supply additional security services. If that third party has access to your data, it may be necessary to separately assess their service against these 14 cloud security principles .

If your cloud provider supports all of the goals listed in this guidance, but does not enable them by default, the provider may make it easy to programmatically configure the service to meet the goals described in these principles. You should be confident that you understand how their published templates, blueprints or scripts meet the goals.

The cloud provider could supply links to published good practice guides with step-by-step instructions.

#### Configuration is your responsibility

Even if your provider embraces a secure by default approach, the configuration of the cloud services that you use remains your responsibility. You should check that their recommendations meet your security needs, using our guide to using cloud services securely to help you. Periodically audit your configuration as part of a wider security assessment, or penetration test .

Some cloud platforms have adopted a more secure by default approach recently, and only apply those good defaults to new accounts or tenants. Similarly, as the threat landscape changes, their updated default configuration may only be applied to new accounts or tenants.

You should periodically review your service configuration against the platform’s good practice guides to determine whether you need to proactively enable newer mitigations as they may not be retroactively applied to your service configuration.

## Principle 14.2: Help customers meet their security responsibilities

#### Goals

Your service provider should make it easy for you to be confident that you are using the cloud securely. It should be easy for you to see what services you have in the cloud, and how they have been configured.

###### You should be confident that:

- all service configuration can be set and audited using infrastructure as code, or via an API
- there is a single place where you can see all of your deployed resources across all services and regions offered by that cloud platform
- all service configurations are visible and intuitive to humans, so that they can easily audit what services they are using, where their data is, and how those services are configured

###### You should prefer a provider that:

- raises an actionable alert when your configuration of the service could weaken your security stance, or leave you vulnerable to a breach
- gives you tools to help meet your responsibilities, such as hardened container base images, CI/CD tooling, and detection of common vulnerabilities in the applications that you deploy
- monitors the workloads you deploy for out-of-date dependencies and missing security updates. The service may raise a security alert or automatically remediate the problem

#### Suggested implementation approaches

A cloud service may be designed such that it natively meets all the goals described above.

The cloud provider may supply dashboards and pre-defined alerts to highlight good and poor practice. This may include a prioritised list of security improvements, mechanisms to remediate issues automatically or programmatically, and advice on how you might remediate the issues yourself. You can read more about security alerting in Principle 13: audit information and alerting for customers .

The platform may provide the raw data required to meet the goals but not provide the associated service which would depend on this data. In this case, you will need to either connect that data to a third party service that implements the goals, or you will need to deploy your own code to interpret that data yourself, using the platform’s native features, such as Functions-as-a-service.

#### Additional considerations

As described in the shared responsibility model , you will always be responsible for some aspects of the security of your data. The specific service you use and the way that you are using it will influence how much responsibility you have. You should identify those responsibilities and ensure that you act on them when initially deploying to the cloud, and throughout the lifetime of your workloads and data being hosted there.
