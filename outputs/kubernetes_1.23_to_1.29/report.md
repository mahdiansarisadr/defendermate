# Kubernetes 1.23 → 1.29: upgrade risk report

> Documentation-derived risk conditions; not a migration plan.

Kubernetes 1.23 -> 1.29 crosses 6 release(s) (1.24, 1.25, 1.26, 1.27, 1.28, 1.29). 83 risk paths: 13 critical, 30 high, 32 medium, 7 low. Main risk types: removed_api (40), changed_behavior (18), configuration_change (11). Critical: batch/v1beta1 CronJob API removed in 1.25; EndpointSlice discovery.k8s.io/v1beta1 no longer served; CSIStorageCapacity storage.k8s.io/v1beta1 removal; HorizontalPodAutoscaler autoscaling/v2beta1 removal; Removed deprecated API versions in v1.29. 48 context facts and 0 disqualified candidates are listed separately. Documentation-derived risk conditions; not a migration plan.

Overall confidence: **medium**. Validation: `{"errors": 0, "warnings": 5, "by_code": {"W4_no_search_queries": 5}}`

## Risk paths

| Level | Confidence | Type | Surface | Release | Path |
|---|---|---|---|---|---|
| critical | high | removed_api | application_code | 1.25 | `kubernetes_02214acf74` batch/v1beta1 CronJob API removed in 1.25 |
| critical | high | removed_api | application_code | 1.25 | `kubernetes_28e51fa8fe` EndpointSlice discovery.k8s.io/v1beta1 no longer served |
| critical | high | removed_api | application_code | 1.27 | `kubernetes_50b8d8e0fd` CSIStorageCapacity storage.k8s.io/v1beta1 removal |
| critical | medium | removed_api | deployment | 1.25 | `kubernetes_6689115982` HorizontalPodAutoscaler autoscaling/v2beta1 removal |
| critical | low | removed_api | application_code | 1.29 | `kubernetes_70f592d3da` Removed deprecated API versions in v1.29 |
| critical | high | removed_api | application_code | 1.25 | `kubernetes_7861414339` policy/v1beta1 PodDisruptionBudget no longer served |
| critical | high | removed_api | application_code | 1.26 | `kubernetes_7b8a1ea444` HorizontalPodAutoscaler autoscaling/v2beta2 no longer served |
| critical | medium | removed_api | application_code | 1.26 | `kubernetes_997b64cd86` flowcontrol.apiserver.k8s.io/v1beta1 FlowSchema and PriorityLevelConfiguration no longer served |
| critical | medium | removed_api | application_code | 1.29 | `kubernetes_b84274af9e` flowcontrol.apiserver.k8s.io/v1beta2 FlowSchema and PriorityLevelConfiguration removed in v1.29 |
| critical | medium | removed_api | application_code | 1.24 | `kubernetes_c2e5521796` RuntimeClass node.k8s.io/v1alpha1 API no longer served |
| critical | medium | removed_api | application_code | 1.26 | `kubernetes_e6d21bce2d` Deprecated beta APIs removed in v1.26 |
| critical | high | removed_api | deployment | 1.25 | `kubernetes_f51a904d3d` RuntimeClass node.k8s.io/v1beta1 removed |
| critical | medium | removed_api | application_code | 1.25 | `kubernetes_fc16f3bccf` events.k8s.io/v1beta1 Event API removed |
| high | high | removed_api | application_code | 1.24 | `kubernetes_0089fb8601` client-go credential plugin relying on client.authentication.k8s.io/v1alpha1 ExecCredential |
| high | high | changed_behavior | application_code | 1.29 | `kubernetes_1a5432e398` Creating new CronJobs with TZ or CRON_TZ in .spec.schedule |
| high | medium | removed_api | configuration | 1.25 | `kubernetes_1f10d2a281` kube-controller-manager removed flags deleting-pods-qps, deleting-pods-burst, register-retry-count |
| high | medium | removed_api | deployment | 1.28 | `kubernetes_262d87f013` kubectl version --short flag removed |
| high | medium | dependency_requirement | deployment | * | `kubernetes_3a107f9c1e` kubelet version skew before kube-apiserver upgrade |
| high | medium | operational_risk | deployment | * | `kubernetes_43d8c248a4` single-instance kube-apiserver skips minor version (1.23 to 1.29) |
| high | medium | removed_api | application_code | 1.26 | `kubernetes_471b45948b` gcp-azure-auth-plugins-removed |
| high | medium | removed_api | deployment | 1.26 | `kubernetes_4da15810ad` In-tree OpenStack cloud provider removed |
| high | medium | configuration_change | configuration | 1.24 | `kubernetes_5b5d9d0ac5` kubeadm config files still reference the dockershim socket |
| high | medium | removed_api | application_code | 1.26 | `kubernetes_61e40b3bda` HorizontalPodAutoscaler targetAverageUtilization field replaced |
| high | medium | removed_api | configuration | 1.28 | `kubernetes_6a9aabc985` kube-scheduler --lock-object-name flag removed |
| high | medium | changed_behavior | configuration | 1.26 | `kubernetes_71ae8992a8` HPA targetAverageUtilization replaced |
| high | medium | removed_api | application_code | 1.26 | `kubernetes_8b7a9adfd6` GlusterFS in-tree storage driver removed in v1.26 |
| high | medium | changed_behavior | application_code | 1.28 | `kubernetes_9ee51f7127` Scheduler EnqueueExtension EventsToRegister return type change |
| high | medium | removed_api | deployment | 1.27 | `kubernetes_a1ff166364` In-tree EBS storage plugin removed |
| high | high | removed_api | configuration | 1.25 | `kubernetes_ab919afc13` PodSecurityPolicy admission plugin removed in 1.25 |
| high | high | removed_api | deployment | 1.25 | `kubernetes_b8ccd4eaaa` Removed in-tree volume plugin: quobyte |
| high | high | removed_api | application_code | 1.29 | `kubernetes_baa4052480` Removed networking alpha API ClusterCIDR |
| high | medium | removed_api | deployment | 1.26 | `kubernetes_bf90a0c464` In-tree cinder volume provider removed |
| high | medium | removed_api | configuration | 1.25 | `kubernetes_c1fd329e73` Removed API server flag --service-account-api-audiences |
| high | high | removed_api | deployment | 1.25 | `kubernetes_c48826c6b8` Removed in-tree volume plugin: flocker |
| high | medium | operational_risk | configuration | * | `kubernetes_c83275ac09` Admission webhooks not updated for new REST resource versions and fields before kube-apiserver upgrade |
| high | medium | removed_api | deployment | 1.27 | `kubernetes_d90e72f835` In-tree AWS cloud provider removed |
| high | medium | removed_api | runtime | 1.24 | `kubernetes_db1c331258` Kubelet dockershim Docker runtime removed in 1.24 |
| high | medium | removed_api | configuration | 1.28 | `kubernetes_e21f521ab8` kube-scheduler --lock-object-namespace flag removed |
| high | medium | removed_api | configuration | 1.24 | `kubernetes_e4f538b8cc` Removed kubelet flag --experimental-check-node-capabilities-before-mount |
| high | medium | removed_api | application_code | 1.24 | `kubernetes_e82868187c` Service tolerate-unready-endpoints annotation removed |
| high | medium | operational_risk | deployment | * | `kubernetes_ec1ed44946` kubelet newer than kube-apiserver during upgrade |
| high | medium | removed_api | configuration | 1.27 | `kubernetes_f37fdc8f97` IPv6DualStack feature gate manually enabled for external cloud providers |
| high | medium | removed_api | deployment | 1.25 | `kubernetes_ff27941095` Removed in-tree volume plugin: storageos |
| medium | high | removed_api | runtime | 1.25 | `kubernetes_0214e6aee0` Windows winkernel kube-proxy no longer supports HNS v1 APIs |
| medium | medium | changed_behavior | configuration | 1.29 | `kubernetes_05f82d70f3` kubeadm admin.conf RBAC binding change and super-admin.conf |
| medium | medium | runtime_requirement | configuration | 1.25 | `kubernetes_098e6337df` In-tree vSphere volume on vSphere releases below 7.0u2 |
| medium | medium | changed_default | application_code | 1.24 | `kubernetes_1ae44fcc5b` LegacyServiceAccountTokenNoAutoGeneration: apps relying on auto-generated ServiceAccount token Secrets |
| medium | medium | changed_behavior | deployment | 1.28 | `kubernetes_2367ae9f77` kubectl version default output changed |
| medium | medium | changed_behavior | configuration | 1.24 | `kubernetes_29aeab2f1c` multiple CRI sockets on host with empty criSocket during cluster creation |
| medium | medium | removed_api | configuration | 1.24 | `kubernetes_2e91042cd0` Removed experimental dynamic log sanitization feature |
| medium | medium | changed_behavior | application_code | 1.29 | `kubernetes_3cf225fc10` PriorityLevelConfiguration spec.limited.assuredConcurrencyShares renamed in flowcontrol.apiserver.k8s.io/v1beta3 |
| medium | high | changed_behavior | configuration | 1.25 | `kubernetes_4d1a7508d9` PodDisruptionBudget policy/v1 empty spec.selector |
| medium | medium | configuration_change | configuration | 1.25 | `kubernetes_54d1b6b275` kubeadm imageRepository k8s.gcr.io rewrite during upgrade |
| medium | medium | changed_behavior | deployment | 1.24 | `kubernetes_58f3704548` kubeadm upgrade adds control-plane NoSchedule taint to existing control plane nodes |
| medium | medium | configuration_change | configuration | 1.29 | `kubernetes_612defa966` PriorityLevelConfiguration assuredConcurrencyShares renamed to nominalConcurrencyShares |
| medium | medium | changed_behavior | configuration | 1.25 | `kubernetes_655168da6e` PodDisruptionBudget empty spec.selector in policy/v1 |
| medium | medium | changed_behavior | application_code | 1.25 | `kubernetes_783b0b093f` EndpointSlice topology field not writable in v1 |
| medium | medium | changed_behavior | deployment | 1.25 | `kubernetes_794be3349b` control-plane-noschedule-taint-removed-on-kubeadm-upgrade |
| medium | medium | configuration_change | configuration | 1.24 | `kubernetes_8a1e841ec0` kube-apiserver insecure address flags removed |
| medium | medium | changed_behavior | application_code | 1.25 | `kubernetes_8e7dabc5b0` events.k8s.io/v1 Event field changes for clients creating events |
| medium | medium | configuration_change | configuration | 1.24 | `kubernetes_954dc817ef` kube-controller-manager insecure address flags removed |
| medium | medium | configuration_change | configuration | 1.25 | `kubernetes_965870d781` kubeadm kubelet-config ConfigMap rename for clusters using UnversionedKubeletConfigMap=false |
| medium | medium | changed_behavior | application_code | 1.27 | `kubernetes_98774b6ac3` Pods with RestartPolicy=Always may reach Succeeded phase |
| medium | medium | changed_behavior | application_code | 1.25 | `kubernetes_9972c3a8b9` EndpointSlice topology zone key |
| medium | medium | operational_risk | deployment | * | `kubernetes_9b35c15a85` Control plane component version skew during 1.23 to 1.29 upgrade |
| medium | medium | configuration_change | deployment | 1.24 | `kubernetes_9d0391887c` kubeadm upgrade removes node-role.kubernetes.io/master label from existing control plane nodes |
| medium | low | operational_risk | deployment | * | `kubernetes_9e61fc9ebd` kube-proxy older than allowed skew after apiserver upgrade |
| medium | medium | configuration_change | configuration | 1.29 | `kubernetes_beac686c4e` kubeadm upgrade plan --config component config for kube-proxy and kubelet |
| medium | medium | operational_risk | configuration | 1.25 | `kubernetes_c19bd052ab` Admission/Policy registry allowlists need registry.k8s.io |
| medium | medium | changed_behavior | deployment | 1.24 | `kubernetes_d9554c0e18` Pod topology spread skew now excludes nodes not matching node affinity/selector |
| medium | medium | changed_behavior | application_code | 1.25 | `kubernetes_ddf8635e3c` EndpointSlice topology hostname key |
| medium | medium | configuration_change | configuration | 1.24 | `kubernetes_de350dc7b2` vSphere vCenter credentials in secret with Zones feature: node update RBAC for vsphere-legacy-cloud-provider |
| medium | medium | configuration_change | configuration | 1.24 | `kubernetes_e5b62c5ec0` csiMigrationRBD feature gate misspelling |
| medium | medium | operational_risk | deployment | 1.24 | `kubernetes_f99278a4ed` Dashboard cluster addon removed |
| medium | medium | removed_api | configuration | 1.27 | `kubernetes_fea98e9bba` Alpha seccomp annotations removed |
| low | high | configuration_change | configuration | 1.24 | `kubernetes_0ef6155acc` Removed feature gates ValidateProxyRedirects and StreamingProxyRedirects |
| low | medium | operational_risk | deployment | 1.28 | `kubernetes_0ffaca21b0` CephFS in-tree volume plugin deprecation |
| low | medium | operational_risk | deployment | 1.28 | `kubernetes_305dd46055` RBD in-tree volume plugin deprecation |
| low | medium | removed_api | application_code | 1.24 | `kubernetes_3d5dbb8cc8` Removed insecure serving configuration in cloud-provider package |
| low | high | changed_behavior | application_code | 1.24 | `kubernetes_517a769c03` metadata.clusterName accidental client use |
| low | medium | operational_risk | deployment | 1.28 | `kubernetes_8c73624e95` Ceph RBD CSI migration support deprecation |
| low | medium | changed_default | configuration | 1.29 | `kubernetes_f2ea0031b7` PriorityLevelConfiguration nominalConcurrencyShares default and explicit zero |
| unknown | medium | removed_api | application_code | 1.25 | `kubernetes_9c957094cf` Deprecated API versions no longer served in v1.25 |

### batch/v1beta1 CronJob API removed in 1.25

`kubernetes_02214acf74` · critical · confidence high · introduced in 1.25 · fires at upgrade

The batch/v1beta1 API version of CronJob is no longer served as of v1.25, so manifests and API clients that use it stop working when the upgrade crosses 1.25. Migrate them to batch/v1, available since v1.21.

- **[required] version** `in_range` `{"current_version": "< 1.25", "target_version": ">= 1.25"}`: The upgrade crosses Kubernetes release 1.25, the release in which batch/v1beta1 CronJob stopped being served. (confidence high, judge supported)
  - k8s_deprecation_guide: "The batch/v1beta1 API version of CronJob is no longer served as of v1.25"
  - k8s_deprecation_guide: "no longer served as of v1.25"
- **[required] api_usage** `present` `"batch/v1beta1"`: The application, manifests or API clients use the batch/v1beta1 API version of CronJob. (confidence high, judge supported)
  - k8s_deprecation_guide: "The batch/v1beta1 API version of CronJob"
  - k8s_deprecation_guide: "The batch/v1beta1 API version of CronJob is no longer served"

Actions:
- Migrate manifests and API clients to use the batch/v1 API version, available since v1.21.
- Verify existing persisted objects are accessible through the batch/v1 API after migration.
- Update existing CronJob manifests from batch/v1beta1 to batch/v1 before upgrading to v1.25 or later.

### EndpointSlice discovery.k8s.io/v1beta1 no longer served

`kubernetes_28e51fa8fe` · critical · confidence high · introduced in 1.25 · fires at upgrade

The discovery.k8s.io/v1beta1 API version of EndpointSlice is no longer served as of v1.25. Manifests and API clients must migrate to discovery.k8s.io/v1.

- **[required] version** `in_range` `{"current_version": "< 1.25", "target_version": ">= 1.25"}`: The upgrade from 1.23 crosses release 1.25, where the discovery.k8s.io/v1beta1 EndpointSlice API stops being served. (confidence high, judge supported)
  - k8s_deprecation_guide: "The discovery.k8s.io/v1beta1 API version of EndpointSlice is no longer served as of v1.25."
- **[required] api_usage** `present` `"discovery.k8s.io/v1beta1"`: The application or deployment uses the discovery.k8s.io/v1beta1 API version of EndpointSlice. (confidence high, judge supported)
  - k8s_deprecation_guide: "The discovery.k8s.io/v1beta1 API version of EndpointSlice is no longer served as of v1.25."
- **[optional] behavior** `present` `"topology"`: The application reads or writes the EndpointSlice topology field, which is replaced in v1. (confidence high, judge supported)
  - k8s_deprecation_guide: "topology is replaced with the deprecatedTopology field which is not writable in v1"

Actions:
- Migrate manifests and API clients to use the discovery.k8s.io/v1 API version, available since v1.21.
- Use the per Endpoint nodeName field instead of the deprecated topology kubernetes.io/hostname field.
- Use the per Endpoint zone field instead of the deprecated topology topology.kubernetes.io/zone field.
- Migrate manifests and API clients to use the discovery.k8s.io/v1 API version.
- Replace topology["kubernetes.io/hostname"] with the per Endpoint nodeName field.
- Replace topology["topology.kubernetes.io/zone"] with the per Endpoint zone field.

### CSIStorageCapacity storage.k8s.io/v1beta1 removal

`kubernetes_50b8d8e0fd` · critical · confidence high · introduced in 1.27 · fires at upgrade

The storage.k8s.io/v1beta1 API version of CSIStorageCapacity is no longer served as of v1.27. Applications, manifests, or API clients that use this version will fail when the cluster is upgraded past v1.27.

- **[required] version** `in_range` `{"current_version": "< 1.27", "target_version": ">= 1.27"}`: The upgrade from 1.23 to 1.29 crosses release v1.27, the release in which the storage.k8s.io/v1beta1 API version of CSIStorageCapacity stops being served. (confidence high, judge supported)
  - k8s_deprecation_guide: "no longer served as of v1.27"
  - k8s_deprecation_guide: "The storage.k8s.io/v1beta1 API version of CSIStorageCapacity is no longer served as of v1.27."
- **[required] api_usage** `present` `"storage.k8s.io/v1beta1"`: The application, manifests, or API clients use the storage.k8s.io/v1beta1 API version of CSIStorageCapacity. (confidence high, judge supported)
  - k8s_deprecation_guide: "The storage.k8s.io/v1beta1 API version of CSIStorageCapacity"
  - k8s_deprecation_guide: "The storage.k8s.io/v1beta1 API version of CSIStorageCapacity is no longer served as of v1.27."

Actions:
- Migrate manifests and API clients to use the storage.k8s.io/v1 API version, which is available since v1.24.
- Confirm that all existing persisted objects are accessible via the storage.k8s.io/v1 API version before upgrading past v1.27.
- Migrate manifests and API clients to use the storage.k8s.io/v1 API version.
- Confirm that storage.k8s.io/v1 is available in the target cluster, as it has been available since v1.24.

### HorizontalPodAutoscaler autoscaling/v2beta1 removal

`kubernetes_6689115982` · critical · confidence medium · introduced in 1.25 · fires at upgrade

The autoscaling/v2beta1 API version of HorizontalPodAutoscaler is no longer served as of v1.25. Manifests and API clients that use autoscaling/v2beta1 must be migrated to autoscaling/v2 before upgrading across 1.25.

- **[required] version** `in_range` `{"current_version": "< 1.25", "target_version": ">= 1.25"}`: The upgrade from 1.23 to 1.29 crosses release 1.25, where the autoscaling/v2beta1 API version stops being served. (confidence medium, judge partially_supported)
  - k8s_deprecation_guide: "The autoscaling/v2beta1 API version of HorizontalPodAutoscaler is no longer served as of v1.25."
- **[required] api_usage** `present` `"autoscaling/v2beta1"`: The application's manifests or API clients use the autoscaling/v2beta1 API version of HorizontalPodAutoscaler. (confidence high, judge supported)
  - k8s_deprecation_guide: "The autoscaling/v2beta1 API version of HorizontalPodAutoscaler is no longer served"
  - k8s_deprecation_guide: "Migrate manifests and API clients to use the autoscaling/v2 API version, available since v1.23."
  - k8s_deprecation_guide: "The autoscaling/v2beta1 API version of HorizontalPodAutoscaler"
- **[optional] api_usage** `present` `"targetAverageUtilization"`: HorizontalPodAutoscaler manifests use the targetAverageUtilization field that is replaced in the autoscaling/v2 API version. (confidence high, judge supported)
  - k8s_deprecation_guide: "targetAverageUtilization is replaced with target.averageUtilization and target.type: Utilization"
- **[optional] configuration** `present` `"targetAverageUtilization"`: HorizontalPodAutoscaler manifests use the targetAverageUtilization field, which is replaced in the autoscaling/v2 API. (confidence high, judge supported)
  - k8s_deprecation_guide: "targetAverageUtilization is replaced with target.averageUtilization and target.type: Utilization."

Actions:
- Migrate manifests and API clients to use the autoscaling/v2 API version, available since v1.23.
- Replace targetAverageUtilization with target.averageUtilization and target.type: Utilization.
- Check that all existing persisted objects are accessible through the autoscaling/v2 API after migration.
- Migrate manifests and API clients to use the autoscaling/v2 API version.
- Replace targetAverageUtilization with target.averageUtilization and target.type: Utilization in HorizontalPodAutoscaler manifests.
- Existing persisted objects remain accessible through the autoscaling/v2 API version.

### Removed deprecated API versions in v1.29

`kubernetes_70f592d3da` · critical · confidence low · introduced in 1.29 · fires at upgrade

The v1.29 release stopped serving the deprecated API versions listed in the source section. The specific API versions are not named in the provided text, so any application or manifest using them would be affected.

- **[required] version** `in_range` `{"current_version": "< 1.29", "target_version": ">= 1.29"}`: The upgrade crosses release 1.29 (starting version is below 1.29 and target is 1.29 or later) (confidence medium, judge partially_supported)
  - k8s_deprecation_guide: "The v1.29 release stopped serving the following deprecated API versions:"
- **[required] api_usage** `present` `"a deprecated API version listed as removed in v1.29"`: The application or deployment uses one of the deprecated API versions that v1.29 stopped serving (confidence low, judge supported)
  - k8s_deprecation_guide: "The v1.29 release stopped serving the following deprecated API versions:"
  - ⚠ The specific API versions are not named in the provided ITEM or PARENT CONTEXT, so the usage cannot be checked against a literal symbol.

Actions:
- Obtain the full list of deprecated API versions stopped in v1.29 from the Removed APIs by release v1.29 section of the Kubernetes Deprecated API Migration Guide.
- Check manifests, Helm charts and clients for use of any listed API version and migrate them to a served version before upgrading.

### policy/v1beta1 PodDisruptionBudget no longer served

`kubernetes_7861414339` · critical · confidence high · introduced in 1.25 · fires at upgrade

The policy/v1beta1 API version of PodDisruptionBudget is no longer served as of v1.25, so manifests and clients using it will fail when the cluster is upgraded past v1.25.

- **[required] version** `in_range` `{"current_version": "< 1.25", "target_version": ">= 1.25"}`: The upgrade crosses release 1.25, where policy/v1beta1 PodDisruptionBudget stops being served (confidence high, judge supported)
  - k8s_deprecation_guide: "is no longer served as of v1.25"
  - k8s_deprecation_guide: "PodSecurityPolicy in the policy/v1beta1 API version is no longer served as of v1.25"
  - k8s_deprecation_guide: "The policy/v1beta1 API version of PodDisruptionBudget is no longer served as of v1.25"
- **[required] api_usage** `present` `"policy/v1beta1"`: Application manifests or API clients use the policy/v1beta1 API version for PodDisruptionBudget (confidence high, judge supported)
  - k8s_deprecation_guide: "The policy/v1beta1 API version of PodDisruptionBudget"
  - k8s_deprecation_guide: "PodSecurityPolicy in the policy/v1beta1 API version"
  - k8s_deprecation_guide: "The policy/v1beta1 API version of PodDisruptionBudget is no longer served"
- **[optional] behavior** `present` `"spec.selector: {}"`: PodDisruptionBudgets migrated to policy/v1 have an empty spec.selector (confidence medium, judge partially_supported)
  - k8s_deprecation_guide: "an empty spec.selector ({}) written to a policy/v1 PodDisruptionBudget selects all pods in the namespace"
  - ⚠ The text does not state the release in which this selector change took effect
- **[optional] configuration** `present` `"PodSecurityPolicy admission controller"`: The cluster relies on the PodSecurityPolicy admission controller. (confidence medium, judge supported)
  - k8s_deprecation_guide: "the PodSecurityPolicy admission controller will be removed"
  - ⚠ The text does not state the release in which the PodSecurityPolicy admission controller is removed.

Actions:
- Migrate manifests and API clients to use the policy/v1 API version
- Review empty spec.selector values before migrating PodDisruptionBudgets to policy/v1
- Migrate workloads from PodSecurityPolicy to Pod Security Admission or a 3rd party admission webhook.
- Follow the migration guide: Migrate from PodSecurityPolicy to the Built-In PodSecurity Admission Controller.
- Remove or rewrite policy/v1beta1 PodSecurityPolicy manifests before upgrading.
- Migrate manifests and API clients to use the policy/v1 API version, available since v1.21.
- Verify that existing persisted PodDisruptionBudget objects are accessible through policy/v1 after migration.

### HorizontalPodAutoscaler autoscaling/v2beta2 no longer served

`kubernetes_7b8a1ea444` · critical · confidence high · introduced in 1.26 · fires at upgrade

The autoscaling/v2beta2 API version of HorizontalPodAutoscaler is no longer served as of v1.26, so manifests and clients that use it will fail after the upgrade crosses v1.26.

- **[required] version** `in_range` `{"current_version": "< 1.26", "target_version": ">= 1.26"}`: The upgrade crosses release 1.26, when autoscaling/v2beta2 stops being served. (confidence high, judge supported)
  - k8s_deprecation_guide: "The autoscaling/v2beta2 API version of HorizontalPodAutoscaler is no longer served as of v1.26."
- **[required] api_usage** `present` `"autoscaling/v2beta2"`: The application or deployment uses the autoscaling/v2beta2 API version of HorizontalPodAutoscaler. (confidence high, judge supported)
  - k8s_deprecation_guide: "The autoscaling/v2beta2 API version of HorizontalPodAutoscaler"
  - k8s_deprecation_guide: "Migrate manifests and API clients to use the autoscaling/v2 API version"
- **[optional] api_usage** `present` `"targetAverageUtilization"`: HPA manifests set targetAverageUtilization, which is replaced in the autoscaling/v2 API. (confidence high, judge supported)
  - k8s_deprecation_guide: "targetAverageUtilization is replaced with target.averageUtilization and target.type: Utilization."

Actions:
- Migrate manifests and API clients to use the autoscaling/v2 API version.
- Replace targetAverageUtilization with target.averageUtilization and target.type: Utilization.
- Migrate manifests and API clients to use the autoscaling/v2 API version, available since v1.23.
- Re-apply existing HorizontalPodAutoscaler objects using the autoscaling/v2 API version.

### flowcontrol.apiserver.k8s.io/v1beta1 FlowSchema and PriorityLevelConfiguration no longer served

`kubernetes_997b64cd86` · critical · confidence medium · introduced in 1.26 · fires at upgrade

The flowcontrol.apiserver.k8s.io/v1beta1 API version of FlowSchema and PriorityLevelConfiguration is no longer served as of v1.26. Manifests or API clients that use this version must be migrated to flowcontrol.apiserver.k8s.io/v1beta2.

- **[required] version** `in_range` `{"current_version": "< 1.26", "target_version": ">= 1.26"}`: The upgrade from 1.23 to 1.29 crosses release 1.26, the release in which the v1beta1 API version stops being served. (confidence high, judge supported)
  - k8s_deprecation_guide: "The flowcontrol.apiserver.k8s.io/v1beta1 API version of FlowSchema and PriorityLevelConfiguration is no longer served as of v1.26."
  - k8s_deprecation_guide: "is no longer served as of v1.26"
- **[required] api_usage** `present` `"flowcontrol.apiserver.k8s.io/v1beta1"`: The application or its manifests or API clients use the flowcontrol.apiserver.k8s.io/v1beta1 API version for FlowSchema or PriorityLevelConfiguration. (confidence medium, judge supported)
  - k8s_deprecation_guide: "The flowcontrol.apiserver.k8s.io/v1beta1 API version of FlowSchema and PriorityLevelConfiguration is no longer served as of v1.26."
  - k8s_deprecation_guide: "The flowcontrol.apiserver.k8s.io/v1beta1 API version of FlowSchema and PriorityLevelConfiguration"
  - k8s_deprecation_guide: "The flowcontrol.apiserver.k8s.io/v1beta2 API version of FlowSchema and PriorityLevelConfiguration is no longer served as of v1.29."
  - ⚠ R3: the remediation names flowcontrol.apiserver.k8s.io/v1beta2, which is itself removed in v1.29 (at or before the target 1.29); migrate to flowcontrol.apiserver.k8s.io/v1 instead.

Actions:
- Migrate manifests and API clients to use the flowcontrol.apiserver.k8s.io/v1beta2 API version. [Superseded: flowcontrol.apiserver.k8s.io/v1beta2 is removed in v1.29; use flowcontrol.apiserver.k8s.io/v1.]
- Confirm that existing persisted FlowSchema and PriorityLevelConfiguration objects are accessible through the v1beta2 API version after the upgrade.
- Existing persisted objects remain accessible through the new API, per the source: All existing persisted objects are accessible via the new API.
- Migrate directly to flowcontrol.apiserver.k8s.io/v1 (served at 1.29).

### flowcontrol.apiserver.k8s.io/v1beta2 FlowSchema and PriorityLevelConfiguration removed in v1.29

`kubernetes_b84274af9e` · critical · confidence medium · introduced in 1.29 · fires at upgrade

The flowcontrol.apiserver.k8s.io/v1beta2 API version of FlowSchema and PriorityLevelConfiguration is no longer served as of v1.29. Manifests and API clients that use this version must be migrated to flowcontrol.apiserver.k8s.io/v1 (available since v1.29) or flowcontrol.apiserver.k8s.io/v1beta3 (available since v1.26). Existing persisted objects remain accessible via the new API. If migrating to v1, the PriorityLevelConfiguration spec.limited.assuredConcurrencyShares field is renamed to spec.limited.nominalConcurrencyShares and defaults to 30 only when unspecified; an explicit value of 0 is not changed to 30.

- **[required] api_usage** `present` `"flowcontrol.apiserver.k8s.io/v1beta2"`: The application or deployment uses the flowcontrol.apiserver.k8s.io/v1beta2 API version for FlowSchema or PriorityLevelConfiguration objects. (confidence medium, judge partially_supported)
  - k8s_deprecation_guide: "The flowcontrol.apiserver.k8s.io/v1beta2 API version of FlowSchema and PriorityLevelConfiguration"
  - k8s_deprecation_guide: "The flowcontrol.apiserver.k8s.io/v1beta3 API version of FlowSchema and PriorityLevelConfiguration is no longer served as of v1.32."
  - ⚠ R3: the replacement flowcontrol.apiserver.k8s.io/v1beta3 is removed later, in v1.32 (after target 1.29); prefer flowcontrol.apiserver.k8s.io/v1 to avoid a second migration.
- **[required] version** `in_range` `{"current_version": "< 1.29", "target_version": ">= 1.29"}`: The upgrade crosses release 1.29, the release in which flowcontrol.apiserver.k8s.io/v1beta2 stops being served. (confidence high, judge supported)
  - k8s_deprecation_guide: "is no longer served as of v1.29"
  - k8s_deprecation_guide: "The flowcontrol.apiserver.k8s.io/v1beta2 API version of FlowSchema and PriorityLevelConfiguration is no longer served as of v1.29."
- **[optional] behavior** `present` `"spec.limited.assuredConcurrencyShares"`: Manifests or clients migrated to flowcontrol.apiserver.k8s.io/v1 use PriorityLevelConfiguration spec.limited.assuredConcurrencyShares, which is renamed in that version. (confidence medium, judge partially_supported)
  - k8s_deprecation_guide: "The PriorityLevelConfiguration spec.limited.assuredConcurrencyShares field is renamed to spec.limited.nominalConcurrencyShares"

Actions:
- Migrate manifests and API clients from flowcontrol.apiserver.k8s.io/v1beta2 to flowcontrol.apiserver.k8s.io/v1 (available since v1.29) or flowcontrol.apiserver.k8s.io/v1beta3 (available since v1.26).
- When migrating to v1, rename spec.limited.assuredConcurrencyShares to spec.limited.nominalConcurrencyShares and set an explicit value where the default of 30 matters.
- Confirm that existing persisted FlowSchema and PriorityLevelConfiguration objects are accessible through the new API after the upgrade.
- Migrate manifests and API clients to use the flowcontrol.apiserver.k8s.io/v1 API version, available since v1.29, or the flowcontrol.apiserver.k8s.io/v1beta3 API version, available since v1.26.
- Note that the text states all existing persisted objects are accessible via the new API.

### RuntimeClass node.k8s.io/v1alpha1 API no longer served

`kubernetes_c2e5521796` · critical · confidence medium · introduced in 1.24 · fires at upgrade

The node.k8s.io/v1alpha1 RuntimeClass API is no longer served, so manifests, tooling or clients that use this API version stop working after the upgrade. Migrate to node.k8s.io/v1, which the text states has been available since v1.20.

- **[required] version** `in_range` `{"current_version": "< 1.24", "target_version": ">= 1.24"}`: The change is introduced in release 1.24, and the upgrade from 1.23 to 1.29 crosses that release. (confidence medium, judge partially_supported)
  - k8s_changelog@1.24: "The node.k8s.io/v1alpha1 RuntimeClass API is no longer served"
  - ⚠ The text itself does not state the release number; the 1.24 introduction comes from the assessment header and the CHANGELOG section.
- **[required] api_usage** `present` `"node.k8s.io/v1alpha1"`: The application, manifests or client tooling use the node.k8s.io/v1alpha1 RuntimeClass API. (confidence high, judge supported)
  - k8s_changelog@1.24: "The node.k8s.io/v1alpha1 RuntimeClass API"

Actions:
- Replace node.k8s.io/v1alpha1 references with the node.k8s.io/v1 API version, as the text states: Use the node.k8s.io/v1 API version, available since v1.20
- Check the cluster for RuntimeClass objects and manifests that still use node.k8s.io/v1alpha1 before upgrading.

### Deprecated beta APIs removed in v1.26

`kubernetes_e6d21bce2d` · critical · confidence medium · introduced in 1.26 · fires at upgrade

Deprecated beta APIs scheduled for removal in v1.26 are no longer served, so workloads or tooling that still use them will fail after upgrading past v1.26. The text does not name the specific APIs; see the linked deprecation guide.

- **[required] version** `in_range` `{"current_version": "< 1.26", "target_version": ">= 1.26"}`: The upgrade crosses release v1.26, where deprecated beta APIs scheduled for removal are no longer served. (confidence medium, judge supported)
  - k8s_changelog@1.26: "Deprecated beta APIs scheduled for removal in v1.26 are no longer served."
  - k8s_changelog@1.25: "Deprecated beta APIs scheduled for removal in 1.25 are no longer served."
  - ⚠ History: in 1.25, 'Deprecated beta APIs no longer served' applied to the same symbol (deprecated beta apis); superseded by the 1.26 change (R2).
- **[required] api_usage** `present` `"deprecated beta apiVersion scheduled for removal in v1.26"`: The application, its manifests, or its clients use a deprecated beta API that is scheduled for removal in v1.26. (confidence medium, judge supported)
  - k8s_changelog@1.26: "Deprecated beta APIs scheduled for removal in v1.26 are no longer served."
  - ⚠ The text does not name which beta APIs are removed; the linked deprecation guide would identify them.

Actions:
- Identify beta APIs in use (manifests, Helm charts, controllers, clients) and check them against the v1.26 deprecation guide at https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-26.
- Migrate affected resources to the GA or replacement API versions named in the deprecation guide before upgrading past v1.26.

### RuntimeClass node.k8s.io/v1beta1 removed

`kubernetes_f51a904d3d` · critical · confidence high · introduced in 1.25 · fires at upgrade

RuntimeClass in the node.k8s.io/v1beta1 API version is no longer served as of v1.25. Manifests and API clients that use this version must migrate to node.k8s.io/v1, available since v1.20. All existing persisted objects are accessible via the new API.

- **[required] version** `in_range` `{"current_version": "< 1.25", "target_version": ">= 1.25"}`: The upgrade crosses release 1.25, where RuntimeClass in node.k8s.io/v1beta1 stops being served. (confidence high, judge supported)
  - k8s_deprecation_guide: "RuntimeClass in the node.k8s.io/v1beta1 API version is no longer served as of v1.25."
  - k8s_deprecation_guide: "RuntimeClass in the node.k8s.io/v1beta1 API version is no longer served as of v1.25"
- **[required] api_usage** `present` `"node.k8s.io/v1beta1 RuntimeClass"`: The application, its manifests, or its API clients use RuntimeClass through the node.k8s.io/v1beta1 API version. (confidence high, judge supported)
  - k8s_deprecation_guide: "RuntimeClass in the node.k8s.io/v1beta1 API version"
  - k8s_deprecation_guide: "RuntimeClass in the node.k8s.io/v1beta1 API version is no longer served"

Actions:
- Migrate manifests and API clients to use the node.k8s.io/v1 API version, available since v1.20.
- Search manifests, Helm charts, and client code for node.k8s.io/v1beta1 and update references to node.k8s.io/v1 before upgrading.
- Check that no RuntimeClass manifests or client code still reference node.k8s.io/v1beta1 before upgrading past v1.25.
- Existing persisted objects are accessible via the new API, so no data conversion is stated as required.

### events.k8s.io/v1beta1 Event API removed

`kubernetes_fc16f3bccf` · critical · confidence medium · introduced in 1.25 · fires at upgrade

The events.k8s.io/v1beta1 API version of Event is no longer served as of v1.25. Manifests and API clients that use it will stop working when the upgrade crosses release 1.25.

- **[required] version** `in_range` `{"current_version": "< 1.25", "target_version": ">= 1.25"}`: The upgrade crosses release 1.25 (source version is below 1.25 and target version is 1.29). (confidence medium, judge partially_supported)
  - k8s_deprecation_guide: "The events.k8s.io/v1beta1 API version of Event is no longer served as of v1.25."
  - k8s_deprecation_guide: "is no longer served as of v1.25"
- **[required] api_usage** `present` `"events.k8s.io/v1beta1"`: The application or deployment uses the events.k8s.io/v1beta1 API version of Event. (confidence medium, judge supported)
  - k8s_deprecation_guide: "The events.k8s.io/v1beta1 API version of Event is no longer served as of v1.25."
  - k8s_deprecation_guide: "Migrate manifests and API clients to use the events.k8s.io/v1 API version"
  - k8s_deprecation_guide: "The events.k8s.io/v1beta1 API version of Event is no longer served"
  - ⚠ The text does not state how the removed version is referenced in manifests or client code, so the search must cover both.
- **[optional] behavior** `present` `"involvedObject"`: The application or deployment creates or reads Events that use involvedObject, which is renamed to regarding in events.k8s.io/v1. (confidence medium, judge partially_supported)
  - k8s_deprecation_guide: "involvedObject is renamed to regarding"

Actions:
- Migrate manifests and API clients to use the events.k8s.io/v1 API version, available since v1.19.
- Rename involvedObject to regarding in Event usage.
- Set action, reason, reportingController, and reportingInstance when creating new events.k8s.io/v1 Events.
- Use eventTime instead of firstTimestamp, series.lastObservedTime instead of lastTimestamp, series.count instead of count, reportingController instead of source.component, and reportingInstance instead of source.host.
- Note that in events.k8s.io/v1 type is limited to Normal and Warning, involvedObject is renamed to regarding, and action, reason, reportingController, and reportingInstance are required when creating new events.
- Use eventTime instead of firstTimestamp, series.lastObservedTime instead of lastTimestamp, series.count instead of count, reportingController instead of source.component, and reportingInstance instead of source.host, since the old fields are not permitted in new events.k8s.io/v1 Events.
- All existing persisted objects are accessible via the new API.
- Migrate manifests and API clients to use the events.k8s.io/v1 API version.
- Existing persisted objects remain accessible through the events.k8s.io/v1 API after migration.

### client-go credential plugin relying on client.authentication.k8s.io/v1alpha1 ExecCredential

`kubernetes_0089fb8601` · high · confidence high · introduced in 1.24 · fires at upgrade

The client.authentication.k8s.io/v1alpha1 ExecCredential API has been removed. A client-go credential plugin that relies on the v1alpha1 API is affected and must migrate to the v1 API.

- **[required] version** `in_range` `{"current_version": "< 1.24", "target_version": ">= 1.24"}`: The upgrade crosses release 1.24, the release in which the client.authentication.k8s.io/v1alpha1 ExecCredential removal was introduced. (confidence high)
  - k8s_changelog@1.24: "The client.authentication.k8s.io/v1alpha1 ExecCredential has been removed."
- **[required] api_usage** `present` `"client-go credential plugin relying on client.authentication.k8s.io/v1alpha1"`: The application or deployment uses a client-go credential plugin that relies on the client.authentication.k8s.io/v1alpha1 API. (confidence high, judge supported)
  - k8s_changelog@1.24: "If you are using a client-go credential plugin that relies on the v1alpha1 API"

Actions:
- Contact the distributor of the client-go credential plugin for instructions on how to migrate to the v1 API.
- Confirm that the credential plugin and kubeconfig no longer reference client.authentication.k8s.io/v1alpha1 before upgrading.

### Creating new CronJobs with TZ or CRON_TZ in .spec.schedule

`kubernetes_1a5432e398` · high · confidence high · introduced in 1.29 · fires at first_use

Creation of new CronJob objects whose .spec.schedule contains TZ or CRON_TZ is disallowed in 1.29. Manifests or tooling that create such CronJobs will fail when creating them on a 1.29 cluster.

- **[required] version** `in_range` `{"current_version": "< 1.29", "target_version": ">= 1.29"}`: The upgrade crosses release 1.29, where creation of CronJobs with TZ or CRON_TZ in .spec.schedule becomes disallowed. (confidence high, judge supported)
  - k8s_changelog@1.29: "Creation of new CronJob objects containing TZ or CRON_TZ in .spec.schedule, accidentally enabled in v1.22, is now disallowed."
- **[required] api_usage** `contains` `"TZ or CRON_TZ in .spec.schedule"`: The application creates or applies CronJob objects whose .spec.schedule contains TZ or CRON_TZ. (confidence high, judge supported)
  - k8s_changelog@1.29: "Creation of new CronJob objects containing TZ or CRON_TZ in .spec.schedule"
- **[disqualifying] configuration** `present` `".spec.timeZone"`: The CronJob uses the .spec.timeZone field instead of a TZ or CRON_TZ prefix in .spec.schedule. (confidence high, judge supported)
  - k8s_changelog@1.29: "Use the .spec.timeZone field instead"
- **[uncertain] configuration** `greater_than` `"1.24"`: The .spec.timeZone replacement is supported only on clusters in v1.25 or later with default configurations. (confidence low, judge partially_supported)
  - k8s_changelog@1.29: "supported in v1.25+ clusters in default configurations"
  - ⚠ The text does not state what happens to .spec.timeZone on clusters with non-default configurations.

Actions:
- Replace TZ or CRON_TZ prefixes in .spec.schedule with the .spec.timeZone field.
- Search manifests, Helm charts, and GitOps repositories for CronJobs that set TZ or CRON_TZ before upgrading to 1.29.
- Confirm the target cluster uses a default configuration that supports .spec.timeZone.

### kube-controller-manager removed flags deleting-pods-qps, deleting-pods-burst, register-retry-count

`kubernetes_1f10d2a281` · high · confidence medium · introduced in 1.25 · fires at upgrade

The kube-controller-manager flags deleting-pods-qps, deleting-pods-burst, and register-retry-count were removed in 1.25. A deployment that still sets these flags on kube-controller-manager is affected at upgrade. The text does not state what happens when a removed flag is still passed.

- **[required] version** `in_range` `{"current_version": "< 1.25", "target_version": ">= 1.25"}`: The upgrade starts from a version below 1.25 and so crosses release 1.25, where the flags were removed. (confidence medium, judge supported)
  - k8s_changelog@1.25: "Kube-controller-manager: Removed flags deleting-pods-qps, deleting-pods-burst, and register-retry-count."
  - ⚠ The text names release 1.25 as the release of the change but does not restate the from-version boundary; the boundary is taken from the stated change release.
- **[required] configuration** `present` `"deleting-pods-qps"`: The kube-controller-manager configuration sets one of the removed flags deleting-pods-qps, deleting-pods-burst, or register-retry-count. (confidence medium, judge supported)
  - k8s_changelog@1.25: "Removed flags deleting-pods-qps, deleting-pods-burst, and register-retry-count."
  - ⚠ The text does not state whether a removed flag causes kube-controller-manager to fail on startup or is silently ignored.

Actions:
- Remove the deleting-pods-qps, deleting-pods-burst, and register-retry-count flags from the kube-controller-manager configuration before upgrading past 1.25.
- The text names no replacement for these flags.

### kubectl version --short flag removed

`kubernetes_262d87f013` · high · confidence medium · introduced in 1.28 · fires at first_use

The --short flag was removed from kubectl version entirely. Scripts or pipelines that invoke kubectl version --short will no longer work after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 1.28", "target_version": ">= 1.28"}`: The upgrade crosses release 1.28, which introduced the removal. (confidence medium, judge partially_supported)
  - k8s_changelog@1.28: "Changed kubectl version default output to be identical to what kubectl version --short printed"
- **[required] api_usage** `present` `"kubectl version --short"`: The application or deployment invokes kubectl version with the --short flag. (confidence high, judge supported)
  - k8s_changelog@1.28: "removed --short flag entirely"

Actions:
- Remove the --short flag from kubectl version invocations in scripts and pipelines.
- If the short output format is needed, parse the default kubectl version output instead, since it now matches what --short printed.

### kubelet version skew before kube-apiserver upgrade

`kubernetes_3a107f9c1e` · high · confidence medium · introduced in * · fires at upgrade

Before the kube-apiserver upgrade, kubelets on all nodes must be at one of the two minor versions below the target release. Kubelets outside this window are not in a supported skew state for the new kube-apiserver, so the upgrade can break node communication unless the kubelets are upgraded first.

- **[required] version** `in_range` `{"applies_to": "every release hop on the upgrade path"}`: The change applies to the upgrade target release, with kubelet instances required at currentVersionAddMinor -1 or currentVersionAddMinor -2 relative to that release. (confidence medium, judge partially_supported)
  - k8s_skew: "kubelet instances on all nodes are at version"
  - ⚠ The text uses skew template placeholders and does not state the resolved version numbers; the mapping to 1.27 and 1.28 for a 1.29 target is not stated in the text.
- **[required] deployment** `in_range` `"{{< skew currentVersionAddMinor -2 >}} to {{< skew currentVersionAddMinor -1 >}}"`: Kubelet instances on all nodes run a minor version within the allowed skew window of the target release. (confidence medium, judge supported)
  - k8s_skew: "kubelet instances on all nodes are at version"
  - k8s_skew: "{{< skew currentVersionAddMinor -1 >}} or {{< skew currentVersionAddMinor -2 >}}"
  - ⚠ The text does not state the current kubelet versions of any specific cluster; this must be checked against the deployment.

Actions:
- Check the kubelet version on every node before upgrading kube-apiserver.
- Upgrade kubelets on nodes outside the allowed skew window so they fall within the two-minor-version window before the kube-apiserver upgrade.
- Follow the project policy of not skipping minor versions when upgrading kube-apiserver, as stated in the note in the parent context.

### single-instance kube-apiserver skips minor version (1.23 to 1.29)

`kubernetes_43d8c248a4` · high · confidence medium · introduced in * · fires at upgrade

In a single-instance cluster the existing kube-apiserver must be at the version one minor below the target before upgrading to the target. The project policy requires kube-apiserver not to skip minor versions, even in single-instance clusters. Upgrading a 1.23 single-instance kube-apiserver directly to 1.29 skips 1.24 through 1.28 and is not a supported upgrade path under this policy.

- **[required] version** `in_range` `{"applies_to": "every release hop on the upgrade path"}`: The upgrade targets release 1.29, the currentVersion of this section. (confidence medium)
  - k8s_skew: "Upgrade kube-apiserver to {{< skew currentVersion >}}"
  - k8s_skew: "this ensures maximum skew of 1 minor version between the oldest and newest kube-apiserver instance"
  - k8s_skew: "Project policies for API deprecation and API change guidelines require kube-apiserver to not skip minor versions when upgrading, even in single-instance clusters."
  - k8s_skew: "The kube-apiserver instances kube-proxy communicates with are at {{< skew currentVersion >}}"
  - k8s_skew: "the newest and oldest kube-apiserver instances must be within one minor version"
  - k8s_skew: "The kube-apiserver instances these components communicate with are at {{< skew currentVersion >}}"
  - k8s_skew: "The kube-apiserver instances the kubelet communicates with are at {{< skew currentVersion >}}"
  - ⚠ The text gives only relative skew macros; the concrete version 1.29 is taken from the assessed upgrade.
  - ⚠ The text uses unresolved template placeholders for version numbers and does not state the concrete release number that the change was introduced in; the release number comes from the assessment request only.
  - ⚠ The release marker is an unresolved placeholder and the package metadata gives no version numbers, so the text does not confirm which release the rule applies to.
  - ⚠ The text uses the placeholder {{< skew currentVersion >}} and does not state the literal version number; the value 1.29 comes from the upgrade being assessed.
  - ⚠ The release number for this change is not stated in the item; the release marker is '*'.
  - ⚠ The item does not state whether the constraint applies to the 1.23 to 1.29 upgrade path.
  - ⚠ The text uses a template placeholder for the version and does not state 1.29 literally.
  - ⚠ Release * is unspecified in the text.
  - ⚠ The text gives the version only as the template variable {{< skew currentVersion >}}, not as a number.
- **[required] deployment** `equals` `"single-instance"`: The cluster is a single-instance cluster with one kube-apiserver instance. (confidence medium, judge supported)
  - k8s_skew: "In a single-instance cluster, the existing kube-apiserver instance is"
  - k8s_skew: "In an HA cluster, all kube-apiserver instances are at"
  - k8s_skew: "Upgrade kube-apiserver to"
  - k8s_skew: "the existing kube-apiserver instance is"
  - k8s_skew: "The kube-apiserver instances kube-proxy communicates with are at {{< skew currentVersion >}}"
  - k8s_skew: "In highly-available (HA) clusters"
  - k8s_skew: "in HA clusters in which these control plane components can communicate with any kube-apiserver instance in the cluster, all kube-apiserver instances must be upgraded before upgrading these components"
  - k8s_skew: "The kube-apiserver instances the kubelet communicates with are at {{< skew currentVersion >}}"
  - ⚠ The text uses unresolved version shortcodes and does not state numeric versions, so the 1.23 and 1.29 values come from the assessment header rather than the text.
  - ⚠ The text does not state how the apiserver version is verified; the kubectl command below is a suggested check, not a documented one.
- **[required] deployment** `not_equals` `"1.28"`: The existing kube-apiserver instance is not at 1.28, the version one minor below 1.29. (confidence medium)
  - k8s_skew: "the existing kube-apiserver instance is {{< skew currentVersionAddMinor -1 >}}"
  - ⚠ The text states the required prerequisite version through a skew macro; the value 1.28 is derived from the target 1.29 by subtracting one minor version.
  - ⚠ The text states the policy against skipping minor versions but does not describe the specific failure that occurs when the policy is violated.
- **[required] runtime** `in_range` `"{{< skew currentVersionAddMinor -1 >}} or {{< skew currentVersion >}}"`: All kube-apiserver instances are running at the version range required by the skew policy before the upgrade. (confidence medium, judge partially_supported)
  - k8s_skew: "all kube-apiserver instances are at"
  - ⚠ The text gives the required range only as unresolved template expressions; the text does not state the concrete versions for the 1.23 to 1.29 upgrade, so the downstream engine must derive them.
- **[optional] behavior** `equals` `"3"`: Kube-proxy instances are persistently three minor versions behind kube-apiserver. (confidence high, judge supported)
  - k8s_skew: "kube-proxy instances that are persistently three minor versions behind kube-apiserver"

Actions:
- Upgrade the single kube-apiserver instance to 1.28 before upgrading it to 1.29, as the Version Skew Policy requires not skipping minor versions.
- Confirm the current kube-apiserver version in the cluster before starting the upgrade.
- Check the version of every kube-apiserver instance in the HA cluster before starting the upgrade.
- Upgrade lagging kube-apiserver instances so that all instances are within the range the skew policy requires before proceeding.
- Upgrade kube-apiserver one minor version at a time, following the documented upgrade order, instead of jumping from 1.23 to 1.29.
- Confirm the current kube-apiserver version on every control plane instance before planning the upgrade path.
- Upgrade the kube-apiserver instances that kube-proxy communicates with to 1.29 before upgrading kube-proxy.
- Optionally upgrade kube-proxy instances to 1.29, or leave them at the earlier supported minor versions; do not let kube-proxy stay three minor versions behind kube-apiserver.
- Check the versions of all kube-apiserver instances before and during the upgrade.
- Keep the newest and oldest kube-apiserver instances within one minor version at every step of the upgrade.
- Upgrade all kube-apiserver instances to the target version before upgrading kube-controller-manager, kube-scheduler and cloud-controller-manager.
- Verify the version of every kube-apiserver instance before starting the upgrade of the other control-plane components.
- Upgrade the kube-apiserver instances to the target version before upgrading any kubelet.
- Before performing a minor version kubelet upgrade, drain pods from that node.

### gcp-azure-auth-plugins-removed

`kubernetes_471b45948b` · high · confidence medium · introduced in 1.26 · fires at upgrade

The gcp and azure auth plugins have been removed from client-go and kubectl. Code or configuration that depends on these plugins will not work after the upgrade. The text points to kubelogin and Kubectl Auth Changes in GKE as cloud-specific replacements.

- **[required] version** `in_range` `{"current_version": "< 1.26", "target_version": ">= 1.26"}`: The upgrade from 1.23 crosses release 1.26, the release in which the gcp and azure auth plugins were removed. (confidence medium, judge partially_supported)
  - k8s_changelog@1.26: "The gcp and azure auth plugins have been removed from client-go and kubectl"
  - k8s_changelog@1.25: "The gcp and azure auth plugins have been removed from client-go and kubectl."
  - ⚠ History: in 1.25, 'Removed gcp and azure auth plugins in client-go and kubectl' applied to the same symbol (gcp and azure auth plugins); superseded by the 1.26 change (R2).
- **[required] configuration** `present` `"gcp or azure auth plugin"`: The application or deployment uses the gcp or azure auth plugin through client-go or kubectl. (confidence medium, judge supported)
  - k8s_changelog@1.26: "The gcp and azure auth plugins have been removed from client-go and kubectl"
  - ⚠ The text does not state which kubeconfig field or setting selects these auth plugins, so the exact literal to search for is not specified.

Actions:
- Identify clients, kubeconfig files, and scripts that use the gcp or azure auth plugins.
- Migrate to kubelogin as the replacement for these plugins, as described in the referenced docs.
- Review Kubectl Auth Changes in GKE for the GKE-specific replacement steps.

### In-tree OpenStack cloud provider removed

`kubernetes_4da15810ad` · high · confidence medium · introduced in 1.26 · fires at upgrade

The in-tree cloud provider for OpenStack was removed in v1.26. Clusters that use it must move to the external cloud provider from cloud-provider-openstack before upgrading past 1.26.

- **[required] version** `in_range` `{"current_version": "< 1.26", "target_version": ">= 1.26"}`: The upgrade crosses release 1.26 (from a version below 1.26 to 1.29). (confidence medium, judge partially_supported)
  - k8s_changelog@1.26: "The in-tree cloud provider for OpenStack (and the cinder volume provider) has been removed."
- **[required] deployment** `present` `"in-tree cloud provider for OpenStack"`: The cluster uses the in-tree cloud provider for OpenStack. (confidence medium, judge supported)
  - k8s_changelog@1.26: "The in-tree cloud provider for OpenStack"
  - ⚠ The text does not name the configuration setting or flag that enables the in-tree OpenStack cloud provider, so the check must be made from the cluster's own configuration.

Actions:
- Migrate to the external cloud provider from cloud-provider-openstack before upgrading to v1.26 or later.

### kubeadm config files still reference the dockershim socket

`kubernetes_5b5d9d0ac5` · high · confidence medium · introduced in 1.24 · fires at upgrade

Kubeadm configuration files on disk that include the dockershim socket break when upgrading across 1.24, unless the cluster still runs kubelet below 1.24 with kubeadm 1.24 or later.

- **[required] version** `in_range` `{"current_version": "< 1.24", "target_version": ">= 1.24"}`: The upgrade crosses release 1.24, where kubeadm defaults the CRI socket to containerd instead of Docker. (confidence medium, judge partially_supported)
  - k8s_changelog@1.24: "Kubeadm: default the kubeadm configuration to the containerd socket"
- **[required] configuration** `contains` `"dockershim socket"`: A kubeadm configuration file on disk includes the dockershim socket. (confidence medium, judge supported)
  - k8s_changelog@1.24: "Make sure you update any kubeadm configuration files on disk, to not include the dockershim socket"
  - ⚠ The text does not give a literal socket path string for the dockershim socket.
- **[disqualifying] version** `less_than` `"kubelet 1.24"`: The cluster still runs kubelet below 1.24 with kubeadm 1.24 or later, in which case the dockershim socket is still needed. (confidence high, judge supported)
  - k8s_changelog@1.24: "unless you are still using kubelet version < 1.24 with kubeadm >= 1.24"

Actions:
- Edit kubeadm configuration files on disk to remove the dockershim socket and use the containerd socket (unix:///var/run/containerd/containerd.sock on Unix, npipe:////./pipe/containerd-containerd on Windows).
- Set nodeRegistration.criSocket explicitly to the containerd socket where kubeadm configuration is used.

### HorizontalPodAutoscaler targetAverageUtilization field replaced

`kubernetes_61e40b3bda` · high · confidence medium · introduced in 1.26 · fires at upgrade

The targetAverageUtilization field is replaced with target.averageUtilization and target.type: Utilization. Manifests and API clients must migrate to the autoscaling/v2 API version.

- **[required] version** `in_range` `{"current_version": "< 1.26", "target_version": ">= 1.26"}`: The upgrade crosses release 1.26, the release in which the autoscaling/v2beta2 HorizontalPodAutoscaler API stops being served. (confidence medium, judge partially_supported)
  - k8s_deprecation_guide: "The autoscaling/v2beta2 API version of HorizontalPodAutoscaler is no longer served as of v1.26."
- **[required] api_usage** `present` `"targetAverageUtilization"`: The application or deployment uses targetAverageUtilization in HorizontalPodAutoscaler manifests or API clients. (confidence high, judge supported)
  - k8s_deprecation_guide: "targetAverageUtilization is replaced with target.averageUtilization"

Actions:
- Migrate manifests and API clients to use the autoscaling/v2 API version.
- Replace targetAverageUtilization with target.averageUtilization and target.type: Utilization.

### kube-scheduler --lock-object-name flag removed

`kubernetes_6a9aabc985` · high · confidence medium · introduced in 1.28 · fires at upgrade

The deprecated kube-scheduler flag --lock-object-name was removed in 1.28. Deployments that still pass this flag to kube-scheduler are affected at upgrade. The text names --leader-elect-resource-name or ComponentConfig as replacements.

- **[required] version** `in_range` `{"current_version": "< 1.28", "target_version": ">= 1.28"}`: The upgrade crosses release 1.28, in which the kube-scheduler flag --lock-object-name was removed. (confidence high, judge supported)
  - k8s_changelog@1.28: "The deprecated flag --lock-object-namespace and --lock-object-name have been removed from kube-scheduler."
- **[required] configuration** `present` `"--lock-object-name"`: The kube-scheduler is started with the flag --lock-object-name. (confidence medium, judge supported)
  - k8s_changelog@1.28: "The deprecated flag --lock-object-namespace and --lock-object-name have been removed from kube-scheduler."
  - ⚠ The text does not state what kube-scheduler does when a removed flag is passed.

Actions:
- Remove --lock-object-name from kube-scheduler startup flags or manifests.
- Use --leader-elect-resource-name instead, or configure the parameter through ComponentConfig.

### HPA targetAverageUtilization replaced

`kubernetes_71ae8992a8` · high · confidence medium · introduced in 1.26 · fires at upgrade

The targetAverageUtilization field is replaced with target.averageUtilization and target.type: Utilization, so manifests that set targetAverageUtilization need their field structure changed when moving to autoscaling/v2.

- **[required] version** `in_range` `{"current_version": "< 1.26", "target_version": ">= 1.26"}`: The upgrade from 1.23 to 1.29 crosses release 1.26, which removes serving of autoscaling/v2beta2 HorizontalPodAutoscaler. (confidence medium, judge supported)
  - k8s_deprecation_guide: "The autoscaling/v2beta2 API version of HorizontalPodAutoscaler is no longer served as of v1.26."
  - k8s_deprecation_guide: "targetAverageUtilization is replaced with target.averageUtilization and target.type: Utilization"
  - ⚠ History: in 1.25, 'HorizontalPodAutoscaler targetAverageUtilization field replaced' applied to the same symbol (targetaverageutilization); superseded by the 1.26 change (R2).
- **[required] configuration** `present` `"targetAverageUtilization"`: The application or deployment sets the targetAverageUtilization field in HorizontalPodAutoscaler manifests. (confidence high, judge supported)
  - k8s_deprecation_guide: "targetAverageUtilization is replaced with target.averageUtilization and target.type: Utilization."

Actions:
- Replace targetAverageUtilization with target.averageUtilization and set target.type to Utilization in HorizontalPodAutoscaler manifests.
- See the Autoscaling on multiple metrics and custom metrics documentation referenced by the source.

### GlusterFS in-tree storage driver removed in v1.26

`kubernetes_8b7a9adfd6` · high · confidence medium · introduced in 1.26 · fires at upgrade

The GlusterFS in-tree storage driver, deprecated in 1.25, is removed entirely in v1.26. Volumes using it must be migrated to an alternate storage solution before upgrading to v1.26.

- **[required] version** `in_range` `{"current_version": "< 1.26", "target_version": ">= 1.26"}`: The upgrade crosses release v1.26, where the GlusterFS in-tree storage driver is removed. (confidence high, judge supported)
  - k8s_changelog@1.26: "is now removed entirely in v1.26"
- **[required] configuration** `present` `"GlusterFS in-tree storage driver volumes"`: The cluster has volumes that use the GlusterFS in-tree storage driver. (confidence medium, judge partially_supported)
  - k8s_changelog@1.26: "GlusterFS in-tree storage driver which was deprecated"
  - ⚠ The text does not name the specific resource kinds or manifest fields that reference the driver.

Actions:
- Identify volumes that use the GlusterFS in-tree storage driver before upgrading.
- Migrate those volumes to an alternate storage solution before upgrading to v1.26.
- The text does not name a specific replacement storage solution.

### Scheduler EnqueueExtension EventsToRegister return type change

`kubernetes_9ee51f7127` · high · confidence medium · introduced in 1.28 · fires at upgrade

Custom scheduler plugins whose EventsToRegister in EnqueueExtension returns ClusterEvent must change to ClusterEventWithHint, a breaking change in the scheduling framework.

- **[required] version** `in_range` `{"current_version": "< 1.28", "target_version": ">= 1.28"}`: Upgrade crosses release 1.28, the release in which the EventsToRegister return type change was introduced (confidence high, judge supported)
  - k8s_changelog@1.28: "The EventsToRegister in EnqueueExtension changed the return value from ClusterEvent to ClusterEventWithHint."
- **[required] api_usage** `present` `"EventsToRegister"`: Custom scheduler plugin implements EnqueueExtension EventsToRegister returning ClusterEvent (confidence medium, judge partially_supported)
  - k8s_changelog@1.28: "Action required for the custom scheduler plugin developers."
  - ⚠ The text does not state which return type existing plugins use in 1.23; check plugin source.
- **[disqualifying] behavior** `equals` `"nil QueueingHintFn"`: Plugin registers ClusterEventWithHint with a nil QueueingHintFn (confidence medium, judge partially_supported)
  - k8s_changelog@1.28: "For backward compatibility, nil QueueingHintFn is treated as always returning QueueAfterBackoff."

Actions:
- Change EventsToRegister to return ClusterEventWithHint instead of ClusterEvent.
- Register an appropriate QueueingHintFn for each ClusterEventWithHint to reduce useless retries.
- To keep existing behavior, register ClusterEventWithHint with no QueueingHintFn.

### In-tree EBS storage plugin removed

`kubernetes_a1ff166364` · high · confidence medium · introduced in 1.27 · fires at upgrade

The EBS storage plugin has been removed in 1.27, so storage that depends on it cannot use it after crossing this release and must move to the CSI driver.

- **[required] version** `in_range` `{"current_version": "< 1.27", "target_version": ">= 1.27"}`: The upgrade crosses release 1.27, in which the EBS storage plugin was removed. (confidence high, judge supported)
  - k8s_changelog@1.27: "The in-tree cloud provider for AWS (and the EBS storage plugin) has now been removed."
- **[required] configuration** `present` `"EBS storage plugin"`: The cluster uses the EBS storage plugin. (confidence medium, judge partially_supported)
  - k8s_changelog@1.27: "EBS storage plugin"
  - ⚠ The text does not name the specific in-tree volume plugin identifier used in cluster configuration.

Actions:
- Use the CSI driver from https://github.com/kubernetes/cloud-provider-aws instead of the EBS storage plugin.

### PodSecurityPolicy admission plugin removed in 1.25

`kubernetes_ab919afc13` · high · confidence high · introduced in 1.25 · fires at upgrade

The beta PodSecurityPolicy admission plugin, deprecated since 1.21, is removed in 1.25. Clusters that rely on it must migrate to the built-in PodSecurity admission plugin (or another third-party policy webhook) before upgrading to v1.25.

- **[required] version** `in_range` `{"current_version": "< 1.25", "target_version": ">= 1.25"}`: The upgrade crosses Kubernetes release 1.25 (from 1.23 to 1.29). (confidence high)
  - k8s_changelog@1.25: "The beta PodSecurityPolicy admission plugin, deprecated since 1.21, is removed."
- **[uncertain] configuration** `present` `"PodSecurityPolicy"`: The cluster uses the PodSecurityPolicy admission plugin. (confidence low, judge not_supported)
  - k8s_changelog@1.25: "The beta PodSecurityPolicy admission plugin"
  - ⚠ The text does not state how the plugin is enabled or configured in a cluster.
  - ⚠ Judge: evidence does not support this claim. The quote only names the beta PodSecurityPolicy admission plugin in the v1.25.0 changelog. It does not state that clusters using this plugin are affected, that the plugin is removed or deprecated, or anything else establishing that a cluster meeting the condition is impacted.

Actions:
- Follow the instructions at https://kubernetes.io/docs/tasks/configure-pod-container/migrate-from-psp/ to migrate to the built-in PodSecurity admission plugin (or to another third-party policy webhook) prior to upgrading to v1.25.

### Removed in-tree volume plugin: quobyte

`kubernetes_b8ccd4eaaa` · high · confidence high · introduced in 1.25 · fires at upgrade

The in-tree quobyte volume plugin support has been completely removed from Kubernetes in 1.25. Workloads or PersistentVolumes that depend on quobyte in-tree volumes cannot rely on it after upgrading past 1.25.

- **[required] version** `in_range` `{"current_version": "< 1.25", "target_version": ">= 1.25"}`: The upgrade crosses release 1.25, where the in-tree quobyte volume plugin support was removed. (confidence high, judge supported)
  - k8s_changelog@1.25: "The intree volume plugin quobyte support has been completely removed from Kubernetes."
- **[required] api_usage** `present` `"quobyte"`: The cluster uses in-tree quobyte volumes. (confidence high, judge supported)
  - k8s_changelog@1.25: "The intree volume plugin quobyte support has been completely removed from Kubernetes."

Actions:
- Search manifests and PersistentVolumes for quobyte usage before upgrading.
- Migrate quobyte volumes to a supported storage option before upgrading past 1.25.

### Removed networking alpha API ClusterCIDR

`kubernetes_baa4052480` · high · confidence high · introduced in 1.29 · fires at upgrade

The networking alpha API ClusterCIDR was removed in release 1.29. Applications or tooling that use this API may break when the cluster is upgraded to 1.29 or later.

- **[required] version** `in_range` `{"current_version": "< 1.29", "target_version": ">= 1.29"}`: The upgrade crosses release 1.29, in which the ClusterCIDR networking alpha API was removed. (confidence high, judge supported)
  - k8s_changelog@1.29: "Removed the networking alpha API ClusterCIDR"
- **[required] api_usage** `present` `"ClusterCIDR"`: The application uses the ClusterCIDR API. (confidence high, judge supported)
  - k8s_changelog@1.29: "Removed the networking alpha API ClusterCIDR"
- **[uncertain] configuration** `unknown` `""`: The cluster serves the ClusterCIDR alpha API before the upgrade. (confidence low, judge partially_supported)
  - k8s_changelog@1.29: "networking alpha API"
  - ⚠ The text does not state whether the ClusterCIDR alpha API was enabled or served by default in release 1.23.

Actions:
- Search manifests, Helm charts, controllers, and tooling for ClusterCIDR usage before upgrading to 1.29.
- Remove or migrate any ClusterCIDR usage before upgrading, since the text does not name a replacement API.

### In-tree cinder volume provider removed

`kubernetes_bf90a0c464` · high · confidence medium · introduced in 1.26 · fires at upgrade

The cinder volume provider was removed together with the in-tree OpenStack cloud provider in v1.26. Volumes that depend on it must move to the CSI driver from cloud-provider-openstack.

- **[required] version** `in_range` `{"current_version": "< 1.26", "target_version": ">= 1.26"}`: The upgrade crosses release 1.26 (from a version below 1.26 to 1.29). (confidence medium, judge partially_supported)
  - k8s_changelog@1.26: "The in-tree cloud provider for OpenStack (and the cinder volume provider) has been removed."
- **[required] deployment** `present` `"cinder volume provider"`: The cluster uses the cinder volume provider for storage. (confidence medium, judge partially_supported)
  - k8s_changelog@1.26: "the cinder volume provider"
  - ⚠ The text does not name the in-tree volume plugin identifier or the storage class settings that use the cinder volume provider, so the check must be made from the cluster's own configuration.

Actions:
- Use the CSI driver from cloud-provider-openstack in place of the in-tree cinder volume provider before upgrading to v1.26 or later.

### Removed API server flag --service-account-api-audiences

`kubernetes_c1fd329e73` · high · confidence medium · introduced in 1.25 · fires at upgrade

The API server's deprecated --service-account-api-audiences flag was removed in 1.25. Deployments that still pass this flag to the API server are affected at upgrade. Replace it with --api-audiences. The text does not state what happens when the removed flag is still passed.

- **[required] version** `in_range` `{"current_version": "< 1.25", "target_version": ">= 1.25"}`: The upgrade crosses release 1.25, where the --service-account-api-audiences flag was removed. (confidence high, judge supported)
  - k8s_changelog@1.25: "API server's deprecated --service-account-api-audiences flag was removed."
- **[required] configuration** `present` `"--service-account-api-audiences"`: The API server configuration or startup command passes the --service-account-api-audiences flag. (confidence medium, judge supported)
  - k8s_changelog@1.25: "deprecated --service-account-api-audiences flag was removed"
  - ⚠ The text does not state the consequence of passing the removed flag to the API server.

Actions:
- Remove --service-account-api-audiences from the API server configuration.
- Use --api-audiences instead, as the changelog states.

### Removed in-tree volume plugin: flocker

`kubernetes_c48826c6b8` · high · confidence high · introduced in 1.25 · fires at upgrade

The in-tree flocker volume plugin support was completely removed from Kubernetes in 1.25. Workloads or PersistentVolumes that depend on flocker in-tree volumes cannot rely on it after upgrading past 1.25.

- **[required] version** `in_range` `{"current_version": "< 1.25", "target_version": ">= 1.25"}`: The upgrade crosses release 1.25, where the in-tree flocker volume plugin support was removed. (confidence high, judge supported)
  - k8s_changelog@1.25: "The intree volume plugin flocker support was completely removed from Kubernetes."
- **[required] api_usage** `present` `"flocker"`: The cluster uses in-tree flocker volumes. (confidence high, judge supported)
  - k8s_changelog@1.25: "The intree volume plugin flocker support was completely removed from Kubernetes."

Actions:
- Search manifests and PersistentVolumes for flocker usage before upgrading.
- Migrate flocker volumes to a supported storage option before upgrading past 1.25.

### Admission webhooks not updated for new REST resource versions and fields before kube-apiserver upgrade

`kubernetes_c83275ac09` · high · confidence medium · introduced in * · fires at upgrade

Registered admission webhooks must be able to handle the data the new kube-apiserver sends. Webhook configuration objects must include new REST resource versions added in the target release, unless matchPolicy: Equivalent is used, and the webhooks must handle new resource versions and new fields added to existing versions.

- **[required] version** `in_range` `{"applies_to": "every release hop on the upgrade path"}`: The upgrade crosses to the target release of this item. (confidence medium, judge supported)
  - k8s_skew: "Upgrade kube-apiserver to {{< skew currentVersion >}}"
  - ⚠ The text uses the placeholder {{< skew currentVersion >}} and does not state the number; 1.29 comes from the assessment request.
- **[required] configuration** `present` `"ValidatingWebhookConfiguration and MutatingWebhookConfiguration objects updated to include new REST resource versions"`: The ValidatingWebhookConfiguration and MutatingWebhookConfiguration objects are updated to include new REST resource versions added in the target release. (confidence medium, judge supported)
  - k8s_skew: "ValidatingWebhookConfiguration and MutatingWebhookConfiguration objects are updated to include any new versions of REST resources added in"
  - ⚠ The text does not name the specific new REST resource versions added in the target release.
- **[disqualifying] configuration** `equals` `"matchPolicy: Equivalent"`: Webhook configurations use matchPolicy: Equivalent, which avoids the need to update them for new resource versions. (confidence medium, judge partially_supported)
  - k8s_skew: "or use the matchPolicy: Equivalent option available in v1.15+"
  - ⚠ The text does not state how matchPolicy: Equivalent behaves for every webhook, so its sufficiency for a given webhook is not confirmed.
- **[required] behavior** `present` `"webhooks handle new REST resource versions and new fields added to existing versions"`: The registered webhooks handle new REST resource versions and new fields added to existing versions in the target release. (confidence medium, judge supported)
  - k8s_skew: "The webhooks are able to handle any new versions of REST resources that will be sent to them"
  - k8s_skew: "and any new fields added to existing versions in"
  - ⚠ The text does not name the specific new resource versions or fields, so the affected webhook logic cannot be identified from the text.

Actions:
- Update ValidatingWebhookConfiguration and MutatingWebhookConfiguration objects to include the new REST resource versions added in the target release, or use matchPolicy: Equivalent (available in v1.15+).
- Verify that each registered webhook can handle new REST resource versions and new fields added to existing versions before upgrading kube-apiserver.

### In-tree AWS cloud provider removed

`kubernetes_d90e72f835` · high · confidence medium · introduced in 1.27 · fires at upgrade

The in-tree cloud provider for AWS has been removed in 1.27, so clusters that still depend on it cannot use it after crossing this release and must move to the external cloud provider.

- **[required] version** `in_range` `{"current_version": "< 1.27", "target_version": ">= 1.27"}`: The upgrade crosses release 1.27, in which the in-tree cloud provider for AWS was removed. (confidence high, judge supported)
  - k8s_changelog@1.27: "The in-tree cloud provider for AWS (and the EBS storage plugin) has now been removed."
- **[required] configuration** `present` `"in-tree AWS cloud provider"`: The cluster is configured to use the in-tree cloud provider for AWS. (confidence medium, judge partially_supported)
  - k8s_changelog@1.27: "The in-tree cloud provider for AWS"
  - ⚠ The text does not state which component settings reference the in-tree provider or how the external provider is configured.

Actions:
- Migrate to the external cloud provider from https://github.com/kubernetes/cloud-provider-aws instead of the in-tree AWS cloud provider.

### Kubelet dockershim Docker runtime removed in 1.24

`kubernetes_db1c331258` · high · confidence medium · introduced in 1.24 · fires at upgrade

Docker runtime support using dockershim was completely removed in the kubelet in 1.24, so nodes relying on Docker through dockershim will not work after crossing this release.

- **[required] version** `in_range` `{"current_version": "< 1.24", "target_version": ">= 1.24"}`: The upgrade crosses release 1.24, where dockershim support was removed. (confidence high, judge supported)
  - k8s_changelog@1.24: "Docker runtime support using dockershim in the kubelet is now completely removed in 1.24."
- **[required] configuration** `present` `"dockershim"`: The kubelet on the node uses the dockershim Docker runtime support. (confidence medium, judge supported)
  - k8s_changelog@1.24: "Docker runtime support using dockershim in the kubelet"
  - ⚠ The text does not state how to detect which runtime a given node uses.

Actions:
- Move nodes to a container runtime that is a full-fledged implementation of CRI (v1alpha1 or v1 compliant) before upgrading.
- Verify each node's kubelet is not configured to use dockershim, and migrate any Docker-based nodes to a CRI-compliant runtime.

### kube-scheduler --lock-object-namespace flag removed

`kubernetes_e21f521ab8` · high · confidence medium · introduced in 1.28 · fires at upgrade

The deprecated kube-scheduler flag --lock-object-namespace was removed in 1.28. Deployments that still pass this flag to kube-scheduler are affected at upgrade. The text names --leader-elect-resource-namespace or ComponentConfig as replacements.

- **[required] version** `in_range` `{"current_version": "< 1.28", "target_version": ">= 1.28"}`: The upgrade crosses release 1.28, in which the kube-scheduler flag --lock-object-namespace was removed. (confidence high, judge supported)
  - k8s_changelog@1.28: "The deprecated flag --lock-object-namespace and --lock-object-name have been removed from kube-scheduler."
- **[required] configuration** `present` `"--lock-object-namespace"`: The kube-scheduler is started with the flag --lock-object-namespace. (confidence medium, judge supported)
  - k8s_changelog@1.28: "The deprecated flag --lock-object-namespace and --lock-object-name have been removed from kube-scheduler."
  - ⚠ The text does not state what kube-scheduler does when a removed flag is passed.

Actions:
- Remove --lock-object-namespace from kube-scheduler startup flags or manifests.
- Use --leader-elect-resource-namespace instead, or configure the parameter through ComponentConfig.

### Removed kubelet flag --experimental-check-node-capabilities-before-mount

`kubernetes_e4f538b8cc` · high · confidence medium · introduced in 1.24 · fires at upgrade

The deprecated kubelet flag --experimental-check-node-capabilities-before-mount is removed in 1.24. Kubelet scripts or manifests that still use it are affected by the upgrade.

- **[required] version** `in_range` `{"current_version": "< 1.24", "target_version": ">= 1.24"}`: The upgrade from 1.23 to 1.29 crosses release 1.24, where the flag is removed. (confidence high, judge supported)
  - k8s_changelog@1.24: "Remove the deprecated flag --experimental-check-node-capabilities-before-mount."
- **[required] configuration** `present` `"--experimental-check-node-capabilities-before-mount"`: Kubelet scripts or manifests use the flag --experimental-check-node-capabilities-before-mount. (confidence medium, judge supported)
  - k8s_changelog@1.24: "Remove any use of --experimental-check-node-capabilities-before-mount from your kubelet scripts or manifests."
  - ⚠ The text does not state what happens to a kubelet started with the removed flag.

Actions:
- Remove any use of --experimental-check-node-capabilities-before-mount from kubelet scripts or manifests before upgrading.
- Use the CSI alternative referenced in the release notes; the text does not name the specific replacement.

### Service tolerate-unready-endpoints annotation removed

`kubernetes_e82868187c` · high · confidence medium · introduced in 1.24 · fires at upgrade

The tolerate-unready-endpoints annotation on Service objects was removed in v1.24. Services that still rely on this annotation are affected at upgrade. The replacement is Service.spec.publishNotReadyAddresses.

- **[required] version** `in_range` `{"current_version": "< 1.24", "target_version": ">= 1.24"}`: The upgrade crosses release 1.24, where the tolerate-unready-endpoints annotation in Service is removed. (confidence medium, judge supported)
  - k8s_changelog@1.24: "Remove tolerate-unready-endpoints annotation in Service deprecated from 1.11, use Service.spec.publishNotReadyAddresses instead."
  - ⚠ The text does not state what behavior changes for a Service when the annotation is removed.
- **[required] api_usage** `present` `"tolerate-unready-endpoints"`: A Service object sets the tolerate-unready-endpoints annotation. (confidence high, judge supported)
  - k8s_changelog@1.24: "tolerate-unready-endpoints annotation in Service"
- **[disqualifying] configuration** `present` `"Service.spec.publishNotReadyAddresses"`: The Service already sets spec.publishNotReadyAddresses instead of the annotation. (confidence low, judge partially_supported)
  - k8s_changelog@1.24: "use Service.spec.publishNotReadyAddresses instead"
  - ⚠ The text names the replacement but does not state that the field fully covers the annotation's behavior.

Actions:
- Find Service objects that set the tolerate-unready-endpoints annotation.
- Replace the annotation with Service.spec.publishNotReadyAddresses on those Services.
- Verify the Service behavior after the change, because the text does not describe the behavior difference.

### kubelet newer than kube-apiserver during upgrade

`kubernetes_ec1ed44946` · high · confidence medium · introduced in * · fires at upgrade

The item states that kubelet must not be newer than kube-apiserver. Upgrading kubelets ahead of kube-apiserver violates this constraint.

- **[required] version** `in_range` `{"applies_to": "every release hop on the upgrade path"}`: The upgrade crosses the release in which the kubelet/kube-apiserver version skew statement applies. (confidence medium, judge partially_supported)
  - k8s_skew: "kubelet must not be newer than kube-apiserver"
  - k8s_skew: "kubelet may be up to three minor versions older than kube-apiserver"
  - k8s_skew: "Optionally upgrade kubelet instances to {{< skew currentVersion >}}"
  - k8s_skew: "Running a cluster with kubelet instances that are persistently three minor versions behind kube-apiserver"
  - ⚠ The text does not state the release number, so the version tie to 1.29 is not confirmed by the text.
  - ⚠ The text does not state what happens when the skew limit is exceeded.
  - ⚠ The text does not tie this statement to release 1.29 explicitly.
- **[required] deployment** `in_range` `"kube-apiserver minus three minor versions through kube-apiserver"`: The kubelet version is within three minor versions of the kube-apiserver version. (confidence medium, judge supported)
  - k8s_skew: "kubelet may be up to three minor versions older than kube-apiserver"
  - k8s_skew: "kubelet < 1.25 may only be up to two minor versions older than kube-apiserver"
  - k8s_skew: "Before performing a minor version kubelet upgrade, drain pods from that node."
  - k8s_skew: "In-place minor version kubelet upgrades are not supported."
  - k8s_skew: "Running a cluster with kubelet instances that are persistently three minor versions behind kube-apiserver"
  - ⚠ The text does not state what happens to workloads if a node is not drained before the kubelet upgrade.
  - ⚠ The text does not state what happens if kubelets are more than three minor versions behind kube-apiserver.
- **[optional] deployment** `less_than` `"1.25"`: The kubelet version is below 1.25. (confidence high, judge supported)
  - k8s_skew: "kubelet < 1.25 may only be up to two minor versions older than kube-apiserver"

Actions:
- Check kubelet versions on all nodes against the kube-apiserver version before and during the upgrade.
- Ensure no kubelet is newer than any kube-apiserver instance.
- Ensure each kubelet is within three minor versions of kube-apiserver, and within two minor versions for kubelet versions below 1.25.
- Check kubelet versions on all nodes against the kube-apiserver version.
- Upgrade kubelets so that no node is more than three minor versions older than kube-apiserver.
- Drain each node's pods (for example with kubectl drain) before performing a minor version kubelet upgrade on that node.
- Do not perform an in-place minor version upgrade of kubelet; upgrade kubelet on drained nodes instead.
- Check the kubelet version on every node against the kube-apiserver version.
- Upgrade kubelet instances that are persistently three minor versions behind kube-apiserver before upgrading the control plane.

### IPv6DualStack feature gate manually enabled for external cloud providers

`kubernetes_f37fdc8f97` · high · confidence medium · introduced in 1.27 · fires at upgrade

The IPv6DualStack feature gate for external cloud providers was removed in 1.27. Components that still manually enable this gate must stop doing so before upgrading.

- **[required] version** `in_range` `{"current_version": "< 1.27", "target_version": ">= 1.27"}`: The upgrade crosses release 1.27 by moving from a version below 1.27 to 1.29. (confidence medium, judge partially_supported)
  - k8s_changelog@1.27: "The IPv6DualStack feature gate for external cloud providers was removed."
  - ⚠ The text does not state what happens at startup when the removed gate is still set; it only says the user must stop enabling it.
- **[required] configuration** `present` `"IPv6DualStack"`: A component configuration manually enables the IPv6DualStack feature gate. (confidence medium, judge partially_supported)
  - k8s_changelog@1.27: "If you were still manually enabling it you must stop now."
  - ⚠ The text does not name which components or which configuration mechanism (flag, config file, or other) is affected.

Actions:
- Search configuration for manual enabling of the IPv6DualStack feature gate.
- Remove the manual IPv6DualStack feature gate setting before upgrading.

### Removed in-tree volume plugin: storageos

`kubernetes_ff27941095` · high · confidence medium · introduced in 1.25 · fires at upgrade

The in-tree storageos volume plugin support has been completely removed from Kubernetes in 1.25. Workloads or PersistentVolumes that depend on storageos in-tree volumes cannot rely on it after upgrading past 1.25.

- **[required] version** `in_range` `{"current_version": "< 1.25", "target_version": ">= 1.25"}`: The upgrade crosses release 1.25, where the in-tree storageos volume plugin support was removed. (confidence high, judge supported)
  - k8s_changelog@1.25: "The intree volume plugin storageos support has been completely removed from Kubernetes."
- **[required] api_usage** `present` `"storageos"`: The cluster uses in-tree storageos volumes. (confidence medium, judge partially_supported)
  - k8s_changelog@1.25: "The intree volume plugin storageos support has been completely removed from Kubernetes."

Actions:
- Search manifests and PersistentVolumes for storageos usage before upgrading.
- Migrate storageos volumes to a supported storage option before upgrading past 1.25.

### Windows winkernel kube-proxy no longer supports HNS v1 APIs

`kubernetes_0214e6aee0` · medium · confidence high · introduced in 1.25 · fires at upgrade

Windows winkernel kube-proxy no longer supports Windows HNS v1 APIs in the 1.25 release. Clusters with Windows nodes running winkernel kube-proxy that depend on HNS v1 APIs may break on upgrade.

- **[required] version** `in_range` `{"current_version": "< 1.25", "target_version": ">= 1.25"}`: The upgrade crosses release 1.25, where winkernel kube-proxy stopped supporting HNS v1 APIs. (confidence high, judge supported)
  - k8s_changelog@1.25: "Windows winkernel kube-proxy no longer supports Windows HNS v1 APIs."
- **[required] deployment** `present` `"winkernel kube-proxy"`: The cluster runs Windows nodes with winkernel kube-proxy. (confidence high, judge supported)
  - k8s_changelog@1.25: "Windows winkernel kube-proxy"
- **[uncertain] api_usage** `unknown` `"HNS v1 APIs"`: The application or cluster uses HNS v1 APIs. (confidence low, judge supported)
  - k8s_changelog@1.25: "no longer supports Windows HNS v1 APIs"
  - ⚠ The text does not state which components or software use the HNS v1 APIs, or how they would be affected.

Actions:
- Check whether any Windows nodes run winkernel kube-proxy before upgrading.
- Identify any workloads or tooling on those nodes that depend on HNS v1 APIs.
- The text does not name a replacement for HNS v1 APIs; confirm the migration path in Windows or Kubernetes documentation.

### kubeadm admin.conf RBAC binding change and super-admin.conf

`kubernetes_05f82d70f3` · medium · confidence medium · introduced in 1.29 · fires at upgrade

kubeadm now binds the User in admin.conf to the RBAC Group kubeadm:cluster-admins with cluster-admin access instead of system:masters. A separate super-admin.conf bound to system:masters is deployed, and kubeadm join --control-plane generates only the less privileged admin.conf.

- **[required] version** `in_range` `{"current_version": "< 1.29", "target_version": ">= 1.29"}`: The upgrade crosses release 1.29, where kubeadm join --control-plane generates only the less privileged admin.conf file. (confidence high, judge supported)
  - k8s_changelog@1.29: "kubeadm join --control-plane will now generate only an admin.conf file that has the less privileged User."
- **[required] behavior** `present` `"admin.conf"`: The application or operator tooling relies on admin.conf being bound to the system:masters Group with its previous privileges. (confidence medium, judge supported)
  - k8s_changelog@1.29: "Before this change, the default admin.conf was bound to system:masters Group, which was undesired."
  - ⚠ The text does not state which tools or scripts depend on the previous binding.
- **[optional] configuration** `present` `"super-admin.conf"`: The cluster has a super-admin.conf file on the node host that is bound to system:masters. (confidence medium, judge partially_supported)
  - k8s_changelog@1.29: "The User in super-admin.conf is now bound to the system:masters built-in super-powers / break-glass Group that can bypass RBAC."

Actions:
- Review scripts and workflows that depend on admin.conf having system:masters privileges and move them to super-admin.conf or to RBAC bindings for kubeadm:cluster-admins.
- Decide whether to keep super-admin.conf on the node host or move it to a safe location, as the text says the cluster admin can decide.
- Note that kubeadm upgrade apply migrates the node to the two-file setup.

### In-tree vSphere volume on vSphere releases below 7.0u2

`kubernetes_098e6337df` · medium · confidence medium · introduced in 1.25 · fires at upgrade

In-tree vSphere volume is not supported on vSphere releases less than 7.0u2 as of Kubernetes v1.25. Upgrade vSphere (both ESXi and vCenter) to 7.0u2 or above.

- **[required] version** `in_range` `{"current_version": "< 1.25", "target_version": ">= 1.25"}`: The upgrade crosses Kubernetes release 1.25 (from 1.23 to 1.29) (confidence medium, judge partially_supported)
  - k8s_changelog@1.25: "VSphere releases less than 7.0u2 are not supported for in-tree vSphere volume as of Kubernetes v1.25"
- **[required] runtime** `less_than` `"7.0u2"`: vSphere (ESXi and vCenter) release is less than 7.0u2 (confidence medium, judge supported)
  - k8s_changelog@1.25: "VSphere releases less than 7.0u2 are not supported"
  - ⚠ The text does not state how to determine the vSphere release from within the cluster.
- **[required] api_usage** `present` `"in-tree vSphere volume"`: Cluster uses the in-tree vSphere volume (confidence medium, judge supported)
  - k8s_changelog@1.25: "not supported for in-tree vSphere volume"
  - ⚠ The text does not state what happens to existing in-tree vSphere volumes on unsupported vSphere releases.

Actions:
- Upgrade vSphere (both ESXi and vCenter) to 7.0u2 or above before upgrading to Kubernetes v1.25 or later.

### LegacyServiceAccountTokenNoAutoGeneration: apps relying on auto-generated ServiceAccount token Secrets

`kubernetes_1ae44fcc5b` · medium · confidence medium · introduced in 1.24 · fires at upgrade

The LegacyServiceAccountTokenNoAutoGeneration feature gate is beta and enabled by default. When enabled, Secret API objects containing service account tokens are no longer auto-generated for every ServiceAccount. Applications or deployments that depend on those auto-generated token Secrets are affected. The text provides a workaround: use the TokenRequest API, or create a Secret for the token controller to populate if a non-expiring token is required.

- **[required] version** `in_range` `{"current_version": "< 1.24", "target_version": ">= 1.24"}`: The upgrade crosses release 1.24, where the LegacyServiceAccountTokenNoAutoGeneration feature gate is beta and enabled by default. (confidence high, judge supported)
  - k8s_changelog@1.24: "The LegacyServiceAccountTokenNoAutoGeneration feature gate is beta, and enabled by default."
- **[required] api_usage** `present` `"Secret"`: The application or deployment depends on Secret API objects containing service account tokens that are auto-generated for each ServiceAccount. (confidence medium, judge supported)
  - k8s_changelog@1.24: "Secret API objects containing service account tokens are no longer auto-generated for every ServiceAccount"
  - ⚠ The text does not state whether existing auto-generated token Secrets are removed or kept after the upgrade.
- **[disqualifying] api_usage** `present` `"TokenRequest"`: The application obtains service account tokens through the TokenRequest API instead of relying on auto-generated Secrets. (confidence medium, judge partially_supported)
  - k8s_changelog@1.24: "Use the TokenRequest API to acquire service account tokens"

Actions:
- Acquire service account tokens through the TokenRequest API instead of reading auto-generated token Secrets.
- If a non-expiring token is required, create a Secret API object for the token controller to populate with a service account token, following the guide linked in the source changelog.

### kubectl version default output changed

`kubernetes_2367ae9f77` · medium · confidence medium · introduced in 1.28 · fires at first_use

The default output of kubectl version was changed to be identical to what kubectl version --short printed. Scripts that parse the previous default output may behave differently.

- **[required] version** `in_range` `{"current_version": "< 1.28", "target_version": ">= 1.28"}`: The upgrade crosses release 1.28, which introduced the output change. (confidence high, judge supported)
  - k8s_changelog@1.28: "Changed kubectl version default output to be identical to what kubectl version --short printed"
- **[required] behavior** `present` `"kubectl version"`: The application or deployment parses the default output of kubectl version. (confidence medium, judge partially_supported)
  - k8s_changelog@1.28: "Changed kubectl version default output"
  - ⚠ The text does not describe the exact format of the previous or new default output.

Actions:
- Review scripts that parse kubectl version default output and update them to the new format, which matches the former --short output.

### multiple CRI sockets on host with empty criSocket during cluster creation

`kubernetes_29aeab2f1c` · medium · confidence medium · introduced in 1.24 · fires at first_use

When criSocket is empty during cluster creation and multiple sockets are found on the host, kubeadm now always throws an error instead of choosing one.

- **[required] version** `in_range` `{"current_version": "< 1.24", "target_version": ">= 1.24"}`: The upgrade crosses release 1.24, where the kubeadm CRI socket behavior changed. (confidence high, judge supported)
  - k8s_changelog@1.24: "Kubeadm: default the kubeadm configuration to the containerd socket"
- **[required] configuration** `equals` `"empty"`: The criSocket field is empty in the kubeadm configuration while cluster creation runs on a host where multiple sockets exist. (confidence medium, judge partially_supported)
  - k8s_changelog@1.24: "If the Init|JoinConfiguration.nodeRegistration.criSocket field is empty during cluster creation and multiple sockets are found on the host"
  - ⚠ The text does not state how many sockets trigger the error beyond 'multiple'.

Actions:
- Set Init|JoinConfiguration.nodeRegistration.criSocket explicitly in kubeadm configuration to the CRI socket to use, so cluster creation does not fail on hosts with multiple sockets.

### Removed experimental dynamic log sanitization feature

`kubernetes_2e91042cd0` · medium · confidence medium · introduced in 1.24 · fires at upgrade

The experimental dynamic log sanitization feature was deprecated and removed in 1.24 and is no longer available for use, so deployments that depend on it are affected by the upgrade.

- **[required] version** `in_range` `{"current_version": "< 1.24", "target_version": ">= 1.24"}`: The upgrade crosses Kubernetes release 1.24, in which the experimental dynamic log sanitization feature was removed. (confidence high, judge supported)
  - k8s_changelog@1.24: "The experimental dynamic log sanitization feature has been deprecated and removed in the 1.24 release."
- **[required] configuration** `present` `"dynamic log sanitization feature"`: The application or deployment uses the dynamic log sanitization feature. (confidence medium, judge supported)
  - k8s_changelog@1.24: "The feature is no longer available for use."
  - ⚠ The text does not state how the feature is enabled or which setting or flag controls it, so no literal symbol can be searched for.

Actions:
- Check whether the application or deployment uses the dynamic log sanitization feature.
- Remove any use of the dynamic log sanitization feature before upgrading to 1.24 or later.

### PriorityLevelConfiguration spec.limited.assuredConcurrencyShares renamed in flowcontrol.apiserver.k8s.io/v1beta3

`kubernetes_3cf225fc10` · medium · confidence medium · introduced in 1.29 · fires at upgrade

In flowcontrol.apiserver.k8s.io/v1beta3, the PriorityLevelConfiguration spec.limited.assuredConcurrencyShares field is renamed to spec.limited.nominalConcurrencyShares. Manifests or API clients that use the old field name in v1beta3 must be updated to the new name.

- **[required] version** `in_range` `{"current_version": "< 1.29", "target_version": ">= 1.29"}`: The upgrade crosses release 1.29, the release in which this change is introduced. (confidence medium, judge supported)
  - k8s_deprecation_guide: "The PriorityLevelConfiguration spec.limited.assuredConcurrencyShares field is renamed to spec.limited.nominalConcurrencyShares"
  - ⚠ The text does not state the exact 1.29 behavior of the old field name beyond the rename.
  - ⚠ The text does not state whether the rename also applies to flowcontrol.apiserver.k8s.io/v1beta3 beyond listing it as a notable change in that version.
- **[required] api_usage** `present` `"flowcontrol.apiserver.k8s.io/v1beta3"`: The application or manifests use the flowcontrol.apiserver.k8s.io/v1beta3 API version for PriorityLevelConfiguration. (confidence medium, judge supported)
  - k8s_deprecation_guide: "Notable changes in flowcontrol.apiserver.k8s.io/v1beta3:"
  - k8s_deprecation_guide: "The PriorityLevelConfiguration spec.limited.assuredConcurrencyShares field"
  - k8s_deprecation_guide: "The flowcontrol.apiserver.k8s.io/v1beta3 API version of FlowSchema and PriorityLevelConfiguration is no longer served as of v1.32."
  - ⚠ The text does not state how a v1beta3 request that still uses the old field name is handled after the upgrade.
  - ⚠ R3: the replacement flowcontrol.apiserver.k8s.io/v1beta3 is removed later, in v1.32 (after target 1.29); prefer flowcontrol.apiserver.k8s.io/v1 to avoid a second migration.
- **[required] api_usage** `present` `"spec.limited.assuredConcurrencyShares"`: The application or manifests use the spec.limited.assuredConcurrencyShares field of PriorityLevelConfiguration. (confidence high, judge supported)
  - k8s_deprecation_guide: "The PriorityLevelConfiguration spec.limited.assuredConcurrencyShares field is renamed to spec.limited.nominalConcurrencyShares"

Actions:
- Rename spec.limited.assuredConcurrencyShares to spec.limited.nominalConcurrencyShares in PriorityLevelConfiguration manifests and API clients that use flowcontrol.apiserver.k8s.io/v1beta3.
- Migrate manifests and API clients to the flowcontrol.apiserver.k8s.io/v1 API version, available since v1.29, or keep flowcontrol.apiserver.k8s.io/v1beta3, available since v1.26.
- Rename spec.limited.assuredConcurrencyShares to spec.limited.nominalConcurrencyShares in manifests and API clients that use flowcontrol.apiserver.k8s.io/v1.
- Review any explicit value of 0 for the field, since it is not changed to 30 under the new name.

### PodDisruptionBudget policy/v1 empty spec.selector

`kubernetes_4d1a7508d9` · medium · confidence high · introduced in 1.25 · fires at first_use

In policy/v1, an empty spec.selector on a PodDisruptionBudget selects all pods in the namespace, whereas in policy/v1beta1 it selected no pods. Manifests migrated from policy/v1beta1 with an empty selector will select a different set of pods.

- **[required] version** `in_range` `{"current_version": "< 1.25", "target_version": ">= 1.25"}`: The cluster serves the policy/v1beta1 PodDisruptionBudget API, which is no longer served as of v1.25, so the upgrade crosses release 1.25. (confidence high, judge supported)
  - k8s_deprecation_guide: "The policy/v1beta1 API version of PodDisruptionBudget is no longer served as of v1.25."
- **[required] configuration** `present` `"spec.selector: {}"`: A PodDisruptionBudget is written to policy/v1 with an empty spec.selector ({}). (confidence high, judge supported)
  - k8s_deprecation_guide: "an empty spec.selector ({}) written to a policy/v1 PodDisruptionBudget"

Actions:
- Find PodDisruptionBudget objects with an empty spec.selector.
- For each one, either set an explicit label selector or leave spec.selector unset if no pods should be selected, since an unset spec.selector selects no pods in either API version.

### kubeadm imageRepository k8s.gcr.io rewrite during upgrade

`kubernetes_54d1b6b275` · medium · confidence medium · introduced in 1.25 · fires at upgrade

During kubeadm upgrade apply, diff, or node, a ClusterConfiguration.imageRepository stored in the kubeadm-config ConfigMap that contains the legacy k8s.gcr.io repository is modified to the new default registry.k8s.io. The change is reflected in the in-cluster ConfigMap only during upgrade apply.

- **[required] version** `in_range` `{"current_version": "< 1.25", "target_version": ">= 1.25"}`: The upgrade from 1.23 to 1.29 crosses release 1.25, which introduced the kubeadm imageRepository change. (confidence high, judge supported)
  - k8s_changelog@1.25: "Kubeadm: during "upgrade apply/diff/node", in case the ClusterConfiguration.imageRepository stored in the "kubeadm-config" ConfigMap contains the legacy "k8s.gcr.io" repository"
- **[required] configuration** `present` `"k8s.gcr.io"`: The cluster's kubeadm-config ConfigMap contains ClusterConfiguration.imageRepository set to the legacy k8s.gcr.io repository. (confidence medium, judge supported)
  - k8s_changelog@1.25: "contains the legacy "k8s.gcr.io" repository"
  - ⚠ The text does not state what happens when imageRepository is already set to registry.k8s.io or is unset.

Actions:
- Check the imageRepository value in the kube-system kubeadm-config ConfigMap before upgrading.
- Confirm that registry.k8s.io is reachable from control plane and worker nodes so the rewritten repository can be used.
- Review any image mirrors or pull configuration that reference k8s.gcr.io, since the stored default is changed to registry.k8s.io.

### kubeadm upgrade adds control-plane NoSchedule taint to existing control plane nodes

`kubernetes_58f3704548` · medium · confidence medium · introduced in 1.24 · fires at upgrade

Clusters upgraded to 1.24 with kubeadm upgrade apply receive the taint node-role.kubernetes.io/control-plane:NoSchedule on existing control plane nodes. Workloads that need to run on control plane nodes must tolerate this taint.

- **[required] version** `in_range` `{"current_version": "< 1.24", "target_version": ">= 1.24"}`: The upgrade crosses release 1.24, where kubeadm upgrade apply adds the node-role.kubernetes.io/control-plane:NoSchedule taint to existing control plane nodes. (confidence high, judge supported)
  - k8s_changelog@1.24: "For clusters that are being upgraded to 1.24 with kubeadm upgrade apply, the command will add the new taint node-role.kubernetes.io/control-plane:NoSchedule to existing control plane nodes."
- **[required] configuration** `absent` `"toleration for node-role.kubernetes.io/control-plane:NoSchedule"`: The deployment has workloads that must schedule onto control plane nodes but do not tolerate the node-role.kubernetes.io/control-plane:NoSchedule taint. (confidence medium, judge partially_supported)
  - k8s_changelog@1.24: "In release 1.20 (first stage), a release note instructed to preemptively tolerate the new taint."
  - ⚠ The text does not explicitly state the scheduling outcome for pods that lack this toleration.

Actions:
- Add a toleration for node-role.kubernetes.io/control-plane:NoSchedule to workloads that must run on control plane nodes.
- Adapt infrastructure to the taint change as the release note advises.
- Note that the old taint node-role.kubernetes.io/master:NoSchedule is removed in 1.25 according to the text, so tolerations for it are not a substitute.

### PriorityLevelConfiguration assuredConcurrencyShares renamed to nominalConcurrencyShares

`kubernetes_612defa966` · medium · confidence medium · introduced in 1.29 · fires at upgrade

The PriorityLevelConfiguration spec.limited.assuredConcurrencyShares field is renamed to spec.limited.nominalConcurrencyShares in flowcontrol.apiserver.k8s.io/v1, so manifests and clients that use the old field name need to be migrated.

- **[required] version** `in_range` `{"current_version": "< 1.29", "target_version": ">= 1.29"}`: The change is introduced in release 1.29 and the upgrade from 1.23 crosses release 1.29. (confidence medium, judge partially_supported)
  - k8s_deprecation_guide: "The PriorityLevelConfiguration spec.limited.assuredConcurrencyShares field is renamed to spec.limited.nominalConcurrencyShares"
- **[required] api_usage** `present` `"spec.limited.assuredConcurrencyShares"`: The application or deployment uses the PriorityLevelConfiguration field spec.limited.assuredConcurrencyShares. (confidence medium, judge supported)
  - k8s_deprecation_guide: "The PriorityLevelConfiguration spec.limited.assuredConcurrencyShares field is renamed to spec.limited.nominalConcurrencyShares"
  - ⚠ The text does not state whether the old field name is still accepted in flowcontrol.apiserver.k8s.io/v1 after the rename.

Actions:
- Rename spec.limited.assuredConcurrencyShares to spec.limited.nominalConcurrencyShares in PriorityLevelConfiguration manifests and API clients.

### PodDisruptionBudget empty spec.selector in policy/v1

`kubernetes_655168da6e` · medium · confidence medium · introduced in 1.25 · fires at rollout

An empty spec.selector written to a policy/v1 PodDisruptionBudget selects all pods in the namespace, whereas in policy/v1beta1 it selected no pods. Migrated PodDisruptionBudgets with an empty selector can change which pods are protected.

- **[required] version** `in_range` `{"current_version": "< 1.25", "target_version": ">= 1.25"}`: The upgrade crosses Kubernetes release 1.25, where policy/v1beta1 PodDisruptionBudget stops being served and policy/v1 becomes the replacement. (confidence medium, judge partially_supported)
  - k8s_deprecation_guide: "The policy/v1beta1 API version of PodDisruptionBudget is no longer served as of v1.25"
- **[required] configuration** `equals` `"{}"`: A PodDisruptionBudget written to policy/v1 has an empty spec.selector set to {}. (confidence high, judge supported)
  - k8s_deprecation_guide: "an empty spec.selector ({}) written to a policy/v1 PodDisruptionBudget selects all pods in the namespace"

Actions:
- Review migrated PodDisruptionBudgets with an empty spec.selector and confirm the intended pod selection before applying them under policy/v1.
- Use an explicit spec.selector if the PodDisruptionBudget should select no pods, since an unset spec.selector selects no pods in either API version.

### EndpointSlice topology field not writable in v1

`kubernetes_783b0b093f` · medium · confidence medium · introduced in 1.25 · fires at upgrade

Writes to the EndpointSlice topology field fail to persist in discovery.k8s.io/v1 because the replacement deprecatedTopology field is not writable.

- **[required] version** `in_range` `{"current_version": "< 1.25", "target_version": ">= 1.25"}`: The upgrade crosses release 1.25 (1.23 to 1.29). (confidence medium, judge partially_supported)
  - k8s_deprecation_guide: "The discovery.k8s.io/v1beta1 API version of EndpointSlice is no longer served as of v1.25."
- **[required] api_usage** `present` `"topology"`: The application writes the topology field on EndpointSlice objects. (confidence medium, judge supported)
  - k8s_deprecation_guide: "topology is replaced with the deprecatedTopology field which is not writable in v1"
  - ⚠ The text does not state what happens to a write to the topology field in v1.

Actions:
- Stop writing the topology field on discovery.k8s.io/v1 EndpointSlice objects and use the nodeName and zone fields instead.

### control-plane-noschedule-taint-removed-on-kubeadm-upgrade

`kubernetes_794be3349b` · medium · confidence medium · introduced in 1.25 · fires at upgrade

kubeadm stops applying the node-role.kubernetes.io/master:NoSchedule taint to control plane nodes for new clusters and removes it from existing control plane nodes during kubeadm upgrade apply, so the control plane nodes no longer carry that taint after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 1.25", "target_version": ">= 1.25"}`: The upgrade crosses release 1.25 (from a version below 1.25 to 1.29). (confidence high)
  - k8s_changelog@1.25: "stop applying the node-role.kubernetes.io/master:NoSchedule taint to control plane nodes for new clusters"
- **[required] configuration** `present` `"node-role.kubernetes.io/master:NoSchedule"`: The cluster is kubeadm-managed and its control plane nodes carry the node-role.kubernetes.io/master:NoSchedule taint before the upgrade. (confidence medium, judge partially_supported)
  - k8s_changelog@1.25: "Remove the taint from existing control plane nodes during"
  - ⚠ The text does not state whether taint removal applies to clusters not created by kubeadm, or how workload scheduling changes after the taint is removed.

Actions:
- Check which control plane nodes currently carry the node-role.kubernetes.io/master:NoSchedule taint before running kubeadm upgrade apply.
- Check whether workloads depend on control plane nodes being excluded from scheduling, and if so, enforce that with their own scheduling rules after the upgrade.

### kube-apiserver insecure address flags removed

`kubernetes_8a1e841ec0` · medium · confidence medium · introduced in 1.24 · fires at upgrade

The insecure address flags --address, --insecure-bind-address, --port and --insecure-port of kube-apiserver are removed in release 1.24. They were inert since 1.20, so a deployment that still sets them must drop them before the upgrade.

- **[required] version** `in_range` `{"current_version": "< 1.24", "target_version": ">= 1.24"}`: The upgrade crosses release 1.24, where the insecure address flags are removed from kube-apiserver. (confidence high, judge supported)
  - k8s_changelog@1.24: "Kube-apiserver: the insecure address flags --address, --insecure-bind-address, --port and --insecure-port (inert since 1.20) are removed"
- **[required] configuration** `present` `"--address, --insecure-bind-address, --port or --insecure-port"`: The kube-apiserver configuration sets one of the removed insecure flags. (confidence medium, judge supported)
  - k8s_changelog@1.24: "Kube-apiserver: the insecure address flags --address, --insecure-bind-address, --port and --insecure-port"
  - ⚠ The text does not state whether kube-apiserver rejects a removed flag at startup or ignores it.
- **[uncertain] behavior** `unknown` `""`: The removed flags are only inert when kube-apiserver runs and do not change behavior before the removal. (confidence low, judge partially_supported)
  - k8s_changelog@1.24: "Kube-apiserver: the insecure address flags --address, --insecure-bind-address, --port and --insecure-port (inert since 1.20) are removed"
  - ⚠ The text does not state what happens to a configuration that still passes the removed flags after the upgrade.

Actions:
- Remove --address, --insecure-bind-address, --port and --insecure-port from the kube-apiserver startup configuration before upgrading to 1.29.
- The text names no replacement flag for these insecure address flags.

### events.k8s.io/v1 Event field changes for clients creating events

`kubernetes_8e7dabc5b0` · medium · confidence medium · introduced in 1.25 · fires at first_use

Clients that move to events.k8s.io/v1 must use renamed and required fields, and deprecated field names are not permitted in new events.k8s.io/v1 Events.

- **[required] version** `in_range` `{"current_version": "< 1.25", "target_version": ">= 1.25"}`: The upgrade crosses release v1.25, where the events.k8s.io/v1 Event changes are documented as part of the removal of events.k8s.io/v1beta1. (confidence medium, judge partially_supported)
  - k8s_deprecation_guide: "is no longer served as of v1.25"
  - ⚠ The text lists these changes under the v1.25 section but does not state the exact field-level behavior difference for clients still on v1beta1.
- **[required] api_usage** `present` `"involvedObject"`: The application or deployment creates or manipulates Events that use the involvedObject field. (confidence high, judge supported)
  - k8s_deprecation_guide: "involvedObject is renamed to regarding"
- **[required] api_usage** `present` `"action, reason, reportingController, reportingInstance"`: The application or deployment creates new events.k8s.io/v1 Events without the required fields. (confidence high, judge supported)
  - k8s_deprecation_guide: "action, reason, reportingController, and reportingInstance are required when creating new events.k8s.io/v1 Events"

Actions:
- Use regarding instead of involvedObject.
- Set action, reason, reportingController, and reportingInstance when creating new events.k8s.io/v1 Events.
- Use eventTime instead of firstTimestamp, series.lastObservedTime instead of lastTimestamp, series.count instead of count, reportingController instead of source.component, and reportingInstance instead of source.host.

### kube-controller-manager insecure address flags removed

`kubernetes_954dc817ef` · medium · confidence medium · introduced in 1.24 · fires at upgrade

The insecure address flags --address and --port in kube-controller-manager have had no effect since v1.20 and are removed in v1.24. Clusters whose kube-controller-manager configuration still sets these flags are affected by the upgrade.

- **[required] version** `in_range` `{"current_version": "< 1.24", "target_version": ">= 1.24"}`: The upgrade crosses release 1.24 (from below 1.24 to 1.29). (confidence medium, judge partially_supported)
  - k8s_changelog@1.24: "and are removed in v1.24"
- **[alternative] configuration** `present` `"--address"`: kube-controller-manager is started with the --address flag. (confidence medium, judge supported)
  - k8s_changelog@1.24: "The insecure address flags --address"
  - ⚠ The text does not state whether a kube-controller-manager still passing these flags fails to start or only logs an error.
- **[alternative] configuration** `present` `"--port"`: kube-controller-manager is started with the --port flag. (confidence medium, judge supported)
  - k8s_changelog@1.24: "--address and --port in kube-controller-manager"
  - ⚠ The text does not state whether a kube-controller-manager still passing these flags fails to start or only logs an error.

Actions:
- Remove --address and --port from the kube-controller-manager configuration before upgrading to 1.24 or later, since these flags have had no effect since v1.20.

### kubeadm kubelet-config ConfigMap rename for clusters using UnversionedKubeletConfigMap=false

`kubernetes_965870d781` · medium · confidence medium · introduced in 1.25 · fires at upgrade

Kubeadm clusters that previously used the legacy naming format with UnversionedKubeletConfigMap=false must manually copy the kubelet ConfigMap from kube-system/kubelet-config-x.yy to kube-system/kubelet-config before upgrading to v1.25, because the kubelet ConfigMap and RBAC naming is now locked to kubelet-config.

- **[required] version** `in_range` `{"current_version": "< 1.25", "target_version": ">= 1.25"}`: The upgrade crosses release 1.25, since the migration step must be done before upgrading to v1.25. (confidence medium, judge supported)
  - k8s_changelog@1.25: "you must manually copy the config map from kube-system/kubelet-config-x.yy to kube-system/kubelet-config before upgrading to v1.25"
  - k8s_changelog@1.24: "instead of the legacy kubelet-config-x.yy naming"
  - ⚠ History: in 1.24, 'kubeadm legacy kubelet ConfigMap naming during upgrade' applied to the same symbol (unversionedkubeletconfigmap); superseded by the 1.25 change (R2).
- **[required] configuration** `equals` `"UnversionedKubeletConfigMap=false"`: The cluster previously used the legacy naming format with the feature gate UnversionedKubeletConfigMap set to false. (confidence medium, judge supported)
  - k8s_changelog@1.25: "If you have previously used the old naming format with UnversionedKubeletConfigMap=false"
  - ⚠ The text does not state how the gate was set on a given cluster, so the check must determine the effective value.
- **[required] configuration** `absent` `"kube-system/kubelet-config"`: The kube-system/kubelet-config ConfigMap has not yet been created by copying from the legacy kubelet-config-x.yy ConfigMap. (confidence medium, judge partially_supported)
  - k8s_changelog@1.25: "copy the config map from kube-system/kubelet-config-x.yy to kube-system/kubelet-config"

Actions:
- Before upgrading to v1.25 or later, copy the config map from kube-system/kubelet-config-x.yy to kube-system/kubelet-config.
- Confirm that the kube-system/kubelet-config ConfigMap exists and matches the legacy kubelet-config-x.yy contents before running the upgrade.

### Pods with RestartPolicy=Always may reach Succeeded phase

`kubernetes_98774b6ac3` · medium · confidence medium · introduced in 1.27 · fires at upgrade

Pods using RestartPolicy=Always can now enter the Succeeded phase on pod deletion or graceful node shutdown. Controllers that assumed these pods never reach Succeeded may need to be adapted.

- **[required] version** `in_range` `{"current_version": "< 1.27", "target_version": ">= 1.27"}`: The upgrade crosses release 1.27, where the terminal phase change was introduced. (confidence high, judge supported)
  - k8s_changelog@1.27: "Give terminal phase correctly to all pods that will not be restarted."
- **[required] behavior** `present` `"pods with RestartPolicy=Always"`: The application relies on pods with RestartPolicy=Always being assigned the Succeeded phase. (confidence medium, judge supported)
  - k8s_changelog@1.27: "pods which use RestartPolicy=Always may end up in the Succeeded phase"
  - ⚠ The text does not state when after upgrade these pods first reach Succeeded in a given deployment.
- **[required] api_usage** `present` `"controllers checking pod phase"`: The application has controllers that depend on pods with RestartPolicy=Always never entering the Succeeded phase. (confidence high, judge supported)
  - k8s_changelog@1.27: "Users who maintain controllers which relied on the fact that pods with RestartPolicy=Always never enter the Succeeded phase may need to adapt their controllers."

Actions:
- Review controllers and tooling that assume pods with RestartPolicy=Always never reach the Succeeded phase.
- Adapt those controllers to handle pods in the Succeeded phase, as the release notes advise.

### EndpointSlice topology zone key

`kubernetes_9972c3a8b9` · medium · confidence medium · introduced in 1.25 · fires at upgrade

Code that uses the deprecated topology zone key on EndpointSlice must use the per Endpoint zone field instead.

- **[required] version** `in_range` `{"current_version": "< 1.25", "target_version": ">= 1.25"}`: The upgrade crosses release 1.25 (1.23 to 1.29). (confidence medium, judge partially_supported)
  - k8s_deprecation_guide: "The discovery.k8s.io/v1beta1 API version of EndpointSlice is no longer served as of v1.25."
- **[required] api_usage** `present` `"topology[\"topology.kubernetes.io/zone\"]"`: The application uses the topology zone key on EndpointSlice objects. (confidence medium, judge supported)
  - k8s_deprecation_guide: "use per Endpoint zone field instead of deprecated topology["topology.kubernetes.io/zone"] field"
  - ⚠ The text does not state whether the deprecated key stops working or is only replaced.

Actions:
- Replace topology["topology.kubernetes.io/zone"] with the per Endpoint zone field.

### Control plane component version skew during 1.23 to 1.29 upgrade

`kubernetes_9b35c15a85` · medium · confidence medium · introduced in * · fires at upgrade

kube-controller-manager, kube-scheduler, and cloud-controller-manager must not be newer than the kube-apiserver instances they communicate with, and may be at most one minor version older. A multi-minor upgrade from 1.23 to 1.29 can leave these components outside that window if they are not upgraded in step with kube-apiserver.

- **[required] version** `in_range` `{"applies_to": "every release hop on the upgrade path"}`: The upgrade spans from 1.23 to 1.29, and the skew rule for control plane components applies to this release. (confidence medium, judge partially_supported)
  - k8s_skew: "must not be newer than the kube-apiserver instances they communicate with"
  - k8s_skew: "The kube-controller-manager, kube-scheduler, and cloud-controller-manager instances that communicate with this server are at version"
  - ⚠ The item does not state a release number; release metadata is absent. The 1.23 to 1.29 span comes from the assessment request.
  - ⚠ The text uses a template placeholder and does not state the numeric version; mapping the placeholder to a concrete version for the 1.23 to 1.29 upgrade is not stated in the text.
- **[required] deployment** `less_than` `"kube-apiserver minor version"`: A control plane component (kube-controller-manager, kube-scheduler, or cloud-controller-manager) runs at a minor version older than the kube-apiserver it communicates with. (confidence high, judge supported)
  - k8s_skew: "may be up to one minor version older (to allow live upgrades)"
  - k8s_skew: "instances that communicate with this server"

Actions:
- Check the version of each kube-controller-manager, kube-scheduler, and cloud-controller-manager against the kube-apiserver version.
- Confirm that no control plane component is newer than the kube-apiserver instances it communicates with.
- Confirm that each control plane component is within one minor version of the kube-apiserver instances it communicates with before proceeding.
- Check the version of kube-controller-manager, kube-scheduler and cloud-controller-manager against the skew version in the upgrade order before upgrading kube-apiserver.
- Upgrade these control-plane components to the required skew version before upgrading kube-apiserver to the target release.

### kubeadm upgrade removes node-role.kubernetes.io/master label from existing control plane nodes

`kubernetes_9d0391887c` · medium · confidence medium · introduced in 1.24 · fires at upgrade

Clusters upgraded to 1.24 with kubeadm upgrade apply lose the node-role.kubernetes.io/master label on existing control plane nodes. Workloads or tooling that select nodes by this label may stop matching.

- **[required] version** `in_range` `{"current_version": "< 1.24", "target_version": ">= 1.24"}`: The upgrade crosses release 1.24, where kubeadm upgrade apply removes the node-role.kubernetes.io/master label from existing control plane nodes. (confidence high, judge supported)
  - k8s_changelog@1.24: "For clusters that are being upgraded to 1.24 with kubeadm upgrade apply, the command will remove the label node-role.kubernetes.io/master from existing control plane nodes."
- **[required] configuration** `present` `"node-role.kubernetes.io/master"`: The application or deployment selects nodes or places workloads using the node-role.kubernetes.io/master label. (confidence medium, judge partially_supported)
  - k8s_changelog@1.24: "the command will remove the label node-role.kubernetes.io/master from existing control plane nodes"
  - ⚠ The text does not state which workloads or tools rely on this label; this must be checked in the deployment.

Actions:
- Search manifests, scripts and automation for node-role.kubernetes.io/master and update selectors to node-role.kubernetes.io/control-plane before upgrading.
- Adapt infrastructure to the label change as the release note advises.

### kube-proxy older than allowed skew after apiserver upgrade

`kubernetes_9e61fc9ebd` · medium · confidence low · introduced in * · fires at upgrade

The item limits how far kube-proxy may lag kube-apiserver. When the apiserver is upgraded to 1.29 and kube-proxy stays on an older minor version beyond the allowed skew, the deployment is outside the supported skew.

- **[uncertain] version** `in_range` `{"applies_to": "every release hop on the upgrade path"}`: The upgrade crosses the release stated by the item (release * is not named in the text). (confidence low, judge partially_supported)
  - k8s_skew: "kube-proxy may be up to three minor versions older than kube-apiserver"
  - k8s_skew: "kube-proxy must not be newer than kube-apiserver."
  - k8s_skew: "kube-proxy may be up to three minor versions older or newer than the kubelet instance it runs alongside"
  - k8s_skew: "Running a cluster with kube-proxy instances that are persistently three minor versions behind kube-apiserver means they must be upgraded before the control plane can be upgraded."
  - k8s_skew: "kube-proxy must not be newer than kube-apiserver"
  - ⚠ The text states the change was introduced in release *, which is not specified; the version metadata provides no release number.
  - ⚠ The release is given as * in the source metadata, so the exact release that introduced this rule is not stated.
  - ⚠ The text does not name the release tied to this change, so it does not confirm the change applies to the 1.23 to 1.29 upgrade.
  - ⚠ The text uses unresolved skew placeholders and does not state the concrete kube-proxy version for the 1.23 to 1.29 jump.
- **[uncertain] deployment** `less_than` `"kube-apiserver minor version minus 3"`: The kube-proxy minor version is more than three minor versions older than the kube-apiserver minor version. (confidence low, judge not_supported)
  - k8s_skew: "kube-proxy may be up to three minor versions older than kube-apiserver"
  - k8s_skew: "kube-proxy must not be newer than kube-apiserver."
  - k8s_skew: "kube-proxy may be up to three minor versions older or newer than the kubelet instance it runs alongside"
  - k8s_skew: "kube-proxy instances that are persistently three minor versions behind kube-apiserver"
  - k8s_skew: "kube-proxy must not be newer than kube-apiserver"
  - ⚠ Judge: evidence does not support this claim. The quotes set the permitted skew at up to three minor versions and say persistently three-behind proxies must be upgraded. They do not state that a proxy more than three minor versions older exists or is permitted; that state falls outside the stated limit.
- **[uncertain] deployment** `less_than` `"kube-apiserver minor version minus 2 for kube-proxy below 1.25"`: The kube-proxy version is below 1.25 and is more than two minor versions older than kube-apiserver. (confidence low, judge not_supported)
  - k8s_skew: "kube-proxy < 1.25 may only be up to two minor versions older than kube-apiserver"
  - ⚠ Judge: evidence does not support this claim. The quote limits kube-proxy below 1.25 to at most two minor versions older than kube-apiserver. It does not say a proxy more than two minor versions older exists or is allowed; that state falls outside the stated limit.

Actions:
- Upgrade kube-proxy so its minor version is within the allowed skew of the target kube-apiserver version.
- Check kube-proxy versions on all nodes before and after the kube-apiserver upgrade.
- Upgrade kube-apiserver before upgrading kube-proxy so that kube-proxy is not newer than kube-apiserver.
- Check the kube-proxy and kube-apiserver versions in the cluster before and after each upgrade step.
- Compare the kubelet version on each node with the kube-proxy image version.
- Upgrade kube-proxy and kubelet so that the minor-version gap stays within the stated window at every step of the upgrade.
- Upgrade kube-proxy instances before upgrading the kube-apiserver control plane.
- Avoid leaving kube-proxy instances persistently three minor versions behind kube-apiserver.
- Upgrade kube-apiserver before kube-proxy so that kube-proxy is never newer than kube-apiserver.

### kubeadm upgrade plan --config component config for kube-proxy and kubelet

`kubernetes_beac686c4e` · medium · confidence medium · introduced in 1.29 · fires at upgrade

kubeadm no longer accepts component configuration for kube-proxy and kubelet during kubeadm upgrade plan --config. That option was legacy and was only usable at the plan stage to check whether cluster-stored component config needs manual version migration.

- **[required] version** `in_range` `{"current_version": "< 1.29", "target_version": ">= 1.29"}`: The upgrade crosses release 1.29, which stopped accepting kube-proxy and kubelet component configuration in kubeadm upgrade plan --config. (confidence high, judge supported)
  - k8s_changelog@1.29: "Stopped accepting component configuration for kube-proxy and kubelet during kubeadm upgrade plan --config."
- **[required] configuration** `present` `"kubeadm upgrade plan --config"`: The deployment uses kubeadm upgrade plan with the --config option to check kube-proxy or kubelet component configuration. (confidence medium, judge supported)
  - k8s_changelog@1.29: "could be used only at the plan stage to determine if the configuration for these components stored in the cluster needs manual version migration"
  - ⚠ The text does not state the exact failure mode when the removed --config option is used.

Actions:
- Check upgrade scripts and runbooks for kubeadm upgrade plan --config and remove or replace that step before upgrading to 1.29.
- Plan manual migration of kube-proxy and kubelet component configuration stored in the cluster, as the text says it may be needed.

### Admission/Policy registry allowlists need registry.k8s.io

`kubernetes_c19bd052ab` · medium · confidence medium · introduced in 1.25 · fires at rollout

A new image registry registry.k8s.io was introduced in 1.25. Admission or policy integrations with an allowlist of registries must include registry.k8s.io alongside k8s.gcr.io.

- **[required] version** `in_range` `{"current_version": "< 1.25", "target_version": ">= 1.25"}`: The upgrade crosses release 1.25, where the registry.k8s.io image registry was introduced. (confidence high, judge supported)
  - k8s_changelog@1.25: "There is a new OCI image registry (registry.k8s.io) that can be used to pull Kubernetes images."
- **[required] configuration** `present` `"allowlist of registries"`: The cluster uses an admission or policy integration with an allowlist of registries. (confidence medium, judge partially_supported)
  - k8s_changelog@1.25: "Admission/Policy integrations that have an allowlist of registries need to include registry.k8s.io alongside k8s.gcr.io."

Actions:
- Add registry.k8s.io alongside k8s.gcr.io in admission or policy registry allowlists before upgrading.
- Update air-gapped environments and image garbage-collection configurations to pre-pull and preserve images under registry.k8s.io as well as k8s.gcr.io.

### Pod topology spread skew now excludes nodes not matching node affinity/selector

`kubernetes_d9554c0e18` · medium · confidence medium · introduced in 1.24 · fires at upgrade

From 1.24 the Pod topology spread skew calculation excludes nodes that do not match the node affinity/selector. Pods that previously relied on matching pods on those excluded nodes may become unschedulable, especially when the topologyKey is not node-level.

- **[required] version** `in_range` `{"current_version": "< 1.24", "target_version": ">= 1.24"}`: The upgrade crosses release 1.24, where the Pod topology spread skew change was introduced. (confidence high, judge supported)
  - k8s_changelog@1.24: "The calculations for Pod topology spread skew now exclude nodes that don't match the node affinity/selector."
- **[required] configuration** `present` `"topology spread constraints"`: The cluster uses Pod topology spread constraints whose pods match the spreading selector on nodes that do not match the node affinity/selector. (confidence medium, judge partially_supported)
  - k8s_changelog@1.24: "This may lead to unschedulable pods if you previously had pods matching the spreading selector on those excluded nodes"
  - ⚠ The text does not state how to detect such placements; it only describes the condition.
- **[optional] configuration** `present` `"non-node-level topologyKey"`: The topologyKey used is not node-level. (confidence medium, judge partially_supported)
  - k8s_changelog@1.24: "especially when the topologyKey is not node-level"

Actions:
- Revisit the node affinity and/or pod selector in the topology spread constraints to avoid this scenario.

### EndpointSlice topology hostname key

`kubernetes_ddf8635e3c` · medium · confidence medium · introduced in 1.25 · fires at upgrade

Code that uses the deprecated topology hostname key on EndpointSlice must use the per Endpoint nodeName field instead.

- **[required] version** `in_range` `{"current_version": "< 1.25", "target_version": ">= 1.25"}`: The upgrade crosses release 1.25 (1.23 to 1.29). (confidence medium, judge partially_supported)
  - k8s_deprecation_guide: "The discovery.k8s.io/v1beta1 API version of EndpointSlice is no longer served as of v1.25."
- **[required] api_usage** `present` `"topology[\"kubernetes.io/hostname\"]"`: The application uses the topology hostname key on EndpointSlice objects. (confidence medium, judge supported)
  - k8s_deprecation_guide: "use per Endpoint nodeName field instead of deprecated topology["kubernetes.io/hostname"] field"
  - ⚠ The text does not state whether the deprecated key stops working or is only replaced.

Actions:
- Replace topology["kubernetes.io/hostname"] with the per Endpoint nodeName field.

### vSphere vCenter credentials in secret with Zones feature: node update RBAC for vsphere-legacy-cloud-provider

`kubernetes_de350dc7b2` · medium · confidence medium · introduced in 1.24 · fires at upgrade

Fixed bug with leads to Node goes Not-ready state when credentials for vCenter stored in a secret and Zones feature is in use. Zone labels setup moved to KCM component, kubelet skips this step during startup in such case. For proper functioning kube-system:vsphere-legacy-cloud-provider should be allowed to update node object if vCenter credentials stored in secret and Zone feature used.

- **[required] version** `in_range` `{"current_version": "< 1.24", "target_version": ">= 1.24"}`: The change is introduced in release 1.24, so the upgrade from 1.23 to 1.29 crosses release 1.24. (confidence high, judge supported)
  - k8s_changelog@1.24: "Fixed bug with leads to Node goes Not-ready state when credentials for vCenter stored in a secret and Zones feature is in use."
- **[required] configuration** `equals` `"vCenter credentials in secret and Zones feature in use"`: The cluster uses vCenter credentials stored in a secret and the Zones feature is in use. (confidence high, judge supported)
  - k8s_changelog@1.24: "when credentials for vCenter stored in a secret and Zones feature is in use"
- **[disqualifying] configuration** `equals` `"credentials stored in cloud-provider config file as plaintext"`: Credentials are stored in the cloud-provider config file as plaintext, in which case the behavior does not change. (confidence high, judge supported)
  - k8s_changelog@1.24: "If credentials stored in cloud-provider config file as plaintext current behaviour does not change and no action required."
- **[required] configuration** `present` `"kube-system:vsphere-legacy-cloud-provider permitted to update node objects"`: The kube-system:vsphere-legacy-cloud-provider identity is permitted to update node objects. (confidence medium, judge partially_supported)
  - k8s_changelog@1.24: "should be allowed to update node object"
  - ⚠ The text does not state the exact RBAC resource or verbs to grant, nor what symptoms occur if the permission is absent.

Actions:
- Confirm vCenter credentials are stored in a secret and the Zones feature is in use before upgrading.
- Ensure kube-system:vsphere-legacy-cloud-provider is allowed to update node objects before the upgrade.
- Verify that zone labels are set by the KCM component after upgrade.

### csiMigrationRBD feature gate misspelling

`kubernetes_e5b62c5ec0` · medium · confidence medium · introduced in 1.24 · fires at upgrade

The feature gate name was documented as csiMigrationRBD but the correct name is CSIMigrationRBD. Users who configured the feature gate as csiMigrationRBD must reconfigure it to CSIMigrationRBD from release 1.24 onward.

- **[required] version** `in_range` `{"current_version": "< 1.24", "target_version": ">= 1.24"}`: The upgrade crosses release 1.24, where the feature gate name was corrected to CSIMigrationRBD. (confidence high, judge supported)
  - k8s_changelog@1.24: "This release correct the same and keep it as CSIMigrationRBD."
- **[required] configuration** `present` `"csiMigrationRBD"`: The application or deployment configures the feature gate using the name csiMigrationRBD. (confidence medium, judge supported)
  - k8s_changelog@1.24: "users who have configured this feature gate as csiMigrationRBD"
  - ⚠ The text does not state what happens to a configuration that uses the misspelled name after the upgrade, such as whether it is ignored or rejected.
- **[uncertain] configuration** `present` `"CSIMigrationRBD"`: The feature gate is already configured with the corrected name CSIMigrationRBD, so no reconfiguration is needed. (confidence low, judge not_supported)
  - k8s_changelog@1.24: "has to reconfigure the same to CSIMigrationRBD"
  - ⚠ Judge: evidence does not support this claim. The quote says users have to reconfigure the gate to CSIMigrationRBD, which contradicts the claim that no reconfiguration is needed.

Actions:
- Reconfigure the feature gate from csiMigrationRBD to CSIMigrationRBD before or after upgrading to release 1.24 or later.

### Dashboard cluster addon removed

`kubernetes_f99278a4ed` · medium · confidence medium · introduced in 1.24 · fires at upgrade

The cluster addon for dashboard was removed in 1.24. Clusters that relied on the dashboard addon need to install dashboard separately.

- **[required] version** `in_range` `{"current_version": "< 1.24", "target_version": ">= 1.24"}`: The upgrade crosses release 1.24, in which the dashboard cluster addon was removed. (confidence high, judge supported)
  - k8s_changelog@1.24: "The cluster addon for dashboard was removed."
- **[required] deployment** `present` `"dashboard cluster addon"`: The cluster uses the dashboard cluster addon that was removed. (confidence medium, judge supported)
  - k8s_changelog@1.24: "The cluster addon for dashboard was removed."
  - ⚠ The text does not state how the dashboard addon was installed or which resources it created.
  - ⚠ The text references a link ("see here") for installing dashboard, but the link target is not included in the provided text.

Actions:
- Check whether the cluster runs or depends on the dashboard addon before upgrading.
- If dashboard is needed after the upgrade, install it separately using the instructions referenced in the release notes (link not included in the provided text).

### Alpha seccomp annotations removed

`kubernetes_fea98e9bba` · medium · confidence medium · introduced in 1.27 · fires at upgrade

The alpha seccomp annotations seccomp.security.alpha.kubernetes.io/pod and container.seccomp.security.alpha.kubernetes.io have been completely removed. Seccomp fields are no longer auto-populated from these annotations when pods are created, so pods that depend on them need migration to the securityContext.seccompProfile field.

- **[required] version** `in_range` `{"current_version": "< 1.27", "target_version": ">= 1.27"}`: The upgrade from 1.23 to 1.29 crosses release 1.27, in which the alpha seccomp annotations were removed. (confidence medium)
  - k8s_changelog@1.27: "now have been completely removed"
  - k8s_changelog@1.25: "seccomp.security.alpha.kubernetes.io/pod and container.seccomp.security.alpha.kubernetes.io"
  - ⚠ History: in 1.25, 'Pods using alpha seccomp annotations' applied to the same symbol (seccomp.security.alpha.kubernetes.io/pod); superseded by the 1.27 change (R2).
- **[required] configuration** `present` `"seccomp.security.alpha.kubernetes.io/pod"`: Application pods use the alpha seccomp annotation seccomp.security.alpha.kubernetes.io/pod or container.seccomp.security.alpha.kubernetes.io. (confidence high, judge supported)
  - k8s_changelog@1.27: "seccomp.security.alpha.kubernetes.io/pod and container.seccomp.security.alpha.kubernetes.io"
- **[required] behavior** `present` `"seccomp annotations on pod creation"`: Pods with seccomp annotations no longer get their seccomp fields auto-populated when created. (confidence medium, judge supported)
  - k8s_changelog@1.27: "The seccomp fields are no longer auto-populated when pods with seccomp annotations are created."
  - ⚠ The text does not state what runtime behavior results for pods whose seccomp fields are no longer populated.
- **[disqualifying] api_usage** `present` `"securityContext.seccompProfile"`: Pods already set the securityContext.seccompProfile field instead of the removed annotations. (confidence medium, judge partially_supported)
  - k8s_changelog@1.27: "Pods should use the corresponding pod or container securityContext.seccompProfile field instead."

Actions:
- Find pods and pod templates that set seccomp.security.alpha.kubernetes.io/pod or container.seccomp.security.alpha.kubernetes.io annotations.
- Replace these annotations with the pod or container securityContext.seccompProfile field before upgrading.

### Removed feature gates ValidateProxyRedirects and StreamingProxyRedirects

`kubernetes_0ef6155acc` · low · confidence high · introduced in 1.24 · fires at upgrade

Feature gates ValidateProxyRedirects and StreamingProxyRedirects were removed in 1.24. Clusters that set these gates in their configuration may need that configuration changed. The text does not state what happens when a removed gate is still set.

- **[required] version** `in_range` `{"current_version": "< 1.24", "target_version": ">= 1.24"}`: The upgrade crosses release 1.24, where the feature gates are removed. (confidence high, judge supported)
  - k8s_changelog@1.24: "Remove deprecated feature gates ValidateProxyRedirects and StreamingProxyRedirects"
- **[required] configuration** `present` `"ValidateProxyRedirects or StreamingProxyRedirects"`: The cluster configuration sets feature gate ValidateProxyRedirects or StreamingProxyRedirects. (confidence high, judge supported)
  - k8s_changelog@1.24: "Remove deprecated feature gates ValidateProxyRedirects and StreamingProxyRedirects"
- **[uncertain] behavior** `unknown` `""`: Setting a removed feature gate causes a failure or is ignored after the upgrade. (confidence low, judge partially_supported)
  - k8s_changelog@1.24: "Remove deprecated feature gates ValidateProxyRedirects and StreamingProxyRedirects"
  - ⚠ The text states only that the feature gates are removed. It does not state the effect of setting them after removal.

Actions:
- Search configuration for the removed feature gate names before upgrading.
- Remove ValidateProxyRedirects and StreamingProxyRedirects from feature gate settings if present.

### CephFS in-tree volume plugin deprecation

`kubernetes_0ffaca21b0` · low · confidence medium · introduced in 1.28 · fires at future_removal

The kubernetes.io/cephfs volume plugin is deprecated in this release and will be removed in a later release; workloads using it should move to the CephFS CSI driver.

- **[required] version** `in_range` `{"current_version": "< 1.28", "target_version": ">= 1.28"}`: Upgrade crosses release 1.28, in which the CephFS volume plugin was deprecated (confidence high, judge supported)
  - k8s_changelog@1.28: "CephFS volume plugin (kubernetes.io/cephfs) has been deprecated in this release"
- **[required] configuration** `present` `"kubernetes.io/cephfs"`: Cluster uses the in-tree kubernetes.io/cephfs volume plugin (confidence medium, judge supported)
  - k8s_changelog@1.28: "CephFS volume plugin (kubernetes.io/cephfs) has been deprecated in this release"
  - ⚠ The text does not state the release in which the CephFS plugin will be removed, only a subsequent release.

Actions:
- Migrate CephFS volumes to the CephFS CSI driver (https://github.com/ceph/ceph-csi/).

### RBD in-tree volume plugin deprecation

`kubernetes_305dd46055` · low · confidence medium · introduced in 1.28 · fires at future_removal

The kubernetes.io/rbd volume plugin is deprecated in this release and will be removed in a later release; workloads using it should move to the RBD CSI driver.

- **[required] version** `in_range` `{"current_version": "< 1.28", "target_version": ">= 1.28"}`: Upgrade crosses release 1.28, in which the RBD volume plugin was deprecated (confidence high, judge supported)
  - k8s_changelog@1.28: "RBD volume plugin (kubernetes.io/rbd) has been deprecated in this release"
- **[required] configuration** `present` `"kubernetes.io/rbd"`: Cluster uses the in-tree kubernetes.io/rbd volume plugin (confidence medium, judge supported)
  - k8s_changelog@1.28: "RBD volume plugin (kubernetes.io/rbd) has been deprecated in this release"
  - ⚠ The text does not state the release in which the RBD plugin will be removed, only a subsequent release.

Actions:
- Migrate RBD volumes to the RBD CSI driver (https://github.com/ceph/ceph-csi/).

### Removed insecure serving configuration in cloud-provider package

`kubernetes_3d5dbb8cc8` · low · confidence medium · introduced in 1.24 · fires at upgrade

The cloud-provider package, consumed by cloud-controller-managers, had its insecure serving configuration removed. Code or builds that depend on that configuration may be affected at upgrade. The text does not state the exact symbols removed or the replacement.

- **[required] version** `in_range` `{"current_version": "< 1.24", "target_version": ">= 1.24"}`: The upgrade crosses release 1.24, the release that introduced the removal. (confidence high, judge supported)
  - k8s_changelog@1.24: "Remove insecure serving configuration from cloud-provider package, which is consumed by cloud-controller-managers"
- **[required] configuration** `present` `"insecure serving configuration in cloud-provider"`: The deployment runs a cloud-controller-manager or build that uses the cloud-provider package's insecure serving configuration. (confidence medium, judge supported)
  - k8s_changelog@1.24: "Remove insecure serving configuration from cloud-provider package, which is consumed by cloud-controller-managers"
  - ⚠ The text does not state which insecure serving settings were removed, what replaces them, or what breaks when they are absent.

Actions:
- Check custom or forked cloud-controller-manager builds for use of insecure serving configuration from the cloud-provider package.
- Consult the Kubernetes v1.24.0 changelog or the cloud-provider package source for the replacement configuration, which the text does not state.

### metadata.clusterName accidental client use

`kubernetes_517a769c03` · low · confidence high · introduced in 1.24 · fires at future_removal

The metadata.clusterName field is deprecated and its Go struct name was changed so that accidental client uses are found before complete removal. Clients that reference this field may be affected.

- **[required] version** `in_range` `{"current_version": "< 1.24", "target_version": ">= 1.24"}`: The upgrade crosses release 1.24, the release in which the metadata.clusterName change was introduced. (confidence high, judge supported)
  - k8s_changelog@1.24: "Out of an abundance of caution, this release we have merely changed the name in the go struct"
- **[required] api_usage** `present` `"metadata.clusterName"`: The application or deployment uses the metadata.clusterName field or the Go struct field ClusterName. (confidence high, judge supported)
  - k8s_changelog@1.24: "The metadata.clusterName field is deprecated."
- **[uncertain] behavior** `unknown` `""`: The metadata.clusterName field is removed in a later release. (confidence low, judge supported)
  - k8s_changelog@1.24: "its presence is confusing, so we will remove it next release"
  - ⚠ The text does not state whether the field has been removed by Kubernetes 1.29.

Actions:
- Search manifests, clients and Go code for metadata.clusterName and ClusterName and remove any uses.
- Do not rely on metadata.clusterName, since the field is always unwritable and always blank according to the release notes.

### Ceph RBD CSI migration support deprecation

`kubernetes_8c73624e95` · low · confidence medium · introduced in 1.28 · fires at future_removal

Support for CSI migration of Ceph RBD volumes is deprecated in this release; users relying on migration to an out-of-tree storage driver should complete it before support is removed.

- **[required] version** `in_range` `{"current_version": "< 1.28", "target_version": ">= 1.28"}`: Upgrade crosses release 1.28, in which support for CSI migration of Ceph RBD volumes was deprecated (confidence high, judge supported)
  - k8s_changelog@1.28: "Deprecated support for CSI migration of Ceph RBD volumes."
- **[required] configuration** `present` `"CSI migration"`: Cluster relies on Kubernetes CSI migration of Ceph RBD volumes to an out-of-tree storage driver (confidence medium, judge partially_supported)
  - k8s_changelog@1.28: "Users who were relying on Kubernetes' ability to migrate to an out-of-tree storage driver"
  - ⚠ The text does not name the feature gate or setting that enables the migration, and does not state the release in which support is removed.

Actions:
- Complete the migration to the out-of-tree storage driver before support for CSI migration of Ceph RBD volumes is removed.

### PriorityLevelConfiguration nominalConcurrencyShares default and explicit zero

`kubernetes_f2ea0031b7` · low · confidence medium · introduced in 1.29 · fires at upgrade

The spec.limited.nominalConcurrencyShares field defaults to 30 only when unspecified, and an explicit value of 0 is not changed to 30.

- **[required] version** `in_range` `{"current_version": "< 1.29", "target_version": ">= 1.29"}`: The change is introduced in release 1.29 and the upgrade from 1.23 crosses release 1.29. (confidence medium, judge partially_supported)
  - k8s_deprecation_guide: "only defaults to 30 when unspecified, and an explicit value of 0 is not changed to 30"
- **[required] configuration** `equals` `"0"`: The application or deployment sets spec.limited.nominalConcurrencyShares to an explicit value of 0 in a PriorityLevelConfiguration. (confidence medium, judge partially_supported)
  - k8s_deprecation_guide: "only defaults to 30 when unspecified, and an explicit value of 0 is not changed to 30"
  - ⚠ The text does not state what value an explicit 0 was treated as in earlier versions, so the size of the behavior change is not stated.

Actions:
- Review PriorityLevelConfiguration objects that set nominalConcurrencyShares to 0 and confirm the intended concurrency value after the upgrade.
- Set nominalConcurrencyShares explicitly when a specific value is required rather than relying on the default.

### Deprecated API versions no longer served in v1.25

`kubernetes_9c957094cf` · unknown · confidence medium · introduced in 1.25 · fires at upgrade

The v1.25 release stopped serving deprecated API versions. The item is truncated and does not list the specific API versions, so the affected symbols cannot be identified from the text provided.

- **[required] version** `in_range` `{"current_version": "< 1.25", "target_version": ">= 1.25"}`: The upgrade crosses Kubernetes release v1.25 (from 1.23 to 1.29). (confidence medium, judge partially_supported)
  - k8s_deprecation_guide: "The v1.25 release stopped serving the following deprecated API versions:"
  - ⚠ The item does not name the API versions in the list, so the version-specific change cannot be matched to a concrete resource type.
- **[uncertain] api_usage** `present` `"deprecated API version removed in v1.25"`: The application or deployment uses one of the deprecated API versions that v1.25 stopped serving. (confidence low, judge supported)
  - k8s_deprecation_guide: "stopped serving the following deprecated API versions"
  - ⚠ The item text ends before the list of removed API versions, so the specific apiVersion strings that would be checked are not stated.

Actions:
- Obtain the full list of API versions removed in v1.25 from the Kubernetes Deprecated API Migration Guide, section Removed APIs by release / v1.25.
- Search manifests, Helm charts and client code for each listed apiVersion and migrate them to a version served by the target cluster before upgrading.

## Review checklist

### Low confidence or disputed

- [ ] kubernetes_70f592d3da: Removed deprecated API versions in v1.29
- [ ] kubernetes_ab919afc13: PodSecurityPolicy admission plugin removed in 1.25
- [ ] kubernetes_9e61fc9ebd: kube-proxy older than allowed skew after apiserver upgrade
- [ ] kubernetes_e5b62c5ec0: csiMigrationRBD feature gate misspelling

### Inferred conditions

- [ ] kubernetes_70f592d3da: The application or deployment uses one of the deprecated API versions that v1.29 stopped serving
- [ ] kubernetes_e82868187c: The Service already sets spec.publishNotReadyAddresses instead of the annotation.
- [ ] kubernetes_9c957094cf: The application or deployment uses one of the deprecated API versions that v1.25 stopped serving.

### Source disagreements

- remediation for kubernetes_997b64cd86: Per-release guidance names flowcontrol.apiserver.k8s.io/v1beta2, which is removed in v1.29. → Remediation recomputed against the target version (R3).

### Open questions

- Only 'Urgent Upgrade Notes' and 'Changes by Kind / Deprecation' of each CHANGELOG were mined; 'API Change' and 'Feature' entries may hide further behavior changes.
- Managed distributions (EKS, GKE, AKS, OpenShift) add their own upgrade constraints that are not in upstream docs.
- Third-party controllers, CNI/CSI drivers, Helm charts and admission webhooks may use removed APIs; compatibility depends on their own releases.
- [kubernetes_1a5432e398] Unconfirmed: The .spec.timeZone replacement is supported only on clusters in v1.25 or later with default configurations. (The text does not state what happens to .spec.timeZone on clusters with non-default configurations.)
- [kubernetes_ab919afc13] Unconfirmed: The cluster uses the PodSecurityPolicy admission plugin. (The text does not state how the plugin is enabled or configured in a cluster.)
- [kubernetes_baa4052480] Unconfirmed: The cluster serves the ClusterCIDR alpha API before the upgrade. (The text does not state whether the ClusterCIDR alpha API was enabled or served by default in release 1.23.)
- [kubernetes_0214e6aee0] Unconfirmed: The application or cluster uses HNS v1 APIs. (The text does not state which components or software use the HNS v1 APIs, or how they would be affected.)
- [kubernetes_8a1e841ec0] Unconfirmed: The removed flags are only inert when kube-apiserver runs and do not change behavior before the removal. (The text does not state what happens to a configuration that still passes the removed flags after the upgrade.)
- [kubernetes_9e61fc9ebd] Unconfirmed: The upgrade crosses the release stated by the item (release * is not named in the text). (The text states the change was introduced in release *, which is not specified; the version metadata provides no release number.)
- [kubernetes_9e61fc9ebd] Unconfirmed: The kube-proxy minor version is more than three minor versions older than the kube-apiserver minor version. (Judge: evidence does not support this claim. The quotes set the permitted skew at up to three minor versions and say persistently three-behind proxies must be upgraded. They do not state that a proxy )
- [kubernetes_9e61fc9ebd] Unconfirmed: The kube-proxy version is below 1.25 and is more than two minor versions older than kube-apiserver. (Judge: evidence does not support this claim. The quote limits kube-proxy below 1.25 to at most two minor versions older than kube-apiserver. It does not say a proxy more than two minor versions older )
- [kubernetes_e5b62c5ec0] Unconfirmed: The feature gate is already configured with the corrected name CSIMigrationRBD, so no reconfiguration is needed. (Judge: evidence does not support this claim. The quote says users have to reconfigure the gate to CSIMigrationRBD, which contradicts the claim that no reconfiguration is needed.)
- [kubernetes_0ef6155acc] Unconfirmed: Setting a removed feature gate causes a failure or is ignored after the upgrade. (The text states only that the feature gates are removed. It does not state the effect of setting them after removal.)
- [kubernetes_517a769c03] Unconfirmed: The metadata.clusterName field is removed in a later release. (The text does not state whether the field has been removed by Kubernetes 1.29.)
- [kubernetes_9c957094cf] Unconfirmed: The application or deployment uses one of the deprecated API versions that v1.25 stopped serving. (The item text ends before the list of removed API versions, so the specific apiVersion strings that would be checked are not stated.)

## Context facts (not risks)

- (1.24) VSphere releases less than 7.0u2 are deprecated as of v1.24. — _The item describes deprecations only. It says vSphere releases less than 7.0u2 are deprecated as of v1.24 and recommends upgrading vSphere, and it says support for these deprecations will be available till October 15, 2022. It does not state that anything is removed or breaks at upgrade, so it needs no required action for the 1.23 to 1.29 upgrade beyond the recommendation to upgrade vSphere._
- (1.28) Removed tracking annotation from validation and defaulting. — _The item states only that a tracking annotation was removed from validation and defaulting in v1.28.0. It does not name the annotation, any API or setting affected, or any user action, so the text states no concrete breakage or migration step for 1.23 to 1.29 upgrades._
- (1.28) Removed withdrawn feature NetworkPolicyStatus. — _The item states only that the withdrawn feature NetworkPolicyStatus was removed in v1.28.0. The text does not name any API, setting, or user action that applications or deployments must change, so no upgrade risk path can be stated from it._
- (*) {{< note >}} If version skew exists between kube-apiserver instances in an HA cluster, this narrows the allowed kubelet versions. — _The item is a policy clarification from the Kubernetes Version Skew Policy. It states that kube-apiserver version skew in an HA cluster narrows the allowed kubelet versions. It does not describe a removed API, changed default, changed behavior, or new requirement for 1.23 to 1.29, so it needs no user action as a risk item._
- (*) {{< note >}} If version skew exists between kube-apiserver instances in an HA cluster, this narrows the allowed kube-proxy versions. — _The item is a note restating a version skew constraint: when kube-apiserver instances in an HA cluster differ in version, the allowed kube-proxy versions are narrowed. It does not name an API, setting, default, or requirement that changes in this release, and the text does not tie the constraint to the 1.23 to 1.29 upgrade. It describes an existing policy rather than a change that breaks an app or deployment, so no risk path is produced._
- (1.29) All existing persisted objects are accessible via the new API — _It states that existing persisted objects remain accessible through the new API, which indicates no data migration is needed._
- (1.27) The v1.27 release stopped serving the following deprecated API versions: — _This is a section heading introducing the list of removed API versions, with no actionable change stated by itself._
- (1.27) All existing persisted objects are accessible via the new API — _It states that existing persisted objects remain accessible via the new API, meaning no data migration is needed, though it is informational._
- (1.26) The v1.26 release stopped serving the following deprecated API versions: — _The heading-like sentence only introduces the list of removed API versions and contains no actionable change by itself._
- (1.26) All existing persisted objects are accessible via the new API — _Stating that persisted objects remain accessible via the new API indicates no data migration is needed, though it is informational._
- (1.25) All existing persisted objects are accessible via the new API — _It states existing persisted objects remain accessible through the new API, so no data migration is needed, though it is reassuring rather than a required action._
- (1.24) kubeadm.k8s.io/v1beta2 has been deprecated and will be removed in a future release, possibly in 3 releases (one year). — _kubeadm.k8s.io/v1beta2 is deprecated with removal only planned for a future release, so it still works and the item notes a migration command without requiring action now._
- (1.24) Deprecated Service.Spec.LoadBalancerIP. This field was under-specified and its meaning varies across implementations. — _Service.spec.loadBalancerIP is deprecated but still functions, and the item only encourages annotations with no required action in this release._
- (1.24) Kube-apiserver: the --master-count flag and --endpoint-reconciler-type=master-count reconciler are deprecated in favor of the lease reconciler — _The --master-count flag and master-count reconciler are deprecated in favor of the lease reconciler but still work, so this is a warning only._
- (1.24) The --pod-infra-container-image kubelet flag is deprecated and will be removed in future releases — _The --pod-infra-container-image kubelet flag is deprecated with removal only in future releases, so it still works today and requires no action now._
- (1.24) The in-tree Azure plugin has been deprecated. — _The in-tree Azure plugin is only deprecated and logs a warning, with an out-of-tree replacement named and no removal in this release._
- (1.25) Ginkgo.Measure has been deprecated in Ginkgo V2, switch to use gomega/gmeasure instead — _Ginkgo.Measure is deprecated only inside the Kubernetes e2e test framework and still works, so it does not affect application or deployment users._
- (1.25) GlusterFS provisioner (kubernetes.io/glusterfs) has been deprecated in this release. — _The GlusterFS provisioner is deprecated but still functions in this release, so it is a warning with no required action yet._
- (1.26) CLI flag pod-eviction-timeout is deprecated and will be removed together with enable-taint-manager in v1.27. — _The pod-eviction-timeout CLI flag is only deprecated, still works in v1.26, and is scheduled for removal in v1.27._
- (1.26) Kube-apiserver: the unused --master-service-namespace flag was deprecated and will be removed in v1.27. — _The unused --master-service-namespace flag is deprecated with removal in v1.27, so it still works and needs no action now._
- (1.27) Added a warning response when handling requests that set the deprecated spec.externalID field for a Node. — _Requests setting the deprecated spec.externalID Node field now get a warning, but the field still works, so no action is required at this release._
- (1.27) Added warnings to the Services API. Kubernetes now warns for Services in the case of: - IPv4 addresses with leading zeros - IPv6 address in non-canonical format (RFC 5952) — _Services now produce warnings for leading-zero IPv4 and non-canonical IPv6 addresses, which are warning-only and need no user action._
- (1.27) The SecurityContextDeny admission plugin is going deprecated and will be removed in future versions. — _The SecurityContextDeny admission plugin is deprecated and still functions, so it is a future-removal notice with no action needed at this release._
- (1.28) Kube-controller-manager deprecate --volume-host-cidr-denylist and --volume-host-allow-local-loopback flags. — _The kube-controller-manager flags are only deprecated in this release, so they still work and require no immediate user action._
- (1.28) Kubelet: The --azure-container-registry-config flag has been deprecated and will be removed in a future release, please use --image-credential-provider-config and --image-credential-provider-bin-dir to setup acr credential provider instead. — _The kubelet --azure-container-registry-config flag is deprecated with removal planned for a future release, but it still works now._
- (1.28) KMSv1 is deprecated and will only receive security updates going forward. — _KMSv1 is deprecated and receives only security updates, but it remains usable now and the feature-gate instruction applies only to a future release._
- (*) Kubernetes versions are expressed as x.y.z, where x is the major version, y is the minor version, and z is the patch version, following Semantic Versioning terminology. — _It describes the patch-support policy for release branches and requires no user action at this upgrade._
- (*) newest kube-apiserver is at {{< skew currentVersion >}} — _It is a labeled example line showing the newest kube-apiserver at the current version._
- (*) other kube-apiserver instances are supported at {{< skew currentVersion >}} and {{< skew currentVersionAddMinor -1 >}} — _It is an example showing other kube-apiserver instances supported at the current and previous minor versions._
- (*) kube-apiserver is at {{< skew currentVersion >}} — _It is an example line showing kube-apiserver at the current version._
- (*) kubelet is supported at {{< skew currentVersion >}}, {{< skew currentVersionAddMinor -1 >}}, {{< skew currentVersionAddMinor -2 >}}, and {{< skew currentVersionAddMinor -3 >}} — _It lists the kubelet versions supported with the current kube-apiserver, which is informational and needs no action._
- (*) kube-apiserver instances are at {{< skew currentVersion >}} and {{< skew currentVersionAddMinor -1 >}} — _It is an example showing kube-apiserver instances at the current and previous minor versions._
- (*) kubelet is supported at {{< skew currentVersionAddMinor -1 >}}, {{< skew currentVersionAddMinor -2 >}}, and {{< skew currentVersionAddMinor -3 >}} ({{< skew currentVersion >}} is not supported because that would be newer than the kube-apiserver instance at version {{< skew — _It is an explanatory example stating which kubelet versions are not supported because they would be newer than kube-apiserver._
- (*) kube-proxy is supported at {{< skew currentVersion >}}, {{< skew currentVersionAddMinor -1 >}}, {{< skew currentVersionAddMinor -2 >}}, and {{< skew currentVersionAddMinor -3 >}} — _It lists the kube-proxy versions supported with the current kube-apiserver, which is informational and needs no action._
- (*) kube-proxy is supported at {{< skew currentVersionAddMinor -1 >}}, {{< skew currentVersionAddMinor -2 >}}, and {{< skew currentVersionAddMinor -3 >}} ({{< skew currentVersion >}} is not supported because that would be newer than the kube-apiserver instance at version {{< skew — _It is an example listing supported kube-proxy versions and explaining why the current version is excluded._
- (*) kube-controller-manager, kube-scheduler, and cloud-controller-manager are supported at {{< skew currentVersion >}} and {{< skew currentVersionAddMinor -1 >}} — _States which control plane component versions are supported with the target kube-apiserver, which is accurate reference information that needs no action by itself._
- (*) {{< note >}} If version skew exists between kube-apiserver instances in an HA cluster, and these components can communicate with any kube-apiserver instance in the cluster (for example, via a load balancer), this narrows the allowed versions of these components. — _The note explains that HA kube-apiserver version skew narrows the allowed versions of other components, which is informational guidance._
- (*) kube-controller-manager, kube-scheduler, and cloud-controller-manager communicate with a load balancer that can route to any kube-apiserver instance — _Describes how controller-manager, scheduler, and cloud-controller-manager reach kube-apiserver through a load balancer, which is a descriptive statement._
- (*) kube-controller-manager, kube-scheduler, and cloud-controller-manager are supported at {{< skew currentVersionAddMinor -1 >}} ({{< skew currentVersion >}} is not supported because that would be newer than the kube-apiserver instance at version {{< skew currentVersionAddMinor -1 >}}) — _Gives the supported version range for control plane components, explaining why the target version is excluded, with no action required._
- (*) kubectl is supported within one minor version (older or newer) of kube-apiserver. — _States the kubectl version skew policy of one minor version either way, which is reference information._
- (*) kubectl is supported at {{< skew currentVersionAddMinor 1 >}}, {{< skew currentVersion >}}, and {{< skew currentVersionAddMinor -1 >}} — _Lists the kubectl versions supported against the kube-apiserver, which is reference information._
- (*) {{< note >}} If version skew exists between kube-apiserver instances in an HA cluster, this narrows the supported kubectl versions. — _The note says HA apiserver version skew narrows supported kubectl versions, which is informational._
- (*) kubectl is supported at {{< skew currentVersion >}} and {{< skew currentVersionAddMinor -1 >}} (other versions would be more than one minor version skewed from one of the kube-apiserver components) — _Lists the supported kubectl versions and explains why others are excluded, which is reference information._
- (1.32) Scheduled for removal in 1.32 (after target 1.29): The v1.32 release stopped serving the following deprecated API versions: — _Still works at 1.29; it is removed only in 1.32, after the target (R6)._
- (1.32) Scheduled for removal in 1.32 (after target 1.29): The flowcontrol.apiserver.k8s.io/v1beta3 API version of FlowSchema and PriorityLevelConfiguration is no longer served as of v1.32. — _Still works at 1.29; it is removed only in 1.32, after the target (R6)._
- (1.32) Scheduled for removal in 1.32 (after target 1.29): Migrate manifests and API clients to use the flowcontrol.apiserver.k8s.io/v1 API version, available since v1.29. — _Still works at 1.29; it is removed only in 1.32, after the target (R6)._
- (1.32) Scheduled for removal in 1.32 (after target 1.29): All existing persisted objects are accessible via the new API — _Still works at 1.29; it is removed only in 1.32, after the target (R6)._
- (1.32) Scheduled for removal in 1.32 (after target 1.29): Notable changes in flowcontrol.apiserver.k8s.io/v1: * The PriorityLevelConfiguration spec.limited.nominalConcurrencyShares field only defaults to 30 when unspecified, and an explicit value of 0 is not changed to 30. — _Still works at 1.29; it is removed only in 1.32, after the target (R6)._

## Disqualified candidates


## Sources

| Source | Type | Tier | Status | Pinned ref |
|---|---|---|---|---|
| [k8s_changelog@1.24](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md) | official_changelog | 1 | used | `master@52e85074042f` |
| [k8s_changelog@1.25](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md) | official_changelog | 1 | used | `master@d9c7616d4b2f` |
| [k8s_changelog@1.26](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md) | official_changelog | 1 | used | `master@60aee81561a5` |
| [k8s_changelog@1.27](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md) | official_changelog | 1 | used | `master@29e4f5a893bf` |
| [k8s_changelog@1.28](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md) | official_changelog | 1 | used | `master@c8681531abd8` |
| [k8s_changelog@1.29](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md) | official_changelog | 1 | used | `master@3eaa04785092` |
| [k8s_deprecation_guide](https://kubernetes.io/docs/reference/using-api/deprecation-guide/) | official_deprecation_notice | 1 | used | `main@9f1af2971c32` |
| [k8s_skew](https://kubernetes.io/releases/version-skew-policy/) | official_api_docs | 1 | used | `main@03c191bcc446` |

## What we trusted and what we did not

- Trusted: package metadata for version numbers; official guides, release notes and changelogs pinned to a tag, branch or commit.
- Not trusted: LLM self-reported confidence, unpinned current pages when they disagree with pinned ones, any quote that fails exact match, transclusion stubs.
