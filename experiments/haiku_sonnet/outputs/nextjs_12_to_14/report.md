# Next.js 12 → 14: upgrade risk report

> Documentation-derived risk conditions; not a migration plan.

Next.js 12 -> 14 crosses 2 release(s) (13, 14). 16 risk paths: 1 critical, 8 high, 5 medium, 2 low. Main risk types: removed_api (7), dependency_requirement (3), changed_behavior (3). Critical: Node.js requirement raised to >=18.17.0. 1 context facts and 0 disqualified candidates are listed separately. Documentation-derived risk conditions; not a migration plan.

Overall confidence: **medium**. Validation: `{"errors": 0, "warnings": 0, "by_code": {}}`

## Risk paths

| Level | Confidence | Type | Surface | Release | Path |
|---|---|---|---|---|---|
| critical | high | runtime_requirement | runtime | 14 | `nextjs_f3317b5b79` Node.js requirement raised to >=18.17.0 |
| high | high | dependency_requirement | dependencies | 13 | `nextjs_2323185baa` React minimum version bumped to 18.2.0 |
| high | high | changed_default | application_code | 13 | `nextjs_2ba045f66c` next/image default switched to new Image component behavior |
| high | high | dependency_requirement | dependencies | 14 | `nextjs_4315b5fb92` React (peer dependency) requirement raised to ^18.2.0 |
| high | medium | changed_behavior | application_code | 13 | `nextjs_523375afdf` Link no longer expects a nested <a> child |
| high | medium | removed_api | deployment | 14 | `nextjs_5a5f2f6714` next export command removed |
| high | high | removed_api | configuration | 13 | `nextjs_67098be47b` target configuration property removed |
| high | high | removed_api | application_code | 14 | `nextjs_8392155aea` @next/font package removed in favor of next/font |
| high | medium | removed_api | application_code | 14 | `nextjs_fea20fefe0` ImageResponse import from next/server renamed to next/og |
| medium | high | changed_default | configuration | 13 | `nextjs_16494e4a2c` swcMinify default changed from false to true |
| medium | medium | removed_api | application_code | 13 | `nextjs_24962734e7` next/future/image import renamed to next/image |
| medium | medium | removed_api | dependencies | 14 | `nextjs_86709c1d69` next-swc WASM target removed |
| medium | low | removed_api | runtime | 13 | `nextjs_87c679607f` Internet Explorer support dropped in Next.js 13 |
| medium | medium | changed_behavior | runtime | 13 | `nextjs_c5a065b9b5` Internet Explorer no longer supported |
| low | medium | changed_behavior | application_code | 13 | `nextjs_b09465bce4` next/script behavior change when incrementally adopting app |
| low | medium | dependency_requirement | dependencies | 14 | `nextjs_fdd92fa177` Upgrade @types/react and @types/react-dom for TypeScript projects |

### Node.js requirement raised to >=18.17.0

`nextjs_f3317b5b79` · critical · confidence high · introduced in 14 · fires at upgrade

Package metadata changes the Node.js requirement from '>=12.22.0' (12) to '>=18.17.0' (14). Installs or runtimes that do not satisfy it fail.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: Next.js 14 declares Node.js requirement '>=18.17.0' (was '>=12.22.0' in 12). (confidence high)
  - next_pkg@v12.3.4: "engines.node = '>=12.22.0'"
  - next_pkg@v14.0.0: "engines.node = '>=18.17.0'"
  - next_guide_14_tag: "The minimum Node.js version has been bumped from 16.14 to 18.17"
  - next_guide_13_current: "The minimum Node.js version has been bumped from 12.22.0 to 16.14.0"
  - next_guide_13_tag: "bumped from 12.22.0 to 14.6.0"
  - ⚠ History: in 13, 'Node.js minimum version raised to 16.14.0' applied to the same symbol (node); superseded by the 14 change (R2).
  - ⚠ Source disagreement: Next.js 'How to upgrade to version 13' (current docs) says the minimum Node.js for 13 is 16.14.0; next_pkg@v13.0.0 (engines.node) says '>=14.6.0'. Package metadata outranks prose. The prose matches later 13.x metadata (next_pkg@v13.5.0), so the page was likely edited after release to reflect the latest 13.x floor.
- **[required] runtime** `less_than` `"18.17.0"`: The application's Node.js version does not satisfy '>=18.17.0' (is below 18.17.0). (confidence high)
  - next_pkg@v14.0.0: "engines.node = '>=18.17.0'"
  - next_guide_14_tag: "The minimum Node.js version has been bumped from 16.14 to 18.17"

Actions:
- Check the deployed Node.js version against '>=18.17.0' before upgrading.
- Upgrade Node.js in all development, CI/CD and production environments to 18.17.0 or later before upgrading Next.js.
- Update the engines.node field, .nvmrc, Dockerfile base images and CI node-version settings to 18.17 or newer.

### React minimum version bumped to 18.2.0

`nextjs_2323185baa` · high · confidence high · introduced in 13 · fires at upgrade

Next.js 13 raises the minimum React version from 17.0.2 to 18.2.0. Apps on React 17 or earlier do not meet the new minimum and must upgrade React. Package metadata shows the react peer dependency as ^18.0.0-0 at v13.0.0 and ^18.2.0 from v13.4.0.

- **[required] version** `in_range` `{"current_version": "< 13", "target_version": ">= 13"}`: The upgrade crosses Next.js release 13, which bumped the minimum React version. (confidence high, judge supported)
  - next_guide_13_current: "The minimum React version has been bumped from 17.0.2 to 18.2.0."
  - next_guide_13_tag: "The minimum React version has been bumped from 17.0.2 to 18.2.0"
  - ⚠ Source disagreement: Next.js 'How to upgrade to version 13' (current docs) says the minimum React (peer dependency) for 13 is 18.2.0; next_pkg@v13.0.0 (peerDependencies.react) says '^18.0.0-0'. Package metadata outranks prose. The prose matches later 13.x metadata (next_pkg@v13.4.0, next_pkg@v13.5.0), so the page was likely edited after release to reflect the latest 13.x floor.
  - ⚠ Source disagreement: Next.js upgrade guide at v13.0.0 (Upgrading from 12 to 13) says the minimum React (peer dependency) for 13 is 18.2.0; next_pkg@v13.0.0 (peerDependencies.react) says '^18.0.0-0'. Package metadata outranks prose. The prose matches later 13.x metadata (next_pkg@v13.4.0, next_pkg@v13.5.0), so the page was likely edited after release to reflect the latest 13.x floor.
- **[required] dependency** `less_than` `"18.2.0"`: The application uses a React version below 18.2.0, for example 17.0.2. (confidence high, judge supported)
  - next_guide_13_current: "The minimum React version has been bumped from 17.0.2 to 18.2.0."
  - next_guide_13_tag: "bumped from 17.0.2 to 18.2.0"
  - ⚠ The text does not say whether versions between 17.0.2 and 18.2.0 are blocked. Package metadata shows ^18.0.0-0 at v13.0.0 and ^18.2.0 from v13.4.0.
  - ⚠ Package metadata for 13.0.0 lists the react peer as ^18.0.0-0 while the item text states 18.2.0; 13.4.0 and later list ^18.2.0.
  - ⚠ Source disagreement: Next.js 'How to upgrade to version 13' (current docs) says the minimum React (peer dependency) for 13 is 18.2.0; next_pkg@v13.0.0 (peerDependencies.react) says '^18.0.0-0'. Package metadata outranks prose. The prose matches later 13.x metadata (next_pkg@v13.4.0, next_pkg@v13.5.0), so the page was likely edited after release to reflect the latest 13.x floor.
- **[disqualifying] dependency** `greater_than` `"18.2.0 or later"`: The application already uses React 18.2.0 or later. (confidence medium)
  - next_guide_13_current: "The minimum React version has been bumped from 17.0.2 to 18.2.0."
  - ⚠ Source disagreement: Next.js 'How to upgrade to version 13' (current docs) says the minimum React (peer dependency) for 13 is 18.2.0; next_pkg@v13.0.0 (peerDependencies.react) says '^18.0.0-0'. Package metadata outranks prose. The prose matches later 13.x metadata (next_pkg@v13.4.0, next_pkg@v13.5.0), so the page was likely edited after release to reflect the latest 13.x floor.

Actions:
- Upgrade react and react-dom to 18.2.0 or later before or together with upgrading Next.js.
- Verify that the application and its other dependencies work with React 18.
- Upgrade react and react-dom to 18.2.0 or later together with Next.js.
- Test the application against React 18 behavior.

### next/image default switched to new Image component behavior

`nextjs_2ba045f66c` · high · confidence high · introduced in 13 · fires at upgrade

Starting in Next.js 13, the new Image component behavior (previously available as next/future/image) is the default for next/image. Applications that import next/image and rely on the Next.js 12 behavior will get different behavior after the upgrade unless imports are renamed to next/legacy/image, which the next-image-to-legacy-image codemod does automatically, or the code is migrated to the new component.

- **[required] version** `in_range` `{"current_version": "< 13", "target_version": ">= 13"}`: The upgrade from 12 to 14 crosses release 13, where the new next/image behavior became the default. (confidence high, judge partially_supported)
  - next_guide_13_current: "Starting in Next.js 13, this new behavior is now the default for next/image."
  - next_guide_13_tag: "The next/future/image import was renamed to next/image"
  - next_guide_13_current: "The next/image import was renamed to next/legacy/image."
- **[required] api_usage** `present` `"next/image"`: The application imports next/image and relies on the Next.js 12 behavior of the component. (confidence high, judge supported)
  - next_guide_13_current: "rename next/image imports to next/legacy/image to maintain the same behavior as Next.js 12"
  - next_guide_13_tag: "The next/image import was renamed to next/legacy/image"
  - next_guide_13_tag: "The next/future/image import was renamed to next/image"
  - next_guide_13_current: "this new behavior is now the default for next/image"
  - next_guide_13_current: "The next/image import was renamed to next/legacy/image."
  - ⚠ The text does not list which specific props or behaviors break, only that behavior differs from Next.js 12.
  - ⚠ The text does not describe behavior differences between the old and new image components.
  - ⚠ The text does not state how the new next/image component behaves differently from the old one.
- **[disqualifying] api_usage** `present` `"next/legacy/image"`: The application already imports from next/legacy/image rather than next/image (for example after running the codemod), so Next.js 12 behavior is preserved. (confidence low, judge partially_supported)
  - next_guide_13_current: "rename next/image imports to next/legacy/image"

Actions:
- Run the next-image-to-legacy-image codemod to rename next/image imports to next/legacy/image and keep the Next.js 12 behavior.
- Optionally run the experimental next-image-experimental codemod afterwards to move next/legacy/image to the new next/image; it covers only static usage, not dynamic usage such as <Image {...props} />.
- Alternatively, manually migrate to the new next/image by following the migration guide.
- Run the available codemod to rename the imports safely and automatically.
- Import next/legacy/image where the previous next/image behavior must be kept.
- Run the next-image-to-legacy-image codemod to rename next/image imports to next/legacy/image and maintain Next.js 12 behavior.
- Optionally run the next-image-experimental codemod afterward to upgrade next/legacy/image to the new next/image, which removes unused props and adds inline styles.
- Manually update dynamic usages such as <Image {...props} /> since the experimental codemod covers only static usage.
- Run the provided codemod to rename the imports automatically.
- To keep the previous component, change imports of next/image to next/legacy/image.
- Or review each next/image usage against the new component, which was formerly next/future/image.

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

### Link no longer expects a nested <a> child

`nextjs_523375afdf` · high · confidence medium · introduced in 13 · fires at upgrade

In Next.js 13, <Link> always renders <a> itself and forwards props to it. Code written for Next.js 12 that nests a manual <a> inside <Link> follows the old pattern and needs migration. The text says the nested <a> is no longer required, and a codemod is provided to upgrade links.

- **[required] version** `in_range` `{"current_version": "< 13", "target_version": ">= 13"}`: The upgrade crosses release 13, where <Link> always renders <a> by default. (confidence high, judge supported)
  - next_guide_13_current: "In Next.js 13, <Link> always renders <a> and allows you to forward props to the underlying tag."
  - next_guide_13_tag: "The next/link child can no longer be <a>"
  - next_guide_13_current: "The next/link child can no longer be <a>."
- **[required] api_usage** `present` `"next/link"`: The application uses the <Link> component imported from next/link. (confidence high, judge supported)
  - next_guide_13_current: "import Link from 'next/link'"
  - next_guide_13_tag: "The next/link child can no longer be <a>"
  - next_guide_13_tag: "Add the legacyBehavior prop to use the legacy behavior"
  - next_guide_13_current: "The next/link child can no longer be <a>."
  - next_guide_13_current: "Add the legacyBehavior prop to use the legacy behavior"
  - ⚠ The text does not state how the failure appears (build error, runtime error or warning).
  - ⚠ The text does not state how long legacyBehavior will be supported.
- **[required] api_usage** `present` `"<Link> with nested <a> child"`: The application nests a manual <a> tag as a child of <Link>, the Next.js 12 pattern. (confidence medium, judge partially_supported)
  - next_guide_13_current: "<a> has to be nested otherwise it's excluded"
  - ⚠ The text does not state what happens in Next.js 13 when a nested <a> remains inside <Link>, only that it is no longer required.
- **[uncertain] configuration** `unknown` `"experimental option enabled"`: The application already enabled the experimental <Link> behavior added in 12.2 and has no nested <a> children. (confidence low, judge partially_supported)
  - next_guide_13_current: "This behavior was added as an experimental option in version 12.2 and is now the default."
  - ⚠ The text does not name the experimental option or state its effect on apps that enabled it.

Actions:
- Run the new-link codemod to upgrade links to Next.js 13.
- Remove the nested <a> child from <Link> components and put the link text or content directly inside <Link>.
- Pass props that were previously set on the nested <a> directly to <Link>, which forwards them to the underlying <a>.
- Run the available codemod to automatically upgrade next/link usage.
- Alternatively add the legacyBehavior prop to Link or remove the <a> child.
- Run the available codemod to automatically upgrade next/link usages.
- Alternatively, remove the <a> child so that next/link renders the anchor itself.
- Alternatively, add the legacyBehavior prop to each next/link that keeps an <a> child to use the legacy behavior.

### next export command removed

`nextjs_5a5f2f6714` · high · confidence medium · introduced in 14 · fires at upgrade

The `next export` command has been removed in Next.js 14 in favor of the `output: 'export'` config. Build or deploy scripts that invoke `next export` will break and must be migrated to the config option.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where the next export command was removed. (confidence high, judge supported)
  - next_guide_14_tag: "The next export command has been removed in favor of output: 'export' config."
- **[required] deployment** `present` `"next export"`: Build scripts, CI/CD pipelines, Dockerfiles or documentation invoke the `next export` command. (confidence medium, judge partially_supported)
  - next_guide_14_tag: "The next export command has been removed in favor of output: 'export' config."
- **[optional] configuration** `absent` `"output: 'export'"`: The Next.js config does not already set output: 'export'; the replacement must be configured so static export still occurs. (confidence low, judge partially_supported)
  - next_guide_14_tag: "in favor of output: 'export' config"

Actions:
- Set output: 'export' in next.config.js (or next.config.mjs).
- Remove `next export` invocations from package.json scripts, CI pipelines and Dockerfiles; `next build` produces the static export instead.
- Consult the Next.js static export docs for details on the replacement.

### target configuration property removed

`nextjs_67098be47b` · high · confidence high · introduced in 13 · fires at upgrade

The target configuration property was removed and superseded by Output File Tracing, so configs that set it need to be migrated.

- **[required] version** `in_range` `{"current_version": "< 13", "target_version": ">= 13"}`: The upgrade from 12 to 14 crosses release 13, which removed the target configuration property. (confidence high)
  - next_guide_13_tag: "The target configuration property has been removed and superseded by Output File Tracing"
  - next_guide_13_current: "The target configuration property has been removed and superseded by Output File Tracing."
- **[required] configuration** `present` `"target"`: The Next.js configuration sets the target property. (confidence high, judge supported)
  - next_guide_13_tag: "The target configuration property has been removed"
  - next_guide_13_current: "The target configuration property has been removed"
  - ⚠ The text does not state what happens when a removed target value is still set.
  - ⚠ The text does not state what happens at build time when a removed target property is still set (ignored vs. error).

Actions:
- Remove the target property from the Next.js config.
- Migrate to Output File Tracing as the replacement.
- Remove the target property from next.config.js.
- Migrate to Output File Tracing as the replacement mechanism for what target provided.

### @next/font package removed in favor of next/font

`nextjs_8392155aea` · high · confidence high · introduced in 14 · fires at upgrade

The @next/font package has been fully removed in release 14 in favor of the built-in next/font. Code that still imports from @next/font will break and must be migrated to next/font imports (a codemod is available).

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where @next/font was fully removed. (confidence high, judge supported)
  - next_guide_14_tag: "The @next/font package has been fully removed in favor of the built-in next/font."
- **[required] api_usage** `present` `"@next/font"`: The application imports from the @next/font package. (confidence high, judge supported)
  - next_guide_14_tag: "The @next/font package has been fully removed in favor of the built-in next/font."
- **[optional] dependency** `present` `"@next/font"`: The application's dependencies list @next/font in package.json. (confidence medium, judge supported)
  - next_guide_14_tag: "The @next/font package has been fully removed in favor of the built-in next/font."

Actions:
- Replace imports from @next/font with imports from next/font.
- Run the provided codemod to automatically rename the imports.
- Remove @next/font from package.json dependencies after migration.

### ImageResponse import from next/server renamed to next/og

`nextjs_fea20fefe0` · high · confidence medium · introduced in 14 · fires at upgrade

The ImageResponse import path next/server was renamed to next/og in release 14. Application code that still imports ImageResponse from next/server needs its imports updated. A codemod is available to rename the imports automatically.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where the ImageResponse import was renamed. (confidence high, judge supported)
  - next_guide_14_tag: "The next/server import for ImageResponse was renamed to next/og."
- **[required] api_usage** `present` `"ImageResponse imported from next/server"`: The application imports ImageResponse from next/server. (confidence medium, judge supported)
  - next_guide_14_tag: "The next/server import for ImageResponse was renamed to next/og."
  - ⚠ The text does not state whether the old next/server import path still works in 14 or fails.
- **[disqualifying] api_usage** `present` `"next/og"`: The application already imports ImageResponse from next/og, so no change is needed. (confidence low, judge partially_supported)
  - next_guide_14_tag: "The next/server import for ImageResponse was renamed to next/og."

Actions:
- Rename ImageResponse imports from next/server to next/og.
- Run the available codemod to rename the imports automatically.
- Re-run builds and tests for routes that generate images with ImageResponse.

### swcMinify default changed from false to true

`nextjs_16494e4a2c` · medium · confidence high · introduced in 13 · fires at upgrade

The swcMinify configuration property changed from false to true, so builds that do not set it explicitly now use SWC minification.

- **[required] version** `in_range` `{"current_version": "< 13", "target_version": ">= 13"}`: The upgrade from 12 to 14 crosses release 13, which changed the swcMinify default. (confidence high)
  - next_guide_13_tag: "The swcMinify configuration property was changed from false to true"
  - next_guide_13_current: "The swcMinify configuration property was changed from false to true."
- **[required] configuration** `absent` `"swcMinify"`: The Next.js configuration does not set swcMinify explicitly, so it picks up the new default. (confidence high, judge supported)
  - next_guide_13_tag: "The swcMinify configuration property was changed from false to true"
  - next_guide_13_current: "The swcMinify configuration property was changed from false to true."
  - ⚠ The text does not describe what breaks with SWC minification; it only refers to the Next.js Compiler docs.
  - ⚠ The text does not state that explicit settings are unaffected; this is inferred from the nature of a default change.
  - ⚠ The text does not state how explicit values behave; inferred from default semantics.
- **[disqualifying] configuration** `present` `"swcMinify"`: The configuration explicitly sets swcMinify, so the default change does not apply. (confidence low, judge partially_supported)
  - next_guide_13_tag: "The swcMinify configuration property was changed from false to true"

Actions:
- Test production builds with SWC minification.
- Set swcMinify: false explicitly in the Next.js config if the previous behavior is needed.
- Check next.config.js (or next.config.mjs) for an explicit swcMinify setting.
- If relying on the default, verify production builds and runtime behavior with SWC minification enabled; see the Next.js Compiler documentation.
- Set swcMinify explicitly if the previous behavior must be preserved.

### next/future/image import renamed to next/image

`nextjs_24962734e7` · medium · confidence medium · introduced in 13 · fires at upgrade

The next/future/image import was renamed to next/image. Code that still imports next/future/image must be updated to next/image. A codemod is available.

- **[required] version** `in_range` `{"current_version": "< 13", "target_version": ">= 13"}`: The upgrade crosses release 13, which renamed the next/future/image import to next/image. (confidence high, judge supported)
  - next_guide_13_current: "The next/future/image import was renamed to next/image."
- **[required] api_usage** `present` `"next/future/image"`: The application imports from next/future/image. (confidence medium, judge supported)
  - next_guide_13_current: "The next/future/image import was renamed to next/image."
  - ⚠ The text does not state whether the old next/future/image path still resolves after the upgrade.

Actions:
- Rename imports of next/future/image to next/image.
- Use the provided codemod to rename the imports automatically.

### next-swc WASM target removed

`nextjs_86709c1d69` · medium · confidence medium · introduced in 14 · fires at upgrade

The WASM target for next-swc was removed in Next.js 14. Projects or deployments that depend on the WASM build of next-swc can no longer use it after upgrading. The text names no replacement or workaround.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where the WASM target for next-swc was removed. (confidence high, judge supported)
  - next_guide_14_tag: "The WASM target for next-swc has been removed."
- **[required] dependency** `present` `"next-swc WASM target"`: The application or deployment relies on the WASM target of next-swc (e.g. the WASM SWC package). (confidence medium, judge supported)
  - next_guide_14_tag: "The WASM target for next-swc has been removed."
  - ⚠ The text does not say which packages, platforms or environments use the WASM target, or what to use instead.

Actions:
- Check whether the project or its build/deployment environment uses the WASM target of next-swc.
- If it does, plan an alternative before upgrading, since the WASM target is removed in Next.js 14.

### Internet Explorer support dropped in Next.js 13

`nextjs_87c679607f` · medium · confidence low · introduced in 13 · fires at upgrade

Next.js 13 changed its Supported Browsers to drop Internet Explorer and target modern browsers. Applications that still need to serve Internet Explorer users are affected.

- **[required] version** `in_range` `{"current_version": "< 13", "target_version": ">= 13"}`: The upgrade crosses release 13, which changed the Supported Browsers to drop Internet Explorer. (confidence high, judge supported)
  - next_guide_13_current: "The Supported Browsers have been changed to drop Internet Explorer and target modern browsers."
- **[required] behavior** `present` `"Internet Explorer"`: The application must still support or serve Internet Explorer users. (confidence low, judge supported)
  - next_guide_13_current: "drop Internet Explorer and target modern browsers"
  - ⚠ The text does not say how Internet Explorer users will fail (for example, whether the app breaks or only loses support), nor what exact browser versions are now targeted.

Actions:
- Check whether your users or analytics show Internet Explorer traffic and decide whether dropping IE support is acceptable.
- Review browser-targeting configuration and polyfills that exist only for Internet Explorer.

### Internet Explorer no longer supported

`nextjs_c5a065b9b5` · medium · confidence medium · introduced in 13 · fires at upgrade

Supported browsers now target modern browsers and drop Internet Explorer, so users on Internet Explorer may not be supported.

- **[required] version** `in_range` `{"current_version": "< 13", "target_version": ">= 13"}`: The upgrade from 12 to 14 crosses release 13, which changed the supported browsers. (confidence high)
  - next_guide_13_tag: "The Supported Browsers have been changed to drop Internet Explorer and target modern browsers"
- **[required] runtime** `present` `"Internet Explorer"`: The application needs to serve users on Internet Explorer. (confidence medium, judge partially_supported)
  - next_guide_13_tag: "drop Internet Explorer and target modern browsers"
  - ⚠ The text does not state what specifically fails on Internet Explorer.

Actions:
- Confirm that Internet Explorer support is no longer required, or keep a Next.js version that supports it.
- Review the browserslist configuration against the new modern-browser targets.

### next/script behavior change when incrementally adopting app

`nextjs_b09465bce4` · low · confidence medium · introduced in 13 · fires at upgrade

The behavior of next/script was updated in release 13 to support both pages and app. The text directs apps incrementally adopting app to read the upgrade guide, but does not state what specifically changed or what breaks.

- **[required] version** `in_range` `{"current_version": "< 13", "target_version": ">= 13"}`: The upgrade crosses release 13, where the behavior of next/script was updated. (confidence high, judge supported)
  - next_guide_13_current: "The behavior of next/script has been updated to support both pages and app."
- **[required] api_usage** `present` `"next/script"`: The application uses next/script. (confidence medium, judge supported)
  - next_guide_13_current: "The behavior of next/script has been updated to support both pages and app."
  - ⚠ The text does not describe what specifically changed in next/script behavior or what could break.
- **[uncertain] configuration** `present` `"app directory"`: The application is incrementally adopting the app directory alongside pages. (confidence low, judge supported)
  - next_guide_13_current: "If incrementally adopting app, read the upgrade guide."
  - ⚠ The text does not state whether the behavior change affects apps that remain on pages only.

Actions:
- If incrementally adopting app, read the upgrade guide.
- Review usages of next/script for behavior differences when using both pages and app.

### Upgrade @types/react and @types/react-dom for TypeScript projects

`nextjs_fdd92fa177` · low · confidence medium · introduced in 14 · fires at upgrade

TypeScript projects are told to also upgrade @types/react and @types/react-dom to their latest versions when moving to Next.js 14. If these type packages are left at older versions, type-related problems may occur. The text does not state the specific failure.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses Next.js release 14 (upgrading from 13 to 14 guidance). (confidence high, judge supported)
  - next_guide_14_tag: "Upgrading from 13 to 14"
  - next_guide_13_current: "If you are using TypeScript, ensure you also upgrade @types/react and @types/react-dom to their latest versions."
  - ⚠ History: in 13, 'TypeScript type packages must be upgraded with the Next.js 13 upgrade' applied to the same symbol (@types/react); superseded by the 14 change (R2).
- **[required] configuration** `present` `"TypeScript"`: The application uses TypeScript. (confidence high, judge supported)
  - next_guide_14_tag: "If you are using TypeScript"
- **[required] dependency** `present` `"@types/react"`: The project depends on @types/react and @types/react-dom, which may be at versions older than the latest. (confidence medium, judge partially_supported)
  - next_guide_14_tag: "ensure you also upgrade @types/react and @types/react-dom to their latest versions"
  - ⚠ The text does not state what breaks if these packages are not upgraded, nor a specific minimum version.

Actions:
- Upgrade @types/react and @types/react-dom to their latest versions together with next, react, react-dom and eslint-config-next.
- Run the TypeScript type check after upgrading.

## Review checklist

### Low confidence or disputed

- [ ] nextjs_f3317b5b79: Node.js requirement raised to >=18.17.0
- [ ] nextjs_2323185baa: React minimum version bumped to 18.2.0
- [ ] nextjs_87c679607f: Internet Explorer support dropped in Next.js 13

### Inferred conditions

- [ ] nextjs_2ba045f66c: The application already imports from next/legacy/image rather than next/image (for example after running the codemod), so Next.js 12 behavior is preserved.
- [ ] nextjs_5a5f2f6714: The Next.js config does not already set output: 'export'; the replacement must be configured so static export still occurs.
- [ ] nextjs_8392155aea: The application's dependencies list @next/font in package.json.
- [ ] nextjs_fea20fefe0: The application already imports ImageResponse from next/og, so no change is needed.
- [ ] nextjs_16494e4a2c: The configuration explicitly sets swcMinify, so the default change does not apply.
- [ ] nextjs_87c679607f: The application must still support or serve Internet Explorer users.

### Source disagreements

- node minimum for 13: Next.js 'How to upgrade to version 13' (current docs) says the minimum Node.js for 13 is 16.14.0; next_pkg@v13.0.0 (engines.node) says '>=14.6.0'. → Package metadata outranks prose. The prose matches later 13.x metadata (next_pkg@v13.5.0), so the page was likely edited after release to reflect the latest 13.x floor.
- react_peer minimum for 13: Next.js 'How to upgrade to version 13' (current docs) says the minimum React (peer dependency) for 13 is 18.2.0; next_pkg@v13.0.0 (peerDependencies.react) says '^18.0.0-0'. → Package metadata outranks prose. The prose matches later 13.x metadata (next_pkg@v13.4.0, next_pkg@v13.5.0), so the page was likely edited after release to reflect the latest 13.x floor.
- react_peer minimum for 13: Next.js upgrade guide at v13.0.0 (Upgrading from 12 to 13) says the minimum React (peer dependency) for 13 is 18.2.0; next_pkg@v13.0.0 (peerDependencies.react) says '^18.0.0-0'. → Package metadata outranks prose. The prose matches later 13.x metadata (next_pkg@v13.4.0, next_pkg@v13.5.0), so the page was likely edited after release to reflect the latest 13.x floor.

### Open questions

- Next.js 13.x and 14.x minor release notes (blog posts, GitHub releases) were not mined; deprecations introduced in minors (for example in 13.3/13.4) may be missing.
- Hosting platforms (Vercel, Netlify, self-hosted Node, Docker) and third-party Next.js plugins have their own compatibility windows.
- App Router adoption is optional; risks specific to migrating pages/ to app/ are out of scope unless the guides state them.
- Source next_guide_14_pages_canary was rejected (transclusion_stub); its content was not used.
- [nextjs_523375afdf] Unconfirmed: The application already enabled the experimental <Link> behavior added in 12.2 and has no nested <a> children. (The text does not name the experimental option or state its effect on apps that enabled it.)
- [nextjs_b09465bce4] Unconfirmed: The application is incrementally adopting the app directory alongside pages. (The text does not state whether the behavior change affects apps that remain on pages only.)

## Context facts (not risks)

- (13) next-image-experimental: After running the previous codemod, you can optionally run this experimental codemod to upgrade next/legacy/image to the new next/image, which will remove unused props and add inline styles. — _The item describes an optional, experimental codemod (next-image-experimental) that upgrades next/legacy/image to the new next/image. It is a migration aid, not a breaking change, and running it is not required. The stated limitation, that it covers only static usage and not dynamic usage such as <Image {...props} />, affects only users who choose to run it. The behavior change to next/image itself is a separate item, and the text says the first codemod keeps the Next.js 12 behavior._

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
