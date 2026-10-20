# Next.js 12 → 14: upgrade risk report

> Documentation-derived risk conditions; not a migration plan.

Next.js 12 -> 14 crosses 2 release(s) (13, 14). 19 risk paths: 1 critical, 7 high, 7 medium, 4 low. Main risk types: removed_api (7), changed_behavior (5), dependency_requirement (3). Critical: Node.js requirement raised to >=18.17.0. 1 context facts and 0 disqualified candidates are listed separately. Documentation-derived risk conditions; not a migration plan.

Overall confidence: **medium**. Validation: `{"errors": 0, "warnings": 2, "by_code": {"W4_no_search_queries": 2}}`

## Risk paths

| Level | Confidence | Type | Surface | Release | Path |
|---|---|---|---|---|---|
| critical | high | runtime_requirement | runtime | 14 | `nextjs_f3317b5b79` Node.js requirement raised to >=18.17.0 |
| high | high | dependency_requirement | dependencies | 13 | `nextjs_2323185baa` React minimum version raised to 18.2.0 |
| high | high | removed_api | application_code | 13 | `nextjs_24962734e7` next/future/image import renamed to next/image |
| high | high | dependency_requirement | dependencies | 14 | `nextjs_4315b5fb92` React (peer dependency) requirement raised to ^18.2.0 |
| high | high | changed_behavior | application_code | 13 | `nextjs_523375afdf` next/link child <a> no longer supported |
| high | high | removed_api | application_code | 14 | `nextjs_5a5f2f6714` next export command removed |
| high | high | removed_api | dependencies | 14 | `nextjs_8392155aea` @next/font package removed in favor of built-in next/font |
| high | medium | removed_api | application_code | 14 | `nextjs_fea20fefe0` ImageResponse import moved from next/server to next/og |
| medium | medium | changed_behavior | application_code | 13 | `nextjs_1300ee090f` Link component nested anchor child |
| medium | high | changed_default | configuration | 13 | `nextjs_16494e4a2c` swcMinify default changed to true |
| medium | high | removed_api | application_code | 13 | `nextjs_1c253f96bf` next/image import renamed to next/legacy/image |
| medium | medium | configuration_change | configuration | 13 | `nextjs_1e5e6decf1` target configuration property removed |
| medium | high | changed_default | application_code | 13 | `nextjs_2ba045f66c` next/image default behavior changed in Next.js 13 |
| medium | medium | removed_api | configuration | 13 | `nextjs_67098be47b` Removed target configuration property |
| medium | medium | changed_behavior | runtime | 13 | `nextjs_c5a065b9b5` Internet Explorer support dropped in v13 |
| low | medium | changed_behavior | runtime | 13 | `nextjs_2a246a90c5` Internet Explorer support dropped |
| low | medium | removed_api | dependencies | 14 | `nextjs_539d9094ea` next-swc WASM target removal |
| low | medium | changed_behavior | application_code | 13 | `nextjs_b09465bce4` next/script behavior change |
| low | medium | dependency_requirement | dependencies | 14 | `nextjs_fdd92fa177` TypeScript projects must upgrade @types/react and @types/react-dom |

### Node.js requirement raised to >=18.17.0

`nextjs_f3317b5b79` · critical · confidence high · introduced in 14 · fires at upgrade

Package metadata changes the Node.js requirement from '>=12.22.0' (12) to '>=18.17.0' (14). Installs or runtimes that do not satisfy it fail.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: Next.js 14 declares Node.js requirement '>=18.17.0' (was '>=12.22.0' in 12). (confidence high)
  - next_pkg@v12.3.4: "engines.node = '>=12.22.0'"
  - next_pkg@v14.0.0: "engines.node = '>=18.17.0'"
  - next_guide_14_tag: "The minimum Node.js version has been bumped from 16.14 to 18.17"
  - next_guide_13_tag: "The minimum Node.js version has been bumped from 12.22.0 to 14.6.0"
  - next_guide_13_current: "The minimum Node.js version has been bumped from 12.22.0 to 16.14.0"
  - ⚠ History: in 13, 'Node.js minimum runtime raised to 14.6.0' applied to the same symbol (node); superseded by the 14 change (R2).
  - ⚠ Source disagreement: Next.js 'How to upgrade to version 13' (current docs) says the minimum Node.js for 13 is 16.14.0; next_pkg@v13.0.0 (engines.node) says '>=14.6.0'. Package metadata outranks prose. The prose matches later 13.x metadata (next_pkg@v13.5.0), so the page was likely edited after release to reflect the latest 13.x floor.
- **[required] runtime** `less_than` `"18.17.0"`: The application's Node.js version does not satisfy '>=18.17.0' (is below 18.17.0). (confidence high)
  - next_pkg@v14.0.0: "engines.node = '>=18.17.0'"
  - next_guide_14_tag: "The minimum Node.js version has been bumped from 16.14 to 18.17, since 16.x has reached end-of-life."
  - ⚠ The text does not state which Node.js version the application currently runs, so this must be checked against the codebase or deployment.

Actions:
- Check the deployed Node.js version against '>=18.17.0' before upgrading.
- Upgrade the Node.js runtime used by the application and its deployment images to 18.17 or later before upgrading Next.js to 14.

### React minimum version raised to 18.2.0

`nextjs_2323185baa` · high · confidence high · introduced in 13 · fires at upgrade

The minimum React version was raised from 17.0.2 to 18.2.0, so applications using older React versions may fail after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 13", "target_version": ">= 13"}`: Upgrade crosses release 13 (confidence high, judge supported)
  - next_guide_13_tag: "The minimum React version has been bumped from 17.0.2 to 18.2.0"
  - next_guide_13_current: "The minimum React version has been bumped from 17.0.2 to 18.2.0."
  - ⚠ Package metadata lists a react peer of ^18.0.0-0 for release 13.0.0 but ^18.2.0 for 13.4.0 and 13.5.0, which conflicts with the 18.2.0 minimum stated in the text for the 13 release.
  - ⚠ Source disagreement: Next.js upgrade guide at v13.0.0 (Upgrading from 12 to 13) says the minimum React (peer dependency) for 13 is 18.2.0; next_pkg@v13.0.0 (peerDependencies.react) says '^18.0.0-0'. Package metadata outranks prose. The prose matches later 13.x metadata (next_pkg@v13.4.0, next_pkg@v13.5.0), so the page was likely edited after release to reflect the latest 13.x floor.
  - ⚠ Source disagreement: Next.js 'How to upgrade to version 13' (current docs) says the minimum React (peer dependency) for 13 is 18.2.0; next_pkg@v13.0.0 (peerDependencies.react) says '^18.0.0-0'. Package metadata outranks prose. The prose matches later 13.x metadata (next_pkg@v13.4.0, next_pkg@v13.5.0), so the page was likely edited after release to reflect the latest 13.x floor.
- **[required] dependency** `less_than` `"18.2.0"`: Application depends on react below 18.2.0 (confidence high, judge supported)
  - next_guide_13_tag: "The minimum React version has been bumped from 17.0.2 to 18.2.0"
  - next_guide_13_current: "The minimum React version has been bumped from 17.0.2 to 18.2.0."
  - ⚠ The text states 18.2.0 as the minimum for this change; the provided package metadata lists a React peer of ^18.0.0-0 for release 13.0.0 and ^18.2.0 for later 13.x releases.
  - ⚠ Source disagreement: Next.js upgrade guide at v13.0.0 (Upgrading from 12 to 13) says the minimum React (peer dependency) for 13 is 18.2.0; next_pkg@v13.0.0 (peerDependencies.react) says '^18.0.0-0'. Package metadata outranks prose. The prose matches later 13.x metadata (next_pkg@v13.4.0, next_pkg@v13.5.0), so the page was likely edited after release to reflect the latest 13.x floor.
  - ⚠ Source disagreement: Next.js 'How to upgrade to version 13' (current docs) says the minimum React (peer dependency) for 13 is 18.2.0; next_pkg@v13.0.0 (peerDependencies.react) says '^18.0.0-0'. Package metadata outranks prose. The prose matches later 13.x metadata (next_pkg@v13.4.0, next_pkg@v13.5.0), so the page was likely edited after release to reflect the latest 13.x floor.

Actions:
- Upgrade react to at least 18.2.0 before or together with the Next.js upgrade.
- Check that other react-dependent packages are compatible with the new React version.
- Upgrade the react dependency to 18.2.0 or later before or as part of the Next.js 13 upgrade.

### next/future/image import renamed to next/image

`nextjs_24962734e7` · high · confidence high · introduced in 13 · fires at upgrade

The next/future/image import was renamed to next/image, so code importing next/future/image will break after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 13", "target_version": ">= 13"}`: Upgrade crosses release 13 (confidence high, judge supported)
  - next_guide_13_tag: "The next/future/image import was renamed to next/image."
  - next_guide_13_current: "The next/future/image import was renamed to next/image"
- **[required] api_usage** `present` `"next/future/image"`: Application imports next/future/image (confidence high, judge supported)
  - next_guide_13_tag: "The next/future/image import was renamed to next/image."
  - next_guide_13_current: "The next/future/image import was renamed to next/image"
  - ⚠ The text does not state what behavior differs between next/future/image and next/image, so the impact on app code is not specified.

Actions:
- Run the codemod that renames imports to safely update next/future/image imports to next/image.
- Verify no code still imports next/future/image after the change.
- Rename next/future/image imports to next/image, or use the codemod to rename the imports automatically.
- Run the codemod that is available to safely and automatically rename imports.

### React (peer dependency) requirement raised to ^18.2.0

`nextjs_4315b5fb92` · high · confidence high · introduced in 14 · fires at upgrade

Package metadata changes the React (peer dependency) requirement from '^17.0.2 || ^18.0.0-0' (12) to '^18.2.0' (14). Installs or runtimes that do not satisfy it fail.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: Next.js 14 declares React (peer dependency) requirement '^18.2.0' (was '^17.0.2 || ^18.0.0-0' in 12). (confidence high)
  - next_pkg@v12.3.4: "peerDependencies.react = '^17.0.2 || ^18.0.0-0'"
  - next_pkg@v14.0.0: "peerDependencies.react = '^18.2.0'"
- **[required] dependency** `less_than` `"18.2.0"`: The application's React (peer dependency) version does not satisfy '^18.2.0' (is below 18.2.0). (confidence high)
  - next_pkg@v14.0.0: "peerDependencies.react = '^18.2.0'"

Actions:
- Check the deployed React (peer dependency) version against '^18.2.0' before upgrading.

### next/link child <a> no longer supported

`nextjs_523375afdf` · high · confidence high · introduced in 13 · fires at upgrade

The next/link child can no longer be an <a> element, so next/link usages with an <a> child will change or break unless the legacyBehavior prop is set.

- **[required] version** `in_range` `{"current_version": "< 13", "target_version": ">= 13"}`: Upgrade crosses release 13 (confidence high, judge supported)
  - next_guide_13_tag: "The next/link child can no longer be <a>."
  - next_guide_13_current: "Upgrading from 12 to 13"
- **[required] api_usage** `present` `"<a>"`: Application renders next/link with an <a> child (confidence high, judge supported)
  - next_guide_13_tag: "The next/link child can no longer be <a>."
  - next_guide_13_current: "The next/link child can no longer be <a>"
  - next_guide_13_current: "Add the legacyBehavior prop to use the legacy behavior"
  - ⚠ A multi-line JSX pattern may not match a single-line search.
- **[disqualifying] api_usage** `present` `"legacyBehavior"`: Application sets the legacyBehavior prop on next/link (confidence high, judge supported)
  - next_guide_13_tag: "Add the legacyBehavior prop to use the legacy behavior"

Actions:
- Run the codemod that automatically upgrades next/link usages.
- Alternatively add the legacyBehavior prop to keep the legacy behavior, or remove the <a> element.
- Remove the <a> child of next/link, or add the legacyBehavior prop to keep the legacy behavior.
- Run the codemod to automatically upgrade the code.

### next export command removed

`nextjs_5a5f2f6714` · high · confidence high · introduced in 14 · fires at upgrade

The next export command has been removed in favor of output: 'export' config. Applications that run the next export command at upgrade to 14 will no longer have it available.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The change statement ties the removal of the next export command to release 14. (confidence high, judge supported)
  - next_guide_14_tag: "The next export command has been removed in favor of output: 'export' config."
- **[required] api_usage** `present` `"next export"`: The application invokes the next export command (for example in a package.json script). (confidence high, judge supported)
  - next_guide_14_tag: "The next export command has been removed"

Actions:
- Remove the next export invocation from scripts and CI configuration.
- Set output: 'export' in the Next.js config instead, as the item directs; see the referenced docs for details, which are not included in the provided text.

### @next/font package removed in favor of built-in next/font

`nextjs_8392155aea` · high · confidence high · introduced in 14 · fires at upgrade

The @next/font package has been fully removed in favor of the built-in next/font. Applications that import @next/font will be affected at upgrade. A codemod is available to safely and automatically rename your imports.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, in which the @next/font package was fully removed. (confidence high, judge supported)
  - next_guide_14_tag: "The @next/font package has been fully removed in favor of the built-in next/font."
- **[required] dependency** `present` `"@next/font"`: The application imports or depends on the @next/font package. (confidence high, judge supported)
  - next_guide_14_tag: "The @next/font package has been fully removed"

Actions:
- Replace @next/font imports with the built-in next/font.
- Run the codemod that renames @next/font imports to next/font.

### ImageResponse import moved from next/server to next/og

`nextjs_fea20fefe0` · high · confidence medium · introduced in 14 · fires at upgrade

The next/server import for ImageResponse was renamed to next/og. Application code importing ImageResponse from next/server is affected by the rename at upgrade to 14. A codemod is available to rename the imports.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where the ImageResponse import was renamed. (confidence medium, judge partially_supported)
  - next_guide_14_tag: "The next/server import for ImageResponse was renamed to next/og."
- **[required] api_usage** `present` `"ImageResponse imported from next/server"`: The application imports ImageResponse from next/server. (confidence high, judge supported)
  - next_guide_14_tag: "The next/server import for ImageResponse was renamed to next/og."

Actions:
- Rename the ImageResponse import from next/server to next/og.
- Run the codemod to automatically rename the imports, as the text states a codemod is available.

### Link component nested anchor child

`nextjs_1300ee090f` · medium · confidence medium · introduced in 13 · fires at upgrade

In Next.js 13, <Link> always renders <a>. Next.js 12 required the developer to nest an <a> tag as a child of <Link>; that child must be removed on upgrade so the app does not nest a second anchor under the element Link now renders.

- **[required] version** `in_range` `{"current_version": "< 13", "target_version": ">= 13"}`: The upgrade crosses release 13, the release that introduced <Link> always rendering <a>. (confidence high, judge supported)
  - next_guide_13_current: "In Next.js 13, <Link> always renders <a> and allows you to forward props to the underlying tag."
- **[required] api_usage** `present` `"<a> child inside <Link>"`: The application nests an <a> element as a child of a <Link> component. (confidence medium, judge partially_supported)
  - next_guide_13_current: "<a> has to be nested otherwise it's excluded"
  - ⚠ The text does not state what happens to a nested <a> child in Next.js 13 or 14; it only states that Link always renders <a>.
- **[required] behavior** `present` `"Link renders a"`: The <Link> component always renders an <a> element under the hood in the upgraded version. (confidence high, judge supported)
  - next_guide_13_current: "<Link> always renders <a> under the hood"

Actions:
- Remove the nested <a> child from each <Link> and place the link text directly inside <Link>.
- Forward any props that were on the nested <a> to <Link>, since Link now forwards props to the underlying tag.
- Run the new-link codemod to upgrade links to the Next.js 13 form.

### swcMinify default changed to true

`nextjs_16494e4a2c` · medium · confidence high · introduced in 13 · fires at upgrade

The swcMinify configuration property default changed from false to true, so applications relying on the default will get the new setting.

- **[required] version** `in_range` `{"current_version": "< 13", "target_version": ">= 13"}`: Upgrade crosses release 13 (confidence high, judge supported)
  - next_guide_13_tag: "The swcMinify configuration property was changed from false to true."
  - next_guide_13_current: "Upgrading from 12 to 13"
- **[required] configuration** `absent` `"swcMinify"`: Application does not set swcMinify in its Next.js configuration (confidence high, judge supported)
  - next_guide_13_tag: "The swcMinify configuration property was changed from false to true."
  - next_guide_13_current: "swcMinify configuration property was changed from false to true"
  - ⚠ The text does not state what behavior changes when swcMinify is true.
  - ⚠ The text does not state whether an unset swcMinify was treated as false in release 12.
- **[disqualifying] configuration** `equals` `"false"`: Application explicitly sets swcMinify to false (confidence medium, judge partially_supported)
  - next_guide_13_tag: "The swcMinify configuration property was changed from false to true."

Actions:
- Review the Next.js Compiler documentation referenced by the upgrade guide.
- Set swcMinify explicitly if the previous false behavior must be kept.
- Search the Next.js configuration for swcMinify and check whether it is set to false.
- If the previous minification behavior is required, set swcMinify explicitly after upgrading and test the build output.
- Review the Next.js Compiler documentation referenced by the migration guide for more information.

### next/image import renamed to next/legacy/image

`nextjs_1c253f96bf` · medium · confidence high · introduced in 13 · fires at upgrade

The next/image import was renamed to next/legacy/image. Applications importing next/image are affected by this rename in the 12 to 13 upgrade, and a codemod is available to rename the imports.

- **[required] version** `in_range` `{"current_version": "< 13", "target_version": ">= 13"}`: The upgrade crosses release 13, where the next/image import was renamed. (confidence high, judge partially_supported)
  - next_guide_13_current: "The next/image import was renamed to next/legacy/image"
  - next_guide_13_tag: "The next/image import was renamed to next/legacy/image."
  - next_guide_13_current: "Starting in Next.js 13, this new behavior is now the default for next/image."
- **[required] api_usage** `present` `"next/image"`: The application imports from next/image. (confidence high, judge supported)
  - next_guide_13_current: "The next/image import was renamed to next/legacy/image"
  - next_guide_13_tag: "The next/image import was renamed to next/legacy/image."
  - next_guide_13_current: "rename next/image imports to next/legacy/image to maintain the same behavior"
  - ⚠ The text does not state what behavior differs between next/image and next/legacy/image, so the impact on app code is not specified.
  - ⚠ The text does not state how the component behavior differs between next/image and next/legacy/image.
  - ⚠ The text does not describe the specific differences between the new next/image behavior and the Next.js 12 behavior.

Actions:
- Rename next/image imports to next/legacy/image, or use the codemod to rename the imports automatically.
- Run the codemod that is available to safely and automatically rename imports.
- Run the codemod that renames imports to safely update next/image imports.
- Review image usage after the rename, since the text does not describe behavior differences.
- Run the next-image-to-legacy-image codemod to rename next/image imports to next/legacy/image and keep the Next.js 12 behavior.
- Alternatively, manually change next/image imports to next/legacy/image, following the migration guide.
- Optionally, after the codemod, run the next-image-experimental codemod to move next/legacy/image to the new next/image.

### target configuration property removed

`nextjs_1e5e6decf1` · medium · confidence medium · introduced in 13 · fires at upgrade

The target configuration property was removed and superseded by Output File Tracing, so configurations that set target need to be updated.

- **[required] version** `in_range` `{"current_version": "< 13", "target_version": ">= 13"}`: Upgrade crosses release 13 (confidence high, judge supported)
  - next_guide_13_tag: "The target configuration property has been removed and superseded by Output File Tracing."
- **[required] configuration** `present` `"target"`: Application sets the target property in its Next.js configuration (confidence medium, judge supported)
  - next_guide_13_tag: "The target configuration property has been removed and superseded by Output File Tracing."
  - ⚠ The text does not state whether a remaining target setting causes an error or is ignored.

Actions:
- Remove the target setting from the Next.js configuration.
- Review Output File Tracing as the replacement mechanism.

### next/image default behavior changed in Next.js 13

`nextjs_2ba045f66c` · medium · confidence high · introduced in 13 · fires at upgrade

Starting in Next.js 13, the new next/image behavior is the default. Apps that import next/image and expect the Next.js 12 behavior need migration work. The text gives a codemod that renames next/image imports to next/legacy/image to keep the Next.js 12 behavior.

- **[required] version** `in_range` `{"current_version": "< 13", "target_version": ">= 13"}`: The upgrade crosses release 13, where the new next/image behavior becomes the default. (confidence high, judge supported)
  - next_guide_13_current: "Starting in Next.js 13, this new behavior is now the default for next/image"
- **[required] api_usage** `present` `"next/image"`: The application imports the next/image module. (confidence high, judge supported)
  - next_guide_13_current: "rename next/image imports to next/legacy/image to maintain the same behavior as Next.js 12"
- **[uncertain] behavior** `unknown` `""`: The application depends on Next.js 12 next/image rendering or styling behavior. (confidence low, judge partially_supported)
  - next_guide_13_current: "These improvements included less client-side JavaScript, easier ways to extend and style images"
  - ⚠ The text lists the improvements but does not state which specific output or markup differences would break an app.

Actions:
- Run the next-image-to-legacy-image codemod to rename next/image imports to next/legacy/image and keep Next.js 12 behavior.
- Optionally run the next-image-experimental codemod after the first codemod to upgrade next/legacy/image to the new next/image.
- Alternatively, manually update following the migration guide and the legacy comparison.

### Removed target configuration property

`nextjs_67098be47b` · medium · confidence medium · introduced in 13 · fires at upgrade

The target configuration property has been removed in release 13 and superseded by Output File Tracing. Applications that set the target configuration property must remove it and use Output File Tracing instead.

- **[required] version** `in_range` `{"current_version": "< 13", "target_version": ">= 13"}`: The upgrade crosses release 13, the release in which the target configuration property was removed. (confidence high, judge supported)
  - next_guide_13_current: "The target configuration property has been removed and superseded by Output File Tracing."
- **[required] configuration** `present` `"target"`: The application configuration sets the target configuration property. (confidence medium, judge supported)
  - next_guide_13_current: "The target configuration property has been removed"
  - ⚠ The text does not state whether a remaining target setting causes an error or is silently ignored after the upgrade.
  - ⚠ The text does not name the replacement setting used to enable Output File Tracing.

Actions:
- Remove the target property from the Next.js configuration file.
- Use Output File Tracing as the replacement, as stated in the change description.
- Check the Output File Tracing documentation for the configuration needed, since the text does not name it.

### Internet Explorer support dropped in v13

`nextjs_c5a065b9b5` · medium · confidence medium · introduced in 13 · fires at upgrade

The Supported Browsers were changed to drop Internet Explorer and target modern browsers in release 13. Applications that must serve Internet Explorer users are affected. The text does not state what breaks or what workaround applies.

- **[required] version** `in_range` `{"current_version": "< 13", "target_version": ">= 13"}`: The upgrade crosses release 13, where the Supported Browsers change was introduced. (confidence high, judge supported)
  - next_guide_13_current: "Upgrading from 12 to 13"
  - next_guide_13_current: "The Supported Browsers have been changed to drop Internet Explorer and target modern browsers."
- **[required] behavior** `present` `"Internet Explorer"`: The application must serve Internet Explorer browsers. (confidence medium, judge supported)
  - next_guide_13_current: "drop Internet Explorer and target modern browsers"
  - ⚠ The text does not state what breaks for Internet Explorer users or what workaround applies.

Actions:
- Confirm whether the application must support Internet Explorer users.
- If Internet Explorer support is required, plan browser support changes before upgrading to 14.

### Internet Explorer support dropped

`nextjs_2a246a90c5` · low · confidence medium · introduced in 13 · fires at upgrade

The Supported Browsers were changed to drop Internet Explorer, so applications serving Internet Explorer users are no longer supported.

- **[required] version** `in_range` `{"current_version": "< 13", "target_version": ">= 13"}`: Upgrade crosses release 13 (confidence high, judge supported)
  - next_guide_13_tag: "The Supported Browsers have been changed to drop Internet Explorer and target modern browsers."
- **[required] behavior** `present` `"Internet Explorer"`: Application must serve Internet Explorer users (confidence medium, judge supported)
  - next_guide_13_tag: "The Supported Browsers have been changed to drop Internet Explorer and target modern browsers."
  - ⚠ The text does not state which browsers remain supported beyond modern browsers.

Actions:
- Confirm whether any users access the application with Internet Explorer.
- Test the application in the modern browsers that remain supported.

### next-swc WASM target removal

`nextjs_539d9094ea` · low · confidence medium · introduced in 14 · fires at upgrade

The WASM target for next-swc has been removed in release 14. Applications or deployments that depend on the WASM target for next-swc may be affected at upgrade.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, in which the WASM target for next-swc was removed. (confidence medium, judge partially_supported)
  - next_guide_14_tag: "The WASM target for next-swc has been removed."
- **[required] dependency** `present` `"WASM target for next-swc"`: The application or deployment uses the WASM target for next-swc. (confidence medium, judge supported)
  - next_guide_14_tag: "The WASM target for next-swc has been removed."
  - ⚠ The text does not state how the WASM target for next-swc is selected or used, or what replaces it.

Actions:
- Check whether the project or deployment relies on the WASM target for next-swc.
- Consult the official Next.js version 14 upgrade guide for any replacement, since the text does not name one.

### next/script behavior change

`nextjs_b09465bce4` · low · confidence medium · introduced in 13 · fires at upgrade

The behavior of next/script was updated to support both pages and app. The item does not state what the behavior change is or whether it breaks existing pages-only usage.

- **[required] version** `in_range` `{"current_version": "< 13", "target_version": ">= 13"}`: The upgrade crosses release 13, where the next/script behavior change was introduced. (confidence medium, judge partially_supported)
  - next_guide_13_current: "The behavior of next/script has been updated to support both pages and app."
- **[required] api_usage** `present` `"next/script"`: The application uses next/script. (confidence high, judge supported)
  - next_guide_13_current: "The behavior of next/script has been updated"
- **[uncertain] behavior** `unknown` `""`: The application is incrementally adopting the app directory. (confidence low, judge supported)
  - next_guide_13_current: "If incrementally adopting app, read the upgrade guide."
  - ⚠ The text does not state what the behavior change is or whether it breaks existing pages-only usage.

Actions:
- Read the upgrade guide section on next/script behavior.
- Test pages that use next/script after upgrading to confirm they behave as expected.

### TypeScript projects must upgrade @types/react and @types/react-dom

`nextjs_fdd92fa177` · low · confidence medium · introduced in 14 · fires at upgrade

The upgrade guide says TypeScript users should also upgrade @types/react and @types/react-dom to their latest versions. The text does not state what breaks if this is skipped.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses into Next.js release 14, which is the release that introduced this change. (confidence medium, judge partially_supported)
  - next_guide_14_tag: "ensure you also upgrade @types/react and @types/react-dom to their latest versions"
  - next_guide_13_current: "If you are using TypeScript"
  - ⚠ The item does not restate the release number. The link to release 14 comes from the section heading and the stated introduction release.
  - ⚠ History: in 13, 'TypeScript projects must upgrade @types/react and @types/react-dom' applied to the same symbol (@types/react); superseded by the 14 change (R2).
- **[required] dependency** `present` `"TypeScript"`: The application uses TypeScript. (confidence high, judge supported)
  - next_guide_14_tag: "If you are using TypeScript"
- **[uncertain] dependency** `unknown` `"latest"`: The application's @types/react and @types/react-dom packages are not at their latest versions. (confidence low, judge supported)
  - next_guide_14_tag: "upgrade @types/react and @types/react-dom to their latest versions"
  - ⚠ The text gives no version numbers, so the current versions cannot be compared to the latest ones from this text alone.

Actions:
- If the project uses TypeScript, upgrade @types/react and @types/react-dom to their latest versions.

## Review checklist

### Low confidence or disputed

- [ ] nextjs_f3317b5b79: Node.js requirement raised to >=18.17.0
- [ ] nextjs_2323185baa: React minimum version raised to 18.2.0

### Inferred conditions

- [ ] nextjs_2ba045f66c: The application depends on Next.js 12 next/image rendering or styling behavior.

### Source disagreements

- node minimum for 13: Next.js 'How to upgrade to version 13' (current docs) says the minimum Node.js for 13 is 16.14.0; next_pkg@v13.0.0 (engines.node) says '>=14.6.0'. → Package metadata outranks prose. The prose matches later 13.x metadata (next_pkg@v13.5.0), so the page was likely edited after release to reflect the latest 13.x floor.
- react_peer minimum for 13: Next.js upgrade guide at v13.0.0 (Upgrading from 12 to 13) says the minimum React (peer dependency) for 13 is 18.2.0; next_pkg@v13.0.0 (peerDependencies.react) says '^18.0.0-0'. → Package metadata outranks prose. The prose matches later 13.x metadata (next_pkg@v13.4.0, next_pkg@v13.5.0), so the page was likely edited after release to reflect the latest 13.x floor.
- react_peer minimum for 13: Next.js 'How to upgrade to version 13' (current docs) says the minimum React (peer dependency) for 13 is 18.2.0; next_pkg@v13.0.0 (peerDependencies.react) says '^18.0.0-0'. → Package metadata outranks prose. The prose matches later 13.x metadata (next_pkg@v13.4.0, next_pkg@v13.5.0), so the page was likely edited after release to reflect the latest 13.x floor.

### Open questions

- Next.js 13.x and 14.x minor release notes (blog posts, GitHub releases) were not mined; deprecations introduced in minors (for example in 13.3/13.4) may be missing.
- Hosting platforms (Vercel, Netlify, self-hosted Node, Docker) and third-party Next.js plugins have their own compatibility windows.
- App Router adoption is optional; risks specific to migrating pages/ to app/ are out of scope unless the guides state them.
- Source next_guide_14_pages_canary was rejected (transclusion_stub); its content was not used.
- [nextjs_2ba045f66c] Unconfirmed: The application depends on Next.js 12 next/image rendering or styling behavior. (The text lists the improvements but does not state which specific output or markup differences would break an app.)
- [nextjs_b09465bce4] Unconfirmed: The application is incrementally adopting the app directory. (The text does not state what the behavior change is or whether it breaks existing pages-only usage.)
- [nextjs_fdd92fa177] Unconfirmed: The application's @types/react and @types/react-dom packages are not at their latest versions. (The text gives no version numbers, so the current versions cannot be compared to the latest ones from this text alone.)

## Context facts (not risks)

- (13) next-image-experimental: After running the previous codemod, you can optionally run this experimental codemod to upgrade next/legacy/image to the new next/image, which will remove unused props and add inline styles. — _The item describes an optional, experimental codemod that the text says you can optionally run after the previous codemod to move next/legacy/image to next/image. It is not stated to be required, and the text does not say that skipping it breaks anything. The parent context says the earlier codemod keeps Next.js 12 behavior, so no upgrade-time action is required at 14._

## Disqualified candidates


## Sources

| Source | Type | Tier | Status | Pinned ref |
|---|---|---|---|---|
| [next_guide_13_current](https://nextjs.org/docs/pages/guides/upgrading/version-13) | official_migration_guide | 1 | used | `canary@2e2ee08b604c` |
| [next_guide_13_tag](https://github.com/vercel/next.js/blob/v13.0.0/docs/upgrading.md) | official_migration_guide | 1 | used | `tag:v13.0.0` |
| [next_guide_14_pages_canary](https://nextjs.org/docs/pages/guides/upgrading/version-14) | official_migration_guide | 1 | rejected (transclusion_stub) | `canary@ae1cad07dd32` |
| [next_guide_14_tag](https://github.com/vercel/next.js/blob/v14.2.0/docs/02-app/01-building-your-application/11-upgrading/03-version-14.mdx) | official_migration_guide | 1 | used | `tag:v14.2.0` |
| [next_pkg@v12.3.4](https://github.com/vercel/next.js/blob/v12.3.4/packages/next/package.json) | package_registry_metadata | 1 | used | `tag:v12.3.4` |
| [next_pkg@v13.0.0](https://github.com/vercel/next.js/blob/v13.0.0/packages/next/package.json) | package_registry_metadata | 1 | used | `tag:v13.0.0` |
| [next_pkg@v13.4.0](https://github.com/vercel/next.js/blob/v13.4.0/packages/next/package.json) | package_registry_metadata | 1 | used | `tag:v13.4.0` |
| [next_pkg@v13.5.0](https://github.com/vercel/next.js/blob/v13.5.0/packages/next/package.json) | package_registry_metadata | 1 | used | `tag:v13.5.0` |
| [next_pkg@v14.0.0](https://github.com/vercel/next.js/blob/v14.0.0/packages/next/package.json) | package_registry_metadata | 1 | used | `tag:v14.0.0` |

## What we trusted and what we did not

- Trusted: package metadata for version numbers; official guides, release notes and changelogs pinned to a tag, branch or commit.
- Not trusted: LLM self-reported confidence, unpinned current pages when they disagree with pinned ones, any quote that fails exact match, transclusion stubs.
