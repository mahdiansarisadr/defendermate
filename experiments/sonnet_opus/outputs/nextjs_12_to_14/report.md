# Next.js 12 → 14: upgrade risk report

> Documentation-derived risk conditions; not a migration plan.

Next.js 12 -> 14 crosses 2 release(s) (13, 14). 14 risk paths: 2 critical, 9 high, 2 medium, 1 low. Main risk types: removed_api (6), dependency_requirement (3), changed_behavior (3). Critical: Minimum React version raised to 18.2.0; Node.js requirement raised to >=18.17.0. 0 context facts and 0 disqualified candidates are listed separately. Documentation-derived risk conditions; not a migration plan.

Overall confidence: **medium**. Validation: `{"errors": 0, "warnings": 2, "by_code": {"W4_no_search_queries": 2}}`

## Risk paths

| Level | Confidence | Type | Surface | Release | Path |
|---|---|---|---|---|---|
| critical | high | dependency_requirement | dependencies | 13 | `nextjs_2323185baa` Minimum React version raised to 18.2.0 |
| critical | high | runtime_requirement | runtime | 14 | `nextjs_f3317b5b79` Node.js requirement raised to >=18.17.0 |
| high | high | removed_api | application_code | 13 | `nextjs_24962734e7` next/future/image renamed to next/image |
| high | high | dependency_requirement | dependencies | 14 | `nextjs_4315b5fb92` React (peer dependency) requirement raised to ^18.2.0 |
| high | high | changed_behavior | application_code | 13 | `nextjs_523375afdf` next/link <Link> with manually nested <a> child must be migrated (new-link codemod) |
| high | high | removed_api | deployment | 14 | `nextjs_5a5f2f6714` next export command removed |
| high | high | removed_api | configuration | 13 | `nextjs_67098be47b` target configuration property removed |
| high | high | removed_api | application_code | 14 | `nextjs_8392155aea` @next/font package removed in favor of built-in next/font |
| high | medium | removed_api | runtime | 14 | `nextjs_86709c1d69` next-swc WASM target removed |
| high | high | changed_behavior | application_code | 13 | `nextjs_f8d3770f36` next/image default behavior switched to former next/future/image |
| high | medium | removed_api | application_code | 14 | `nextjs_fea20fefe0` ImageResponse import from next/server renamed to next/og |
| medium | medium | changed_default | configuration | 13 | `nextjs_16494e4a2c` swcMinify default changed from false to true |
| medium | medium | changed_behavior | application_code | 13 | `nextjs_c5a065b9b5` Internet Explorer dropped from supported browsers |
| low | medium | dependency_requirement | dependencies | 14 | `nextjs_fdd92fa177` TypeScript projects must upgrade @types/react and @types/react-dom with Next.js 14 |

### Minimum React version raised to 18.2.0

`nextjs_2323185baa` · critical · confidence high · introduced in 13 · fires at upgrade

Next.js 13 raises the minimum React version from 17.0.2 to 18.2.0.

- **[required] version** `in_range` `{"current_version": "< 13", "target_version": ">= 13"}`: The upgrade crosses Next.js release 13. (confidence high, judge supported)
  - next_guide_13_tag: "The minimum React version has been bumped from 17.0.2 to 18.2.0."
  - next_guide_13_current: "The minimum React version has been bumped from 17.0.2 to 18.2.0."
  - ⚠ Source disagreement: Next.js upgrade guide at v13.0.0 (Upgrading from 12 to 13) says the minimum React (peer dependency) for 13 is 18.2.0; next_pkg@v13.0.0 (peerDependencies.react) says '^18.0.0-0'. Package metadata outranks prose. The prose matches later 13.x metadata (next_pkg@v13.4.0, next_pkg@v13.5.0), so the page was likely edited after release to reflect the latest 13.x floor.
  - ⚠ Source disagreement: Next.js 'How to upgrade to version 13' (current docs) says the minimum React (peer dependency) for 13 is 18.2.0; next_pkg@v13.0.0 (peerDependencies.react) says '^18.0.0-0'. Package metadata outranks prose. The prose matches later 13.x metadata (next_pkg@v13.4.0, next_pkg@v13.5.0), so the page was likely edited after release to reflect the latest 13.x floor.
- **[required] dependency** `less_than` `"18.2.0"`: The application depends on a React version below 18.2.0. (confidence high, judge supported)
  - next_guide_13_tag: "The minimum React version has been bumped from 17.0.2 to 18.2.0."
  - next_guide_13_current: "The minimum React version has been bumped from 17.0.2 to 18.2.0."
  - ⚠ Package metadata for v13.0.0 declares peerDependencies.react ^18.0.0-0, while the guide states 18.2.0; ^18.2.0 is declared from v13.4.0.
  - ⚠ The text names only react; whether react-dom must be bumped in step is not stated.
  - ⚠ Source disagreement: Next.js upgrade guide at v13.0.0 (Upgrading from 12 to 13) says the minimum React (peer dependency) for 13 is 18.2.0; next_pkg@v13.0.0 (peerDependencies.react) says '^18.0.0-0'. Package metadata outranks prose. The prose matches later 13.x metadata (next_pkg@v13.4.0, next_pkg@v13.5.0), so the page was likely edited after release to reflect the latest 13.x floor.
  - ⚠ Source disagreement: Next.js 'How to upgrade to version 13' (current docs) says the minimum React (peer dependency) for 13 is 18.2.0; next_pkg@v13.0.0 (peerDependencies.react) says '^18.0.0-0'. Package metadata outranks prose. The prose matches later 13.x metadata (next_pkg@v13.4.0, next_pkg@v13.5.0), so the page was likely edited after release to reflect the latest 13.x floor.

Actions:
- Upgrade react and react-dom to 18.2.0 or later.
- Upgrade react to 18.2.0 or later (satisfying peerDependencies ^18.2.0) before or along with upgrading Next.js to 14.
- Upgrade react-dom to a matching 18.2.x version.
- Test the application for React 18 behavior changes after the bump.

### Node.js requirement raised to >=18.17.0

`nextjs_f3317b5b79` · critical · confidence high · introduced in 14 · fires at upgrade

Package metadata changes the Node.js requirement from '>=12.22.0' (12) to '>=18.17.0' (14). Installs or runtimes that do not satisfy it fail.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: Next.js 14 declares Node.js requirement '>=18.17.0' (was '>=12.22.0' in 12). (confidence high)
  - next_pkg@v12.3.4: "engines.node = '>=12.22.0'"
  - next_pkg@v14.0.0: "engines.node = '>=18.17.0'"
  - next_guide_14_tag: "The minimum Node.js version has been bumped from 16.14 to 18.17"
  - next_guide_13_tag: "The minimum Node.js version has been bumped from 12.22.0 to 14.6.0, since 12.x has reached end-of-life."
  - next_guide_13_current: "The minimum Node.js version has been bumped from 12.22.0 to 16.14.0, since 12.x and 14.x have reached end-of-life."
  - ⚠ History: in 13, 'Minimum Node.js version raised to 14.6.0' applied to the same symbol (node); superseded by the 14 change (R2).
  - ⚠ Source disagreement: Next.js 'How to upgrade to version 13' (current docs) says the minimum Node.js for 13 is 16.14.0; next_pkg@v13.0.0 (engines.node) says '>=14.6.0'. Package metadata outranks prose. The prose matches later 13.x metadata (next_pkg@v13.5.0), so the page was likely edited after release to reflect the latest 13.x floor.
- **[required] runtime** `less_than` `"18.17.0"`: The application's Node.js version does not satisfy '>=18.17.0' (is below 18.17.0). (confidence high)
  - next_pkg@v14.0.0: "engines.node = '>=18.17.0'"
  - next_guide_14_tag: "The minimum Node.js version has been bumped from 16.14 to 18.17, since 16.x has reached end-of-life."

Actions:
- Check the deployed Node.js version against '>=18.17.0' before upgrading.
- Upgrade Node.js to version 18.17.0 or later in all build, CI and runtime environments (Dockerfiles, CI configs, .nvmrc, engines field).
- Update package.json engines.node to ">=18.17.0".

### next/future/image renamed to next/image

`nextjs_24962734e7` · high · confidence high · introduced in 13 · fires at upgrade

In Next.js 13 the next/future/image import was renamed to next/image.

- **[required] version** `in_range` `{"current_version": "< 13", "target_version": ">= 13"}`: The upgrade crosses Next.js release 13. (confidence high, judge supported)
  - next_guide_13_tag: "The next/future/image import was renamed to next/image."
  - next_guide_13_current: "The next/future/image import was renamed to next/image."
- **[required] api_usage** `present` `"next/future/image"`: The application imports next/future/image. (confidence high, judge supported)
  - next_guide_13_tag: "The next/future/image import was renamed to next/image."
  - next_guide_13_current: "The next/future/image import was renamed to next/image."
  - ⚠ The text does not state whether next/future/image is removed outright or still resolves in 13/14.

Actions:
- Run the provided codemod to rename next/future/image imports to next/image.
- Run the codemod to rename next/future/image imports to next/image.

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

### next/link <Link> with manually nested <a> child must be migrated (new-link codemod)

`nextjs_523375afdf` · high · confidence high · introduced in 13 · fires at upgrade

In Next.js 13, <Link> always renders an <a> tag itself and no longer requires a manually nested <a> child. Next.js 12 code that nests <a> inside <Link> needs updating; the docs recommend the new-link codemod. The text does not say exactly what happens to unmigrated <Link><a>…</a></Link> code at runtime.

- **[required] version** `in_range` `{"current_version": "< 13", "target_version": ">= 13"}`: The upgrade crosses Next.js 13, where <Link> always renders <a> by default (confidence high, judge supported)
  - next_guide_13_current: "In Next.js 13, <Link> always renders <a> and allows you to forward props to the underlying tag."
  - next_guide_13_current: "To upgrade your links to Next.js 13, you can use the new-link codemod."
  - next_guide_13_tag: "The next/link child can no longer be <a>."
  - next_guide_13_current: "The next/link child can no longer be <a>."
- **[required] api_usage** `present` `"<Link ...><a>...</a></Link>"`: The application imports Link from 'next/link' and nests an <a> tag as the child of <Link> (Next.js 12 pattern) (confidence high, judge supported)
  - next_guide_13_current: "import Link from 'next/link'"
  - next_guide_13_current: "<a> has to be nested otherwise it's excluded"
  - next_guide_13_tag: "The next/link child can no longer be <a>."
  - next_guide_13_tag: "Add the legacyBehavior prop to use the legacy behavior"
  - next_guide_13_current: "The next/link child can no longer be <a>."
  - next_guide_13_current: "Add the legacyBehavior prop to use the legacy behavior"
  - next_guide_13_current: "Next.js 12: <a> has to be nested otherwise it's excluded"
  - ⚠ The text does not state exactly what happens at runtime to Links that still contain a nested <a> child (e.g. error vs. nested anchors).
- **[disqualifying] configuration** `present` `"experimental new Link behavior option enabled"`: The application had already opted into the new Link behavior through the experimental option introduced in 12.2 (confidence low, judge supported)
  - next_guide_13_current: "This behavior was added as an experimental option in version 12.2 and is now the default."
  - ⚠ The text does not name the experimental option or how it was configured.
  - ⚠ The text does not name the experimental option or setting key.
- **[uncertain] behavior** `unknown` `"unknown"`: The consequence of leaving a nested <a> inside <Link> in Next.js 13 (e.g. error vs. nested anchors) is not stated (confidence low, judge partially_supported)
  - next_guide_13_current: "The <Link> Component no longer requires manually adding an <a> tag as a child."
  - ⚠ The text does not state whether unmigrated <Link><a> code errors, renders nested anchors, or keeps working.

Actions:
- Run the new-link codemod to upgrade <Link> usages to the Next.js 13 form.
- Remove manually nested <a> children from <Link> and pass the props that were on <a> directly to <Link>, which forwards them to the underlying tag.
- Review links after migration to confirm rendering and forwarded props behave as expected.
- Remove the <a> child from next/link or add the legacyBehavior prop; a codemod is available to automatically upgrade code.
- Remove the <a> child from next/link usages, moving its attributes onto <Link>.
- Alternatively, add the legacyBehavior prop to <Link> to keep the legacy behavior.
- Run the available Next.js codemod to automatically upgrade next/link usages.
- Run the new-link codemod to upgrade links to Next.js 13.
- Remove manually nested <a> children from <Link> and forward props (e.g. className) directly to <Link>.

### next export command removed

`nextjs_5a5f2f6714` · high · confidence high · introduced in 14 · fires at upgrade

The `next export` CLI command was removed in Next.js 14. Build scripts or deployment pipelines that run `next export` will break after upgrading. The replacement is the `output: 'export'` setting in the Next.js config.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses Next.js release 14, where the next export command was removed. (confidence high, judge supported)
  - next_guide_14_tag: "The next export command has been removed in favor of output: 'export' config."
- **[required] deployment** `present` `"next export"`: The project's scripts, CI or deployment pipeline invokes the `next export` command. (confidence high, judge supported)
  - next_guide_14_tag: "The next export command has been removed"
- **[disqualifying] configuration** `present` `"output: 'export'"`: The project already uses `output: 'export'` in the Next.js config instead of `next export`. (confidence medium, judge supported)
  - next_guide_14_tag: "in favor of output: 'export' config"
  - ⚠ The text does not say whether the behavior of output: 'export' differs from next export; it defers to the docs.

Actions:
- Remove `next export` from package.json scripts and CI/deployment pipelines.
- Set `output: 'export'` in next.config.js and use `next build` to produce the static export.
- Consult the Next.js static export docs for details.

### target configuration property removed

`nextjs_67098be47b` · high · confidence high · introduced in 13 · fires at upgrade

In Next.js 13 the target configuration property has been removed and superseded by Output File Tracing.

- **[required] version** `in_range` `{"current_version": "< 13", "target_version": ">= 13"}`: The upgrade crosses Next.js release 13. (confidence high, judge supported)
  - next_guide_13_tag: "The target configuration property has been removed and superseded by Output File Tracing."
  - next_guide_13_current: "The target configuration property has been removed and superseded by Output File Tracing."
- **[required] configuration** `present` `"target"`: The application's next.config sets the target property. (confidence high, judge supported)
  - next_guide_13_tag: "The target configuration property has been removed"
  - next_guide_13_current: "The target configuration property has been removed"
  - ⚠ The text does not state whether a set target causes an error or is ignored.
  - ⚠ The text does not state whether a remaining `target` setting causes a build error, a warning, or is silently ignored.

Actions:
- Remove the target property from next.config and migrate to Output File Tracing.
- Remove the `target` property from next.config.js/next.config.mjs.
- Migrate to Output File Tracing as the replacement for the removed `target` property and verify the deployment packaging works with it.

### @next/font package removed in favor of built-in next/font

`nextjs_8392155aea` · high · confidence high · introduced in 14 · fires at upgrade

In Next.js 14 the @next/font package has been fully removed. Applications importing from @next/font must switch their imports to the built-in next/font (a codemod is available).

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses Next.js release 14, where @next/font was fully removed. (confidence high, judge supported)
  - next_guide_14_tag: "The @next/font package has been fully removed in favor of the built-in next/font."
- **[required] dependency** `present` `"@next/font"`: The application imports from or depends on the @next/font package. (confidence high, judge supported)
  - next_guide_14_tag: "The @next/font package has been fully removed in favor of the built-in next/font."

Actions:
- Run the official Next.js codemod to rename @next/font imports to next/font.
- Replace imports from '@next/font/...' with 'next/font/...' and remove @next/font from package.json dependencies.

### next-swc WASM target removed

`nextjs_86709c1d69` · high · confidence medium · introduced in 14 · fires at upgrade

Next.js 14 removes the WASM target for next-swc. Environments that relied on the WASM build of the SWC compiler (e.g. platforms without a native next-swc binary) will no longer have that fallback.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses Next.js release 14, where the next-swc WASM target was removed (confidence high, judge supported)
  - next_guide_14_tag: "The WASM target for next-swc has been removed."
- **[required] dependency** `present` `"next-swc WASM target"`: The application or build environment uses the WASM target for next-swc (confidence medium, judge supported)
  - next_guide_14_tag: "The WASM target for next-swc has been removed."
  - ⚠ The text does not name the specific package names (e.g. @next/swc-wasm-nodejs) or which platforms used the WASM target, nor does it name a replacement.

Actions:
- Check whether your build environment relies on the WASM build of next-swc (e.g. @next/swc-wasm-* packages) and ensure a native next-swc binary is available for your platform before upgrading to Next.js 14.

### next/image default behavior switched to former next/future/image

`nextjs_f8d3770f36` · high · confidence high · introduced in 13 · fires at upgrade

Starting in Next.js 13, next/image adopts the new Image Component behavior (formerly next/future/image). Apps using next/image with Next.js 12 behavior (e.g. layout prop) must migrate, either by renaming imports to next/legacy/image or by updating to the new component.

- **[required] version** `in_range` `{"current_version": "< 13", "target_version": ">= 13"}`: The upgrade crosses Next.js 13, where the new Image behavior becomes the default for next/image. (confidence high, judge supported)
  - next_guide_13_current: "Starting in Next.js 13, this new behavior is now the default for next/image."
  - next_guide_13_tag: "The next/image import was renamed to next/legacy/image."
  - next_guide_13_current: "The next/image import was renamed to next/legacy/image."
- **[required] api_usage** `present` `"next/image"`: The application imports the Image component from next/image. (confidence high, judge supported)
  - next_guide_13_current: "Starting in Next.js 13, this new behavior is now the default for next/image."
  - next_guide_13_tag: "The next/image import was renamed to next/legacy/image."
  - next_guide_13_current: "The next/image import was renamed to next/legacy/image."
  - next_guide_13_current: "rename next/image imports to next/legacy/image to maintain the same behavior as Next.js 12"
  - ⚠ The text does not describe the specific behavioral differences between the legacy and new image components.
  - ⚠ The text does not enumerate which specific behaviors or props break; it only says next/legacy/image maintains Next.js 12 behavior.
- **[optional] api_usage** `present` `"layout="`: Usage of props removed in the new component (e.g. layout) raises impact; the experimental codemod removes unused props and adds inline styles. (confidence low, judge partially_supported)
  - next_guide_13_current: "upgrade next/legacy/image to the new next/image, which will remove unused props and add inline styles"
  - ⚠ The text does not list exactly which props are removed beyond the layout example.
- **[optional] api_usage** `present` `"<Image {...props} />"`: Dynamic Image usage (spread props) is not covered by the experimental codemod and requires manual migration. (confidence medium, judge partially_supported)
  - next_guide_13_current: "only covers static usage (such as <Image src={img} layout="responsive" />) but not dynamic usage (such as <Image {...props} />)"
- **[uncertain] api_usage** `present` `"next/future/image"`: If the application already uses next/future/image, it already uses the new behavior. (confidence low, judge partially_supported)
  - next_guide_13_current: "Next.js 12 introduced many improvements to the Image Component with a temporary import: next/future/image."
  - ⚠ The text does not state what happens to next/future/image imports in Next.js 13/14.
- **[optional] behavior** `present` `"next/image"`: After upgrade, next/image provides the component formerly at next/future/image. (confidence medium, judge supported)
  - next_guide_13_tag: "The next/future/image import was renamed to next/image."
  - ⚠ The specific behavioral differences between the components are not described in this text.

Actions:
- Run the next-image-to-legacy-image codemod to rename next/image imports to next/legacy/image and keep Next.js 12 behavior.
- Optionally run the experimental next-image-experimental codemod to migrate next/legacy/image to the new next/image; manually migrate dynamic usages like <Image {...props} />.
- Alternatively, manually update following the Image migration guide and legacy comparison.
- Run the provided codemod to rename next/image imports to next/legacy/image, or migrate to the new next/image.
- Run the Next.js codemod to rename next/image imports to next/legacy/image (and next/future/image to next/image).
- Alternatively migrate usages to the new next/image component.
- Run the next-image-to-legacy-image codemod (npx @next/codemod next-image-to-legacy-image) to rename next/image imports to next/legacy/image and keep Next.js 12 behavior.
- Optionally run the experimental next-image-experimental codemod afterwards to migrate next/legacy/image to the new next/image; it only covers static usage, so manually update dynamic usage such as <Image {...props} /> following the migration guide.

### ImageResponse import from next/server renamed to next/og

`nextjs_fea20fefe0` · high · confidence medium · introduced in 14 · fires at upgrade

In Next.js 14, the ImageResponse import was moved from next/server to next/og. Code importing ImageResponse from next/server must be updated; a codemod is available.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses Next.js release 14, where the ImageResponse import was renamed from next/server to next/og. (confidence high, judge supported)
  - next_guide_14_tag: "The next/server import for ImageResponse was renamed to next/og."
- **[required] api_usage** `present` `"ImageResponse imported from next/server"`: The application imports ImageResponse from next/server. (confidence medium, judge supported)
  - next_guide_14_tag: "The next/server import for ImageResponse was renamed to next/og."
  - ⚠ The text does not state whether the old next/server import fails outright or still works with a deprecation warning in 14.

Actions:
- Change imports of ImageResponse from 'next/server' to 'next/og'.
- Run the official Next.js codemod to automatically rename the ImageResponse imports.

### swcMinify default changed from false to true

`nextjs_16494e4a2c` · medium · confidence medium · introduced in 13 · fires at upgrade

In Next.js 13 the swcMinify configuration property's default changed from false to true. Applications that relied on the previous default will have their production JavaScript minified by the SWC minifier after upgrading, which may change build output behavior.

- **[required] version** `in_range` `{"current_version": "< 13", "target_version": ">= 13"}`: The upgrade crosses Next.js release 13, where the swcMinify default changed from false to true. (confidence high, judge supported)
  - next_guide_13_current: "The swcMinify configuration property was changed from false to true."
  - next_guide_13_tag: "The swcMinify configuration property was changed from false to true."
- **[required] configuration** `absent` `"swcMinify"`: The application does not explicitly set swcMinify in its Next.js config and therefore relies on the default value. (confidence medium, judge supported)
  - next_guide_13_current: "The swcMinify configuration property was changed from false to true."
  - next_guide_13_tag: "The swcMinify configuration property was changed from false to true."
  - ⚠ The text does not describe what concrete behavior differences the new default causes or whether builds may break.
  - ⚠ The text does not describe output differences caused by SWC minification.
- **[uncertain] configuration** `equals` `"false"`: The application explicitly sets swcMinify: false in its Next.js config, opting out of the new default. (confidence low, judge partially_supported)
  - next_guide_13_current: "The swcMinify configuration property was changed from false to true."
  - ⚠ The text does not state whether explicitly setting swcMinify to false remains supported in version 14.

Actions:
- Check next.config.js for a swcMinify setting; if absent, test production builds with SWC minification enabled after upgrading.
- Review the Next.js Compiler documentation for details on swcMinify.
- Test production builds with SWC minification; set swcMinify explicitly if needed. See Next.js Compiler docs.

### Internet Explorer dropped from supported browsers

`nextjs_c5a065b9b5` · medium · confidence medium · introduced in 13 · fires at upgrade

Next.js 13 changes Supported Browsers to drop Internet Explorer and target modern browsers.

- **[required] version** `in_range` `{"current_version": "< 13", "target_version": ">= 13"}`: The upgrade crosses Next.js release 13. (confidence high, judge supported)
  - next_guide_13_tag: "The Supported Browsers have been changed to drop Internet Explorer and target modern browsers."
  - next_guide_13_current: "The Supported Browsers have been changed to drop Internet Explorer and target modern browsers."
- **[required] behavior** `present` `"Internet Explorer"`: The application must support Internet Explorer users. (confidence medium, judge supported)
  - next_guide_13_tag: "drop Internet Explorer and target modern browsers"
  - ⚠ The text does not describe how output fails in Internet Explorer.
- **[required] deployment** `present` `"IE"`: The application must support Internet Explorer users (e.g. targets IE in its browser targets). (confidence medium, judge supported)
  - next_guide_13_current: "drop Internet Explorer and target modern browsers"
  - ⚠ The text does not state how support is dropped (e.g. browserslist defaults, polyfills) or whether IE can be re-enabled.

Actions:
- Confirm whether Internet Explorer support is required before upgrading; if so, plan an alternative.
- Confirm whether any users require Internet Explorer; if so, plan for IE no longer being a supported target in Next.js 13+.
- Review browser target configuration (e.g. browserslist) against the modern-browser defaults.

### TypeScript projects must upgrade @types/react and @types/react-dom with Next.js 14

`nextjs_fdd92fa177` · low · confidence medium · introduced in 14 · fires at upgrade

When upgrading to Next.js 14, TypeScript users are told to also upgrade @types/react and @types/react-dom to their latest versions. The text does not say what fails if they are left outdated.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade moves the application to Next.js version 14. (confidence high, judge supported)
  - next_guide_14_tag: "To update to Next.js version 14, run the following command using your preferred package manager"
  - next_guide_13_current: "If you are using TypeScript, ensure you also upgrade @types/react and @types/react-dom"
  - ⚠ History: in 13, 'TypeScript projects must upgrade @types/react and @types/react-dom alongside Next.js 13' applied to the same symbol (@types/react); superseded by the 14 change (R2).
- **[required] dependency** `present` `"typescript"`: The application uses TypeScript. (confidence high, judge supported)
  - next_guide_14_tag: "If you are using TypeScript, ensure you also upgrade @types/react and @types/react-dom"
- **[required] dependency** `present` `"@types/react"`: The application depends on @types/react or @types/react-dom at a version that is not the latest. (confidence medium, judge supported)
  - next_guide_14_tag: "ensure you also upgrade @types/react and @types/react-dom to their latest versions"
  - ⚠ The text does not state which minimum @types versions are required or what errors occur if they are not upgraded.

Actions:
- Upgrade @types/react and @types/react-dom to their latest versions alongside next, react, react-dom and eslint-config-next (e.g. npm i @types/react@latest @types/react-dom@latest).
- Run a TypeScript type check after upgrading to confirm there are no type errors.

## Review checklist

### Low confidence or disputed

- [ ] nextjs_2323185baa: Minimum React version raised to 18.2.0
- [ ] nextjs_f3317b5b79: Node.js requirement raised to >=18.17.0

### Inferred conditions

- [ ] nextjs_523375afdf: The application had already opted into the new Link behavior through the experimental option introduced in 12.2
- [ ] nextjs_523375afdf: The consequence of leaving a nested <a> inside <Link> in Next.js 13 (e.g. error vs. nested anchors) is not stated
- [ ] nextjs_f8d3770f36: Usage of props removed in the new component (e.g. layout) raises impact; the experimental codemod removes unused props and adds inline styles.
- [ ] nextjs_f8d3770f36: If the application already uses next/future/image, it already uses the new behavior.
- [ ] nextjs_16494e4a2c: The application does not explicitly set swcMinify in its Next.js config and therefore relies on the default value.
- [ ] nextjs_16494e4a2c: The application explicitly sets swcMinify: false in its Next.js config, opting out of the new default.

### Source disagreements

- node minimum for 13: Next.js 'How to upgrade to version 13' (current docs) says the minimum Node.js for 13 is 16.14.0; next_pkg@v13.0.0 (engines.node) says '>=14.6.0'. → Package metadata outranks prose. The prose matches later 13.x metadata (next_pkg@v13.5.0), so the page was likely edited after release to reflect the latest 13.x floor.
- react_peer minimum for 13: Next.js upgrade guide at v13.0.0 (Upgrading from 12 to 13) says the minimum React (peer dependency) for 13 is 18.2.0; next_pkg@v13.0.0 (peerDependencies.react) says '^18.0.0-0'. → Package metadata outranks prose. The prose matches later 13.x metadata (next_pkg@v13.4.0, next_pkg@v13.5.0), so the page was likely edited after release to reflect the latest 13.x floor.
- react_peer minimum for 13: Next.js 'How to upgrade to version 13' (current docs) says the minimum React (peer dependency) for 13 is 18.2.0; next_pkg@v13.0.0 (peerDependencies.react) says '^18.0.0-0'. → Package metadata outranks prose. The prose matches later 13.x metadata (next_pkg@v13.4.0, next_pkg@v13.5.0), so the page was likely edited after release to reflect the latest 13.x floor.

### Open questions

- Next.js 13.x and 14.x minor release notes (blog posts, GitHub releases) were not mined; deprecations introduced in minors (for example in 13.3/13.4) may be missing.
- Hosting platforms (Vercel, Netlify, self-hosted Node, Docker) and third-party Next.js plugins have their own compatibility windows.
- App Router adoption is optional; risks specific to migrating pages/ to app/ are out of scope unless the guides state them.
- Source next_guide_14_pages_canary was rejected (transclusion_stub); its content was not used.
- [nextjs_523375afdf] Unconfirmed: The consequence of leaving a nested <a> inside <Link> in Next.js 13 (e.g. error vs. nested anchors) is not stated (The text does not state whether unmigrated <Link><a> code errors, renders nested anchors, or keeps working.)
- [nextjs_f8d3770f36] Unconfirmed: If the application already uses next/future/image, it already uses the new behavior. (The text does not state what happens to next/future/image imports in Next.js 13/14.)
- [nextjs_16494e4a2c] Unconfirmed: The application explicitly sets swcMinify: false in its Next.js config, opting out of the new default. (The text does not state whether explicitly setting swcMinify to false remains supported in version 14.)

## Context facts (not risks)


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
