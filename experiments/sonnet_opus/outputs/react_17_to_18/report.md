# React 17 → 18: upgrade risk report

> Documentation-derived risk conditions; not a migration plan.

React 17 -> 18 crosses 1 release(s) (18). 30 risk paths: 1 critical, 4 high, 16 medium, 9 low. Main risk types: changed_behavior (20), runtime_requirement (4), removed_api (3). Critical: Internet Explorer no longer supported. 33 context facts and 0 disqualified candidates are listed separately. Documentation-derived risk conditions; not a migration plan.

Overall confidence: **medium**. Validation: `{"errors": 0, "warnings": 9, "by_code": {"W4_no_search_queries": 9}}`

## Risk paths

| Level | Confidence | Type | Surface | Release | Path |
|---|---|---|---|---|---|
| critical | high | runtime_requirement | runtime | 18 | `react_77c14b0b1f` Internet Explorer no longer supported |
| high | low | runtime_requirement | runtime | 18 | `react_0c8f3e839e` React 18 requires a global Symbol implementation |
| high | medium | runtime_requirement | runtime | 18 | `react_54ca1125eb` Modern JS environment features required (Promise, Symbol, Object.assign) |
| high | medium | removed_api | application_code | 18 | `react_66adbc474f` scheduler/tracing API removed |
| high | medium | removed_api | application_code | 18 | `react_e611605e84` unstable_changedBits API removed |
| medium | low | changed_behavior | application_code | 18 | `react_090a4a6780` Hydration text mismatches now errors and fall back to client rendering |
| medium | medium | changed_behavior | application_code | 18 | `react_0cdcfd833f` Implicit children prop removed from React component prop types |
| medium | low | changed_behavior | tests | 18 | `react_1174c2e1c2` Expanded act() warnings in test environments |
| medium | medium | removed_api | application_code | 18 | `react_2489111975` Render callback removed in new root API (root.render) |
| medium | low | changed_behavior | application_code | 18 | `react_362d1d0639` Automatic batching changes state update rendering behavior |
| medium | medium | dependency_requirement | dependencies | 18 | `react_36dbc741d4` Stricter React 18 type definitions surface previously ignored type errors |
| medium | medium | changed_behavior | application_code | 18 | `react_385fe7836e` hydrate replaced by hydrateRoot from react-dom/client |
| medium | medium | changed_behavior | application_code | 18 | `react_44cfb7b19d` Suspense discards incomplete trees and retries rendering from scratch |
| medium | high | changed_behavior | application_code | 18 | `react_479331dfb5` renderToStaticMarkup emits Suspense fallback instead of erroring on server suspend |
| medium | medium | changed_behavior | application_code | 18 | `react_4aaaf16b0e` useEffect synchronous flush on discrete input events |
| medium | medium | changed_behavior | application_code | 18 | `react_6c336940af` renderToString emits Suspense fallback instead of erroring when suspending on the server |
| medium | high | changed_behavior | application_code | 18 | `react_7123c14ec9` unmountComponentAtNode replaced by root.unmount |
| medium | high | changed_behavior | application_code | 18 | `react_71acd3a7ef` Strict Mode double mount/unmount in development |
| medium | medium | changed_behavior | application_code | 18 | `react_ab2c7932c2` Suspense fallback={undefined} no longer ignored |
| medium | medium | changed_behavior | application_code | 18 | `react_c0e4ce54e4` Layout effects cleaned up and re-created when Suspense tree re-suspends |
| medium | medium | changed_behavior | application_code | 18 | `react_e56a0f9df4` Automatic batching of state updates outside React event handlers under createRoot |
| low | high | changed_behavior | application_code | 18 | `react_1ae332ab77` lazy() components resolving to the same component treated as equivalent |
| low | medium | changed_behavior | application_code | 18 | `react_385fe7836e_5bce` ReactDOM.hydrate should be migrated to hydrateRoot to enable React 18 features |
| low | high | changed_behavior | application_code | 18 | `react_4a4e72c4eb` ReactDOM.render legacy root API deprecated in favor of createRoot |
| low | medium | changed_behavior | dependencies | 18 | `react_6f939e43ca` react-refresh package.json exports field may restrict deep/subpath imports |
| low | medium | changed_behavior | application_code | 18 | `react_6fff665547` Deprecated renderToNodeStream now warns in React 18 |
| low | medium | changed_default | tests | 18 | `react_bf8746ac22` act warnings no longer emitted by default in unit tests |
| low | medium | changed_behavior | application_code | 18 | `react_d7f515143b` SSR omits function/symbol values on custom elements |
| low | medium | configuration_change | tests | 18 | `react_dc5cc879a8` Test console warning about act environment after switching tests to createRoot |
| low | high | runtime_requirement | runtime | 18 | `react_e5d2f27aa2` React no longer bundles object-assign polyfill; legacy runtimes without native Object.assign may break |

### Internet Explorer no longer supported

`react_77c14b0b1f` · critical · confidence high · introduced in 18 · fires at upgrade

React 18 drops support for Internet Explorer; new features rely on modern browser features such as microtasks that cannot be adequately polyfilled in IE. Apps that must support IE should stay on React 17.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React release 18, which drops Internet Explorer support. (confidence high, judge supported)
  - react_upgrade_guide: "In this release, React is dropping support for Internet Explorer"
- **[required] runtime** `present` `"Internet Explorer"`: The application needs to support Internet Explorer as a target browser. (confidence high, judge supported)
  - react_upgrade_guide: "If you need to support Internet Explorer we recommend you stay with React 17."

Actions:
- Determine whether the application must support Internet Explorer (check browserslist and support requirements).
- If Internet Explorer support is required, stay with React 17 as recommended.

### React 18 requires a global Symbol implementation

`react_0c8f3e839e` · high · confidence low · introduced in 18 · fires at upgrade

React 18 assumes Symbols are always available and no longer accommodates JavaScript environments without Symbol. Applications running in environments that lack native Symbol support and do not load a polyfill may fail to run React.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React release 18, where React begins assuming Symbols are always available. (confidence high, judge supported)
  - react_changelog: "Assume Symbols are always available."
- **[required] runtime** `absent` `"Symbol"`: The application runs (or supports running) in a JavaScript environment that lacks a native global Symbol and does not load a Symbol polyfill. (confidence low, judge partially_supported)
  - react_changelog: "Assume Symbols are always available."
  - ⚠ The text does not name which browsers or runtimes lack Symbol (e.g. older browsers), nor what exactly fails when Symbol is missing.
  - ⚠ The text does not state whether a polyfill is sufficient, though that is implied by 'available'.

Actions:
- Verify all target browsers/runtimes provide a native global Symbol.
- For environments without native Symbol, load a Symbol polyfill (e.g. via core-js) before React is loaded.
- Test the application in the oldest supported target environment after upgrading to React 18.

### Modern JS environment features required (Promise, Symbol, Object.assign)

`react_54ca1125eb` · high · confidence medium · introduced in 18 · fires at upgrade

React 18 depends on modern browser features including Promise, Symbol, and Object.assign. Applications supporting older browsers/devices such as Internet Explorer that lack these natively or have non-compliant implementations may break unless a global polyfill is included in the bundle.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React release 18, which introduces the new JS environment requirements. (confidence high, judge supported)
  - react_changelog: "React now depends on modern browsers features including Promise, Symbol, and Object.assign."
- **[required] runtime** `present` `"Internet Explorer"`: The application supports older browsers or devices (e.g. Internet Explorer) that do not provide Promise, Symbol, or Object.assign natively or have non-compliant implementations. (confidence medium, judge partially_supported)
  - react_changelog: "If you support older browsers and devices such as Internet Explorer which do not provide modern browser features natively or have non-compliant implementations"
- **[disqualifying] dependency** `present` `"global polyfill"`: The bundled application already includes a global polyfill for Promise, Symbol, and Object.assign. (confidence low, judge partially_supported)
  - react_changelog: "consider including a global polyfill in your bundled application."
  - ⚠ The text does not name a specific polyfill library.

Actions:
- Identify whether supported browsers/devices (e.g. Internet Explorer) lack native Promise, Symbol, or Object.assign.
- Include a global polyfill for these features in the bundled application if supporting such environments.

### scheduler/tracing API removed

`react_66adbc474f` · high · confidence medium · introduced in 18 · fires at upgrade

The unstable scheduler/tracing API is removed in React 18; code importing or using it will break.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React release 18, where the scheduler/tracing API is removed. (confidence high, judge supported)
  - react_changelog: "Remove unstable scheduler/tracing API"
- **[required] api_usage** `present` `"scheduler/tracing"`: The application imports or uses the scheduler/tracing API. (confidence medium, judge supported)
  - react_changelog: "Remove unstable scheduler/tracing API"
  - ⚠ The text does not name specific exported functions of scheduler/tracing or a replacement.
  - ⚠ The text does not list the specific functions exported by scheduler/tracing or name a replacement.

Actions:
- Search the codebase for imports of 'scheduler/tracing' and remove that usage before upgrading to React 18.
- Remove imports and usages of scheduler/tracing before upgrading to React 18.

### unstable_changedBits API removed

`react_e611605e84` · high · confidence medium · introduced in 18 · fires at upgrade

React 18 removes the unsupported unstable_changedBits API. Code relying on it will no longer have it available.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React release 18, where unstable_changedBits is removed. (confidence high, judge supported)
  - react_changelog: "Remove unsupported unstable_changedBits API."
- **[required] api_usage** `present` `"unstable_changedBits"`: The application uses the unstable_changedBits API. (confidence medium, judge supported)
  - react_changelog: "Remove unsupported unstable_changedBits API."
  - ⚠ The text does not say what happens at runtime to code still passing unstable_changedBits (error vs. silently ignored).

Actions:
- Search the codebase and dependencies for unstable_changedBits and remove its usage before upgrading to React 18.

### Hydration text mismatches now errors and fall back to client rendering

`react_090a4a6780` · medium · confidence low · introduced in 18 · fires at first_use

In React 18, hydration mismatches due to missing or extra text content are treated as errors instead of warnings. React no longer patches up individual nodes and instead reverts to client rendering up to the closest <Suspense> boundary. Apps doing server rendering with hydration that have text mismatches will see errors and client re-rendering.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React 18, where hydration mismatches became errors. (confidence high, judge supported)
  - react_changelog: "Hydration mismatches due to missing or extra text content are now treated like errors instead of warnings."
  - react_changelog: "Revert to client render on text mismatch."
- **[required] api_usage** `present` `"hydrate"`: The application hydrates server-rendered markup on the client. (confidence low, judge supported)
  - react_changelog: "attempt to match the server markup, and will revert to client rendering"
  - react_changelog: "Revert to client render on text mismatch."
  - ⚠ The text does not name the specific hydration API (e.g. hydrate or hydrateRoot).
  - ⚠ The text does not name the hydration API involved; hydrateRoot/hydrate are inferred.
- **[required] behavior** `present` `"text content mismatch between server and client render"`: Server-rendered output differs from client render in text content (missing or extra text). (confidence medium, judge supported)
  - react_changelog: "Hydration mismatches due to missing or extra text content"
  - react_changelog: "Revert to client render on text mismatch."
  - ⚠ The text does not state the scope of the client re-render or any performance or warning impact.
- **[optional] api_usage** `present` `"Suspense"`: Presence of <Suspense> boundaries determines how much of the tree reverts to client rendering. (confidence high, judge supported)
  - react_changelog: "will revert to client rendering up to the closest <Suspense> boundary in the tree"

Actions:
- Audit server-rendered pages for hydration text mismatch warnings under React 17 and fix them before upgrading.
- Ensure server and client render identical text content (e.g. avoid time/locale/random-dependent text during initial render).
- Consider placing <Suspense> boundaries to limit the scope of client-rendering fallback.
- Check SSR pages for hydration text mismatches (e.g. timestamps, random IDs, locale formatting) and make server and client output identical.
- Test hydrated pages under React 18 for unexpected client re-rendering.

### Implicit children prop removed from React component prop types

`react_0cdcfd833f` · medium · confidence medium · introduced in 18 · fires at upgrade

With React 18 @types/react, the children prop is no longer implicitly included in component props; components that use children without declaring it in their props type will fail type checking.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: Upgrade crosses React 18, which ships updated TypeScript definitions (confidence medium, judge partially_supported)
  - react_upgrade_guide: "you will need to update your @types/react and @types/react-dom dependencies to the latest versions"
- **[required] dependency** `present` `"@types/react"`: The project uses TypeScript with @types/react / @types/react-dom (confidence high, judge supported)
  - react_upgrade_guide: "If your project uses TypeScript, you will need to update your @types/react and @types/react-dom dependencies"
- **[required] api_usage** `present` `"children"`: Components use the children prop without listing it explicitly in their props type (confidence medium, judge supported)
  - react_upgrade_guide: "the children prop now needs to be listed explicitly when defining props"
  - ⚠ The text does not name which helper types (e.g. React.FC) previously supplied implicit children.

Actions:
- Update @types/react and @types/react-dom to the latest versions.
- Add children explicitly to props types, e.g. children?: React.ReactNode.
- Use the automated migration script to port application code to the new typings.
- Review the React 18 typings pull request for the full list of type-only changes.

### Expanded act() warnings in test environments

`react_1174c2e1c2` · medium · confidence low · introduced in 18 · fires at upgrade

In React 18 the act warning is expanded to cover all APIs that might schedule React work, so test suites may emit new act-related warnings. This is warning-only; test suites that treat console warnings as failures may start failing.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React release 18, where the act warning was expanded. (confidence high, judge supported)
  - react_changelog: "Expand act warning to cover all APIs that might schedule React work."
  - react_changelog: "Throw when act is used in production."
  - react_changelog: "Make act batch updates."
- **[required] test_coverage** `present` `"act"`: The test suite exercises React APIs that schedule React work, possibly outside act(). (confidence low, judge supported)
  - react_changelog: "Expand act warning to cover all APIs that might schedule React work."
  - react_changelog: "Make act batch updates."
  - ⚠ The text does not list which specific APIs are now covered by the warning.
- **[uncertain] test_coverage** `present` `"console.error failure hook"`: The test setup treats console warnings/errors as test failures, turning the new warnings into failures. (confidence low, judge partially_supported)
  - react_changelog: "Expand act warning to cover all APIs that might schedule React work."
  - ⚠ The text does not state whether the warning is emitted via console.error or whether it causes failures.
- **[optional] configuration** `present` `"IS_REACT_ACT_ENVIRONMENT"`: The test environment sets global.IS_REACT_ACT_ENVIRONMENT, which supports disabling spurious act warnings. (confidence medium, judge supported)
  - react_changelog: "Support disabling spurious act warnings with global.IS_REACT_ACT_ENVIRONMENT."
  - ⚠ The text does not state exactly how this flag interacts with the expanded warning.
- **[required] api_usage** `present` `"act"`: The application or its tests call act. (confidence high, judge supported)
  - react_changelog: "Throw when act is used in production."
- **[required] runtime** `equals` `"production"`: act is executed against a production build of React (e.g. NODE_ENV=production). (confidence medium, judge supported)
  - react_changelog: "Throw when act is used in production."
  - ⚠ The text does not define how 'production' is determined (e.g. NODE_ENV or production bundle).
- **[uncertain] behavior** `unknown` `"assertions relying on unbatched updates inside act"`: Tests assert on intermediate render states between multiple updates inside a single act call. (confidence low, judge partially_supported)
  - react_changelog: "Make act batch updates."
  - ⚠ The text does not describe which test patterns break or the exact batching semantics.

Actions:
- Run the test suite after upgrading and wrap React-work-scheduling interactions in act() where warnings appear.
- Configure global.IS_REACT_ACT_ENVIRONMENT appropriately in the test setup to disable spurious act warnings.
- Ensure act is only used in development/test builds of React, not in production bundles.
- Check test runner configuration so NODE_ENV is not set to production when tests using act run.
- Run the test suite after upgrading and update assertions that depended on unbatched updates inside act.

### Render callback removed in new root API (root.render)

`react_2489111975` · medium · confidence medium · introduced in 18 · fires at first_use

React 18 removes the completion callback from render. Code passing a third callback argument to render must be restructured when moving to createRoot/root.render. The guide suggests running the logic in a useEffect inside a wrapper component, and says there is no one-to-one replacement.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React 18, where the render callback was removed. (confidence high, judge supported)
  - react_upgrade_guide: "We've also removed the callback from render, since it usually does not have the expected result when using Suspense"
- **[required] api_usage** `present` `"render(element, container, callback)"`: The application calls render with a third callback argument that runs after rendering. (confidence medium, judge supported)
  - react_upgrade_guide: "render(<App tab="home" />, container, () => { console.log('rendered'); });"
  - react_upgrade_guide: "There is no one-to-one replacement for the old render callback API"
  - react_upgrade_guide: "Until you switch to the new API, your app will behave as if it's running React 17."
  - ⚠ The text does not explicitly state whether the legacy render in React 18 still invokes the callback.
- **[uncertain] api_usage** `present` `"createRoot"`: The application has migrated, or is migrating, to createRoot/root.render. The guide says apps still using the legacy API behave as on React 17. (confidence low, judge partially_supported)
  - react_upgrade_guide: "Until you switch to the new API, your app will behave as if it's running React 17."
  - ⚠ The text does not explicitly state whether legacy ReactDOM.render still invokes the callback in React 18, or whether the removal applies only to root.render.
- **[optional] behavior** `present` `"useEffect"`: No direct replacement exists for the callback. The replacement behavior depends on the use case, for example a useEffect in a wrapper component. (confidence medium, judge partially_supported)
  - react_upgrade_guide: "There is no one-to-one replacement for the old render callback API — it depends on your use case."

Actions:
- Find render calls that pass a callback as the third argument.
- Move the post-render logic into a useEffect inside a wrapper component (e.g. AppWithCallbackAfterRender), then render it via createRoot(container).render(...).
- Review the working group post 'Replacing render with createRoot' for use-case-specific replacements, since there is no one-to-one replacement.
- Replace the render callback with a wrapper component that runs the logic in useEffect, then render it via createRoot(container).render(...).
- Consult the working group post 'Replacing render with createRoot' for use-case-specific replacements.

### Automatic batching changes state update rendering behavior

`react_362d1d0639` · medium · confidence low · introduced in 18 · fires at upgrade

React 18 batches state updates automatically in more cases, changing how many renders occur. Code that relied on non-batched updates (e.g. synchronous re-render after a state update) may behave differently; opt out by wrapping the state update in flushSync.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React release 18, which changes update batching. (confidence high, judge supported)
  - react_changelog: "This release introduces a performance improvement that changes to the way React batches updates to do more batching automatically."
- **[required] behavior** `present` `"state updates relying on non-batched rendering"`: The application performs React state updates whose behavior depends on updates not being batched. (confidence low, judge partially_supported)
  - react_changelog: "In the rare case that you need to opt out, wrap the state update in flushSync."
  - ⚠ The text does not specify which update contexts (e.g. timeouts, promises, native event handlers) gained batching, nor what breakage results.

Actions:
- Review code that depends on state updates rendering immediately and test for changed render behavior.
- Where opting out of automatic batching is required, wrap the state update in flushSync (from react-dom).

### Stricter React 18 type definitions surface previously ignored type errors

`react_36dbc741d4` · medium · confidence medium · introduced in 18 · fires at upgrade

Updating to the latest @types/react and @types/react-dom for React 18 introduces safer types that catch issues previously ignored by the type checker, which may cause new compile errors.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: Upgrade crosses React 18 requiring updated type definitions (confidence high, judge supported)
  - react_upgrade_guide: "you will need to update your @types/react and @types/react-dom dependencies to the latest versions"
- **[required] dependency** `present` `"@types/react-dom"`: The project uses TypeScript with @types/react or @types/react-dom (confidence medium, judge partially_supported)
  - react_upgrade_guide: "The new types are safer and catch issues that used to be ignored by the type checker."
  - ⚠ The full list of type-only changes is only referenced (typings pull request), not given.

Actions:
- Update @types/react and @types/react-dom to the latest versions and fix resulting type errors.
- Use the automated migration script; report typing bugs to DefinitelyTyped.

### hydrate replaced by hydrateRoot from react-dom/client

`react_385fe7836e` · medium · confidence medium · introduced in 18 · fires at upgrade

Apps using server-side rendering with hydration must replace legacy hydrate from 'react-dom' with hydrateRoot from 'react-dom/client'. Until they switch, React 18 shows a console warning and the app behaves as if it's running React 17. hydrateRoot takes the container first and the element second, and returns a root without needing a separate root.render() call.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React 18, which introduces the new root API. (confidence medium, judge partially_supported)
  - react_upgrade_guide: "When you first install React 18, you will see a warning in the console"
- **[required] api_usage** `present` `"hydrate"`: The application uses server-side rendering with hydration via hydrate from 'react-dom'. (confidence medium, judge partially_supported)
  - react_upgrade_guide: "if your app uses server-side rendering with hydration, upgrade hydrate to hydrateRoot"
- **[optional] behavior** `present` `"legacy root behavior"`: Until migrated, the app behaves as if running React 17 (legacy mode), so new concurrent features are not enabled. (confidence low, judge partially_supported)
  - react_upgrade_guide: "Until you switch to the new API, your app will behave as if it's running React 17."
  - ⚠ The warning text in the parent context names ReactDOM.render explicitly; the text does not explicitly state the same warning applies to hydrate.
- **[optional] behavior** `present` `"hydrateRoot(container, element)"`: hydrateRoot differs in signature: container is the first argument and no separate root.render() call is needed. (confidence medium, judge partially_supported)
  - react_upgrade_guide: "Unlike with createRoot, you don't need a separate root.render() call here."

Actions:
- Replace `import { hydrate } from 'react-dom'` with `import { hydrateRoot } from 'react-dom/client'`.
- Change `hydrate(<App />, container)` to `const root = hydrateRoot(container, <App />)`; do not add a separate root.render() call.

### Suspense discards incomplete trees and retries rendering from scratch

`react_44cfb7b19d` · medium · confidence medium · introduced in 18 · fires at upgrade

In React 18, if a component suspends before it's fully added to the tree, React no longer adds it in an incomplete state or fires its effects; it throws away the new tree, waits for the async operation, and retries rendering from scratch concurrently. Components relying on effects firing or state persisting in partially-mounted suspended trees may behave differently.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React release 18, where Suspense trees are always consistent (confidence high, judge supported)
  - react_changelog: "Suspense trees are always consistent: If a component suspends before it's fully added to the tree"
  - react_changelog: "Make Suspense remount layout effects when content reappears."
- **[required] api_usage** `present` `"Suspense"`: The application uses Suspense with components that suspend before being fully added to the tree (confidence medium, judge partially_supported)
  - react_changelog: "React will not add it to the tree in an incomplete state or fire its effects"
  - react_changelog: "React will throw away the new tree completely, wait for the asynchronous operation to finish, and then retry rendering again from scratch"
  - react_changelog: "Make Suspense remount layout effects when content reappears."
  - ⚠ The text does not describe the prior (React 17) behavior explicitly or which application patterns break.
  - ⚠ The text says 'layout effects' without naming specific APIs; whether class lifecycle methods like componentDidMount are included is not stated.
- **[uncertain] behavior** `present` `"effects in suspending subtrees"`: Components rely on effects firing or render work persisting for a tree that suspended before completing mount (confidence low, judge partially_supported)
  - react_changelog: "React will not add it to the tree in an incomplete state or fire its effects"
  - react_changelog: "Make Suspense remount layout effects when content reappears."
  - ⚠ The text does not state what specific code patterns depend on the old behavior.
  - ⚠ The text does not describe the impact on effects or what breaks.

Actions:
- Review components rendered inside Suspense boundaries for reliance on effects or state from partially-rendered trees that suspend.
- Ensure components tolerate rendering being discarded and retried from scratch.
- Review useLayoutEffect usages inside Suspense boundaries to ensure they have proper cleanup functions and are safe to re-run when content reappears.

### renderToStaticMarkup emits Suspense fallback instead of erroring on server suspend

`react_479331dfb5` · medium · confidence high · introduced in 18 · fires at upgrade

In React 18, renderToStaticMarkup no longer throws when a component suspends on the server; it emits the fallback HTML for the closest <Suspense> boundary and retries rendering on the client. Code relying on the error (e.g. catching it) or expecting full content in the static markup may behave differently.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React release 18, where renderToStaticMarkup behavior on server suspension changed. (confidence high, judge supported)
  - react_changelog: "renderToStaticMarkup: Will no longer error when suspending on the server."
  - react_upgrade_guide: "renderToStaticMarkup: Will no longer error when suspending on the server."
- **[required] api_usage** `present` `"renderToStaticMarkup"`: The application calls renderToStaticMarkup on the server. (confidence high, judge supported)
  - react_changelog: "renderToStaticMarkup: Will no longer error when suspending on the server."
  - react_upgrade_guide: "renderToStaticMarkup: Will no longer error when suspending on the server."
- **[required] behavior** `present` `"Suspense"`: Components rendered via renderToStaticMarkup suspend on the server within a <Suspense> boundary. (confidence high, judge supported)
  - react_changelog: "it will emit the fallback HTML for the closest <Suspense> boundary and retry rendering on the client"
  - react_upgrade_guide: "Instead, it will emit the fallback HTML for the closest <Suspense> boundary."
  - react_upgrade_guide: "Will no longer error when suspending on the server."
  - ⚠ The text does not say what happens if no <Suspense> boundary exists above the suspending component.
  - ⚠ The text does not state what happens if there is no enclosing <Suspense> boundary.
  - ⚠ The text does not describe specific breakage; impact on error-handling code is inferred.
- **[uncertain] behavior** `present` `"error handling around renderToStaticMarkup"`: The application relies on renderToStaticMarkup throwing an error when suspending (e.g. catch/fallback logic). (confidence low, judge supported)
  - react_changelog: "Will no longer error when suspending on the server."
  - ⚠ The text does not state impact on apps that depended on the error; inferred from the change.

Actions:
- Audit renderToStaticMarkup call sites for components that may suspend and verify the emitted fallback HTML is acceptable.
- Remove or adjust error-handling logic that depended on renderToStaticMarkup throwing on suspension.
- Note that static markup has no client hydration in many uses, so the client-side retry may not occur; verify output for such use cases.
- Review all renderToStaticMarkup call sites for components that may suspend and verify the emitted fallback HTML is acceptable.
- Update any error handling or tests that expected renderToStaticMarkup to throw on suspension.

### useEffect synchronous flush on discrete input events

`react_4aaaf16b0e` · medium · confidence medium · introduced in 18 · fires at upgrade

In React 18, effect functions are always flushed synchronously when the update was triggered during a discrete user input event (e.g. click, keydown). Code relying on the previous, less predictable effect timing may behave differently.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React release 18, which changes useEffect timing. (confidence high, judge supported)
  - react_changelog: "React now always synchronously flushes effect functions if the update was triggered during a discrete user input event"
  - react_changelog: "Flush useEffect resulting from discrete events like clicks synchronously."
- **[required] api_usage** `present` `"useEffect"`: The application uses useEffect in components whose updates are triggered by discrete user input events such as click or keydown. (confidence medium, judge supported)
  - react_changelog: "Consistent useEffect timing"
  - react_changelog: "such as a click or a keydown event"
  - react_changelog: "Flush useEffect resulting from discrete events like clicks synchronously."
  - ⚠ The text does not state what the previous timing was or which application patterns would break; impact on apps relying on effect timing is not described.
- **[uncertain] behavior** `unknown` `"reliance on deferred effect flushing"`: The application depends on the previous (asynchronous/inconsistent) timing of effect execution relative to the event. (confidence low, judge partially_supported)
  - react_changelog: "Previously, the behavior wasn't always predictable or consistent."
  - ⚠ The text does not describe what specific code patterns break due to the timing change.

Actions:
- Review useEffect hooks triggered by click/keydown handlers for assumptions about when effects run relative to the event.
- Test interactive flows involving effects after upgrading to React 18.
- Review useEffect hooks that run in response to click or other discrete event handlers for assumptions about effect timing, and re-test those interactions after upgrading to React 18.

### renderToString emits Suspense fallback instead of erroring when suspending on the server

`react_6c336940af` · medium · confidence medium · introduced in 18 · fires at upgrade

In React 18, renderToString no longer throws when a component suspends during server rendering. It emits the fallback HTML for the closest <Suspense> boundary and retries rendering that content on the client. Server code that relied on the error, for example by catching it, will now silently get fallback HTML in the server output.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React 18, where renderToString stops erroring on server suspension (confidence high, judge supported)
  - react_changelog: "renderToString: Will no longer error when suspending on the server."
- **[required] api_usage** `present` `"renderToString"`: The application renders on the server with renderToString (confidence high, judge supported)
  - react_changelog: "renderToString: Will no longer error when suspending on the server."
- **[required] behavior** `present` `"Suspense"`: Components suspend during server rendering, inside a <Suspense> boundary (confidence medium, judge partially_supported)
  - react_changelog: "it will emit the fallback HTML for the closest <Suspense> boundary and then retry rendering the same content on the client"
  - ⚠ The text does not say what happens when no <Suspense> boundary encloses the suspending component.

Actions:
- Find renderToString calls whose rendered tree can suspend. Check that emitting Suspense fallback HTML on the server, with rendering retried on the client, is acceptable.
- Remove any error handling that relied on renderToString throwing when a component suspends.
- Switch to a streaming API such as renderToPipeableStream or renderToReadableStream, as recommended.

### unmountComponentAtNode replaced by root.unmount

`react_7123c14ec9` · medium · confidence high · introduced in 18 · fires at upgrade

React 18 changes unmountComponentAtNode to root.unmount() as part of the new root API. Code calling unmountComponentAtNode(container) needs to move to calling unmount() on a root created with createRoot.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React release 18, where unmountComponentAtNode was changed to root.unmount. (confidence high, judge supported)
  - react_upgrade_guide: "We've also changed unmountComponentAtNode to root.unmount"
- **[required] api_usage** `present` `"unmountComponentAtNode"`: The application calls unmountComponentAtNode. (confidence high, judge supported)
  - react_upgrade_guide: "// Before unmountComponentAtNode(container); // After root.unmount();"
- **[uncertain] behavior** `unknown` `"unmountComponentAtNode still functional in React 18"`: Whether unmountComponentAtNode stops working immediately in React 18 or continues in legacy (React 17-like) mode until the app switches to the new root API. (confidence low, judge partially_supported)
  - react_upgrade_guide: "Until you switch to the new API, your app will behave as if it's running React 17."
  - ⚠ The text says the API was 'changed' but does not state whether unmountComponentAtNode is removed, deprecated, or still functional in React 18.

Actions:
- Create roots with createRoot from 'react-dom/client' and keep a reference to the root.
- Replace unmountComponentAtNode(container) calls with root.unmount() on the corresponding root.

### Strict Mode double mount/unmount in development

`react_71acd3a7ef` · medium · confidence high · introduced in 18 · fires at upgrade

React 18 adds a development-only Strict Mode check: on first mount, every component is automatically unmounted and remounted, with the previous state restored on the second mount. Components that are not resilient to remounting with existing state may break in development. The text's workaround is to remove Strict Mode until the components are fixed.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React 18, which introduces the new Strict Mode check (confidence high, judge supported)
  - react_changelog: "React 18 introduces a new development-only check to Strict Mode"
  - react_upgrade_guide: "React 18 introduces a new development-only check to Strict Mode."
  - react_changelog: "Make <StrictMode> re-run effects to check for restorable state."
  - react_upgrade_guide: "Strict Mode has gotten stricter in React 18"
- **[required] api_usage** `present` `"StrictMode"`: The application renders components inside Strict Mode (confidence high, judge supported)
  - react_changelog: "consider removing Strict Mode until you can fix the components"
  - react_upgrade_guide: "With Strict Mode in React 18, React will simulate unmounting and remounting the component in development mode"
  - react_changelog: "Make <StrictMode> re-run effects to check for restorable state."
  - react_upgrade_guide: "check whether it's wrapped in <StrictMode>"
  - ⚠ The text does not state whether this applies only in development builds.
- **[required] runtime** `equals` `"development"`: The check runs only in development builds (confidence high, judge supported)
  - react_changelog: "a new development-only check to Strict Mode"
  - react_upgrade_guide: "React 18 introduces a new development-only check to Strict Mode."
  - react_upgrade_guide: "React will simulate unmounting and remounting the component in development mode"
  - react_upgrade_guide: "not all your components may be resilient to the new checks it adds in development mode"
  - ⚠ The text does not describe what the new checks are or which component patterns fail them.
- **[uncertain] behavior** `present` `"non-idempotent mount/unmount logic"`: Components are not resilient to being unmounted and remounted with existing state (e.g., mount-time side effects that are not cleaned up) (confidence low, judge partially_supported)
  - react_changelog: "fix the components to be resilient to remounting with existing state"
  - react_upgrade_guide: "some effects assume they are only mounted or destroyed once"
  - react_changelog: "re-run effects to check for restorable state"
  - ⚠ The text does not specify which component patterns break; effects as the cause is an inference.
  - ⚠ The text does not specify which effect patterns are non-resilient beyond assuming single mount/destroy.
  - ⚠ The text does not specify which effect patterns break; most effects are stated to work without changes.
  - ⚠ The text does not name specific effect hooks or describe the exact sequence of re-running.

Actions:
- Fix components to be resilient to unmounting and remounting with existing state.
- If this breaks the app, temporarily remove Strict Mode until the components are fixed.
- Audit effects inside StrictMode trees to ensure they are resilient to being mounted and destroyed multiple times (proper cleanup functions, idempotent setup).
- Run the app in development with StrictMode to surface effects that break on simulated unmount/remount.
- See the Working Group posts 'Adding Reusable State to StrictMode' and 'How to support Reusable State in Effects'.
- Make effects resilient to being mounted and destroyed multiple times, with cleanup functions that fully undo setup.
- Test components under React 18 Strict Mode in development to surface effects that assume single mount/unmount.
- Audit effects in components rendered under <StrictMode> to ensure cleanup functions fully restore state so effects can safely run again.
- Test the app under StrictMode after upgrading to detect duplicated side effects (subscriptions, network requests, analytics).
- If the app doesn't work after upgrading, try removing <StrictMode> temporarily during the upgrade.
- Fix the issues Strict Mode points out, then add <StrictMode> back (at the top or for a part of the tree).

### Suspense fallback={undefined} no longer ignored

`react_ab2c7932c2` · medium · confidence medium · introduced in 18 · fires at upgrade

In React 18, a Suspense boundary with fallback={undefined} behaves the same as fallback={null} instead of being ignored. Code relying on the boundary being ignored (so suspension propagates to an outer boundary) will now show an empty fallback at this boundary instead.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React 18.0.0, where Suspense fallback={undefined} behavior changed. (confidence high, judge supported)
  - react_changelog: "Suspense fallback={undefined} now behaves the same as null and isn't ignored."
- **[required] api_usage** `present` `"<Suspense fallback={undefined}"`: The application renders a Suspense component whose fallback prop is undefined (explicitly or via a variable that may be undefined). (confidence medium, judge supported)
  - react_changelog: "Suspense fallback={undefined} now behaves the same as null and isn't ignored."
  - ⚠ Fallbacks passed via variables that evaluate to undefined at runtime cannot be detected by static search alone.
- **[uncertain] behavior** `present` `"reliance on nested Suspense with undefined fallback being ignored"`: The application relies on a Suspense boundary with undefined fallback being skipped so that an outer boundary's fallback is shown. (confidence low, judge partially_supported)
  - react_changelog: "now behaves the same as null and isn't ignored"
  - ⚠ The text does not describe the visible impact beyond the boundary no longer being ignored.

Actions:
- Search for Suspense boundaries with undefined fallbacks and either provide an explicit fallback or remove the boundary if the outer boundary's fallback should be shown.

### Layout effects cleaned up and re-created when Suspense tree re-suspends

`react_c0e4ce54e4` · medium · confidence medium · introduced in 18 · fires at first_use

In React 18, when a tree re-suspends and reverts to a Suspense fallback, React cleans up layout effects and re-creates them when the content is shown again. Components with layout effects inside Suspense boundaries will see extra cleanup/setup cycles.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React 18, which introduces the layout-effect cleanup on re-suspend. (confidence high, judge supported)
  - react_changelog: "When a tree re-suspends and reverts to a fallback, React will now clean up layout effects"
- **[required] api_usage** `present` `"Suspense"`: The application renders components inside a Suspense boundary that can re-suspend and revert to a fallback. (confidence high, judge supported)
  - react_changelog: "When a tree re-suspends and reverts to a fallback"
- **[required] api_usage** `present` `"useLayoutEffect"`: Components inside the Suspense boundary use layout effects whose cleanup/re-creation may not be idempotent. (confidence medium, judge partially_supported)
  - react_changelog: "React will now clean up layout effects, and then re-create them when the content inside the boundary is shown again"
  - ⚠ Text says 'layout effects' without naming APIs; class lifecycle methods (componentDidMount/componentWillUnmount) may also be affected but are not stated.

Actions:
- Review useLayoutEffect usages inside Suspense boundaries to ensure cleanup and re-setup are safe to run multiple times.
- Test UI flows where Suspense content re-suspends and shows the fallback again.

### Automatic batching of state updates outside React event handlers under createRoot

`react_e56a0f9df4` · medium · confidence medium · introduced in 18 · fires at upgrade

In React 18 with createRoot, state updates inside timeouts, promises, native event handlers or any other event are batched into a single re-render, whereas before React 18 they each triggered a separate render. Code relying on synchronous re-render/DOM updates between consecutive state updates outside React event handlers may behave differently. Opt out with flushSync.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: Upgrade crosses React 18, where automatic batching for all updates was introduced (confidence high, judge supported)
  - react_upgrade_guide: "Starting in React 18 with createRoot, all updates will be automatically batched, no matter where they originate from."
- **[required] api_usage** `present` `"createRoot"`: The application renders with createRoot (confidence high, judge supported)
  - react_upgrade_guide: "Starting in React 18 with createRoot, all updates will be automatically batched"
  - react_upgrade_guide: "To opt-out of automatic batching, you can use flushSync"
- **[required] behavior** `present` `"state updates outside React event handlers"`: The application performs multiple state updates inside timeouts, promises, native event handlers or other non-React events (confidence medium, judge supported)
  - react_upgrade_guide: "updates inside of timeouts, promises, native event handlers or any other event will batch the same way as updates inside of React events"
  - ⚠ The text does not state which specific application patterns break; it only says this is a breaking change.
  - ⚠ The text does not specify which application patterns would break as a result of batching; it only states it is a breaking change.
- **[disqualifying] api_usage** `present` `"flushSync"`: Updates already wrapped in flushSync opt out of automatic batching (confidence high, judge supported)
  - react_upgrade_guide: "To opt-out of automatic batching, you can use flushSync"

Actions:
- Review state updates in setTimeout, promises, and native event handlers for code that depends on intermediate re-renders or DOM state between updates.
- Where immediate re-render is required, wrap updates with flushSync imported from 'react-dom'.
- Review state updates in setTimeout, promises and native event handlers for code that depends on the DOM updating after each individual update.
- Where synchronous DOM updates are required, wrap the state updates in flushSync imported from 'react-dom'.

### lazy() components resolving to the same component treated as equivalent

`react_1ae332ab77` · low · confidence high · introduced in 18 · fires at upgrade

In React 18, all lazy() wrappers that resolve to the same component are considered equivalent. Apps that create multiple lazy() wrappers for the same underlying component may see different reconciliation behavior than in React 17. The text does not describe the exact effect.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React release 18, where lazy() equivalence changed (confidence high, judge supported)
  - react_changelog: "Consider all lazy() resolving to the same component equivalent."
- **[required] api_usage** `present` `"lazy("`: The application uses lazy() to load components (confidence high, judge supported)
  - react_changelog: "Consider all lazy() resolving to the same component equivalent."
- **[uncertain] behavior** `present` `"multiple lazy() calls resolving to the same component"`: The application has multiple separate lazy() wrappers that resolve to the same component and depends on them being treated as distinct (e.g. remounting or state reset when switching between them) (confidence low, judge partially_supported)
  - react_changelog: "Consider all lazy() resolving to the same component equivalent."
  - ⚠ The text does not state the practical effect (e.g. state preservation vs. remount) of treating them as equivalent.

Actions:
- Review lazy() usages for multiple wrappers resolving to the same component and verify behavior under React 18.
- If the application relies on remounting when switching between such wrappers, use an explicit key to force remounts.

### ReactDOM.hydrate should be migrated to hydrateRoot to enable React 18 features

`react_385fe7836e_5bce` · low · confidence medium · introduced in 18 · fires at upgrade

React 18 adds hydrateRoot, exported from react-dom/client, to hydrate server-rendered apps. Apps that keep using ReactDOM.hydrate will not get React 18's new features, which require hydrateRoot. The text does not say ReactDOM.hydrate is removed or stops working.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React 18.0.0, where hydrateRoot was introduced in react-dom/client. (confidence medium, judge partially_supported)
  - react_changelog: "These new APIs are now exported from react-dom/client"
  - react_changelog: "react-dom: ReactDOM.hydrate has been deprecated."
- **[required] api_usage** `present` `"ReactDOM.hydrate"`: The application hydrates a server-rendered app using ReactDOM.hydrate. (confidence medium, judge supported)
  - react_changelog: "Use it instead of ReactDOM.hydrate in conjunction with the new React DOM Server APIs"
  - react_changelog: "Using it will warn and run your app in React 17 mode."
  - ⚠ The text does not state whether ReactDOM.hydrate is deprecated, warns, or will be removed. It only says new features don't work without hydrateRoot.
  - ⚠ The text does not name a replacement API or say when hydrate will be removed.
- **[disqualifying] api_usage** `present` `"hydrateRoot"`: The application already uses hydrateRoot from react-dom/client. (confidence medium, judge partially_supported)
  - react_changelog: "hydrateRoot: New method to hydrate a server rendered application."
- **[optional] behavior** `present` `"React 18 new features"`: The application relies on new React 18 features, which do not work without hydrateRoot. (confidence medium, judge partially_supported)
  - react_changelog: "New features in React 18 don't work without it."
  - ⚠ The text does not list which new features depend on hydrateRoot.
- **[optional] behavior** `absent` `"onRecoverableError"`: After migrating to hydrateRoot, React reports recoverable hydration errors via reportError (or console.error in older browsers) unless an onRecoverableError option is provided. (confidence medium, judge partially_supported)
  - react_changelog: "By default, React will use reportError, or console.error in the older browsers."

Actions:
- Replace ReactDOM.hydrate calls with hydrateRoot imported from react-dom/client, used with the new React DOM Server APIs.
- Optionally pass onRecoverableError to hydrateRoot to log errors React recovers from during hydration.
- Find all calls to ReactDOM.hydrate.
- Migrate off ReactDOM.hydrate using React 18's recommended root API, so the app no longer runs in React 17 mode and no longer emits the deprecation warning.

### ReactDOM.render legacy root API deprecated in favor of createRoot

`react_4a4e72c4eb` · low · confidence high · introduced in 18 · fires at future_removal

In React 18, ReactDOM.render is no longer supported and logs a console warning. Apps that keep using it continue to run as if on React 17 (legacy root, no concurrent renderer). Migrating to createRoot from 'react-dom/client' enables the new concurrent renderer.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React 18, where ReactDOM.render is no longer supported. (confidence high, judge supported)
  - react_upgrade_guide: "ReactDOM.render is no longer supported in React 18. Use createRoot instead."
  - react_changelog: "New features in React 18 don't work without it."
  - react_changelog: "react-dom: ReactDOM.render has been deprecated."
- **[required] api_usage** `present` `"ReactDOM.render"`: The application renders its root with ReactDOM.render / render imported from 'react-dom'. (confidence high, judge supported)
  - react_upgrade_guide: "import { render } from 'react-dom';"
  - react_upgrade_guide: "render(<App tab="home" />, container);"
  - react_changelog: "Use it instead of ReactDOM.render."
  - react_changelog: "These new APIs are now exported from react-dom/client"
  - react_changelog: "Using it will warn and run your app in React 17 mode."
  - ⚠ The text does not say whether ReactDOM.render still works, warns, or fails in React 18. It only says new features don't work without createRoot.
  - ⚠ The text does not name a replacement API or say when ReactDOM.render will be removed.
  - ⚠ The text does not say what specifically differs between React 17 mode and React 18 behavior.
- **[required] behavior** `present` `"console warning: ReactDOM.render is no longer supported in React 18"`: Until migrated, the app logs a console warning and behaves as if running React 17. (confidence high, judge supported)
  - react_upgrade_guide: "When you first install React 18, you will see a warning in the console"
  - react_upgrade_guide: "Until you switch to the new API, your app will behave as if it's running React 17."
  - react_changelog: "By default, React will use reportError, or console.error in the older browsers."
  - ⚠ The text does not state when ReactDOM.render will be removed entirely.
- **[disqualifying] api_usage** `present` `"createRoot"`: The application already uses createRoot from 'react-dom/client'. (confidence high, judge supported)
  - react_upgrade_guide: "import { createRoot } from 'react-dom/client';"
- **[optional] behavior** `present` `"concurrent renderer"`: Switching to createRoot enables the new concurrent renderer, changing rendering behavior compared to the legacy root. (confidence medium, judge partially_supported)
  - react_upgrade_guide: "The new root API also enables the new concurrent renderer, which allows you to opt-into concurrent features."
  - ⚠ The text does not detail which behaviors differ under the concurrent renderer.

Actions:
- Replace `import { render } from 'react-dom'` and `render(<App />, container)` with `import { createRoot } from 'react-dom/client'`, `const root = createRoot(container); root.render(<App />);`.
- In TypeScript, use `createRoot(container!)`.
- Test the app after migration since the new root enables the concurrent renderer.
- Replace ReactDOM.render(element, container) with createRoot(container).render(element), importing createRoot from 'react-dom/client'.
- Optionally pass onRecoverableError to createRoot if you want to log errors React recovers from.
- Find all ReactDOM.render calls in the codebase.
- Plan a migration off ReactDOM.render to the non-deprecated React 18 root API (see the React 18 upgrade documentation), so the app stops running in React 17 mode and avoids the deprecation warning.

### react-refresh package.json exports field may restrict deep/subpath imports

`react_6f939e43ca` · low · confidence medium · introduced in 18 · fires at upgrade

In React 18.0.0, the React Refresh package added an "exports" field to its package.json. The changelog does not describe any impact. An exports field generally limits which module paths a bundler or Node.js can resolve, so code or tooling that imports react-refresh subpaths might be affected. This impact is inferred, not stated.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React release 18.0.0, where an exports field was added to the React Refresh package.json. (confidence medium, judge partially_supported)
  - react_changelog: "Add exports field to package.json."
- **[uncertain] dependency** `present` `"react-refresh/"`: The application or its build tooling imports react-refresh, possibly via deep/subpath imports that may no longer resolve under the new exports map. (confidence low, judge partially_supported)
  - react_changelog: "Add exports field to package.json. (#23087 by @otakustay)"
  - ⚠ The changelog does not state which paths are exported or whether any previously resolvable import paths are now blocked.
  - ⚠ The changelog does not state any breaking impact; the effect on subpath imports is inferred.

Actions:
- Search the codebase and build configuration for imports of react-refresh, especially subpath imports such as react-refresh/...
- After upgrading, run the dev build with Fast Refresh to confirm the react-refresh module paths still resolve.

### Deprecated renderToNodeStream now warns in React 18

`react_6fff665547` · low · confidence medium · introduced in 18 · fires at future_removal

React 18 deprecates the old Node streaming API (renderToNodeStream) from react-dom/server. It does not support incremental Suspense streaming on the server, and using it now emits a deprecation warning. renderToPipeableStream is the replacement for streaming in Node environments.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React 18, where the old Node streaming API is deprecated and warns on use. (confidence medium, judge partially_supported)
  - react_upgrade_guide: "we're deprecating the old Node streaming API, which does not support incremental Suspense streaming on the server"
- **[required] api_usage** `present` `"renderToNodeStream"`: The application calls renderToNodeStream from react-dom/server. (confidence medium, judge partially_supported)
  - react_upgrade_guide: "renderToNodeStream: Deprecated ⛔️️ Instead, for streaming in Node environments, use: renderToPipeableStream: New ✨"
  - ⚠ The text does not state when renderToNodeStream will be removed.

Actions:
- Replace renderToNodeStream with renderToPipeableStream for streaming SSR in Node environments.
- For edge runtimes such as Deno or Cloudflare workers, consider renderToReadableStream.

### act warnings no longer emitted by default in unit tests

`react_bf8746ac22` · low · confidence medium · introduced in 18 · fires at upgrade

In React 18, act warnings in tests are opt-in. Unit tests that relied on act warnings to catch unwrapped state updates will no longer see them unless the opt-in mechanism is enabled. This only affects warnings and does not break tests.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React 18, where act warnings became opt-in (confidence high, judge supported)
  - react_changelog: "In tests, act warnings are now opt-in"
- **[required] test_coverage** `present` `"act"`: The project has unit tests that use act or rely on act warnings (confidence medium, judge supported)
  - react_changelog: "enable them only for unit tests where they are useful and beneficial"
  - ⚠ The text does not name the opt-in mechanism or setting.
- **[disqualifying] test_coverage** `present` `"end-to-end tests only"`: Only end-to-end tests are run, so act warnings are unnecessary (confidence high, judge supported)
  - react_changelog: "If you're running end-to-end tests, the act warnings are unnecessary."

Actions:
- Enable the opt-in act warning mechanism for unit test environments where act warnings are useful.
- Leave act warnings disabled for end-to-end test suites.

### SSR omits function/symbol values on custom elements

`react_d7f515143b` · low · confidence medium · introduced in 18 · fires at upgrade

In React 18 the server renderer ignores function and symbol values passed as props to custom elements. Server-rendered HTML for custom elements that receive such values may differ from React 17 output.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React 18, where the server renderer ignores function and symbol values inside custom elements. (confidence high, judge supported)
  - react_changelog: "Ignore function and symbol values inside custom elements on the server."
- **[required] api_usage** `present` `"React DOM Server rendering of custom elements"`: The application server-renders custom elements (hyphenated tag names) using React DOM Server. (confidence high, judge supported)
  - react_changelog: "Ignore function and symbol values inside custom elements on the server."
- **[required] behavior** `present` `"function or symbol prop values on custom elements"`: The application passes function or symbol values as props to those custom elements and relies on their previous server-rendered output. (confidence medium, judge supported)
  - react_changelog: "Ignore function and symbol values inside custom elements on the server."
  - ⚠ The text does not state how React 17 rendered these values on the server, so the exact output difference is not specified.

Actions:
- Review server-rendered custom elements that receive function or symbol props and verify the HTML output and any dependent behavior after upgrading to React 18.
- Attach such values on the client (e.g., after hydration) rather than relying on server-rendered attributes.

### Test console warning about act environment after switching tests to createRoot

`react_dc5cc879a8` · low · confidence medium · introduced in 18 · fires at first_use

When tests are updated to use createRoot under React 18, React logs the warning 'The current testing environment is not configured to support act(...)' unless globalThis.IS_REACT_ACT_ENVIRONMENT is set to true in the test setup.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React 18, where tests using createRoot may emit the act environment warning (confidence medium, judge partially_supported)
  - react_upgrade_guide: "When you first update your tests to use createRoot, you may see this warning in your test console"
- **[required] test_coverage** `present` `"createRoot"`: The test suite renders with createRoot (confidence high, judge supported)
  - react_upgrade_guide: "When you first update your tests to use createRoot"
- **[disqualifying] configuration** `present` `"IS_REACT_ACT_ENVIRONMENT"`: The test setup already sets globalThis.IS_REACT_ACT_ENVIRONMENT, so the warning does not appear (confidence medium, judge partially_supported)
  - react_upgrade_guide: "set globalThis.IS_REACT_ACT_ENVIRONMENT to true before running your test"
- **[uncertain] dependency** `present` `"@testing-library/react"`: The testing library in use (e.g. a React 18-ready React Testing Library version) configures the flag automatically (confidence low, judge partially_supported)
  - react_upgrade_guide: "the next version of React Testing Library has built-in support for React 18 without any additional configuration"
  - ⚠ The text does not state which React Testing Library version includes built-in support.

Actions:
- In your test setup file add: globalThis.IS_REACT_ACT_ENVIRONMENT = true;
- For end-to-end tests that simulate a full browser environment, set globalThis.IS_REACT_ACT_ENVIRONMENT = false to tell React act isn't needed.
- Consider upgrading to a React Testing Library version with built-in React 18 support.

### React no longer bundles object-assign polyfill; legacy runtimes without native Object.assign may break

`react_e5d2f27aa2` · low · confidence high · introduced in 18 · fires at upgrade

React 18 removes its object-assign polyfill. The text does not say what happens next, but this suggests React may rely on native Object.assign, so JavaScript environments without it (e.g., legacy browsers) might fail unless a global polyfill is provided.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React 18.0.0, where the object-assign polyfill was removed (confidence high, judge supported)
  - react_changelog: "Remove object-assign polyfill."
- **[uncertain] runtime** `absent` `"Object.assign"`: The application targets JavaScript runtimes or browsers that lack native Object.assign and does not provide a global polyfill for it (confidence low, judge partially_supported)
  - react_changelog: "Remove object-assign polyfill."
  - ⚠ The changelog does not state that React now requires native Object.assign or name which environments are affected; the impact is inferred from the polyfill removal.

Actions:
- Check the browserslist or other target-runtime configuration for environments lacking native Object.assign (e.g., IE11).
- If such environments are supported, load a global Object.assign polyfill before React.

## Review checklist

### Low confidence or disputed

- [ ] react_0c8f3e839e: React 18 requires a global Symbol implementation
- [ ] react_090a4a6780: Hydration text mismatches now errors and fall back to client rendering
- [ ] react_1174c2e1c2: Expanded act() warnings in test environments
- [ ] react_362d1d0639: Automatic batching changes state update rendering behavior

### Inferred conditions

- [ ] react_0c8f3e839e: The application runs (or supports running) in a JavaScript environment that lacks a native global Symbol and does not load a Symbol polyfill.
- [ ] react_54ca1125eb: The bundled application already includes a global polyfill for Promise, Symbol, and Object.assign.
- [ ] react_090a4a6780: The application hydrates server-rendered markup on the client.
- [ ] react_1174c2e1c2: The test suite exercises React APIs that schedule React work, possibly outside act().
- [ ] react_1174c2e1c2: The test setup treats console warnings/errors as test failures, turning the new warnings into failures.
- [ ] react_1174c2e1c2: Tests assert on intermediate render states between multiple updates inside a single act call.
- [ ] react_2489111975: The application has migrated, or is migrating, to createRoot/root.render. The guide says apps still using the legacy API behave as on React 17.
- [ ] react_362d1d0639: The application performs React state updates whose behavior depends on updates not being batched.
- [ ] react_385fe7836e: Until migrated, the app behaves as if running React 17 (legacy mode), so new concurrent features are not enabled.
- [ ] react_44cfb7b19d: Components rely on effects firing or render work persisting for a tree that suspended before completing mount
- [ ] react_479331dfb5: The application relies on renderToStaticMarkup throwing an error when suspending (e.g. catch/fallback logic).
- [ ] react_4aaaf16b0e: The application depends on the previous (asynchronous/inconsistent) timing of effect execution relative to the event.
- [ ] react_7123c14ec9: Whether unmountComponentAtNode stops working immediately in React 18 or continues in legacy (React 17-like) mode until the app switches to the new root API.
- [ ] react_71acd3a7ef: Components are not resilient to being unmounted and remounted with existing state (e.g., mount-time side effects that are not cleaned up)
- [ ] react_ab2c7932c2: The application relies on a Suspense boundary with undefined fallback being skipped so that an outer boundary's fallback is shown.
- [ ] react_1ae332ab77: The application has multiple separate lazy() wrappers that resolve to the same component and depends on them being treated as distinct (e.g. remounting or state reset when switching between them)
- [ ] react_6f939e43ca: The application or its build tooling imports react-refresh, possibly via deep/subpath imports that may no longer resolve under the new exports map.
- [ ] react_e5d2f27aa2: The application targets JavaScript runtimes or browsers that lack native Object.assign and does not provide a global polyfill for it

### Source disagreements


### Open questions

- Ecosystem packages (@types/react, react-test-renderer users, Enzyme, React Native, state libraries) have their own React 18 support timelines that are not in React's docs.
- React 18.x minor release notes after 18.0.0 were not mined.
- [react_1174c2e1c2] Unconfirmed: The test setup treats console warnings/errors as test failures, turning the new warnings into failures. (The text does not state whether the warning is emitted via console.error or whether it causes failures.)
- [react_1174c2e1c2] Unconfirmed: Tests assert on intermediate render states between multiple updates inside a single act call. (The text does not describe which test patterns break or the exact batching semantics.)
- [react_2489111975] Unconfirmed: The application has migrated, or is migrating, to createRoot/root.render. The guide says apps still using the legacy API behave as on React 17. (The text does not explicitly state whether legacy ReactDOM.render still invokes the callback in React 18, or whether the removal applies only to root.render.)
- [react_44cfb7b19d] Unconfirmed: Components rely on effects firing or render work persisting for a tree that suspended before completing mount (The text does not state what specific code patterns depend on the old behavior.)
- [react_479331dfb5] Unconfirmed: The application relies on renderToStaticMarkup throwing an error when suspending (e.g. catch/fallback logic). (The text does not state impact on apps that depended on the error; inferred from the change.)
- [react_4aaaf16b0e] Unconfirmed: The application depends on the previous (asynchronous/inconsistent) timing of effect execution relative to the event. (The text does not describe what specific code patterns break due to the timing change.)
- [react_7123c14ec9] Unconfirmed: Whether unmountComponentAtNode stops working immediately in React 18 or continues in legacy (React 17-like) mode until the app switches to the new root API. (The text says the API was 'changed' but does not state whether unmountComponentAtNode is removed, deprecated, or still functional in React 18.)
- [react_71acd3a7ef] Unconfirmed: Components are not resilient to being unmounted and remounted with existing state (e.g., mount-time side effects that are not cleaned up) (The text does not specify which component patterns break; effects as the cause is an inference.)
- [react_ab2c7932c2] Unconfirmed: The application relies on a Suspense boundary with undefined fallback being skipped so that an outer boundary's fallback is shown. (The text does not describe the visible impact beyond the boundary no longer being ignored.)
- [react_1ae332ab77] Unconfirmed: The application has multiple separate lazy() wrappers that resolve to the same component and depends on them being treated as distinct (e.g. remounting or state reset when switching between them) (The text does not state the practical effect (e.g. state preservation vs. remount) of treating them as equivalent.)
- [react_6f939e43ca] Unconfirmed: The application or its build tooling imports react-refresh, possibly via deep/subpath imports that may no longer resolve under the new exports map. (The changelog does not state which paths are exported or whether any previously resolvable import paths are now blocked.)
- [react_dc5cc879a8] Unconfirmed: The testing library in use (e.g. a React 18-ready React Testing Library version) configures the flag automatically (The text does not state which React Testing Library version includes built-in support.)
- [react_e5d2f27aa2] Unconfirmed: The application targets JavaScript runtimes or browsers that lack native Object.assign and does not provide a global polyfill for it (The changelog does not state that React now requires native Object.assign or name which environments are affected; the impact is inferred from the polyfill removal.)

## Context facts (not risks)

- (18) react-dom: ReactDOM.unmountComponentAtNode has been deprecated. — _ReactDOM.unmountComponentAtNode is only deprecated in React 18; it still works and no action is required at 18. The text names no removal version, behavior change or replacement, so migration can wait until a future removal._
- (18) react-dom: ReactDOM.renderSubtreeIntoContainer has been deprecated. — _The item only states that ReactDOM.renderSubtreeIntoContainer has been deprecated in React 18. It names no removal, behavior change or required action at 18, so the API is deprecated but still working. Note for later: a future major release may remove it, and code that uses it should eventually migrate. The text names no replacement._
- (18) react-dom/server: ReactDOMServer.renderToNodeStream has been deprecated. — _The text only states that ReactDOMServer.renderToNodeStream is deprecated in React 18. It does not say the API is removed, stops working, or changes behavior, and it names no replacement. A deprecated-but-working API needs no action at 18, though code that uses it may need migration in a future release._
- (18) Components can now render undefined: React no longer throws if you return undefined from a component. — _This relaxes a restriction: React 18 no longer throws when a component returns undefined. Code that worked in React 17 keeps working, so no migration is needed. The only consequence is that a missing return statement before JSX no longer raises an error, and the text addresses this by suggesting a linter rather than describing a breakage._
- (18) No suppression of console logs: When you use Strict Mode, React renders each component twice to help you find unexpected side effects. — _This is a development-only logging change under Strict Mode. React 18 no longer suppresses console logs during the second of the two Strict Mode renders. The only effect described is duplicate console output, which React DevTools greys out and can optionally suppress. The text describes no breakage, required migration, or operational impact, so no action is needed at 18. The only effect is a cosmetic change in log output._
- (18) Don't patch console during first render. — _The item only says React no longer patches console during the first render. The text does not describe any removed API, required migration, or breaking impact. It reads as an internal or dev-tooling logging adjustment that needs no user action when upgrading to 18._
- (18) Use setImmediate when available over MessageChannel. — _Internal scheduler implementation detail: React prefers setImmediate over MessageChannel when available. The text states no user action, removed API, or breaking behavior, so nothing needs to change at 18._
- (18) Fix useReducer observing incorrect props by removing the eager bailout mechanism. — _This is a bug fix: useReducer no longer observes incorrect props because the eager bailout mechanism was removed. The changelog states no breaking impact and no required user action. Any side effects of removing the eager bailout, such as extra renders, are not described in the text._
- (18) Add createRoot and hydrateRoot. — _The item only announces the addition of new APIs (createRoot and hydrateRoot). It is an additive feature. The text states no breaking change, removal or required migration for existing code at 18. Adopting these APIs is opt-in._
- (18) Add the new streaming renderer. — _Adding the new streaming server renderer is an additive feature in React DOM Server 18; the item states no removal, behavior change, or required user action. Related breaking or deprecation items (e.g., deprecation of renderToNodeStream) are separate changelog entries._
- (18) Support disabling spurious act warnings with global.IS_REACT_ACT_ENVIRONMENT. (#22561 by @acdlite) — _Additive opt-in feature: React 18 adds support for global.IS_REACT_ACT_ENVIRONMENT to disable spurious act warnings. The item describes no breaking change and no required action at 18. Related changes in the same section, such as the expanded act warnings and throwing when act is used in production, are separate items._
- (18) March 08, 2022 by Rick Hanlon --- As we shared in the release post, React 18 introduces features powered by our new concurrent renderer, with a gradual adoption strategy for existing applications. — _Introductory overview of the React 18 upgrade guide. It describes the gradual adoption strategy and notes that React 18 will ship for React Native in a future version. It names no breaking change, removed API or required migration step on its own; the specific upgrade steps are covered in other sections._
- (18) renderToNodeStream: Deprecated ⛔️️ — _renderToNodeStream is deprecated in React 18 but still works; the text only says 'Using this API will now warn' and names renderToPipeableStream as the replacement for Node streaming. Nothing breaks at the 17 -> 18 upgrade, and the text gives no removal version, so no migration is required now._
- (18) Instead, for streaming in Node environments, use: — _This item only points to the replacement API (renderToPipeableStream) for Node streaming. The old renderToNodeStream is deprecated in React 18 but still works and only emits a warning, so no action is required at 18. Migrating to renderToPipeableStream is recommended but optional._
- (18) The following APIs will continue working, but with limited support for Suspense: — _The item says renderToString and renderToStaticMarkup "will continue working, but with limited support for Suspense". These APIs are not deprecated or removed, and the text names no required migration or breaking change at React 18. The note only describes limited Suspense support in existing working APIs, so no user action is required at this upgrade._
- (18) renderToString: Limited ⚠️ — _The guide states that renderToString "will continue working, but with limited support for Suspense." It is neither removed nor deprecated, and the text names no breaking behavior or required action at 18. Streaming alternatives (renderToPipeableStream, renderToReadableStream) are available as opt-in options for full Suspense SSR support._
- (18) renderToStaticMarkup: Limited ⚠️ — _The guide says renderToStaticMarkup "will continue working, but with limited support for Suspense" in React 18. It is neither removed nor deprecated, and the text names no breaking behavior or required migration. The 'Limited' label only notes that it lacks the new streaming Suspense capabilities. No action is required at 18._
- (18) In the React 18 Working Group we worked with library maintainers to create new APIs needed to support concurrent rendering for use cases specific to their use case in areas like styles, and external stores. — _This is an introductory sentence announcing new additive APIs for library maintainers, such as useSyncExternalStore and useInsertionEffect, which support concurrent rendering. It says only that 'some libraries may need to switch' to these APIs. It names no removed or changed API and states no breakage or required action for applications upgrading to 18. Any concrete library-level guidance belongs to the individual API items that follow._
- (18) useSyncExternalStore is a new Hook that allows external stores to support concurrent reads by forcing updates to the store to be synchronous. — _useSyncExternalStore is a new, additive Hook in React 18. The text only recommends it for libraries that integrate with state external to React. It does not state that existing app code breaks or that any removal or behavior change requires action at upgrade. Adopting it is an optional library-side improvement for concurrent rendering support._
- (18) Components can now render undefined: React no longer warns if you return undefined from a component. — _Relaxation of a dev warning: React 18 no longer warns when a component returns undefined. Code that worked in 17 still works; nothing breaks and no migration is required. The only effect is that a missing return statement before JSX is no longer flagged. The text suggests a linter for this, but that is an optional safeguard, not a required action._
- (18) No warning about setState on unmounted components: Previously, React warned about memory leaks when you call setState on an unmounted component. — _A warning about setState on unmounted components was removed, which requires no user action._
- (18) Improved memory usage: React now cleans up more internal fields on unmount, making the impact from unfixed memory leaks that may exist in your application code less severe. — _Memory cleanup on unmount is an internal improvement that requires no user action._
- (18) renderToPipeableStream: New ✨ — _renderToPipeableStream is a new additive API that is the replacement for renderToNodeStream._
- (18) We're also introducing a new API to support streaming SSR with Suspense for modern edge runtime environments, such as Deno and Cloudflare workers: — _It introduces a new additive API for edge runtimes and requires no action._
- (18) renderToReadableStream: New ✨ — _renderToReadableStream is a purely additive new API._
- (18) Finally, this API will continue to work for rendering e-mails: — _It says the API continues to work for rendering e-mails, so no action is needed._
- (18) renderToStaticNodeStream — _renderToStaticNodeStream continues to work, so no action is required._
- (18) For more information on the changes to server rendering APIs, see the working group post on Upgrading to React 18 on the server, a deep dive on the new Suspense SSR Architecture, and Shaundai Person's talk on Streaming Server Rendering — _It is a documentation pointer to further reading on server rendering changes._
- (18) See the React 18 typings pull request for a full list of type-only changes. — _Points to the typings PR, migration script, and issue reporting without itself requiring action._
- (18) React 18 adds out-of-the-box performance improvements by doing more batching by default. — _Describes the prior batching behavior as background before the change._
- (18) For more information, see the Automatic batching deep dive. — _Documentation pointer to a deep dive._
- (18) For more information, see the Working Group posts for Adding Reusable State to StrictMode and How to support Reusable State in Effects. — _Documentation pointers to working group posts._
- (18) The purpose of the flag is to tell React that it's running in a unit test-like environment. — _Explains the purpose of the act environment flag and background on testing libraries; no extra action beyond the setup._

## Disqualified candidates


## Sources

| Source | Type | Tier | Status | Pinned ref |
|---|---|---|---|---|
| [react_changelog](https://github.com/facebook/react/blob/main/CHANGELOG.md#1800-march-29-2022) | official_changelog | 1 | used | `main@e8738f0c628b` |
| [react_upgrade_guide](https://react.dev/blog/2022/03/08/react-18-upgrade-guide) | official_migration_guide | 1 | used | `main@c3c956bef083` |

## What we trusted and what we did not

- Trusted: package metadata for version numbers; official guides, release notes and changelogs pinned to a tag, branch or commit.
- Not trusted: LLM self-reported confidence, unpinned current pages when they disagree with pinned ones, any quote that fails exact match, transclusion stubs.
