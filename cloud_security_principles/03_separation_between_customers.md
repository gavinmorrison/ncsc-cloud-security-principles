---
title: "Principle 3: Separation between customers"
principle: 3
summary: "Separation techniques ensure a customer's service can't access or affect the service (or data) of another."
source: "https://www.ncsc.gov.uk/collection/cloud/the-cloud-security-principles/principle-3-separation-between-customers"
ogl: "Contains public sector information licensed under the Open Government Licence v3.0. https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/"
---

# Principle 3: Separation between customers

> Separation techniques ensure a customer's service can't access or affect the service (or data) of another.

You rely on security boundaries implemented by your cloud provider to ensure that:

- you can control who can access your data, and how
- the service is robust enough to defend against another customer having malicious code in their instance of the service

Large cloud services, such as cloud platforms, may offer many different services. These services might each take a different approach to separation .

## Goals

Your provider should be able to explain how they have implemented security separation within their service. This includes the security boundaries in:

- compute (such as containerisation, Functions-as-a-Service, and IaaS)
- storage
- data flows and networking

If a SaaS or PaaS service is built on top of other PaaS or IaaS services (such as in a third-party cloud), your provider should explain which separation properties are inherited from the underlying components and infrastructure.

You should be confident that for each service you use, you know which separation mechanisms are used and that they are appropriate for your needs.

## Suggested implementation approaches

The strength of separation that you need will depend on what type of cloud service you are using. You should look for stronger controls if you or other customers area able to run custom code inside the service. Running customer-provided code is normal for IaaS and PaaS, but not SaaS.

For more information on types of separation available in the cloud and what to look for, please refer to the separation guide .

### To gain confidence in the implementation of separation controls, you should look for externally audited evidence of:

- regular penetration tests, including red-team and blue-team exercises (good practice is discussed in our penetration testing guidance )
- independent and internal security reviews of the service design
- an engineering approach that ensures security is a key consideration in developing the service

### Compute separation

You should understand what technologies are used to separate the code running your workload, from other customers.

If you want to run custom executable code, you should look for a service that has hardware-backed separation and a small attack surface. This is usually implemented as virtualisation, using a hypervisor. For some workloads, the attack surface can be further reduced by using confidential computing technologies that include attestation and memory encryption (as outlined in Principle 2.3: data encryption ).

Other software separation techniques have a much greater attack surface exposed to a rogue user. Separation within an application or enforced by the kernel, usually only provides appropriate security separation for services where you cannot run executable code (such as SaaS and some PaaS). Some containerisation techniques fall into this category and so should only be used for functional separation, if not also backed by hardware-backed separation (such as a Type 1 hardware-backed hypervisor).

You can find more detail on common types of compute separation and recommended use cases in the separation guide .

### Storage separation

You should understand what technologies are used to prevent unauthorised parties from accessing your data stored in the cloud service. This will include your data itself, but also logs and the storage associated with any compute workloads.

Cloud services use a central access control mechanism and policy engine to define which service and user identities have access to stored objects. This is often called Identity and Access management (IAM). You should prefer services that deny access to stored objects by default, and integrate with role-based access control, as described in Principle 9: Secure user management .

You should prefer storage services that also uses encryption to implement a security boundary around stored data. This will use per-customer or per-object keys, depending on the use-case, and will usually be managed by the cloud provider. The use of those keys can be audited. The approach using encryption provides a defence in depth when access controls are applied to the key store, such as ensuring a decryption key can only be accessed by specified compute services or privileged users. Refer to Principle 2.3: data encryption for algorithm and key management recommendations.

### Network flow separation

You should use a cloud service that either implements, or is built on, a software defined network (SDN). This allows tight control over data flows, including the ability to more easily detect anomalous traffic. You should prefer an SDN that applies access controls at both ends of the data flow, and can define rules based on labels and identity, rather than just IP, port and subnet. You can implement more fine-grained data flow rules more easily if you use a service mesh.

Your cloud provider should be able to explain how they ensure that the services hosted by one customer cannot exhaust the network capacity that is available to other customers. You can find more detail on common types of network separation and recommended use cases in the separation guide .

## Additional considerations

### Location of security boundaries

Cloud providers use different terminology to describe some of the features that are associated with security boundaries. You should therefore make sure that you understand what the provider means by terms such as account, tenant, organisation, subscription, resource group, project, user, and IAM role.

It is particularly important that you understand which features are considered as a security boundary, if you are using them to implement a tiered service architecture, or other security-enforcing control within your service.

### Security updates

The security separation between customers of a cloud service will only be effective if the service provider has an effective vulnerability management plan, as described in Principle 5: operational security . This will be true, even if you choose to use dedicated or bare-metal hosting options, as you are still relying on the integrity of components such as the shared management plane. The service provider will often also still be responsible for managing the firmware of the dedicated physical device.

### Management networks

Customers will usually administer their use of the service through the same control plane that the cloud provider will use to manage the service. As a result, it’s important for the cloud provider to design the control plane to defend effectively against malicious and compromised customers. While any interface that acts as a control plane needs to be defended well, a shared control plane will also need to enforce separation between customers.

The separation between customers of a cloud service will only be effective if the service provider’s own management plane is well defended, as described in Principle 12: secure service administration .

### Private and community clouds

Community and private clouds may claim that you don't need as strong separation as when using public clouds because all customers agree to a good level of cyber hygiene and a shared risk model. However, the reliance on such procedural controls will not mitigate the risk of lateral movement between a compromised customer and your services. You should, therefore, rely on the same types of technically enforced separation within a private or community cloud as you would if you were using a public cloud.
