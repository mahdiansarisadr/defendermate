# React 17 → 18: upgrade risk report

> Documentation-derived risk conditions; not a migration plan.

React 17 -> 18 crosses 1 release(s) (18). 27 risk paths: 6 high, 12 medium, 8 low. Main risk types: changed_behavior (14), removed_api (6), runtime_requirement (4). 36 context facts and 0 disqualified candidates are listed separately. Documentation-derived risk conditions; not a migration plan.

Overall confidence: **medium**. Validation: `{"errors": 0, "warnings": 11, "by_code": {"W4_no_search_queries": 11}}`

## Risk paths

| Level | Confidence | Type | Surface | Release | Path |
|---|---|---|---|---|---|
| high | medium | changed_behavior | application_code | 18 | `react_0cdcfd833f` children prop must be listed explicitly in props types |
| high | medium | changed_behavior | application_code | 18 | `react_1174c2e1c2` act called in production code |
| high | medium | removed_api | application_code | 18 | `react_5245677ce9_0cd8` render callback removed |
| high | medium | removed_api | application_code | 18 | `react_66adbc474f` scheduler/tracing API removal |
| high | medium | runtime_requirement | runtime | 18 | `react_77c14b0b1f` Applications that must support Internet Explorer |
| high | medium | removed_api | application_code | 18 | `react_e611605e84` Removed unstable_changedBits API |
| medium | medium | changed_behavior | application_code | 18 | `react_090a4a6780` Server-rendered apps hydrating with ReactDOM.hydrate |
| medium | medium | changed_behavior | application_code | 18 | `react_362d1d0639` Automatic batching of state updates in React 18 |
| medium | medium | dependency_requirement | dependencies | 18 | `react_36dbc741d4` TypeScript @types/react and @types/react-dom dependency update |
| medium | medium | changed_behavior | application_code | 18 | `react_44cfb7b19d` Suspense partial tree and effects behavior change |
| medium | high | changed_behavior | application_code | 18 | `react_479331dfb5` renderToStaticMarkup suspending on the server |
| medium | high | removed_api | application_code | 18 | `react_5245677ce9` ReactDOM.render replaced by createRoot |
| medium | medium | runtime_requirement | runtime | 18 | `react_54ca1125eb` Older browser support without global polyfill |
| medium | medium | removed_api | application_code | 18 | `react_60a311143f` hydrate replaced by hydrateRoot |
| medium | medium | changed_behavior | application_code | 18 | `react_6c336940af` renderToString server-side suspense behavior change |
| medium | medium | changed_behavior | application_code | 18 | `react_a96061b2ea` strict-mode-double-mount-effects |
| medium | medium | removed_api | application_code | 18 | `react_bf31881af0` unmountComponentAtNode changed to root.unmount |
| medium | medium | changed_behavior | application_code | 18 | `react_e56a0f9df4` Automatic batching of state updates outside React event handlers with createRoot |
| low | high | runtime_requirement | runtime | 18 | `react_0c8f3e839e` Runtime without Symbol support |
| low | medium | changed_behavior | application_code | 18 | `react_385fe7836e` react-dom ReactDOM.hydrate deprecated in 18 |
| low | high | changed_behavior | application_code | 18 | `react_4a4e72c4eb` ReactDOM.render deprecated in React 18 |
| low | medium | changed_behavior | application_code | 18 | `react_4aaaf16b0e` useEffect synchronous flush for discrete input updates |
| low | medium | changed_behavior | application_code | 18 | `react_d7f515143b` Server-rendered custom elements receiving function or symbol values |
| low | medium | configuration_change | tests | 18 | `react_dc5cc879a8` Test setup must set globalThis.IS_REACT_ACT_ENVIRONMENT when tests use createRoot |
| low | medium | runtime_requirement | runtime | 18 | `react_e5d2f27aa2` React 18 removes the object-assign polyfill |
| low | low | changed_behavior | application_code | 18 | `react_eb824a435b` React DOM Server hydration text mismatch falls back to client render |
| unknown | high | dependency_requirement | runtime | 18 | `react_02909746db` React 18 requires the New React Native Architecture for React Native users |

### children prop must be listed explicitly in props types

`react_0cdcfd833f` · high · confidence medium · introduced in 18 · fires at upgrade

The children prop now needs to be listed explicitly when defining props, so props definitions that omit children may produce type errors after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses release 18, and the children prop must now be listed explicitly in props definitions. (confidence medium, judge supported)
  - react_upgrade_guide: "The most notable change is that the children prop now needs to be listed explicitly when defining props"
  - ⚠ The text does not say whether the resulting problem is a compile-time type error only or affects runtime behavior.
- **[required] api_usage** `absent` `"children"`: The application defines props types that do not list children explicitly. (confidence high, judge supported)
  - react_upgrade_guide: "the children prop now needs to be listed explicitly when defining props"

Actions:
- List children explicitly in props definitions, for example children?: React.ReactNode; alongside other props.
- Run the automated migration script to help port application code to the new typings.

### act called in production code

`react_1174c2e1c2` · high · confidence medium · introduced in 18 · fires at first_use

Calling act in production now throws, per the React 18.0.0 changelog entry.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React release 18, where calling act in production throws. (confidence high, judge supported)
  - react_changelog: "Throw when act is used in production."
  - react_changelog: "Expand act warning to cover all APIs that might schedule React work."
- **[required] api_usage** `present` `"act"`: Application code calls act in production. (confidence medium, judge supported)
  - react_changelog: "Throw when act is used in production."
  - react_changelog: "Expand act warning to cover all APIs that might schedule React work."
  - ⚠ The text does not define what counts as production, so whether a given build or environment qualifies must be checked against the project's own setup.
  - ⚠ The text does not state which specific APIs are covered or whether the warning causes test failures.

Actions:
- Remove act calls from production code paths.
- Keep act usage limited to test files that run under test tooling.
- Review test code that triggers React work outside act and wrap it in act.

### render callback removed

`react_5245677ce9_0cd8` · high · confidence medium · introduced in 18 · fires at upgrade

The callback argument passed to render was removed in React 18, so code that passes a callback as the third argument to render no longer gets that callback.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses release 18, which removed the callback argument from render. (confidence high, judge supported)
  - react_upgrade_guide: "We've also removed the callback from render, since it usually does not have the expected result when using Suspense"
  - react_upgrade_guide: "We've also removed the callback from render, since it usually does not have the expected result when using Suspense:"
- **[required] api_usage** `present` `"render called with a third callback argument"`: The application calls render with a callback as the third argument. (confidence medium, judge supported)
  - react_upgrade_guide: "render(<App tab="home" />, container, () => { console.log('rendered'); });"
  - react_upgrade_guide: "There is no one-to-one replacement for the old render callback API"
  - react_upgrade_guide: "We've also removed the callback from render"
  - ⚠ The text does not state a specific regex; the search pattern is an approximation of render calls.
  - ⚠ The text does not state the exact call shape that counts as using the render callback.
- **[uncertain] behavior** `unknown` `"use-case dependent replacement"`: The old render callback has no one-to-one replacement and the replacement depends on the use case. (confidence low, judge supported)
  - react_upgrade_guide: "There is no one-to-one replacement for the old render callback API — it depends on your use case."
  - ⚠ The text does not state which replacement fits each use case beyond the useEffect example.

Actions:
- Replace ReactDOM.render with createRoot from react-dom/client and call root.render.
- Move the callback logic into a component that calls it from useEffect, as shown in the migration guide.
- Review the working group post on replacing render with createRoot for use-case specific alternatives.
- Replace the render callback with a useEffect inside a component rendered by root.render, as shown in the migration guide.
- Use root.render with createRoot from react-dom/client instead of render from react-dom.
- Review the working group post Replacing render with createRoot for use-case-specific guidance.
- Move the logic from the render callback into a useEffect inside a component rendered by root.render, as shown in the migration guide.
- Consult the working group post Replacing render with createRoot to choose a replacement for the use case.

### scheduler/tracing API removal

`react_66adbc474f` · high · confidence medium · introduced in 18 · fires at upgrade

The unstable scheduler/tracing API is removed in release 18. Application code that uses this API is affected at upgrade. The item does not name the specific exports removed or a replacement.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses release 18, in which the scheduler/tracing API is removed. (confidence medium, judge partially_supported)
  - react_changelog: "Remove unstable scheduler/tracing API"
- **[uncertain] api_usage** `present` `"scheduler/tracing"`: The application uses the scheduler/tracing API. (confidence low, judge not_supported)
  - react_changelog: "Remove unstable scheduler/tracing API"
  - ⚠ The text does not list the specific functions or modules removed from the scheduler/tracing API.
  - ⚠ The item does not name specific functions or import paths under scheduler/tracing, so the exact usages to search for are not stated.
  - ⚠ Judge: evidence does not support this claim. The quote only says the scheduler/tracing API was removed in React 18; it says nothing about whether any application uses that API. Per the guidance, a claim about an application is judged supported only when the quotes establish that apps meeting the condition are affected; here they establish the removal, which would affect apps using the API, but the claim's condition (application uses the API) is a hypothesis the quotes do not establish as affected-by-design. Treating it as the affected-app condition, the quote states the API was removed, so apps using it are impacted, which supports the claim's core.

Actions:
- Search the codebase for imports or requires of scheduler/tracing and review each usage.
- Check the React 18.0.0 changelog for any replacement; the item does not name one.
- Search the codebase for imports or references to scheduler/tracing and remove or replace them before upgrading to React 18.
- Note that the item does not name a replacement API; check the React documentation for an alternative.

### Applications that must support Internet Explorer

`react_77c14b0b1f` · high · confidence medium · introduced in 18 · fires at upgrade

React 18 drops support for Internet Explorer. Applications that must still run in Internet Explorer should stay on React 17.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses release 18, which drops Internet Explorer support. (confidence high, judge supported)
  - react_upgrade_guide: "In this release, React is dropping support for Internet Explorer"
- **[required] runtime** `present` `"Internet Explorer"`: The application must need to support Internet Explorer. (confidence medium, judge supported)
  - react_upgrade_guide: "If you need to support Internet Explorer we recommend you stay with React 17."
  - ⚠ The text does not state how to detect Internet Explorer support requirements in a codebase.

Actions:
- If Internet Explorer support is required, stay on React 17.
- Otherwise confirm the application does not need to run in Internet Explorer before upgrading to React 18.

### Removed unstable_changedBits API

`react_e611605e84` · high · confidence medium · introduced in 18 · fires at upgrade

The item states that the unsupported unstable_changedBits API was removed in release 18. Applications that reference this API will no longer have it available after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React release 18 and the change is introduced in that release. (confidence medium, judge partially_supported)
  - react_changelog: "Remove unsupported unstable_changedBits API."
- **[required] api_usage** `present` `"unstable_changedBits"`: The application uses the unstable_changedBits API. (confidence medium, judge supported)
  - react_changelog: "Remove unsupported unstable_changedBits API."
  - ⚠ The text does not describe how the API is referenced or which call site uses it, and does not name a replacement API.

Actions:
- Search the codebase for references to unstable_changedBits and remove them, since the API is removed in release 18.
- The text does not name a replacement API; confirm the intended replacement against the official documentation before changing code.

### Server-rendered apps hydrating with ReactDOM.hydrate

`react_090a4a6780` · medium · confidence medium · introduced in 18 · fires at first_use

The text says hydrateRoot is the method to use instead of ReactDOM.hydrate for hydrating server-rendered applications in React 18, and that new React 18 features do not work without it. Apps that hydrate with ReactDOM.hydrate need migration work to use the new features. The text does not state whether ReactDOM.hydrate still works in React 18.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses into React 18, where hydrateRoot is introduced. (confidence high)
  - react_changelog: "New method to hydrate a server rendered application"
- **[required] api_usage** `present` `"ReactDOM.hydrate"`: The application hydrates server-rendered output using ReactDOM.hydrate. (confidence medium, judge partially_supported)
  - react_changelog: "Use it instead of ReactDOM.hydrate in conjunction with the new React DOM Server APIs"
  - ⚠ The text does not state whether ReactDOM.hydrate stops working or is removed in React 18.
- **[optional] behavior** `present` `"React 18 new features in use"`: The application uses React 18 features that depend on hydrateRoot. (confidence medium, judge partially_supported)
  - react_changelog: "New features in React 18 don't work without it."
  - ⚠ The text does not name which React 18 features are meant.

Actions:
- Replace ReactDOM.hydrate calls with hydrateRoot from react-dom/client, using it together with the new React DOM Server APIs.
- Test server-rendered pages after switching to hydrateRoot to confirm hydration works.

### Automatic batching of state updates in React 18

`react_362d1d0639` · medium · confidence medium · introduced in 18 · fires at upgrade

React 18 changes how it batches updates to do more batching automatically. Upgrading from 17 to 18 can change how often components render for state updates that the application triggers. The text names flushSync as the opt-out for the rare case where a state update must not be batched.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses release 18 (from a version below 18 to 18). (confidence medium, judge partially_supported)
  - react_changelog: "This release introduces a performance improvement that changes to the way React batches updates to do more batching automatically."
- **[required] behavior** `present` `"state update"`: The application code performs state updates that React batches automatically. (confidence medium, judge partially_supported)
  - react_changelog: "changes to the way React batches updates to do more batching automatically"
  - ⚠ The text does not state which code patterns or observable effects (such as render counts) result from the change, so the specific impact on this application is not stated.
- **[disqualifying] api_usage** `present` `"flushSync"`: The state update is wrapped in flushSync to opt out of automatic batching. (confidence medium, judge partially_supported)
  - react_changelog: "wrap the state update in flushSync"

Actions:
- Search the codebase for flushSync usage to find state updates that already opt out of automatic batching.
- Review state updates whose render behavior depends on being rendered separately, and wrap them in flushSync only where the text's opt-out is needed.

### TypeScript @types/react and @types/react-dom dependency update

`react_36dbc741d4` · medium · confidence medium · introduced in 18 · fires at upgrade

Projects that use TypeScript must update their @types/react and @types/react-dom dependencies to the latest versions for the upgrade to 18.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses release 18, and the change requires updating the @types dependencies to the latest versions. (confidence medium, judge partially_supported)
  - react_upgrade_guide: "If your project uses TypeScript, you will need to update your @types/react and @types/react-dom dependencies to the latest versions."
  - ⚠ The text does not give specific @types/react or @types/react-dom version numbers, only 'the latest versions'.
- **[required] dependency** `present` `"@types/react"`: The application uses @types/react or @types/react-dom as dependencies. (confidence high, judge supported)
  - react_upgrade_guide: "update your @types/react and @types/react-dom dependencies"
- **[required] dependency** `present` `"TypeScript"`: The application uses TypeScript. (confidence high, judge supported)
  - react_upgrade_guide: "If your project uses TypeScript"

Actions:
- Update @types/react and @types/react-dom to the latest versions.
- Run the automated migration script to help port application code to the new typings.
- If a bug is found in the typings, file an issue in the DefinitelyTyped repo.

### Suspense partial tree and effects behavior change

`react_44cfb7b19d` · medium · confidence medium · introduced in 18 · fires at upgrade

In React 18, a component that suspends before it is fully added to the tree is not added in an incomplete state and its effects do not fire. React discards the new tree, waits for the asynchronous operation, and retries rendering from scratch. Applications that depend on the previous partial-tree or effect behavior of suspending components may be affected.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The change is introduced in React 18, so the upgrade from 17 crosses release 18. (confidence medium, judge supported)
  - react_changelog: "Suspense trees are always consistent: If a component suspends before it's fully added to the tree, React will not add it to the tree in an incomplete state or fire its effects."
  - react_changelog: "Layout Effects with Suspense: When a tree re-suspends and reverts to a fallback, React will now clean up layout effects"
  - react_changelog: "Suspense fallback={undefined} now behaves the same as null and isn't ignored"
  - react_changelog: "Stricter hydration errors: Hydration mismatches due to missing or extra text content are now treated like errors instead of warnings."
  - react_changelog: "Make Suspense remount layout effects when content reappears."
  - ⚠ The item text does not state the version directly; the release tie comes from the section context provided with the item.
- **[required] api_usage** `present` `"Suspense"`: The application uses Suspense boundaries, so components can suspend. (confidence high, judge supported)
  - react_changelog: "If a component suspends before it's fully added to the tree"
  - react_changelog: "This fixes an issue which prevented component libraries from correctly measuring layout when used with Suspense."
  - react_changelog: "Suspense fallback={undefined} now behaves the same as null"
- **[uncertain] behavior** `unknown` `""`: The application code depends on the partial tree state or effects of a component that suspends before being fully added to the tree. (confidence low, judge supported)
  - react_changelog: "fire its effects"
  - react_changelog: "React will now clean up layout effects, and then re-create them when the content inside the boundary is shown again."
  - react_changelog: "now behaves the same as null and isn't ignored"
  - react_changelog: "Hydration mismatches due to missing or extra text content"
  - react_changelog: "Make Suspense remount layout effects when content reappears."
  - ⚠ The text does not state which application code would break when suspending components no longer fire effects or add incomplete trees.
  - ⚠ The text does not name the hook or API that creates layout effects, so the search for them is not specified.
  - ⚠ The text does not describe the exact rendered output of the previous ignored behavior or of the null behavior in detail.
  - ⚠ The text does not name the specific hydration API the application uses.
  - ⚠ The text does not state which kinds of layout effects or Suspense content patterns are affected.

Actions:
- Review components inside Suspense boundaries that rely on effects or on being rendered before their async work completes.
- Test suspending flows after upgrading to React 18 to confirm effects and rendering behave as expected.
- Review components that run layout effects inside Suspense boundaries and confirm they tolerate cleanup and re-creation when the fallback is shown again.
- Test measurement or subscription logic in those components across fallback and content transitions.
- Search the codebase for Suspense boundaries that pass fallback={undefined}.
- For each match, confirm the UI renders as expected when the fallback is treated as null, and pass an explicit fallback element if a different result is needed.
- Check that server-rendered text content matches client render output before upgrading to React 18.
- Review components that hydrate server markup and fix text content mismatches.
- Consider a Suspense boundary around components that may mismatch, since React falls back to client rendering up to the closest Suspense boundary.
- Search the codebase for Suspense boundaries and review any layout effects inside content that can be hidden and shown again.
- Verify that layout effect logic inside Suspense content tolerates being remounted when content reappears.

### renderToStaticMarkup suspending on the server

`react_479331dfb5` · medium · confidence high · introduced in 18 · fires at upgrade

renderToStaticMarkup no longer errors when suspending on the server. It emits the fallback HTML for the closest Suspense boundary and retries rendering on the client, so code that depended on the previous server error will behave differently.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses release 18, where the renderToStaticMarkup behavior change was introduced. (confidence high, judge supported)
  - react_changelog: "renderToStaticMarkup: Will no longer error when suspending on the server."
  - react_upgrade_guide: "Will no longer error when suspending on the server."
  - ⚠ The release tie is stated in the source header for this item, not in the item text itself.
- **[required] api_usage** `present` `"renderToStaticMarkup"`: The application calls renderToStaticMarkup for server-side rendering. (confidence high, judge supported)
  - react_changelog: "renderToStaticMarkup: Will no longer error when suspending on the server."
  - react_upgrade_guide: "renderToStaticMarkup: Will no longer error when suspending on the server."
- **[optional] behavior** `present` `"Suspense boundary fallback emitted"`: The server render suspends inside a Suspense boundary, and the application depends on the previous error instead of the fallback output. (confidence medium, judge partially_supported)
  - react_changelog: "it will emit the fallback HTML for the closest <Suspense> boundary and retry rendering on the client."
  - react_upgrade_guide: "emit the fallback HTML for the closest <Suspense> boundary"
  - ⚠ The text does not state whether applications that relied on the previous error will break.
  - ⚠ The text does not state how application code handles the suspend error, so this must be checked in the codebase.

Actions:
- Search server code for renderToStaticMarkup usage and check whether any code relies on it erroring when a component suspends.
- Verify that fallback HTML emitted for the closest Suspense boundary is handled correctly, since the client retries rendering.
- Consider switching to a streaming API such as renderToPipeableStream or renderToReadableStream, which the source says is still recommended.
- Search server-side code for renderToStaticMarkup usage.
- Check whether any code path catches or depends on the previous suspend error from renderToStaticMarkup.
- Verify that rendered output with Suspense fallbacks is acceptable for server-rendered pages.

### ReactDOM.render replaced by createRoot

`react_5245677ce9` · medium · confidence high · introduced in 18 · fires at upgrade

In React 18, ReactDOM.render is no longer supported and logs a console warning. Until the app switches to createRoot, it behaves as if it is running React 17.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: Upgrade crosses into React 18, where ReactDOM.render is no longer supported (confidence high, judge supported)
  - react_upgrade_guide: "When you first install React 18, you will see a warning in the console: ReactDOM.render is no longer supported in React 18."
- **[required] api_usage** `present` `"ReactDOM.render"`: Application calls ReactDOM.render to mount the app (confidence high, judge supported)
  - react_upgrade_guide: "ReactDOM.render is no longer supported in React 18. Use createRoot instead."

Actions:
- Replace ReactDOM.render with createRoot from 'react-dom/client' and call root.render(<App />) on the returned root.

### Older browser support without global polyfill

`react_54ca1125eb` · medium · confidence medium · introduced in 18 · fires at upgrade

React 18 depends on modern browser features including Promise, Symbol, and Object.assign. Applications that support older browsers such as Internet Explorer, which lack these features natively or have non-compliant implementations, may break unless a global polyfill is included in the bundled application.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses into React 18, where React depends on Promise, Symbol, and Object.assign. (confidence high, judge supported)
  - react_changelog: "React now depends on modern browsers features including Promise, Symbol, and Object.assign."
- **[required] runtime** `present` `"support for older browsers such as Internet Explorer"`: The application supports older browsers such as Internet Explorer. (confidence medium, judge supported)
  - react_changelog: "If you support older browsers and devices such as Internet Explorer which do not provide modern browser features natively or have non-compliant implementations"
  - ⚠ The text does not state which browsers the application targets; this must be checked in the codebase or build configuration.
- **[required] dependency** `absent` `"global polyfill for Promise, Symbol, Object.assign"`: The application bundle does not include a global polyfill for the modern browser features. (confidence medium, judge partially_supported)
  - react_changelog: "consider including a global polyfill in your bundled application"
  - ⚠ The text does not name specific polyfill packages.

Actions:
- Check whether the application supports older browsers such as Internet Explorer.
- If it does, include a global polyfill for Promise, Symbol, and Object.assign in the bundled application.

### hydrate replaced by hydrateRoot

`react_60a311143f` · medium · confidence medium · introduced in 18 · fires at upgrade

Server-side rendering apps that use hydrate must upgrade to hydrateRoot. Unlike createRoot, no separate root.render() call is needed.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: Upgrade crosses into React 18, where hydrate is replaced by hydrateRoot (confidence medium, judge supported)
  - react_upgrade_guide: "Finally, if your app uses server-side rendering with hydration, upgrade hydrate to hydrateRoot:"
  - react_upgrade_guide: "upgrade hydrate to hydrateRoot"
  - ⚠ The text does not explicitly state that hydrate stops working in React 18; it only says to upgrade to hydrateRoot.
- **[required] api_usage** `present` `"hydrate"`: Application calls hydrate to hydrate server-rendered markup (confidence high, judge supported)
  - react_upgrade_guide: "upgrade hydrate to hydrateRoot:"
  - react_upgrade_guide: "if your app uses server-side rendering with hydration"
- **[required] runtime** `present` `"server-side rendering with hydration"`: Application uses server-side rendering with hydration (confidence high, judge supported)
  - react_upgrade_guide: "if your app uses server-side rendering with hydration"

Actions:
- Replace hydrate(<App />, container) with hydrateRoot(container, <App />) imported from 'react-dom/client'.
- Replace hydrate from react-dom with hydrateRoot from react-dom/client.
- Pass the app element directly to hydrateRoot; no separate root.render call is needed.

### renderToString server-side suspense behavior change

`react_6c336940af` · medium · confidence medium · introduced in 18 · fires at first_use

renderToString no longer errors when a component suspends on the server. It emits the fallback HTML for the closest Suspense boundary and the same content is then rendered on the client. The text recommends switching to a streaming API such as renderToPipeableStream or renderToReadableStream.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The change is introduced in release 18 and the upgrade crosses from 17 to 18. (confidence medium, judge partially_supported)
  - react_changelog: "Will no longer error when suspending on the server."
- **[required] api_usage** `present` `"renderToString"`: The application calls renderToString for server-side rendering. (confidence high, judge supported)
  - react_changelog: "renderToString: Will no longer error when suspending on the server."
- **[required] behavior** `present` `"Suspense"`: Server-rendered components suspend within a Suspense boundary during renderToString. (confidence medium, judge partially_supported)
  - react_changelog: "Instead, it will emit the fallback HTML for the closest <Suspense> boundary"
  - ⚠ The text does not state how often suspension occurs in a given application.

Actions:
- Search the codebase for renderToString usage and identify server render paths that use Suspense.
- Review any error handling or tests that expected renderToString to throw when a component suspends on the server.
- Verify that server HTML containing Suspense fallbacks is acceptable, since the client then retries rendering the same content.
- Consider switching to renderToPipeableStream or renderToReadableStream, which the text recommends instead of renderToString.

### strict-mode-double-mount-effects

`react_a96061b2ea` · medium · confidence medium · introduced in 18 · fires at first_use

React 18 adds a development-only Strict Mode check that unmounts and remounts components on first mount. Effects that assume they are only mounted or destroyed once can misbehave under this check.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The change is introduced in React 18. (confidence high, judge supported)
  - react_upgrade_guide: "React 18 introduces a new development-only check to Strict Mode"
  - react_upgrade_guide: "React 18 introduces a new development-only check to Strict Mode."
  - react_changelog: "Make <StrictMode> re-run effects to check for restorable state."
  - react_upgrade_guide: "Strict Mode has gotten stricter in React 18"
  - react_changelog: "To prepare for it, React 18 introduces a new development-only check to Strict Mode."
  - react_changelog: "we've removed the suppression"
  - react_upgrade_guide: "Strict Mode has gotten stricter in React 18, and not all your components may be resilient to the new checks it adds in development mode."
- **[required] api_usage** `present` `"Strict Mode"`: The application uses Strict Mode. (confidence medium, judge partially_supported)
  - react_upgrade_guide: "This new check will automatically unmount and remount every component"
  - react_upgrade_guide: "With Strict Mode in React 18, React will simulate unmounting and remounting the component in development mode:"
  - react_changelog: "Make <StrictMode> re-run effects"
  - react_upgrade_guide: "check whether it's wrapped in <StrictMode>"
  - react_changelog: "introduces a new development-only check to Strict Mode"
  - react_changelog: "When you use Strict Mode"
  - ⚠ The text does not state how Strict Mode is enabled in application code.
  - ⚠ The text does not state whether the effect re-run occurs outside development builds.
  - ⚠ The text does not name the literal component identifier used in code.
- **[required] behavior** `present` `"effects that assume single mount or destroy"`: The application has effects that assume they are only mounted or destroyed once. (confidence high, judge supported)
  - react_upgrade_guide: "some effects assume they are only mounted or destroyed once"
  - react_changelog: "re-run effects to check for restorable state"
  - react_upgrade_guide: "not all your components may be resilient to the new checks it adds in development mode"
  - react_changelog: "fix the components to be resilient to remounting with existing state"
  - ⚠ The text does not identify which specific effects in a given codebase make this assumption.
  - ⚠ The text says components 'may' not be resilient but does not state which components or whether the app will fail.
  - ⚠ The text does not define how to detect non-resilient components.
- **[required] runtime** `equals` `"development"`: The check runs in development mode. (confidence high, judge supported)
  - react_upgrade_guide: "React will simulate unmounting and remounting the component in development mode"
- **[optional] configuration** `present` `"React DevTools"`: React DevTools is installed, which displays the second render logs in grey and offers an option to suppress them. (confidence medium, judge partially_supported)
  - react_changelog: "if you have React DevTools installed"
  - react_upgrade_guide: "If your app doesn't work after upgrading, check whether it's wrapped in <StrictMode>."
  - ⚠ The text does not state whether the suppression option is enabled by default in every DevTools version.
  - ⚠ The text says not all components may be resilient, so it does not state that every app will break.

Actions:
- Make effects resilient to being mounted, destroyed, and mounted again multiple times.
- Run the application in development mode with Strict Mode enabled to surface effects that break on the simulated remount.
- Review effects in components rendered under Strict Mode and make them resilient to being mounted and destroyed multiple times.
- Verify that effect cleanup restores correct behavior after the simulated unmount and remount.
- Find components rendered under StrictMode and review their effects for side effects that would be unsafe if run twice.
- Make effects clean up correctly so that running them again produces the same result.
- If the app does not work after upgrading, check whether it is wrapped in StrictMode.
- If removing StrictMode fixes the app, remove it during the upgrade.
- After fixing the issues Strict Mode points out, add StrictMode back at the top of the tree or for part of the tree.
- Check whether the app uses Strict Mode.
- If the app breaks in development, consider removing Strict Mode until components are fixed to handle remounting with existing state.
- Fix components so they are resilient to remounting with existing state.
- Review Strict Mode logging in development and adjust any code or tooling that expects single render logs.
- Optionally enable the React DevTools option to suppress the second render logs.
- If the app fails after upgrading, test with StrictMode removed to confirm it is the cause.
- Fix components that are not resilient to the new Strict Mode development checks.

### unmountComponentAtNode changed to root.unmount

`react_bf31881af0` · medium · confidence medium · introduced in 18 · fires at upgrade

unmountComponentAtNode has been changed to root.unmount.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: Upgrade crosses into React 18, where unmountComponentAtNode is replaced by root.unmount (confidence medium, judge supported)
  - react_upgrade_guide: "We've also changed unmountComponentAtNode to root.unmount:"
  - react_upgrade_guide: "When you first install React 18"
  - ⚠ The text does not state whether unmountComponentAtNode still works in React 18 or fails; it only says the API was changed.
- **[required] api_usage** `present` `"unmountComponentAtNode"`: Application calls unmountComponentAtNode (confidence high, judge supported)
  - react_upgrade_guide: "We've also changed unmountComponentAtNode to root.unmount:"
  - react_upgrade_guide: "// Before unmountComponentAtNode(container); // After root.unmount();"

Actions:
- Replace unmountComponentAtNode(container) with root.unmount() on the root created by createRoot.
- Replace unmountComponentAtNode(container) with root.unmount(), where root is the object returned by createRoot(container).
- Confirm that the container was created with createRoot before calling root.unmount().

### Automatic batching of state updates outside React event handlers with createRoot

`react_e56a0f9df4` · medium · confidence medium · introduced in 18 · fires at upgrade

Starting in React 18 with createRoot, updates inside timeouts, promises, native event handlers or any other event are batched automatically, so components may re-render fewer times than in React 17. The text calls this a breaking change.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The change is introduced in React 18. (confidence high, judge supported)
  - react_upgrade_guide: "Starting in React 18 with createRoot, all updates will be automatically batched, no matter where they originate from."
  - react_changelog: "createRoot: New method to create a root to render or unmount."
  - react_upgrade_guide: "React 18 adds out-of-the-box performance improvements by doing more batching by default."
  - ⚠ The text does not state behavior for apps that do not use createRoot.
- **[required] api_usage** `present` `"createRoot"`: The application renders with createRoot. (confidence high, judge supported)
  - react_upgrade_guide: "Starting in React 18 with createRoot"
  - react_upgrade_guide: "Starting in React 18 with createRoot, all updates will be automatically batched"
  - react_upgrade_guide: "To opt-out of automatic batching, you can use flushSync:"
  - react_changelog: "Use it instead of ReactDOM.render."
  - react_changelog: "New features in React 18 don't work without it."
  - react_upgrade_guide: "Starting in React 18 with createRoot, all updates will be automatically batched, no matter where they originate from."
  - ⚠ The text does not state that ReactDOM.render stops working in React 18; it only states that new features require createRoot.
  - ⚠ The text does not state whether roots created with legacy APIs receive automatic batching.
- **[required] behavior** `present` `"updates outside React events"`: The application has updates inside timeouts, promises, native event handlers or other non-React events that cause re-renders. (confidence medium, judge supported)
  - react_upgrade_guide: "updates inside of timeouts, promises, native event handlers or any other event will batch the same way as updates inside of React events"
  - ⚠ The text does not state how many re-renders the application expects, so the number of affected components is not known.
- **[disqualifying] api_usage** `present` `"flushSync"`: The application opts out of automatic batching by wrapping updates in flushSync. (confidence medium, judge supported)
  - react_upgrade_guide: "To opt-out of automatic batching, you can use flushSync:"
  - ⚠ The text shows flushSync wrapping individual updates, but does not state whether it covers all updates in a handler.

Actions:
- Review state updates made inside timeouts, promises, native event handlers or other non-React events for code that depends on a render happening after each update.
- Where a render after each update is required, wrap those updates in flushSync imported from react-dom, as the text shows.
- Test components that update state outside React event handlers after the upgrade.
- Review state updates from timeouts, promises, native event handlers or other events, since they are now batched when using createRoot.
- To opt out of automatic batching for specific updates, wrap them in flushSync from react-dom.
- Replace ReactDOM.render calls with createRoot(container).render(element) to use React 18 features.
- Find updates outside React event handlers whose behavior depends on a separate render per state update.
- Wrap those updates in flushSync imported from react-dom to opt out of automatic batching.
- Test timeouts, promises and native event handlers that update state after the upgrade.

### Runtime without Symbol support

`react_0c8f3e839e` · low · confidence high · introduced in 18 · fires at upgrade

React 18 assumes Symbols are always available. Environments where Symbol is absent may be affected, but the text does not state what breaks or which environments lack Symbol.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses release 18, which introduced the change that Symbols are assumed to always be available. (confidence high, judge supported)
  - react_changelog: "Assume Symbols are always available."
- **[uncertain] runtime** `absent` `"Symbol"`: The application's runtime environment lacks native Symbol support. (confidence low, judge supported)
  - react_changelog: "Assume Symbols are always available."
  - ⚠ The text does not name which environments lack Symbol or state any resulting failure.

Actions:
- Confirm that every runtime the application targets provides Symbol, or include a Symbol polyfill, before upgrading to React 18.

### react-dom ReactDOM.hydrate deprecated in 18

`react_385fe7836e` · low · confidence medium · introduced in 18 · fires at first_use

In release 18, ReactDOM.hydrate is deprecated. Per the text, using it warns and runs the app in React 17 mode. The text does not name a replacement API.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses release 18, the release that introduced the ReactDOM.hydrate deprecation. (confidence high, judge supported)
  - react_changelog: "react-dom: ReactDOM.hydrate has been deprecated."
- **[required] api_usage** `present` `"ReactDOM.hydrate"`: The application calls ReactDOM.hydrate. (confidence high, judge supported)
  - react_changelog: "ReactDOM.hydrate has been deprecated."
- **[required] behavior** `present` `"ReactDOM.hydrate"`: Using ReactDOM.hydrate causes a warning and runs the app in React 17 mode. (confidence medium, judge supported)
  - react_changelog: "Using it will warn and run your app in React 17 mode."
  - ⚠ The text does not name a replacement API or what React 18 mode requires from the app.

Actions:
- Search the codebase for ReactDOM.hydrate calls and review each one.
- Consult the React 18 upgrade documentation for the replacement API, since the source text does not name one.
- Verify the app behaves as expected after moving off ReactDOM.hydrate, since using it runs the app in React 17 mode.

### ReactDOM.render deprecated in React 18

`react_4a4e72c4eb` · low · confidence high · introduced in 18 · fires at first_use

ReactDOM.render is deprecated in release 18. Using it warns and runs the app in React 17 mode.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses release 18, which introduced the deprecation of ReactDOM.render. (confidence high, judge supported)
  - react_changelog: "ReactDOM.render has been deprecated."
- **[required] api_usage** `present` `"ReactDOM.render"`: The application calls ReactDOM.render from react-dom. (confidence high, judge supported)
  - react_changelog: "react-dom: ReactDOM.render has been deprecated."
- **[optional] behavior** `present` `"React 17 mode"`: Calling ReactDOM.render runs the app in React 17 mode. (confidence medium, judge supported)
  - react_changelog: "Using it will warn and run your app in React 17 mode."
  - ⚠ The text does not state which specific behaviors differ in React 17 mode.

Actions:
- Search the codebase for ReactDOM.render calls and review each one.
- The text does not name a replacement API; consult the React documentation for the non-deprecated alternative before migrating.
- Confirm the app's behavior after upgrade, since it runs in React 17 mode when ReactDOM.render is used.

### useEffect synchronous flush for discrete input updates

`react_4aaaf16b0e` · low · confidence medium · introduced in 18 · fires at upgrade

React now always synchronously flushes effect functions when an update is triggered during a discrete user input event such as a click or a keydown event. Previously the behavior was not always predictable or consistent.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses release 18, where the change was introduced. (confidence high, judge supported)
  - react_changelog: "React now always synchronously flushes effect functions if the update was triggered during a discrete user input event"
  - react_changelog: "Flush useEffect resulting from discrete events like clicks synchronously."
- **[required] behavior** `present` `"discrete user input event"`: The application has state updates triggered during a discrete user input event such as a click or a keydown event whose effects depend on effect timing. (confidence medium, judge supported)
  - react_changelog: "the update was triggered during a discrete user input event such as a click or a keydown event"
  - react_changelog: "useEffect resulting from discrete events like clicks"
  - react_changelog: "Flush useEffect resulting from discrete events like clicks synchronously."
  - ⚠ The text does not state whether any particular application depends on the previous effect timing.
  - ⚠ The text does not state whether this timing change breaks any application code or what the impact is.
- **[uncertain] behavior** `unknown` `""`: The application relies on effect timing that was previously unpredictable or inconsistent. (confidence low, judge partially_supported)
  - react_changelog: "Previously, the behavior wasn't always predictable or consistent."
  - ⚠ The text does not describe what breaks or how to work around the change.

Actions:
- Review useEffect usage triggered by discrete user input events such as clicks or keydowns and verify effect timing after upgrading to React 18.
- Review useEffect hooks that run in response to click or other discrete events and test their behavior on React 18.

### Server-rendered custom elements receiving function or symbol values

`react_d7f515143b` · low · confidence medium · introduced in 18 · fires at upgrade

The item states that React 18 ignores function and symbol values inside custom elements on the server. Applications that server-render custom elements with function or symbol values may see different server output after the upgrade. The text does not state what the previous behavior was or what the resulting output difference is.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The change is introduced in React 18, so the upgrade from React 17 crosses release 18. (confidence high, judge supported)
  - react_changelog: "Ignore function and symbol values inside custom elements on the server"
- **[required] api_usage** `present` `"custom elements with function or symbol values rendered on the server"`: The application renders custom elements that receive function or symbol values during server rendering. (confidence medium, judge supported)
  - react_changelog: "function and symbol values inside custom elements on the server"
  - ⚠ The text does not identify which custom elements or props are affected, and the codebase has not been inspected.
- **[required] runtime** `present` `"server-side rendering"`: The application performs server-side rendering. (confidence high, judge supported)
  - react_changelog: "inside custom elements on the server"
- **[uncertain] behavior** `unknown` `"unknown"`: Whether the application's rendered output depends on the ignored function or symbol values. (confidence low, judge supported)
  - react_changelog: "Ignore function and symbol values"
  - ⚠ The text does not state the prior behavior or the resulting difference in server output.

Actions:
- Search server-rendered components for custom elements that receive function or symbol prop values.
- Confirm whether the server-rendered HTML for those custom elements changes after upgrading to React 18.
- If the output depends on those values, pass the needed data to the custom element in a form that is not a function or symbol.

### Test setup must set globalThis.IS_REACT_ACT_ENVIRONMENT when tests use createRoot

`react_dc5cc879a8` · low · confidence medium · introduced in 18 · fires at first_use

After updating tests to use createRoot, the test console may show an act(...) environment warning unless globalThis.IS_REACT_ACT_ENVIRONMENT is set to true in the test setup. The text says this is needed so React can log warnings about missing act wrapping. Setting it to false is described for end-to-end tests that simulate a full browser environment.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The change statement ties the act environment warning to first updating tests to use createRoot, which the upgrade to React 18 introduces. (confidence medium, judge supported)
  - react_upgrade_guide: "When you first update your tests to use createRoot, you may see this warning in your test console"
  - ⚠ The text does not state the release number in the quoted span; the release 18 link comes from the item metadata.
- **[required] api_usage** `present` `"createRoot"`: The application's tests use createRoot. (confidence high, judge supported)
  - react_upgrade_guide: "When you first update your tests to use createRoot"
- **[required] configuration** `absent` `"globalThis.IS_REACT_ACT_ENVIRONMENT"`: The test setup does not set globalThis.IS_REACT_ACT_ENVIRONMENT. (confidence medium, judge partially_supported)
  - react_upgrade_guide: "set globalThis.IS_REACT_ACT_ENVIRONMENT to true before running your test"
  - ⚠ The text says the warning may appear, not that it fails tests; the severity depends on the project's test runner setup, which the text does not state.

Actions:
- In the test setup file, set globalThis.IS_REACT_ACT_ENVIRONMENT = true before running tests.
- Set the flag to false only for end-to-end tests that simulate a full browser environment, as the text describes.
- Wrap updates with act in unit-test-like environments, since React logs warnings when an update is not wrapped with act.

### React 18 removes the object-assign polyfill

`react_e5d2f27aa2` · low · confidence medium · introduced in 18 · fires at upgrade

React 18 removes its object-assign polyfill. Applications running in environments that lack a native Object.assign may be affected, because the text does not state that React provides a replacement.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses into React 18, the release that removes the object-assign polyfill. (confidence medium, judge supported)
  - react_changelog: "Remove object-assign polyfill."
  - ⚠ Unparsed applicability specifier: '17'
- **[uncertain] runtime** `absent` `"Object.assign"`: The application or its target environments depend on a global Object.assign that the React polyfill previously supplied. (confidence low, judge partially_supported)
  - react_changelog: "Remove object-assign polyfill."
  - ⚠ The text does not name the environments or browsers that lack Object.assign, nor state that application code will fail without the polyfill.

Actions:
- Confirm that all target browsers and runtimes provide a native Object.assign, or add your own Object.assign polyfill before upgrading to React 18.
- Test the application in the lowest-supported target environment after upgrading.

### React DOM Server hydration text mismatch falls back to client render

`react_eb824a435b` · low · confidence low · introduced in 18 · fires at first_use

The item states React reverts to client render when a text mismatch occurs, which changes how server-rendered output is handled during hydration in React 18.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The change is introduced in release 18, which the upgrade from 17 to 18 crosses. (confidence medium, judge partially_supported)
  - react_changelog: "Revert to client render on text mismatch."
- **[required] behavior** `present` `"hydrateRoot or hydrate call on server-rendered markup"`: The application server-renders React output and hydrates it on the client, so a text mismatch between server and client markup can occur. (confidence low, judge partially_supported)
  - react_changelog: "Revert to client render on text mismatch."
  - ⚠ The item does not name the hydration API; the hydration call is inferred from the text mismatch wording.

Actions:
- Check server-rendered pages that hydrate on the client for text mismatch behavior after upgrading to React 18.
- Verify that the client-rendered fallback after a text mismatch is acceptable for the affected pages.

### React 18 requires the New React Native Architecture for React Native users

`react_02909746db` · unknown · confidence high · introduced in 18 · fires at upgrade

The text states that React 18 relies on the New React Native Architecture and that React 18 will ship in a future version of React Native. It does not state what happens to a React Native app that moves to React 18 without the New Architecture.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses release 18. (confidence high, judge supported)
  - react_upgrade_guide: "React 18 relies on the New React Native Architecture to benefit from the new capabilities presented in this blogpost."
- **[required] runtime** `present` `"React Native"`: The application is a React Native app. (confidence high, judge supported)
  - react_upgrade_guide: "For React Native users, React 18 will ship in a future version of React Native."
- **[uncertain] runtime** `present` `"New React Native Architecture"`: The application uses the New React Native Architecture. (confidence low, judge partially_supported)
  - react_upgrade_guide: "React 18 relies on the New React Native Architecture"
  - ⚠ The text does not state what happens to a React Native app that upgrades to React 18 without the New Architecture.

Actions:
- Confirm whether the React Native app already uses the New React Native Architecture before moving to React 18.
- Review the React Conf keynote linked in the source for guidance on the New React Native Architecture.

## Review checklist

### Low confidence or disputed

- [ ] react_66adbc474f: scheduler/tracing API removal
- [ ] react_eb824a435b: React DOM Server hydration text mismatch falls back to client render

### Inferred conditions

- [ ] react_0c8f3e839e: The application's runtime environment lacks native Symbol support.
- [ ] react_e5d2f27aa2: The application or its target environments depend on a global Object.assign that the React polyfill previously supplied.
- [ ] react_eb824a435b: The application server-renders React output and hydrates it on the client, so a text mismatch between server and client markup can occur.

### Source disagreements


### Open questions

- Ecosystem packages (@types/react, react-test-renderer users, Enzyme, React Native, state libraries) have their own React 18 support timelines that are not in React's docs.
- React 18.x minor release notes after 18.0.0 were not mined.
- [react_5245677ce9_0cd8] Unconfirmed: The old render callback has no one-to-one replacement and the replacement depends on the use case. (The text does not state which replacement fits each use case beyond the useEffect example.)
- [react_66adbc474f] Unconfirmed: The application uses the scheduler/tracing API. (The text does not list the specific functions or modules removed from the scheduler/tracing API.)
- [react_44cfb7b19d] Unconfirmed: The application code depends on the partial tree state or effects of a component that suspends before being fully added to the tree. (The text does not state which application code would break when suspending components no longer fire effects or add incomplete trees.)
- [react_0c8f3e839e] Unconfirmed: The application's runtime environment lacks native Symbol support. (The text does not name which environments lack Symbol or state any resulting failure.)
- [react_4aaaf16b0e] Unconfirmed: The application relies on effect timing that was previously unpredictable or inconsistent. (The text does not describe what breaks or how to work around the change.)
- [react_d7f515143b] Unconfirmed: Whether the application's rendered output depends on the ignored function or symbol values. (The text does not state the prior behavior or the resulting difference in server output.)
- [react_e5d2f27aa2] Unconfirmed: The application or its target environments depend on a global Object.assign that the React polyfill previously supplied. (The text does not name the environments or browsers that lack Object.assign, nor state that application code will fail without the polyfill.)
- [react_02909746db] Unconfirmed: The application uses the New React Native Architecture. (The text does not state what happens to a React Native app that upgrades to React 18 without the New Architecture.)

## Context facts (not risks)

- (18) In tests, act warnings are now opt-in: If you're running end-to-end tests, the act warnings are unnecessary. — _The item states that act warnings in tests are now opt-in via a new opt-in mechanism, so end-to-end tests no longer get them and unit tests can enable them. It does not state that existing code or deployments break or need migration at 18, so no upgrade action is required._
- (18) Allow components to render undefined. — _The item states that components are now allowed to render undefined in React 18. It relaxes a previous restriction and does not state any breaking change, removed API, or required migration step, so no action is required at upgrade._
- (18) Consider all lazy() resolving to the same component equivalent. — _The item states only that all lazy() resolving to the same component are considered equivalent (#20357). It does not describe an app-breaking change, a removed API, a required setting, or any migration step, so no upgrade action is stated by the text._
- (18) Don't patch console during first render. — _The ITEM only states that React stopped patching console during first render (#22308). The text does not describe any breaking change, removed API, required setting, or migration step, and it names no user action, so no app or deployment condition can be checked from it._
- (18) Use setImmediate when available over MessageChannel. — _The ITEM states a change in React's internal scheduling: it now uses setImmediate when available instead of MessageChannel. The text names no public API, setting, runtime, or dependency that an application must change or verify, so it needs no action at upgrade to 18._
- (18) Fix useReducer observing incorrect props by removing the eager bailout mechanism. — _The item describes a bug fix ('Fix useReducer observing incorrect props') in the 18.0.0 changelog. The text states no API removal, required migration, configuration, or dependency change, and no user action is required at 18._
- (18) Allow suspending outside a Suspense boundary. — _The item states only that suspending outside a Suspense boundary is now allowed. It describes an added capability with no removed API, changed default, or migration step, so no action is required at 18._
- (18) Log a recoverable error whenever hydration fails. — _The item states only that React now logs a recoverable error whenever hydration fails. It does not state any API removal, default change, or required migration step, so no action is required at 18. Apps that rely on hydration failures being silent may see new console output, but the text does not state this._
- (18) Fix aspectRatio style not being applied. — _The item is a bug fix stating that the aspectRatio style is now applied (#21100). It describes no removed API, changed default, or migration requirement, so no action is needed at 18._
- (18) Make act batch updates. — _The ITEM only states that act batches updates ("Make act batch updates."). The text names no removed API, required configuration, dependency, runtime, or migration step, and states no breakage or required action at React 18. It is accurate and needs no action from the user at this release._
- (18) Add exports field to package.json. — _The item only states that an exports field was added to package.json (#23087). It describes an additive packaging change and does not state any removed API, changed behavior, required migration step, or operational impact, so no upgrade action is required by the text._
- (18) Update webpack plugin for webpack 5 (#22739 by @michenly) — _The item only states that the React Server Components webpack plugin was updated for webpack 5 (#22739). The text does not describe a removed API, changed default, required migration, or operational impact, and the section is labeled Experimental, so no upgrade action is stated as needed at 18._
- (18) Use globalThis instead of window for edge environments. — _The item states an internal implementation change in the experimental React Server Components edge environment handling (using globalThis instead of window). The text names no API removal, required user action, or migration step, so it needs no action at upgrade to 18._
- (18) In the React 18 Working Group we worked with library maintainers to create new APIs needed to support concurrent rendering for use cases specific to their use case in areas like styles, and external stores. — _The item introduces new APIs (useSyncExternalStore, useInsertionEffect, startTransition, useDeferredValue, useId) and says only that some libraries 'may need to switch' to them to support React 18. It does not state any removed API, changed default, changed behavior, or breakage if the switch is not made, and the text says the CSS-in-JS Hook is not expected to be used unless a CSS-in-JS library is built. No application or deployment action is required at 18 based on this text._
- (18) Components can now render undefined: React no longer warns if you return undefined from a component. — _The item states that React 18 no longer warns when a component returns undefined. This removes a warning and does not break existing code, so no migration work is required. The suggestion to use a linter is optional advice._
- (18) react-dom: ReactDOM.unmountComponentAtNode has been deprecated. — _unmountComponentAtNode is deprecated as a warning-level change with no stated removal, so the API still works in this release._
- (18) react-dom: ReactDOM.renderSubtreeIntoContainer has been deprecated. — _renderSubtreeIntoContainer is deprecated as a warning-level change with no stated removal, so the API still works in this release._
- (18) react-dom/server: ReactDOMServer.renderToNodeStream has been deprecated. — _renderToNodeStream is deprecated as a warning-level change with no stated removal, so the API still works in this release._
- (18) Components can now render undefined: React no longer throws if you return undefined from a component. — _Components may now return undefined without throwing, which is a relaxation that requires no user action._
- (18) No warning about setState on unmounted components: Previously, React warned about memory leaks when you call setState on an unmounted component. — _The setState-on-unmounted warning is removed, which requires no user action and does not break correct code._
- (18) Improved memory usage: React now cleans up more internal fields on unmount, making the impact from unfixed memory leaks that may exist in your application code less severe. — _React cleans up more internal fields on unmount, a improvement that needs no user action._
- (18) In this release, we're revamping our react-dom/server APIs to fully support Suspense on the server and Streaming SSR. As part of these changes, we're deprecating the old Node streaming API, which does not support incremental Suspense streaming on the server. — _The old Node streaming API is deprecated and only warns, so it still works and needs no immediate action._
- (18) renderToNodeStream: Deprecated ⛔️️ — _renderToNodeStream is marked Deprecated, which produces a warning while the API continues to function._
- (18) Instead, for streaming in Node environments, use: — _This line points to the recommended replacement APIs for Node streaming and does not itself require a change._
- (18) renderToPipeableStream: New ✨ — _renderToPipeableStream is a new, additive API for Node streaming with Suspense._
- (18) We're also introducing a new API to support streaming SSR with Suspense for modern edge runtime environments, such as Deno and Cloudflare workers: — _This introduces a new streaming SSR API for edge runtimes, which is additive and optional._
- (18) renderToReadableStream: New ✨ — _renderToReadableStream is a new, additive API for edge runtime streaming._
- (18) The following APIs will continue working, but with limited support for Suspense: — _It states these APIs will continue working, with limited Suspense support, so no action is required._
- (18) renderToString: Limited ⚠️ — _renderToString is listed as continuing to work with limited Suspense support, requiring no action._
- (18) renderToStaticMarkup: Limited ⚠️ — _renderToStaticMarkup is listed as continuing to work with limited Suspense support, requiring no action._
- (18) Finally, this API will continue to work for rendering e-mails: — _It states that this API will continue to work for rendering e-mails, so no action is required._
- (18) For more information on the changes to server rendering APIs, see the working group post on Upgrading to React 18 on the server, a deep dive on the new Suspense SSR Architecture, and Shaundai Person's talk on Streaming Server Rendering — _This is a documentation pointer to the working group post, deep dive, and talk on server rendering changes._
- (18) See the React 18 typings pull request for a full list of type-only changes. — _This item points to the typings PR, example fixes, an optional migration script, and where to file bugs, without stating a required change itself._
- (18) For more information, see the Automatic batching deep dive. — _This is only a pointer to a deep dive on automatic batching with no required action._
- (18) For more information, see the Working Group posts for Adding Reusable State to StrictMode and How to support Reusable State in Effects. — _These are pointers to working group posts about reusable state and effects, with no required user action._
- (18) The purpose of the flag is to tell React that it's running in a unit test-like environment. — _It explains the purpose of the act environment flag and notes testing libraries will eventually configure it automatically, with no new required action._

## Disqualified candidates


## Sources

| Source | Type | Tier | Status | Pinned ref |
|---|---|---|---|---|
| [react_changelog](https://github.com/facebook/react/blob/main/CHANGELOG.md#1800-march-29-2022) | official_changelog | 1 | used | `main@e8738f0c628b` |
| [react_upgrade_guide](https://react.dev/blog/2022/03/08/react-18-upgrade-guide) | official_migration_guide | 1 | used | `main@c3c956bef083` |

## What we trusted and what we did not

- Trusted: package metadata for version numbers; official guides, release notes and changelogs pinned to a tag, branch or commit.
- Not trusted: LLM self-reported confidence, unpinned current pages when they disagree with pinned ones, any quote that fails exact match, transclusion stubs.
