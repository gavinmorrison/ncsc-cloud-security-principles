---
title: "Principle 5: Operational security"
principle: 5
summary: "Services must be operated and managed in a way to impede, detect or prevent attacks."
source: "https://www.ncsc.gov.uk/collection/cloud/the-cloud-security-principles/principle-5-operational-security"
ogl: "Contains public sector information licensed under the Open Government Licence v3.0. https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/"
---

# Principle 5: Operational security

> Services must be operated and managed in a way to impede, detect or prevent attacks.

Good operational security should not require complex, bureaucratic, time consuming or expensive processes. The aspects to consider are:

1. Vulnerability management
2. Protective monitoring
3. Incident management
4. Configuration and change management

## Principle 5.1: vulnerability management

#### Goals

Your provider should have a vulnerability management process in place toidentify,triageandmitigate vulnerabilitiesin all components of the service that they are responsible for.

Note:For more information about how to assess and prioritise vulnerabilities, please refer to the NCSC’sVulnerability Management guidance.

###### You should be confident that:

- you know your service provider’s timescales for deploying security updates and other mitigations, and are happy with them
- your provider takes responsibility for applying security updates to all software and hardware, including where they rely on external dependencies (or a third-party supply chain)
- potential new threats, vulnerabilities or exploitation techniques that could affect your service are proactively assessed and corrective action is taken

###### You should prefer a provider that:

- attempts to identify vulnerabilities in off-the-shelf components used by the service that you have deployed on top of the cloud platform
- automatically applies mitigations

#### Suggested implementation approaches

##### Threat monitoring

The provider should monitor sources of information relating to threat, vulnerabilities and exploitation techniques relevant to their service. Some service providers may have an internal threat intelligence team, some may rely on external threat feeds.

The provider should consider the severity and impact of threats and vulnerabilities within the context of the service and use this information to prioritise the implementation of mitigations. Identified vulnerabilities should be tracked until mitigations have been deployed using a suitable change management process.

##### Vulnerability management process

Conformance with a recognised standard such asISO/IEC 30111:2019, andCSA CCM v3.0.1can provide appropriate evidence of aneffective vulnerability management process. Note that these standards donotexplicitly set out acceptable timescales for mitigation.

You should seek evidence, public assertions and prior history that your service provider applies security updates or other effective mitigations within the timescales set out below.

You should be confident that the scope of the vulnerability management process includes all software that your service provider is responsible for. This will include:

- operating systems and hypervisors
- application code and its dependencies on SaaS and PaaS
- firmware and option ROMs on server components
- CPU microcode
- Hardware Security Module (HSM) firmware
- firmware on the infrastructure supporting both physical and software-defined networks

##### Timescales for applying mitigations

If there is evidence to suggest that a vulnerability is being actively exploited in the wild, you should expect your service provider to put mitigations in placeimmediately. An initial response may be to signature the vulnerability so that its attempted use can be detected. A temporary mitigation may then be put in place while a permanent fix or security update is tested and deployed to the service.

If there is no evidence that a vulnerability is being actively exploited, you should expect the service provider to prioritise updates based on the impact of the vulnerability. Your service provider should commit to applying security updates or other effective mitigations to the service within a defined timescale that is relative to the release of the update. You should expect those security updates to be applied as soon as is practical, and not be delayed without good reason.

An effective approach to configuration and change management (seePrinciple 5.4below), and Secure Development (seePrinciple 7) will allow a cloud provider to test and apply mitigations to their service very quickly. A cloud provider should therefore be expected to apply mitigations and/or security updates to their service faster than would usually be expected in individual organisations.

Some providers will treat their commitments as a worst case, so you should also consider statistics of prior performance and published case studies when determining whether a cloud provider meets your needs.

A cloud provider may also enable you to identify and remediate unpatched vulnerabilities in the services and applications that you have deployed on their platform. This includes scanning applications for known vulnerabilities, blocking attacks at the network layer, or detecting vulnerable configuration in your use of the platform. SeePrinciple 14: secure use of the servicefor more information.

#### Additional considerations

An effective vulnerability management process will need to rely on automation to ensure that security updates and configuration changes are applied consistently and promptly across your service provider’s infrastructure. This will be most effective when combined with automated asset management. The cloud provider should make you aware of any components that are not subject to automatic vulnerability management, explaining the procedural and technical processes in place to ensure that those components have mitigations promptly applied.

Cloud services usually include a mixture of bespoke software, third-party software, open source software and code derived from open source software. You should be comfortable that your service provider has a list of such external dependencies, and that their vulnerability management process includes identifying and remediating issues in them.

## 5.2 Protective monitoring

#### Goals

Your provider should monitor for attacks, misuse and malfunction to help it detect successful and unsuccessful attacks against the service as a whole, or the parts of the service that it runs on your behalf. This will allow it to quickly respond to potential compromises of your environment and data.

You should be sufficiently confident that:

- the service generates adequate audit events to support effective identification of suspicious activity
- the collected events are analysed to identify potential compromises or inappropriate use of the cloud service
- the service provider takes prompt and appropriate action to address incidents

#### Suggested implementation approaches

Effective monitoring and analysis usually involves automated data collection and analysis, combined with the intuition of a threat analysis team. Some service providers may use machine learning algorithms to assist with that analysis. The NCSC’ssecurity operations centre (SOC) buyers guideincludes a list of the types of data sources that a cloud provider may feed into their protective monitoring system.

Your cloud provider should take responsibility for monitoring all parts of the service that they are responsible for. This will almost always include authentication to the service, use of administration interfaces, network flows, and the hypervisor. They should be able to describe why their monitoring gives them confidence that they have the ability to detect attempted and successful attacks against the platform. Published case studies of historic attacks can help give you confidence.

Principle 13: Audit information and alerting for customersdescribes the security alerts your cloud provider should be sending you. You should be confident that the provider generates and acts on similar security alerts for their own services. If the cloud provider identifies an attack against their services that affects you or your data, they should alert you as described in Principle 13.2.

A number of standards such asCSA CCM v3.0.1andISO/IEC 27001:2013include controls which cover the need for effective protective monitoring processes. Standards differ in terms of the level of detail applied, and those referenced cover the need for effective protective monitoring, rather than validation of the controls in place. It is worth checking the scope of any certification to verify that protective monitoring controls were covered as part of the assessment. If relying on service provider assertions, you need to decide whether you are content with the level of confidence this gives you.

#### Additional considerations

Services which do not collect relevant accounting and audit information are unlikely to detect and respond quickly to attacks, or attempted attacks. Where attacks are detected through other mechanisms, it will be difficult to identify the extent, duration and severity of compromise if relevant audit data is not available.

Services which collect accounting and audit information but do not have effective analysis of that information are equally unlikely to detect and respond quickly to attacks. There’s no way of knowing whether unexamined data will be sufficient to support an investigation or prosecution, should one occur.

## 5.3 Incident management

#### Goals

Your cloud provider should havepre-planned incident management processes in place, to make it more likely that effective and prompt decisions are made when incidents occur. The processes needn’t be complex or require large amounts of description, but good incident management will minimise the impact to users of security, reliability and environmental issues with a service.

###### You should have confidence that:

- incident management processes are in place for the service and are actively deployed in response to security incidents
- pre-defined processes are in place for responding to common types of incident and attack
- a defined process and contact route exist for customers and external entities to report security incidents and vulnerabilities
- the service provider will inform you if they detect a security incident that affects your data in an acceptable agreed timescale

#### Suggested implementation approaches

Your cloud provider should be able to explain their incident management processes, including how the above goals are met.

The provider may refer to incident management standards such asISO/IEC 27035-1:2016,CSA CCM v3.0.1andISO/IEC 27001:2013. These standards include the need for an organisation to carry out incident management, and require the service to define some goals that they’re aiming to meet (and a provider can be certified against them). It is against these self-selected goals that the organisation is certified.

Each standard has different requirements – some cover incident management controls in detail, others simply require that an incident management process exists. You will need to check the scope of any certifications that your cloud provider is using as evidence that it meets your expectations, including that the audit and assessment was performed by an independent and expert party.

Some types of incidents affecting the cloud platform may affect your data, or use of the shared service. You should ensure that you have an agreement with your provider that they will tell you when they detect or have confirmed an incident that affects your data, and be comfortable with the reporting method and timescales. This is in addition to your security monitoring responsibilities as discussed inPrinciple 13: Audit information and alerting for customers.

Your cloud provider should have a vulnerability disclosure process that allows both customers and security researchers to report vulnerabilities in the services you use. They should be able to show you where this is on their public website and give you confidence that their process is effective. We recommend that a disclosure service is based onISO/IEC 29147:2018andISO/IEC 30111:2019.

#### Additional considerations

If you are publishing services which may be subjected to significant attacks (in terms of volume or technical capability), you should use a provider that can demonstrate robust, well tested and rehearsed incident management procedures.

Where high availability is critical, you should understand which mitigations will be applied by the service provider automatically, and which ones you have to take responsibility for implementing and deploying effectively.

## 5.4 Configuration and change management

#### Goals

Your provider should know what assets make up their service along with their configurations and dependencies, allowing them to identify and manage changes which could affect the security of the service and fully mitigate vulnerabilities that they are aware of.

###### You should be confident that:

- the status, location and configuration of service components (both hardware and software) are tracked throughout their lifetime
- changes to the service are assessed for potential security impact, then managed and tracked through to completion
- unauthorised changes to the deployed service components and their configuration will be detected and prevented
- the cloud provider will give you appropriate notice before making changes that affect how you use the service or your ability to use the service

###### You should prefer a cloud provider that:

- implements all technical change automatically and consistently across their infrastructure

#### Suggested implementation approaches

Your cloud provider should be able to explain what processes are in place to meet the above goals – whether they be procedural or technical.

A number of recognised standards include controls that cover aspects of configuration and change management processes, includingCSA CCM v3.0.1,SOC 2andISO/IEC 27001:2013. Standards differ in terms of the level of detail applied, and those referenced here cover the need for configuration and change management, rather than validation of the process.

It is worth checking the scope of any certification to verify that configuration and change management processes were covered as part of the assessment. If relying on assertions made by a service provider, you need to decide whether you are content with the level of confidence that they give you.

Without good governance of the service (seePrinciple 4: Governance framework) it is likely that change and configuration management practices will be ineffective.

#### Additional considerations

Good change and configuration management processes reduce, but do not eliminate, vulnerabilities being introduced to the configuration of a service.

It is important to have effective change management in place, but you must also realise that the service remains vulnerable until the change process is complete. Consequently, your provider should prioritise changes according to severity of risk.

If the cloud service undergoes significant changes without the provider giving you appropriate notice, then your ability to respond to the changes will be limited. Without such warning, your administrators may be unable to ensure that the service continues to be configured securely and your users may be unable to use the service in the ways they have been advised by security professionals.

Industry good practice would dictate that significant changes (such as the removal or significant alteration of features) are planned and communicated to you in good time, so that you can take action to ensure a smooth transition.
