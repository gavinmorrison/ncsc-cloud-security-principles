---
title: "Principle 2: Asset protection and resilience"
principle: 2
summary: "Your data (and the assets storing or processing it) should be adequately protected."
source: "https://www.ncsc.gov.uk/collection/cloud/the-cloud-security-principles/principle-2-asset-protection-and-resilience"
ogl: "Contains public sector information licensed under the Open Government Licence v3.0. https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/"
---

# Principle 2: Asset protection and resilience

> Your data (and the assets storing or processing it) should be adequately protected.

Data types that are often overlooked include credentials, configuration data, derived metadata and logs. These must also be appropriately protected.

You should consider:

1. Physical location and legal jurisdiction
2. Data centre security
3. Data encryption
4. Data sanitisation and equipment disposal
5. Physical resilience and availability

## Principle 2.1: physical location and legal jurisdiction

### Goals

You should be confident that you know where your data is , and who can access your data . This should include derivatives of your data, such as verbose logs and machine learning models, unless sensitive aspects have been intentionally excluded or removed.

You should understand:

- in which countries your data will be stored, processed and managed
- which legal jurisdiction(s) your data will be subject to, and whether this is acceptable to you
- the rights that the service provider will have to access and use your data
- the legal circumstances under which your data could be accessed without your consent, and how this affects your compliance with UK legislation

### Suggested implementation approaches

### Physical location

Your service provider should present a complete list of countries where your data is stored and processed, and where the service is managed and supported from. This list may vary, depending on which specific services you are using. For example, your data may be stored in a specified local region, but the authentication service used to access it may be replicated worldwide.

The level of confidence you have in the lists provided will vary depending on whether you're reliant on the supplier's assertions, or have additional assurance through independent validation. The supplier should contractually commit to notify you of changes to the list.

### Legal jurisdiction

You need to identify which legal jurisdiction(s) your data could be subject to, seeking legal advice as necessary. This may be more complex than simply clarifying the physical locations where data is stored, processed, or accessed by the service provider.

You should also consider:

- the legal base of the service provider
- locations where the service is supported and operated from
- who owns and is responsible for the physical data centre
- the governing legislation of any contracts/agreements between you as a user of the service (or their suppliers) and the provider

There will be situations where a jurisdiction will be able to request access to your data, from the service provider. This is normal and not specific to cloud services. You should be confident none of the legal jurisdictions under which your data is subject prevents you from meeting you security goals (such as Principle 1: data in transit protection and Principle 2.3: data encryption ) in all but exceptional circumstances.

GDS publishes guidance on multi-region cloud and software-as-a-service . It will help the public sector understand where government data at OFFICIAL (including OFFICIAL SENSITIVE) can be stored and processed.

### Use of your data

You should consider the implications of any rights the service provider will have relating to data stored within the service. Some usage agreements and privacy policies allow the service provider to use customer data for marketing, advertising, machine learning, or other purposes. This may include sharing data with third parties, as discussed in Principle 8: Supply chain security . These types of data-usage agreements are particularly common for free cloud services marketed to individuals, and the free tiers of services aimed at businesses and enterprises.

You should ensure that you are not unintentionally granting rights for the service provider (or their partners) to retain copies of sensitive data or personally identifiable information (PII) for such purposes. You should also check whether any agreements with the service provider relating to their use of your data are acceptable to you, and also not contrary to relevant legislation, such as the Data Protection Act 2018.

### Additional considerations

### Data protection legislation

You will need to determine whether you are storing or processing any personal information in the cloud service. If you are, the General Data Protection Regulation (GDPR) as it applies in the UK – tailored by the Data Protection Act (DPA) 2018 – will apply.

If the physical location or legal jurisdiction is outside of the UK, you will need to determine whether the country or territory that you are transferring data to, or processing it in, would be considered a restricted transfer . If so, you will then need to determine whether it is covered by an adequacy decision or other appropriate safeguards .

Refer to ICO guidance about International Transfers for more information.

## Principle 2.2: data centre security

### Goals

You should be confident that the physical security measures employed by the provider are sufficient to protect against unauthorised access, tampering, theft or reconfiguration of systems, when considered alongside data at rest protections.

### Suggested implementation approaches

Your service provider should disclose information on the security controls around their (or their suppliers’) data centres, ideally having been certified against a recognised and appropriate standard, that covers physical security. Appropriate standards include CSA CCM v3.0.1 and ISAE 3402 .

Standards differ in terms of the level of detail applied to physical controls. Some standards are assessed in a way that only applies to certain deployments of the cloud service. For example, it might only apply to the cloud service as deployed in specific geographic regions. If this is the case, make sure the assessment applies to the cloud service deployment that you will be using. Independent validation that the scope of a certification is correct can be obtained to provide reassurance in this area.

If no recognised standard is referred to by the service provider, you will need to assess assertions and independent audits of physical controls protecting their data centres, using those standards as a baseline.

It is unlikely that a visit to a cloud provider’s data centre will provide evidence against most of the controls in the standards listed above. You should assume that a service provider will give your adversary the same access to a data centre as they will give you. You should therefore prefer a service provider that restricts access to data centres to those that have a need to be there, such as operational staff and auditors.

## Principle 2.3: data encryption

### Goals

Your data should be adequately protected from unauthorised access by parties with physical access to infrastructure, when considered alongside data at rest protections provided by encryption.

Service providers should encrypt all customer data at rest within the service, using an appropriate encryption algorithm and mode, as described below.

You should prefer a cloud provider that encrypts all data at rest by default, including any metadata derived from that data.

For this encryption, a symmetric encryption algorithm should be used in a mode of operation that provides both confidentiality (to prevent unauthorised reading of the data) and integrity (to prevent un-noticed tampering of the encrypted data).

Even a good algorithm will be vulnerable to attack if it’s not used in a good mode of operation. So, both the algorithm and mode of operation used should be approved for general use. For example, an algorithm from NIST-SP-800-131A , and a suitable mode of operation from NIST-SP-800-38 . At the time of writing, these include the symmetric algorithm AES, and the modes of operation GCM and XTS. You may see these described as AES-GCM or AES-XTS.

### Suggested implementation approaches

This section outlines some of the ways in which a supplier could demonstrate that they are achieving the goals. Your cloud provider may choose some other way to meet the goals, which you will need to assess.

### Encryption of all physical media

The service provider should ensure that no data is written to disk in an unencrypted form. This can be achieved using full-disk encryption, or application-layer encryption, or both. Encrypted data should include your customer data, pages in memory, metadata and logs derived from that data. Errors in use of cryptography or poor key management could result in exposure, or loss of integrity of your data and workloads.

Data should be encrypted using well-configured appropriate algorithms, such as those described in NIST 800-131A . Products which have been independently assessed against a good standard such as ISO/IEC 27001:2013 Annex A.10 are recommended.

You need to be confident that the service provider protects data encrypting keys and key encrypting keys through their full lifecycle. This can be achieved using the service provider’s cloud-hosted key management service. See Cloud cryptography and key management services for more details.

Your service provider may also use data encryption as a mechanism to enforce separation between customers, as described in Principle 3: Separation between customers . It could also be used to ensure that data is appropriately sanitised, as described in Principle 2.4: data sanitisation .

To support onboarding and offboarding processes, it may be necessary for storage media to be transferred between you and the service provider. If this is the case, the storage media should be encrypted to the same standards as data held in the service, ensuring that the decryption key is not accessible in transit.

### Encryption of all data in an application

The service provider may implement data encryption inside an application such as a database. Data should be encrypted using well-configured, appropriate algorithms and assessed against standards, as described above.

Relying on application-level encryption usually leaves traces of unencrypted data when the data is accessed or processed, such as in memory pages and application logs. Any application-level encryption should be combined with physical media encryption.

### Encryption of data in memory

The service provider may use hardware that encrypts the memory of a virtual machine, or service, while it is running. For more information, see Confidential computing . This technique is most valuable in cases where you have been unable to gain sufficient confidence in a service provider’s physical security, or their associated operational procedures and governance. The benefits and use cases of such hardware-backed enclaves are discussed in our separation guidance .

### Infeasibility of finding a specific customer’s data on physical devices

The scale of a service provider, obfuscation techniques, or data storage ‘sharding’ make it infeasible for a determined attacker with physical access to a data centre to locate a specific customer’s data and workloads. You should not rely on sharding alone to protect your data against the theft of a physical disk, or interference with a physical server. This approach should instead be considered as a way of providing extra confidence on top of the provider’s encryption and physical security measures.

## Principle 2.4: data sanitisation and equipment disposal

### Goals

The process of provisioning, migrating and de-provisioning resources should not result in unauthorised access to your data. You should be confident that:

- your data is erased when resources are moved or re-provisioned, or when you request it to be erased
- storage media which has held your data is sanitised or securely destroyed at the end of its life

### Suggested implementation approaches

Your service provider should give assurances that previously stored data cannot be accessed by others after it is moved or erased. This will include situations where the equipment used to deliver a service has reached the end of its useful life and should be disposed of in a way which does not compromise the security of the service, or user data stored in the service. You can also refer to our more detailed guidance on the secure sanitisation of storage media .

### Disposing of encryption keys

If your data has been appropriately encrypted, deleting the decryption key will make it inaccessible. This technique is sometimes described as crypto shredding . The confidence you can have in this technique relies on the data being encrypted using well-configured modern algorithms, as described in Principle 2.3: data encryption above, and a robust key disposal mechanism such as one in a FIPS 140-2 Hardware Security Module.

Data on disk may be protected using a key that is shared between several customers. Disposal of such a key is an effective sanitisation technique to protect against a decommissioned disk being accessed.

Data objects may be protected using a managed key that is only accessible by you and your services. Disposal of such a key is also an effective sanitisation technique, making your data irretrievable, from a shared storage service.

### Explicit overwriting of storage

The effectiveness of attempting to overwrite stored data on disk depends on the type of disk used by your provider. Solid-state disks, hybrid drives, solid-state memory and other flash-based media cannot be overwritten with the same degree of assurance as a traditional magnetic hard disk drives.

The type of disk used by your cloud provider may change over time, so you should not assume that the data that had previously been stored on magnetic disks will continue to be. This mitigation should therefore only be used as a defence in depth, in addition to other approaches, such as encryption.

### Secure equipment disposal

Your service provider should disclose information on the processes and techniques they (or their suppliers) use to sanitise equipment before disposal. This may include the use of a service that physically destroys decommissioned storage and systems.

A number of standards include controls which cover the need for secure equipment disposal, including CSA CCM v3.0.1 and ISO/IEC 27001:2013 . The standards referenced cover the need for secure equipment disposal, rather than validation of the process.

It is worth checking the scope of any certification to verify that the existence of appropriate controls was covered as part of the certification assessment. Independent validation is likely to play an important part in providing confidence that remnants of your data cannot be easily retrieved from equipment that has been disposed of.

## Principle 2.5: physical resilience and availability

### Goals

You should be sufficiently confident that:

- the availability commitments of the service, including their ability to recover from outages, meets your business needs
- you understand whether the provider’s resilience processes have any implications for data residency
- you can protect your data from ransomware attacks

You should prefer a service that makes it easy to determine whether your configuration of a cloud service (including the use of multiple regions or availability zones) will provide the level of automatic failover and redundancy that you expect.

### Suggested implementation approaches

Your service provider will likely use contractual commitments or service level agreements (SLAs) to make commitments about the level of service availability. This may provide a mechanism for compensation in the event of outages, but outages will not be prevented if the service design is not appropriate.

Service level agreements that are publicly available on a service provider’s website can show a higher commitment to meeting claims than one that is in a contract only. Services procured without contractual commitment for support should be considered to have no guaranteed support.

The service provider may present historical evidence of service availability. You should evaluate this, and draw your own conclusions on whether this gives you sufficient confidence, when considered alongside the service provider’s commitments and reputation. The service provider may be willing to share information on how they have designed their service to be resilient. Having this information reviewed by a specialist security expert would provide additional confidence.

A service provider may offer the ability to host your service across multiple data centres, availability zones or geographic regions. You should ensure that the type of resilience meets your needs, including determining the impact of a type of outage. Your service provider should describe how they ensure resiliency across energy suppliers, cooling systems, telecoms networks and the impact that an outage of one of those dependent services will have on one or more data centres.

You should consider how your data is protected from unwanted destruction, such as a ransomware attack. The service provider may offer the ability to automatically create backups of your data, such as:

- backups triggered by changes made to the data
- backups based on a user-defined time period

You should be confident that these backups give you the ability to revert or restore data to a ‘known good state’. This functionality could be provided as part of the core service, by pushing data to an external service, or by providing ways for third party services to back up and protect data.

### Additional considerations

### Service level agreements

A cloud service provider usually defines its service level agreements (SLAs) per-service, rather than for the whole of their platform. You may find that the service may not offer a contract that features the percentage availability that you need.

It is usually still possible to achieve the level of availability you need by introducing redundancy into your architecture. We recommend achieving this by using a high-availability architecture built across multiple data centres or geographic regions, within a single cloud service.

In some cases, the SLA may be defined for the whole service. This is most common for services that perform a specific standalone function, such as a content delivery network (CDN). In those cases, it may be possible to increase availability by configuring a failover between multiple services. Ineffective failover will decrease availability, so we recommend engaging with an availability specialist and regularly testing your deployment if you need to take this route. There are also security implications of a multi-cloud approach , so we recommend using multiple data centres and regions in a single service to increase redundancy, where possible.

## Further reading

General Data Protection Regulation (GDPR)

ICO guidance on International Transfers

Secure sanitisation of storage media
