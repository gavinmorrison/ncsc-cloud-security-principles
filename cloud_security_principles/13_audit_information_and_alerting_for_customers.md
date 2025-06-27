---
title: "Principle 13: Audit information and alerting for customers"
principle: 13
summary: "Providers should supply logs needed to monitor access to your service, and the data held within it."
source: "https://www.ncsc.gov.uk/collection/cloud/the-cloud-security-principles/principle-13-audit-information-and-alerting-for-customers"
ogl: "Contains public sector information licensed under the Open Government Licence v3.0. https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/"
---

# Principle 13: Audit information and alerting for customers

> Providers should supply logs needed to monitor access to your service, and the data held within it.

You should be able to identify security incidents and should have the information necessary to determine how and when they occurred.

This will require:

- audit information
- security alerts

## Principle 13.1: audit information

#### Goals

You should be provided with the audit data needed to investigate incidents related to your use of the service and the data held within it. The type of audit information available to you will have a direct impact on your ability to respond to inappropriate or malicious activity within reasonable timescales.

###### You should be sufficiently confident that:

- you are aware of the audit information that will be provided to you, how and when it will be made available, the format of the data, and the retention period associated with it
- the audit information available will meet your needs for investigating misuse or incidents
- the provider will supply relevant audit information for actions taken by its personnel that affect your service (or the data held within it)
- audit information cannot be deleted by the customer or the cloud provider during a defined retention period

###### You should prefer a cloud provider that:

- either enables all audit information services by default, or makes them easy to enable
- provides APIs and tooling to query, process, and archive audit information
- implements an RBAC role for auditors to review logs without needing wider privileges

#### Suggested implementation approaches

Audit information is primarily used in forensic investigations to identify how and when an attack occurred and the impact of that attack. Audit information can also be analysed as it is produced to try to identify attacks, so that an incident response and subsequent investigation can then take place. You should be sufficiently confident that the audit information available to you will be suitable and sufficient for forensic investigations. You may also wish to determine its suitability for real-time incident detection.

##### Data format

The cloud provider should make audit information available in a format and structure that suits your needs. This might be a machine-readable format for efficient automated analysis, human-readable form in a hosted analysis tool, or a common format used by your external investigation tools.

You should consider whether the data format is suitable for each purpose for which you intend to use audit information. You should discuss with your SOC whether the audit information will meet your needs and integrate with your existing tooling.

##### What is recorded

You should be sufficiently confident that all important operations result in audit information. This should include the creation, modification, and deletion of resources, changes to configuration, authentication events (both failed and successful), and data accesses.

You should be confident that the audit information contains enough detail to be effective in an investigation. Some kinds of audit information may have different retention periods. You should consider the default audit retention periods and whether there is a mechanism to extend retention if necessary.

##### Logs from underlying services

As your use of a cloud service will be on a shared platform, some audit information will be derived from the logs from the underlying shared service. The audit information you receive should still be complete and authoritative for your use of the service. You may want to identify whether any additional information is available under restricted circumstances, such as a law enforcement investigation into abuse.

##### Protect audit data

You should ensure that audit information cannot be modified or deleted, either by you or by an attacker. This enables post-incident investigations to take place and prevents the attacker (who may be a malicious insider in your organisation) from hiding their tracks.

Consider whether you require audit records to be held to specific standards, or to be suitable for specific circumstances (e.g. such as being legally admissible in a UK court).

## Principle 13.2: security alerts

#### Goals

You should be provided with alerts when the cloud provider detects attacks against your data, or your use of their services . The cloud provider should be your first line of defence for identifying and preventing common attacks.

###### You should be sufficiently confident that:

- the provider will alert you when they identify attacks against, or vulnerabilities in, your use of their services
- the provider will alert you when they detect attempted or successful compromise of your data held in their services
- the provider will send their alerts promptly to a recipient of your choosing, through an automated means

###### You should prefer a cloud provider that:

- will alert you when your configuration of their services results in security issues
- will make it easy to receive and respond to alerts automatically

#### Suggested implementation approaches

The cloud provider should deliver security alerts promptly, using formats that meet your needs. This should include a structured machine-readable format for automated analysis, and a textual form for operations personnel.

The cloud provider should document each alert type that they can send and should provide a means for simulating alerts to help you check your alert handling regularly, without having to wait for a real incident.

The cloud provider should alert you when they detect signs of a security incident in your use of their services, such as:

- anomalous usage patterns of privileged accounts
- authentication checks being removed, or services being made available to the internet unexpectedly
- communication by your workloads to known malware command and control networks
- unexpected volumes of data leaving one of your virtual networks
- large volumes of data being copied from one tenancy to another
- large volumes of data being deleted

These alerts help you to identify incidents, to reduce the impact of successful attacks, and to begin investigations promptly. It may be necessary for the provider to attach a confidence or impact rating to an alert, to help you measure the urgency with which you investigate the potential incident.
