# React 17 → 18: upgrade risk report

> Documentation-derived risk conditions; not a migration plan.

React 17 -> 18 crosses 1 release(s) (18). 25 risk paths: 4 high, 15 medium, 6 low. Main risk types: changed_behavior (18), removed_api (3), runtime_requirement (2). 39 context facts and 0 disqualified candidates are listed separately. Documentation-derived risk conditions; not a migration plan.

Overall confidence: **medium**. Validation: `{"errors": 0, "warnings": 3, "by_code": {"W4_no_search_queries": 3}}`

## Risk paths

| Level | Confidence | Type | Surface | Release | Path |
|---|---|---|---|---|---|
| high | medium | runtime_requirement | runtime | 18 | `react_38bf30f056` Modern JS environment requirement (Promise, Symbol, Object.assign) for older browsers |
| high | medium | removed_api | application_code | 18 | `react_66adbc474f` Removed unstable scheduler/tracing API |
| high | medium | runtime_requirement | runtime | 18 | `react_77c14b0b1f` Internet Explorer support dropped in React 18 |
| high | medium | removed_api | application_code | 18 | `react_e611605e84` unstable_changedBits removal |
| medium | high | changed_behavior | application_code | 18 | `react_0cdcfd833f` TypeScript children prop must be declared explicitly in props |
| medium | medium | changed_behavior | application_code | 18 | `react_1174c2e1c2` act throws when used in production |
| medium | high | changed_behavior | application_code | 18 | `react_362d1d0639` Automatic batching of state updates outside React event handlers |
| medium | high | changed_behavior | application_code | 18 | `react_385fe7836e` ReactDOM.hydrate deprecated: warns and runs app in React 17 mode |
| medium | medium | changed_behavior | application_code | 18 | `react_44cfb7b19d` Suspense trees discard incomplete new trees and retry rendering from scratch |
| medium | medium | changed_behavior | application_code | 18 | `react_479331dfb5` renderToStaticMarkup suspending behavior change |
| medium | medium | changed_behavior | application_code | 18 | `react_4a4e72c4eb` ReactDOM.render replaced by createRoot |
| medium | medium | changed_behavior | application_code | 18 | `react_4aaaf16b0e` Consistent useEffect timing: synchronous effect flush on discrete input events |
| medium | medium | removed_api | application_code | 18 | `react_5245677ce9` render callback (third argument) removed with createRoot migration |
| medium | medium | changed_behavior | application_code | 18 | `react_60fe36b771` Suspense fallback={undefined} no longer ignored |
| medium | medium | changed_behavior | application_code | 18 | `react_6c336940af` renderToString suspending behavior change |
| medium | medium | changed_behavior | application_code | 18 | `react_71acd3a7ef` Strict Mode dev-only simulated unmount/remount breaks effects that assume single mount/destroy |
| medium | low | changed_behavior | application_code | 18 | `react_a6a01d8772` Layout effects cleaned up and re-created when Suspense boundary re-suspends |
| medium | low | changed_behavior | application_code | 18 | `react_d1fa9e779a` Stricter hydration errors for text content mismatches |
| medium | medium | changed_behavior | application_code | 18 | `react_e56a0f9df4` Automatic batching changes render timing for updates outside React events |
| low | high | changed_behavior | application_code | 18 | `react_7123c14ec9` unmountComponentAtNode replaced by root.unmount |
| low | medium | changed_default | tests | 18 | `react_bf8746ac22` act warnings opt-in for unit tests |
| low | medium | changed_behavior | application_code | 18 | `react_d7f515143b` Function and symbol values on custom elements ignored during server rendering |
| low | medium | configuration_change | tests | 18 | `react_dc5cc879a8` Test environment missing IS_REACT_ACT_ENVIRONMENT flag after switching tests to createRoot |
| low | high | changed_behavior | dependencies | 18 | `react_e87acb5981` package.json exports field restricts module resolution |
| low | medium | changed_behavior | application_code | 18 | `react_eb824a435b` Text mismatch now reverts to client render |

### Modern JS environment requirement (Promise, Symbol, Object.assign) for older browsers

`react_38bf30f056` · high · confidence medium · introduced in 18 · fires at upgrade

React 18 now depends on modern browser features including Promise, Symbol, and Object.assign. Older browsers and devices such as Internet Explorer that lack these features natively or have non-compliant implementations may not run React 18 unless a global polyfill is included in the bundled application.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React release 18, which introduces the new JS environment requirements. (confidence high, judge supported)
  - react_changelog: "New JS Environment Requirements: React now depends on modern browsers features including Promise, Symbol, and Object.assign."
- **[required] runtime** `present` `"Internet Explorer or other older browser targets"`: The application supports older browsers or devices (such as Internet Explorer) that lack native or compliant Promise, Symbol, or Object.assign. (confidence medium, judge supported)
  - react_changelog: "If you support older browsers and devices such as Internet Explorer which do not provide modern browser features natively or have non-compliant implementations"
  - ⚠ The text does not enumerate which specific browsers or versions lack these features beyond naming Internet Explorer.
- **[disqualifying] dependency** `present` `"global polyfill for Promise, Symbol, Object.assign"`: The application does not already include a global polyfill for Promise, Symbol, and Object.assign. (confidence low, judge partially_supported)
  - react_changelog: "consider including a global polyfill in your bundled application"
  - ⚠ The text does not name a specific polyfill library.

Actions:
- Include a global polyfill for Promise, Symbol, and Object.assign in the bundled application if older browsers or devices such as Internet Explorer must be supported.
- Review the supported browser targets for the application before upgrading to React 18.

### Removed unstable scheduler/tracing API

`react_66adbc474f` · high · confidence medium · introduced in 18 · fires at upgrade

The changelog lists removal of the unstable scheduler/tracing API under Breaking Changes in the 18.0.0 section. Code that depends on this API may break after upgrading. The text does not name specific functions or modules, and it places the item under Scheduler (Experimental).

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses release 18, where the unstable scheduler/tracing API is removed. (confidence medium, judge partially_supported)
  - react_changelog: "Remove unstable scheduler/tracing API"
- **[required] api_usage** `present` `"scheduler/tracing"`: The application uses the unstable scheduler/tracing API. (confidence medium, judge supported)
  - react_changelog: "Remove unstable scheduler/tracing API"
  - ⚠ The text does not name the specific exports or functions of the scheduler/tracing API.
  - ⚠ The text does not list which exports of scheduler/tracing were removed.

Actions:
- Search the codebase and dependencies for imports of scheduler/tracing.
- Remove or replace usages of the unstable scheduler/tracing API before upgrading, since the text names no replacement.
- Search the application and its dependencies, including profiling or tracing tools, for imports of scheduler/tracing.
- Remove those usages or replace them. The text does not name a replacement.

### Internet Explorer support dropped in React 18

`react_77c14b0b1f` · high · confidence medium · introduced in 18 · fires at upgrade

React 18 drops support for Internet Explorer because new features rely on modern browser features such as microtasks that cannot be adequately polyfilled in IE. Applications that must support IE should stay on React 17.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses release 18, in which React drops support for Internet Explorer. (confidence high, judge supported)
  - react_upgrade_guide: "In this release, React is dropping support for Internet Explorer"
- **[required] runtime** `present` `"Internet Explorer"`: The application must support users running Internet Explorer as a target browser. (confidence medium, judge supported)
  - react_upgrade_guide: "If you need to support Internet Explorer we recommend you stay with React 17."
  - ⚠ The text does not state exactly how React 18 fails in IE, only that IE is no longer supported and cannot be adequately polyfilled.

Actions:
- Check browserslist and analytics for Internet Explorer users before upgrading.
- If Internet Explorer must be supported, stay on React 17.
- If IE support is not required, drop IE from supported browser targets and proceed with the upgrade.

### unstable_changedBits removal

`react_e611605e84` · high · confidence medium · introduced in 18 · fires at upgrade

React 18 removes the unsupported unstable_changedBits API. Application or library code that still uses it will no longer work after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React release 18, where unstable_changedBits is removed. (confidence high, judge supported)
  - react_changelog: "Remove unsupported unstable_changedBits API."
- **[required] api_usage** `present` `"unstable_changedBits"`: The application or its dependencies use the unstable_changedBits API. (confidence medium, judge supported)
  - react_changelog: "Remove unsupported unstable_changedBits API."
  - ⚠ The text does not say where unstable_changedBits was used, for example createContext or an internal API, and does not name a replacement.

Actions:
- Search the application code and third-party dependencies for unstable_changedBits and remove its usage before upgrading to React 18.
- Update or replace any dependency that relies on unstable_changedBits.

### TypeScript children prop must be declared explicitly in props

`react_0cdcfd833f` · medium · confidence high · introduced in 18 · fires at upgrade

With the updated @types/react and @types/react-dom for React 18, the children prop is no longer implicitly included and must be listed explicitly when defining props. TypeScript projects will see type-check errors where components receive children without declaring it.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React 18, where the TypeScript definitions change so children must be explicit. (confidence high, judge supported)
  - react_upgrade_guide: "The most notable change is that the children prop now needs to be listed explicitly when defining props"
- **[required] dependency** `present` `"@types/react"`: The project uses TypeScript and depends on @types/react and @types/react-dom, which must be updated to the latest versions. (confidence high, judge supported)
  - react_upgrade_guide: "If your project uses TypeScript, you will need to update your @types/react and @types/react-dom dependencies to the latest versions."
- **[uncertain] api_usage** `absent` `"children?: React.ReactNode"`: Component props interfaces/types do not list children explicitly but components receive children. (confidence low, judge not_supported)
  - react_upgrade_guide: "children?: React.ReactNode;"
  - ⚠ The text does not state exactly which prop definitions (e.g., those using React.FC) are affected.
  - ⚠ Judge: evidence does not support this claim. The quote is only a code snippet showing children?: React.ReactNode declared in a props interface; it does not state that props types lacking an explicit children declaration while components receive children are affected, nor any consequence of that situation.

Actions:
- Update @types/react and @types/react-dom to the latest versions.
- Add children?: React.ReactNode to props definitions of components that accept children.
- Use the automated migration script to port application code to the new typings.
- Consult the React 18 typings pull request for the full list of type-only changes.

### act throws when used in production

`react_1174c2e1c2` · medium · confidence medium · introduced in 18 · fires at first_use

In React 18, calling act (from React / React DOM Test Utils) in a production build now throws, whereas it did not before. Code or test setups that run act against production builds will break.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses release 18, where act began throwing in production. (confidence high, judge supported)
  - react_changelog: "Throw when act is used in production."
  - react_changelog: "Expand act warning to cover all APIs that might schedule React work."
  - react_changelog: "Make act batch updates."
- **[required] api_usage** `present` `"act"`: The application or its tests call act. (confidence high, judge supported)
  - react_changelog: "Throw when act is used in production."
- **[required] runtime** `present` `"production"`: act is executed in a production build, or the production-mode React bundle is used where act runs. (confidence medium, judge supported)
  - react_changelog: "Throw when act is used in production."
  - ⚠ The text does not say how production is detected (for example NODE_ENV), nor which act entry points are affected.
- **[required] test_coverage** `present` `"act"`: The application's tests use act, or run React work in a way that the act warning covers. (confidence medium, judge supported)
  - react_changelog: "Expand act warning to cover all APIs that might schedule React work."
  - react_changelog: "Make act batch updates."
  - ⚠ The text does not list which APIs are now covered by the expanded warning.
  - ⚠ The text does not state the exact condition that triggers the warning.
  - ⚠ The text does not describe how the previous unbatched behavior differs or what specific test outcomes change.
- **[optional] configuration** `present` `"IS_REACT_ACT_ENVIRONMENT"`: The test setup sets global.IS_REACT_ACT_ENVIRONMENT, which can disable spurious act warnings. (confidence medium, judge supported)
  - react_changelog: "Support disabling spurious act warnings with global.IS_REACT_ACT_ENVIRONMENT."
  - ⚠ The text does not state the default value or the semantics of the flag for the expanded warning.

Actions:
- Run tests that call act against development builds rather than production builds.
- Remove act calls from production code paths.
- Run the test suite on React 18 and check for new act warnings.
- Wrap the test code that triggers React work in act where the new warnings appear.
- If a warning is spurious, consider global.IS_REACT_ACT_ENVIRONMENT, which the parent context says can disable spurious act warnings.
- Run the existing test suite that uses act after upgrading to React 18 and review failures caused by batched updates.
- Adjust test assertions that depend on intermediate renders or unbatched update ordering inside act.

### Automatic batching of state updates outside React event handlers

`react_362d1d0639` · medium · confidence high · introduced in 18 · fires at upgrade

Starting in React 18 with createRoot, all state updates are batched regardless of origin (timeouts, promises, native event handlers). Previously only updates inside React event handlers were batched. The docs call this a breaking change. Code that depended on a separate re-render per update outside React event handlers will see different render behavior; flushSync is the documented opt-out.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React 18, where automatic batching is introduced and described as a breaking change. (confidence high, judge partially_supported)
  - react_upgrade_guide: "This is a breaking change, but we expect this to result in less work rendering"
  - react_changelog: "This release introduces a performance improvement that changes to the way React batches updates to do more batching automatically."
- **[required] api_usage** `present` `"createRoot"`: The application renders with createRoot, which is what enables automatic batching in React 18. (confidence high, judge supported)
  - react_upgrade_guide: "Starting in React 18 with createRoot, all updates will be automatically batched"
  - react_changelog: "In the rare case that you need to opt out, wrap the state update in flushSync."
  - ⚠ The text does not say whether apps still using the legacy root API (ReactDOM.render) get automatic batching.
- **[required] behavior** `present` `"state updates in setTimeout, promises or native event handlers"`: The application performs state updates inside promises, setTimeout, native event handlers or other non-React events, which were previously not batched. (confidence high, judge supported)
  - react_upgrade_guide: "Updates inside of promises, setTimeout, native event handlers, or any other event were not batched in React by default"
  - react_changelog: "changes to the way React batches updates to do more batching automatically"
  - ⚠ The text does not state which specific application behaviors break, only that this is a breaking change.
  - ⚠ The text does not state which update contexts (e.g. timeouts, promises, native event handlers) were previously unbatched.
  - ⚠ The text calls the need to opt out rare, so impact is limited to code sensitive to render timing.
- **[uncertain] behavior** `present` `"flushSync"`: The application relies on the DOM or render being updated between consecutive state updates outside React events, which would need flushSync to preserve the previous behavior. (confidence low, judge partially_supported)
  - react_upgrade_guide: "To opt-out of automatic batching, you can use flushSync"
  - ⚠ The text does not state what specific application dependency on unbatched rendering is affected.

Actions:
- Audit state updates inside setTimeout, promises and native event handlers for reliance on a separate render per update.
- Where a separate render per update is required, wrap each update in flushSync imported from 'react-dom' to opt out of batching.
- Test affected components after switching to createRoot.
- Review code that depends on the render count or timing following state updates and verify behavior under React 18.
- Where an update must not be batched, wrap that state update in flushSync.

### ReactDOM.hydrate deprecated: warns and runs app in React 17 mode

`react_385fe7836e` · medium · confidence high · introduced in 18 · fires at upgrade

ReactDOM.hydrate is deprecated in React 18. Using it logs a warning and runs the app in React 17 mode, so React 18 concurrent features and behaviors are not enabled for that root until the app migrates.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React release 18, where ReactDOM.hydrate is deprecated. (confidence high, judge supported)
  - react_changelog: "ReactDOM.hydrate has been deprecated."
- **[required] api_usage** `present` `"ReactDOM.hydrate"`: The application calls ReactDOM.hydrate from react-dom to hydrate server-rendered markup. (confidence high, judge supported)
  - react_changelog: "ReactDOM.hydrate has been deprecated. Using it will warn and run your app in React 17 mode."

Actions:
- Find all usages of ReactDOM.hydrate in the codebase.
- The text does not name the replacement API; consult React 18 documentation for the migration path before removing the warning and the React 17 mode behavior.

### Suspense trees discard incomplete new trees and retry rendering from scratch

`react_44cfb7b19d` · medium · confidence medium · introduced in 18 · fires at upgrade

In React 18, if a component suspends before it is fully added to the tree, React no longer adds the tree in an incomplete state or fires its effects. It throws away the new tree, waits for the asynchronous operation to finish, and retries rendering from scratch, concurrently and without blocking the browser. Code that relied on the previous behavior of partially added trees or early effects may behave differently.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React 18, where Suspense trees become always consistent. (confidence high, judge supported)
  - react_changelog: "Suspense trees are always consistent"
  - react_changelog: "Make Suspense remount layout effects when content reappears."
- **[required] api_usage** `present` `"Suspense"`: The application has components that can suspend before they are fully added to the tree, for example inside Suspense boundaries. (confidence medium, judge supported)
  - react_changelog: "If a component suspends before it's fully added to the tree"
  - react_changelog: "Make Suspense remount layout effects when content reappears."
  - ⚠ The text does not list which APIs cause a component to suspend.
  - ⚠ The text does not specify whether class component lifecycles (componentDidMount/componentWillUnmount) are also affected, nor what side effects would break.
- **[optional] behavior** `unknown` `"render-time side effects or effects reliant on pre-suspension execution"`: Component render logic or effects depend on a partially added tree or on effects firing before the suspended content is ready. Such code would now see the tree discarded and rendering retried from scratch. (confidence low, judge partially_supported)
  - react_changelog: "React will throw away the new tree completely, wait for the asynchronous operation to finish, and then retry rendering again from scratch."
  - ⚠ The text does not state which application patterns break because of this behavior.

Actions:
- Review components rendered inside Suspense boundaries for logic that assumes a partially added tree or that effects fire before the component suspends.
- Test suspending components after the upgrade to confirm they behave correctly when React discards the tree and retries rendering from scratch.
- Audit components rendered inside Suspense boundaries that use useLayoutEffect and ensure their setup and cleanup are idempotent and safe to re-run when suspended content reappears.
- Test Suspense fallback transitions to verify layout effects re-running does not cause duplicate side effects.

### renderToStaticMarkup suspending behavior change

`react_479331dfb5` · medium · confidence medium · introduced in 18 · fires at first_use

In React 18, renderToStaticMarkup no longer errors when a component suspends on the server. It emits the fallback HTML for the closest <Suspense> boundary and retries rendering on the client. Code that relied on the earlier error, or that expects complete static markup for suspending content, will see different output.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React release 18, where renderToStaticMarkup no longer errors when suspending on the server. (confidence high, judge supported)
  - react_changelog: "renderToStaticMarkup: Will no longer error when suspending on the server."
  - react_changelog: "Will no longer error when suspending on the server."
  - react_upgrade_guide: "renderToStaticMarkup: Will no longer error when suspending on the server."
- **[required] api_usage** `present` `"renderToStaticMarkup"`: The application calls renderToStaticMarkup. (confidence high, judge supported)
  - react_changelog: "renderToStaticMarkup: Will no longer error when suspending on the server."
  - react_upgrade_guide: "renderToStaticMarkup: Will no longer error when suspending on the server."
- **[required] behavior** `present` `"Suspense"`: Components rendered by renderToStaticMarkup can suspend, so a <Suspense> boundary fallback is emitted. (confidence medium, judge partially_supported)
  - react_changelog: "it will emit the fallback HTML for the closest <Suspense> boundary and retry rendering on the client."
  - react_changelog: "it will emit the fallback HTML for the closest <Suspense> boundary and retry rendering on the client"
  - react_upgrade_guide: "it will emit the fallback HTML for the closest <Suspense> boundary"
  - ⚠ The text does not say what causes suspension.
  - ⚠ The text does not say what happens when a suspending component has no enclosing <Suspense> boundary.
  - ⚠ The text does not state what happens when a component suspends with no enclosing <Suspense> boundary.

Actions:
- Find all renderToStaticMarkup calls and check whether any rendered tree can suspend.
- Verify that fallback HTML for the closest <Suspense> boundary is acceptable for that output, for example static emails or generated pages that are not hydrated on the client.
- Remove any code or tests that depend on renderToStaticMarkup throwing an error when suspending.
- Search for renderToStaticMarkup usages and check whether any rendered tree can suspend.
- Verify that the fallback HTML now emitted for the closest <Suspense> boundary is acceptable where output is consumed without client-side hydration or retry.
- Update any tests or error handling that expected renderToStaticMarkup to throw when suspending.
- Search for renderToStaticMarkup usage where rendered components may suspend (e.g. under <Suspense>).
- Review tests or code that relied on the previous suspend error, and verify that the fallback HTML output is acceptable.
- Add or update tests for static markup output of trees containing <Suspense> boundaries.

### ReactDOM.render replaced by createRoot

`react_4a4e72c4eb` · medium · confidence medium · introduced in 18 · fires at upgrade

In React 18, ReactDOM.render is no longer supported and logs a console warning. Until the app switches to createRoot from react-dom/client, it behaves as if running React 17, so the new root API and concurrent renderer are not enabled. The app must migrate to createRoot and root.render to use the new root API.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React 18, where ReactDOM.render is no longer supported. (confidence high, judge partially_supported)
  - react_upgrade_guide: "ReactDOM.render is no longer supported in React 18. Use createRoot instead."
  - react_changelog: "ReactDOM.render has been deprecated."
- **[required] api_usage** `present` `"ReactDOM.render"`: The application calls render from react-dom (ReactDOM.render) to mount its root. (confidence medium, judge partially_supported)
  - react_upgrade_guide: "import { render } from 'react-dom'; const container = document.getElementById('app'); render(<App tab="home" />, container);"
  - react_changelog: "Using it will warn and run your app in React 17 mode."
  - ⚠ The text does not name the replacement API.
- **[uncertain] api_usage** `present` `"createRoot"`: The application has already switched to createRoot from react-dom/client. (confidence low, judge not_supported)
  - react_upgrade_guide: "Until you switch to the new API, your app will behave as if it's running React 17."
  - ⚠ Judge: evidence does not support this claim. The quote only says that until you switch to the new API the app behaves like React 17; it says nothing about createRoot from react-dom/client being adopted, nor does it describe the state of an application that has already switched.

Actions:
- Replace import { render } from 'react-dom' with import { createRoot } from 'react-dom/client'.
- Create the root with const root = createRoot(container) (createRoot(container!) if you use TypeScript) and call root.render(<App tab="home" />).
- Note that the new root API also enables the new concurrent renderer, which allows you to opt into concurrent features.
- Find all ReactDOM.render calls and migrate them away from the deprecated API so the app runs in React 18 mode instead of React 17 mode.
- Check console output for the deprecation warning after upgrading.

### Consistent useEffect timing: synchronous effect flush on discrete input events

`react_4aaaf16b0e` · medium · confidence medium · introduced in 18 · fires at upgrade

In React 18, effect functions are always synchronously flushed if the update was triggered during a discrete user input event such as a click or keydown. Previously the timing was not always predictable or consistent, so code that relied on the earlier effect timing after such events may behave differently.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React 18, which introduced the consistent useEffect timing change. (confidence high, judge supported)
  - react_changelog: "Consistent useEffect timing: React now always synchronously flushes effect functions if the update was triggered during a discrete user input event"
  - react_changelog: "Flush useEffect resulting from discrete events like clicks synchronously."
- **[required] api_usage** `present` `"useEffect"`: The application uses useEffect with effects that run as a result of updates triggered during discrete user input events (e.g. click, keydown). (confidence medium, judge supported)
  - react_changelog: "React now always synchronously flushes effect functions if the update was triggered during a discrete user input event such as a click or a keydown event"
  - react_changelog: "Flush useEffect resulting from discrete events like clicks synchronously."
  - ⚠ The text does not state which specific timing-dependent behaviors would break, or what other discrete events besides clicks are covered.
- **[uncertain] behavior** `unknown` `"effect timing dependence"`: The application's effects depend on the previous, inconsistent timing of effect execution after user input events. (confidence low, judge partially_supported)
  - react_changelog: "Previously, the behavior wasn't always predictable or consistent."
  - react_changelog: "Flush useEffect resulting from discrete events like clicks synchronously."
  - ⚠ The text does not state which specific effect patterns break or what the old timing was.
  - ⚠ The text does not describe the previous timing or specific failure modes; this is an inference.

Actions:
- Review useEffect hooks triggered by state updates in discrete input event handlers (click, keydown) for dependence on previous effect timing.
- Test interactive flows after upgrading to confirm effects behave correctly with synchronous flushing.
- Review useEffect hooks triggered by click or other discrete event handlers for dependence on asynchronous timing.
- Run tests covering interactions that trigger effects and verify they pass under React 18.

### render callback (third argument) removed with createRoot migration

`react_5245677ce9` · medium · confidence medium · introduced in 18 · fires at upgrade

The callback argument to render has been removed in React 18's new root API because it usually does not behave as expected with Suspense. root.render does not accept a callback. Code that passes a callback to render and migrates to createRoot must be reworked, for example by logging from useEffect in a wrapper component. The text states there is no one-to-one replacement.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React 18, where the render callback was removed. (confidence high, judge supported)
  - react_upgrade_guide: "We've also removed the callback from render, since it usually does not have the expected result when using Suspense"
- **[required] api_usage** `present` `"render(<App />, container, callback)"`: The application calls render with a callback as the third argument. (confidence medium, judge partially_supported)
  - react_upgrade_guide: "render(<App tab="home" />, container, () => { console.log('rendered'); });"
  - ⚠ The text does not state exactly what happens to a callback passed to the legacy ReactDOM.render before the app switches to createRoot, only that the app behaves as if running React 17 until it switches.
- **[uncertain] api_usage** `present` `"createRoot"`: The application migrates from render to createRoot, which has no callback parameter. (confidence low, judge partially_supported)
  - react_upgrade_guide: "const root = createRoot(container);"
  - react_upgrade_guide: "Until you switch to the new API, your app will behave as if it's running React 17."
  - ⚠ The text does not explicitly say that the removed callback applies only after switching to createRoot.

Actions:
- Replace render(<App />, container, callback) with createRoot(container).render(<App />).
- Move the callback logic into a component using useEffect, for example a wrapper component such as AppWithCallbackAfterRender that logs in useEffect and returns <App />.
- Note that there is no one-to-one replacement for the old render callback API and the right approach depends on the use case; consult the working group post on Replacing render with createRoot.

### Suspense fallback={undefined} no longer ignored

`react_60fe36b771` · medium · confidence medium · introduced in 18 · fires at first_use

In React 18, Suspense with fallback={undefined} now behaves the same as fallback={null} and is no longer ignored. Apps that pass an undefined fallback (explicitly or via an undefined variable/prop) may see different loading behavior after upgrade.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses release 18, where Suspense fallback={undefined} behavior changed. (confidence high, judge supported)
  - react_changelog: "Suspense fallback={undefined} now behaves the same as null and isn't ignored."
- **[required] api_usage** `present` `"Suspense fallback={undefined}"`: The application renders Suspense with a fallback prop that is undefined (explicitly or via an undefined value). (confidence medium, judge supported)
  - react_changelog: "Suspense fallback={undefined} now behaves the same as null and isn't ignored."
  - ⚠ The text does not describe the exact previous behavior beyond saying undefined was ignored, nor the visible effect of the new null-like behavior.

Actions:
- Search for Suspense boundaries with fallback={undefined} or fallback props that can evaluate to undefined.
- Verify loading behavior of these boundaries in React 18, and set an explicit fallback (or null) where intended.

### renderToString suspending behavior change

`react_6c336940af` · medium · confidence medium · introduced in 18 · fires at first_use

In React 18, renderToString no longer errors when a component suspends on the server. It emits the fallback HTML for the closest <Suspense> boundary and retries rendering the same content on the client. Apps that relied on the previous error, or that expect fully rendered server HTML for suspending content, will see different output. The changelog still recommends switching to a streaming API such as renderToPipeableStream or renderToReadableStream.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React release 18, where renderToString no longer errors when suspending on the server. (confidence high, judge supported)
  - react_changelog: "Will no longer error when suspending on the server."
- **[required] api_usage** `present` `"renderToString"`: The application calls renderToString for server-side rendering. (confidence high, judge supported)
  - react_changelog: "renderToString: Will no longer error when suspending on the server."
- **[required] behavior** `present` `"Suspense"`: Components rendered by renderToString can suspend, for example via <Suspense> boundaries, lazy loading or data fetching. (confidence medium, judge partially_supported)
  - react_changelog: "emit the fallback HTML for the closest <Suspense> boundary"
  - ⚠ The text does not say which mechanisms (lazy, data fetching) cause suspension.
- **[disqualifying] api_usage** `present` `"renderToPipeableStream"`: The application already uses a streaming API such as renderToPipeableStream or renderToReadableStream instead of renderToString. (confidence medium, judge supported)
  - react_changelog: "streaming API like renderToPipeableStream or renderToReadableStream"
  - ⚠ The text does not state how the streaming APIs behave on suspend; only that they are recommended.

Actions:
- Find all renderToString calls and check whether any rendered tree can suspend.
- Verify that fallback HTML emitted for the closest <Suspense> boundary followed by client-side retry is acceptable for those routes.
- Remove any code or tests that depend on renderToString throwing an error when suspending.
- Consider switching to renderToPipeableStream or renderToReadableStream, as the changelog recommends.

### Strict Mode dev-only simulated unmount/remount breaks effects that assume single mount/destroy

`react_71acd3a7ef` · medium · confidence medium · introduced in 18 · fires at upgrade

React 18 Strict Mode adds a development-only check that automatically unmounts and remounts every component when it first mounts, restoring previous state on the second mount. Effects (and layout effects) that assume they are only mounted or destroyed once may behave incorrectly because setup and cleanup now run multiple times in development.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React 18, which introduces the new development-only Strict Mode check. (confidence high, judge supported)
  - react_upgrade_guide: "React 18 introduces a new development-only check to Strict Mode"
  - react_changelog: "React 18 introduces a new development-only check to Strict Mode"
  - react_changelog: "In React 17, we've suppressed console logs for one of the two renders"
  - react_changelog: "Make <StrictMode> re-run effects to check for restorable state."
  - react_upgrade_guide: "Strict Mode has gotten stricter in React 18"
- **[required] api_usage** `present` `"StrictMode"`: The application renders components within Strict Mode. (confidence high, judge supported)
  - react_upgrade_guide: "React 18 introduces a new development-only check to Strict Mode"
  - react_upgrade_guide: "With Strict Mode in React 18, React will simulate unmounting and remounting the component in development mode"
  - react_changelog: "React will automatically unmount and remount every component, whenever a component mounts for the first time"
  - react_changelog: "When you use Strict Mode, React renders each component twice to help you find unexpected side effects."
  - react_changelog: "Make <StrictMode> re-run effects to check for restorable state."
  - react_upgrade_guide: "check whether it's wrapped in <StrictMode>"
  - ⚠ The text does not state whether the re-run applies only in development builds.
- **[required] behavior** `present` `"useEffect or useLayoutEffect assuming a single mount/destroy"`: The application has effects (or layout effects) that assume they are only mounted or destroyed once. (confidence medium, judge supported)
  - react_upgrade_guide: "some effects assume they are only mounted or destroyed once"
  - react_changelog: "until you can fix the components to be resilient to remounting with existing state"
  - react_changelog: "we've suppressed console logs for one of the two renders"
  - react_changelog: "re-run effects to check for restorable state"
  - react_upgrade_guide: "not all your components may be resilient to the new checks it adds in development mode"
  - ⚠ The text does not name the hooks (useEffect/useLayoutEffect) explicitly; it refers to 'Effect effects' and 'Layout effects'.
  - ⚠ The text does not state how to identify which effects are non-resilient.
  - ⚠ The text does not say which kinds of components or effects are not resilient to remounting.
  - ⚠ The text does not say whether tests or tooling depend on the number of console log calls.
  - ⚠ The text does not describe which effects fail or what the exact impact is.
  - ⚠ The text does not state which specific checks were added or which components fail them.
- **[required] runtime** `equals` `"development mode"`: The effects are exercised in a development build, since the check is development-only. (confidence high, judge supported)
  - react_upgrade_guide: "React 18 introduces a new development-only check to Strict Mode"
  - react_changelog: "React 18 introduces a new development-only check to Strict Mode"
- **[disqualifying] behavior** `absent` `"effects that break when mounted and destroyed multiple times"`: Most effects work without any changes, so effects that are resilient to being mounted and destroyed multiple times are unaffected. (confidence medium, judge partially_supported)
  - react_upgrade_guide: "Most effects will work without any changes"

Actions:
- Review effects and layout effects under Strict Mode in development to find ones that assume a single mount or destroy.
- Make effects resilient to being mounted and destroyed multiple times (ensure setup is paired with proper cleanup).
- See the Working Group posts 'Adding Reusable State to StrictMode' and 'How to support Reusable State in Effects' for guidance.
- Review components rendered under Strict Mode and make effects resilient to being mounted and destroyed multiple times.
- Ensure effects have proper cleanup for their setup code so setup, cleanup, setup works correctly.
- Consult the referenced Working Group posts 'How to support Reusable State in Effects' for guidance.
- Remove Strict Mode until the components can be fixed to be resilient to remounting with existing state.
- Fix components so they tolerate being unmounted and remounted with their previous state restored.
- Expect duplicate console logs from Strict Mode renders after upgrading.
- Install React DevTools to see the second render's logs in grey.
- Enable the React DevTools option (off by default) to suppress the second render's logs completely.
- Review effects in components wrapped in <StrictMode> to ensure they tolerate being re-run.
- Test the application under <StrictMode> after upgrading to React 18.
- If the app does not work after upgrading, check whether it is wrapped in <StrictMode>.
- If removing Strict Mode fixes the app, remove it during the upgrade.
- Fix the issues Strict Mode points out, then add it back at the top or for a part of the tree.

### Layout effects cleaned up and re-created when Suspense boundary re-suspends

`react_a6a01d8772` · medium · confidence low · introduced in 18 · fires at first_use

In React 18, when a tree re-suspends and reverts to a fallback, layout effects inside the boundary are cleaned up and re-created when the content is shown again. Components using layout effects inside Suspense boundaries may see cleanup and setup run additional times, which could break code that assumed layout effects run only on mount and unmount.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React release 18, where this layout effect behavior change was introduced. (confidence high, judge supported)
  - react_changelog: "React will now clean up layout effects, and then re-create them when the content inside the boundary is shown again."
- **[required] api_usage** `present` `"Suspense"`: The application uses Suspense boundaries whose content can re-suspend and revert to a fallback. (confidence high, judge supported)
  - react_changelog: "When a tree re-suspends and reverts to a fallback"
- **[required] api_usage** `present` `"useLayoutEffect"`: Components inside Suspense boundaries use layout effects (useLayoutEffect, or class componentDidMount/componentDidUpdate/componentWillUnmount lifecycles that run in the layout phase), or libraries that do so, for example to measure layout. (confidence low, judge partially_supported)
  - react_changelog: "React will now clean up layout effects"
  - react_changelog: "correctly measuring layout when used with Suspense"
  - ⚠ The text does not name the useLayoutEffect hook or class lifecycles explicitly; it refers only to 'layout effects'.

Actions:
- Audit layout effects used inside Suspense boundaries, including those in third-party component libraries, and make sure their setup and cleanup are safe to run repeatedly.
- Test flows where a Suspense boundary re-suspends and shows its fallback again to confirm layout measurement and side effects behave correctly.

### Stricter hydration errors for text content mismatches

`react_d1fa9e779a` · medium · confidence low · introduced in 18 · fires at first_use

Hydration mismatches due to missing or extra text content are now errors rather than warnings. React no longer patches individual nodes and reverts to client rendering up to the closest <Suspense> boundary, so apps with server/client text mismatches will see client re-rendering and error reporting after upgrading.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React release 18, which introduces stricter hydration errors. (confidence high, judge supported)
  - react_changelog: "Hydration mismatches due to missing or extra text content are now treated like errors instead of warnings."
- **[required] api_usage** `present` `"hydrateRoot"`: The application hydrates server-rendered markup on the client (server-rendered HTML hydrated by React). (confidence low, judge supported)
  - react_changelog: "Hydration mismatches due to missing or extra text content are now treated like errors instead of warnings."
  - ⚠ The text does not name the specific hydration API (e.g. ReactDOM.hydrate or hydrateRoot).
- **[required] behavior** `present` `"hydration text content mismatch"`: The server-rendered markup and client render differ in text content (missing or extra text), for example due to non-deterministic values or differing server/client data. (confidence medium, judge partially_supported)
  - react_changelog: "Hydration mismatches due to missing or extra text content"
- **[optional] api_usage** `present` `"Suspense"`: A <Suspense> boundary enclosing the mismatched content limits how much of the tree reverts to client rendering. (confidence medium, judge supported)
  - react_changelog: "will revert to client rendering up to the closest <Suspense> boundary in the tree"
  - ⚠ The text does not state what happens when no <Suspense> boundary exists in the tree.

Actions:
- Fix server/client text content mismatches so the hydrated tree matches the server markup.
- Review console hydration errors after upgrading and address any missing or extra text content.
- Consider placing <Suspense> boundaries to limit the scope of client-render fallback.

### Automatic batching changes render timing for updates outside React events

`react_e56a0f9df4` · medium · confidence medium · introduced in 18 · fires at upgrade

Before React 18, state updates inside promises, setTimeout, native event handlers or other non-React events each caused a separate re-render. In React 18 with createRoot, they are batched into a single re-render. The text calls this a breaking change. Code that relies on the DOM or state being updated between consecutive setState calls may behave differently. flushSync opts out of batching.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React 18, which introduces automatic batching of all updates as a breaking change. (confidence high, judge supported)
  - react_upgrade_guide: "React 18 adds out-of-the-box performance improvements by doing more batching by default."
  - react_upgrade_guide: "This is a breaking change, but we expect this to result in less work rendering"
  - react_upgrade_guide: "Starting in React 18 with createRoot, all updates will be automatically batched, no matter where they originate from."
- **[required] api_usage** `present` `"createRoot"`: The application renders with createRoot, which is where the text says all updates are automatically batched. (confidence medium, judge supported)
  - react_upgrade_guide: "Starting in React 18 with createRoot, all updates will be automatically batched, no matter where they originate from."
  - react_upgrade_guide: "Starting in React 18 with createRoot, all updates will be automatically batched"
  - react_upgrade_guide: "To opt-out of automatic batching, you can use flushSync"
  - ⚠ The text does not say whether apps still using the legacy ReactDOM.render root get the new batching.
  - ⚠ The text does not state whether automatic batching applies to apps still using the legacy ReactDOM.render root.
- **[required] behavior** `present` `"setState calls inside setTimeout, promises or native event handlers"`: The application performs state updates inside setTimeout, promises, native event handlers or other non-React events, which were previously not batched. (confidence medium, judge supported)
  - react_upgrade_guide: "Updates inside of promises, setTimeout, native event handlers, or any other event were not batched in React by default"
  - react_upgrade_guide: "updates inside of timeouts, promises, native event handlers or any other event will batch the same way as updates inside of React events"
  - ⚠ The text does not say what specific code patterns break, only that this is a breaking change.
- **[uncertain] behavior** `unknown` `"code that reads state or DOM between consecutive state updates"`: The application depends on a re-render or DOM update occurring between consecutive state updates outside React events. (confidence low, judge partially_supported)
  - react_upgrade_guide: "React will render twice, once for each state update (no batching)"
  - ⚠ The text does not state which application patterns break, only that batching changes the number of renders.
- **[disqualifying] api_usage** `present` `"flushSync"`: The application already wraps updates in flushSync, which opts out of automatic batching. (confidence high, judge supported)
  - react_upgrade_guide: "To opt-out of automatic batching, you can use flushSync"

Actions:
- Review state updates made inside setTimeout, promises and native event handlers for reliance on one render per update.
- Wrap updates that must be applied to the DOM immediately in flushSync imported from 'react-dom' to opt out of batching.
- Test components that perform multiple state updates in async callbacks after switching to createRoot.
- Review state updates inside setTimeout, promises, and native event handlers for reliance on a re-render between consecutive updates.
- Where unbatched behavior is required, wrap individual updates in flushSync imported from 'react-dom'.
- Test components under createRoot to verify render behavior.

### unmountComponentAtNode replaced by root.unmount

`react_7123c14ec9` · low · confidence high · introduced in 18 · fires at upgrade

React 18 changes unmountComponentAtNode(container) to root.unmount() as part of the new root API. Code that unmounts a root with unmountComponentAtNode needs migration to root.unmount() on the root returned by createRoot. Until the app switches to the new API, it behaves as if it is running React 17.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade to React 18 introduces the change from unmountComponentAtNode to root.unmount. (confidence high, judge supported)
  - react_upgrade_guide: "We've also changed unmountComponentAtNode to root.unmount"
- **[required] api_usage** `present` `"unmountComponentAtNode"`: The application calls unmountComponentAtNode to unmount a rendered root. (confidence high, judge supported)
  - react_upgrade_guide: "// Before unmountComponentAtNode(container); // After root.unmount();"
- **[uncertain] api_usage** `present` `"createRoot"`: The application has already switched to the new root API (createRoot) from ReactDOM.render. Until then it behaves as if it is running React 17. (confidence low, judge partially_supported)
  - react_upgrade_guide: "Until you switch to the new API, your app will behave as if it's running React 17."
  - ⚠ The text does not state whether unmountComponentAtNode still works, warns, or fails in React 18 once a root is created with createRoot.

Actions:
- When migrating to createRoot, keep the root returned by createRoot(container) and call root.unmount() instead of unmountComponentAtNode(container).
- Search the codebase for unmountComponentAtNode usages and update them together with the ReactDOM.render to createRoot migration.

### act warnings opt-in for unit tests

`react_bf8746ac22` · low · confidence medium · introduced in 18 · fires at upgrade

In React 18, act warnings in tests are opt-in rather than on by default. Unit tests that relied on act warnings will stop showing them unless the opt-in mechanism is enabled. End-to-end tests do not need them.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses release 18, where act warnings in tests became opt-in. (confidence high, judge supported)
  - react_changelog: "In tests, act warnings are now opt-in"
- **[required] test_coverage** `present` `"act"`: The project has unit tests that use act and rely on act warnings to catch problems. (confidence medium, judge partially_supported)
  - react_changelog: "We've introduced an opt-in mechanism so you can enable them only for unit tests where they are useful and beneficial."
  - ⚠ The text does not name the opt-in mechanism or say how to enable it.
- **[disqualifying] test_coverage** `present` `"end-to-end tests only"`: If the project only runs end-to-end tests, act warnings are unnecessary and the change has no impact. (confidence medium, judge partially_supported)
  - react_changelog: "If you're running end-to-end tests, the act warnings are unnecessary."

Actions:
- Check whether unit tests depend on act warnings.
- Enable the act-warning opt-in mechanism for unit test environments where you want those warnings.
- Leave act warnings off for end-to-end tests.

### Function and symbol values on custom elements ignored during server rendering

`react_d7f515143b` · low · confidence medium · introduced in 18 · fires at upgrade

In React 18, server rendering ignores function and symbol values inside custom elements. An app that passes function or symbol values as props or attributes to custom elements and renders them on the server may see those values omitted from the server output.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React 18, which introduced this server rendering change. (confidence high, judge supported)
  - react_changelog: "Ignore function and symbol values inside custom elements on the server."
- **[required] api_usage** `present` `"custom elements with function or symbol values rendered on the server"`: The application renders custom elements on the server and passes function or symbol values to them. (confidence medium, judge supported)
  - react_changelog: "Ignore function and symbol values inside custom elements on the server."
  - ⚠ The text does not say whether these values were previously rendered or how they were serialized before 18.
- **[required] deployment** `present` `"react-dom/server"`: The application uses server-side rendering through React DOM Server. (confidence medium, judge partially_supported)
  - react_changelog: "Ignore function and symbol values inside custom elements on the server."

Actions:
- Search server-rendered components for custom elements (tags with a hyphen) that receive function or symbol values as props or attributes.
- Verify server-rendered output for those elements after upgrading to 18 and confirm the app does not depend on those values being present.

### Test environment missing IS_REACT_ACT_ENVIRONMENT flag after switching tests to createRoot

`react_dc5cc879a8` · low · confidence medium · introduced in 18 · fires at first_use

After updating tests to use createRoot, React logs a console warning that the testing environment is not configured to support act(...) unless globalThis.IS_REACT_ACT_ENVIRONMENT is set to true in the test setup file. The text describes this as a warning only.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React 18, where updating tests to createRoot triggers the act environment warning. (confidence medium, judge partially_supported)
  - react_upgrade_guide: "When you first update your tests to use createRoot, you may see this warning in your test console"
- **[required] api_usage** `present` `"createRoot"`: Tests have been updated to use createRoot. (confidence medium, judge partially_supported)
  - react_upgrade_guide: "When you first update your tests to use createRoot"
- **[required] configuration** `absent` `"globalThis.IS_REACT_ACT_ENVIRONMENT = true"`: The test setup does not set globalThis.IS_REACT_ACT_ENVIRONMENT to true. (confidence medium, judge partially_supported)
  - react_upgrade_guide: "set globalThis.IS_REACT_ACT_ENVIRONMENT to true before running your test"
- **[uncertain] dependency** `unknown` `"testing library without built-in React 18 support"`: Tests use a testing library that does not configure the flag automatically. (confidence low, judge partially_supported)
  - react_upgrade_guide: "Eventually, we expect testing libraries will configure this for you automatically."
  - ⚠ The text only names the next version of React Testing Library as having built-in React 18 support; other libraries are not specified.

Actions:
- Set globalThis.IS_REACT_ACT_ENVIRONMENT = true in the test setup file.
- Optionally set the flag to false for end-to-end tests that simulate a full browser environment, where act is not needed.
- Consider a testing library version with built-in React 18 support, such as the next version of React Testing Library.

### package.json exports field restricts module resolution

`react_e87acb5981` · low · confidence high · introduced in 18 · fires at upgrade

React 18 adds an exports field to package.json. The text does not say what the field contains or what changes. An exports field generally limits which package paths can be imported, but the text does not state this, so any impact on deep or unlisted imports is uncertain.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses release 18, where the exports field was added to package.json. (confidence high, judge supported)
  - react_changelog: "Add exports field to package.json."
- **[uncertain] api_usage** `present` `"deep imports from react or react-dom packages"`: The application imports React package paths other than the package entry points, for example deep or internal file paths, that may be affected by the new exports field. (confidence low, judge partially_supported)
  - react_changelog: "Add exports field to package.json."
  - ⚠ The text does not say which paths the exports field exposes or restricts, or whether any previously importable path stops resolving.

Actions:
- Search the codebase for deep imports of react and react-dom subpaths and confirm each resolves after upgrading to 18.
- Run the build and tests after the upgrade to catch module resolution errors.

### Text mismatch now reverts to client render

`react_eb824a435b` · low · confidence medium · introduced in 18 · fires at first_use

React 18 reverts to client rendering when a text mismatch occurs. Server-rendered output with text content that differs from what the client renders will now behave differently than in 17. The text does not say what the behavior was before or what happens to the rendered output.

- **[required] version** `in_range` `{"current_version": "< 18", "target_version": ">= 18"}`: The upgrade crosses React 18.0.0, which introduced the revert to client render on text mismatch. (confidence high, judge supported)
  - react_changelog: "Revert to client render on text mismatch"
- **[required] behavior** `present` `"text mismatch"`: The application renders text content on the server that can mismatch the text rendered on the client. (confidence medium, judge partially_supported)
  - react_changelog: "Revert to client render on text mismatch"
  - ⚠ The text does not say what the two sides of the mismatch are (server HTML versus client render) or how a mismatch is detected.
- **[uncertain] api_usage** `present` `"react-dom/server"`: The application uses React DOM Server rendering. (confidence low, judge partially_supported)
  - react_changelog: "React DOM Server"
  - ⚠ The item does not name the specific server or hydration APIs affected.

Actions:
- Check server-rendered pages for text content that can differ between server and client output, and fix any mismatches.
- Test server-rendered pages under React 18 for unexpected client re-rendering.

## Review checklist

### Low confidence or disputed

- [ ] react_0cdcfd833f: TypeScript children prop must be declared explicitly in props
- [ ] react_4a4e72c4eb: ReactDOM.render replaced by createRoot
- [ ] react_a6a01d8772: Layout effects cleaned up and re-created when Suspense boundary re-suspends
- [ ] react_d1fa9e779a: Stricter hydration errors for text content mismatches

### Inferred conditions

- [ ] react_38bf30f056: The application does not already include a global polyfill for Promise, Symbol, and Object.assign.
- [ ] react_362d1d0639: The application relies on the DOM or render being updated between consecutive state updates outside React events, which would need flushSync to preserve the previous behavior.
- [ ] react_44cfb7b19d: Component render logic or effects depend on a partially added tree or on effects firing before the suspended content is ready. Such code would now see the tree discarded and rendering retried from scratch.
- [ ] react_4aaaf16b0e: The application's effects depend on the previous, inconsistent timing of effect execution after user input events.
- [ ] react_5245677ce9: The application migrates from render to createRoot, which has no callback parameter.
- [ ] react_71acd3a7ef: The application has effects (or layout effects) that assume they are only mounted or destroyed once.
- [ ] react_a6a01d8772: Components inside Suspense boundaries use layout effects (useLayoutEffect, or class componentDidMount/componentDidUpdate/componentWillUnmount lifecycles that run in the layout phase), or libraries that do so, for example to measure layout.
- [ ] react_d1fa9e779a: The application hydrates server-rendered markup on the client (server-rendered HTML hydrated by React).
- [ ] react_e56a0f9df4: The application depends on a re-render or DOM update occurring between consecutive state updates outside React events.
- [ ] react_e87acb5981: The application imports React package paths other than the package entry points, for example deep or internal file paths, that may be affected by the new exports field.
- [ ] react_eb824a435b: The application uses React DOM Server rendering.

### Source disagreements


### Open questions

- Ecosystem packages (@types/react, react-test-renderer users, Enzyme, React Native, state libraries) have their own React 18 support timelines that are not in React's docs.
- React 18.x minor release notes after 18.0.0 were not mined.
- [react_0cdcfd833f] Unconfirmed: Component props interfaces/types do not list children explicitly but components receive children. (The text does not state exactly which prop definitions (e.g., those using React.FC) are affected.)
- [react_362d1d0639] Unconfirmed: The application relies on the DOM or render being updated between consecutive state updates outside React events, which would need flushSync to preserve the previous behavior. (The text does not state what specific application dependency on unbatched rendering is affected.)
- [react_4a4e72c4eb] Unconfirmed: The application has already switched to createRoot from react-dom/client. (Judge: evidence does not support this claim. The quote only says that until you switch to the new API the app behaves like React 17; it says nothing about createRoot from react-dom/client being adopte)
- [react_4aaaf16b0e] Unconfirmed: The application's effects depend on the previous, inconsistent timing of effect execution after user input events. (The text does not state which specific effect patterns break or what the old timing was.)
- [react_5245677ce9] Unconfirmed: The application migrates from render to createRoot, which has no callback parameter. (The text does not explicitly say that the removed callback applies only after switching to createRoot.)
- [react_e56a0f9df4] Unconfirmed: The application depends on a re-render or DOM update occurring between consecutive state updates outside React events. (The text does not state which application patterns break, only that batching changes the number of renders.)
- [react_7123c14ec9] Unconfirmed: The application has already switched to the new root API (createRoot) from ReactDOM.render. Until then it behaves as if it is running React 17. (The text does not state whether unmountComponentAtNode still works, warns, or fails in React 18 once a root is created with createRoot.)
- [react_dc5cc879a8] Unconfirmed: Tests use a testing library that does not configure the flag automatically. (The text only names the next version of React Testing Library as having built-in React 18 support; other libraries are not specified.)
- [react_e87acb5981] Unconfirmed: The application imports React package paths other than the package entry points, for example deep or internal file paths, that may be affected by the new exports field. (The text does not say which paths the exports field exposes or restricts, or whether any previously importable path stops resolving.)
- [react_eb824a435b] Unconfirmed: The application uses React DOM Server rendering. (The item does not name the specific server or hydration APIs affected.)

## Context facts (not risks)

- (18) createRoot: New method to create a root to render or unmount. — _The item adds createRoot as a new API exported from react-dom/client. It says to use it instead of ReactDOM.render and that new React 18 features don't work without it. It does not say ReactDOM.render is removed or breaks, so existing code is not described as failing at 18. Adopting createRoot is opt-in and needed only to get the new features._
- (18) hydrateRoot: New method to hydrate a server rendered application. — _The item announces hydrateRoot as a new, additive API exported from react-dom/client. It tells users to use it instead of ReactDOM.hydrate to get React 18's new features, which makes adoption opt-in. The text does not say ReactDOM.hydrate is removed or stops working, or that existing server-rendered apps break at the upgrade. No action is required to stay functional at 18._
- (18) Assume Symbols are always available. — _The item only states that React 18 now assumes Symbols are always available. It names no removed API, changed behavior, or required action, and it does not say which environments are affected. Without further text, it describes an internal assumption that needs no action at 18._
- (18) Remove object-assign polyfill. — _The item only says the object-assign polyfill was removed. The text names no affected public API, no required user action and no breaking impact. It reads as an internal implementation change, so there is no application or deployment condition to check._
- (18) Allow components to render undefined. — _The item states that components are now allowed to render undefined. This relaxes a previous restriction and is additive; it describes no breakage, required migration, or operational risk at 18, and the text states no user action._
- (18) Consider all lazy() resolving to the same component equivalent. — _The item says lazy() components that resolve to the same component are now treated as equivalent. It gives no removed API, migration step, or breaking impact, and it does not say any app code must change. It is an informational reconciliation behavior change that needs no action at 18._
- (18) Don't patch console during first render. — _The item only states that React no longer patches console during first render. It does not say what breaks, what an app must change, or which behavior depends on the old patching. No user action is stated, so it is informational context only._
- (18) Use setImmediate when available over MessageChannel. — _The item says React's scheduler now uses setImmediate when available instead of MessageChannel. It is an internal scheduling change. The text names no removed API, config change, required migration, or breakage, so no user action is stated for the 17 -> 18 upgrade._
- (18) Fix useReducer observing incorrect props by removing the eager bailout mechanism. — _The item is a bug fix: useReducer no longer observes incorrect props because the eager bailout mechanism was removed. The text states no API removal, no required code or configuration change, and no breaking impact, so no action is required at 18._
- (18) Allow suspending outside a Suspense boundary. — _The item says suspending outside a Suspense boundary is now allowed. This is a permissive, additive change and the text states no breakage, removed API, or required migration, so no action is needed at 18._
- (18) Log a recoverable error whenever hydration fails. — _The item only states that React now logs a recoverable error whenever hydration fails. It describes added diagnostics rather than a removed API, a changed default that breaks code, or a required migration. The text states no user action and no breaking impact, so it needs no action at 18._
- (18) Fix aspectRatio style not being applied. — _This is a bug fix: the aspectRatio style was not being applied before and is applied in 18. The text states no removed API, no migration step and no breaking behavior, so no upgrade action is required. An app that relied on aspectRatio being ignored might see a layout change, but the text does not say this, so it is not treated as a risk._
- (18) Update webpack plugin for webpack 5 (#22739 by @michenly) — _The item only says the experimental Server Components webpack plugin was updated for webpack 5. It states no removal, changed behavior, required migration, or user action, and the feature is experimental. Nothing in the text says an app must change anything at 18._
- (18) Use globalThis instead of window for edge environments. — _The item is a fix in the experimental Server Components code that uses globalThis instead of window for edge environments. The text states no removed API, changed default, or required user action, and the feature is experimental. It is not a documented risk for the 17 -> 18 upgrade._
- (18) March 08, 2022 by Rick Hanlon --- As we shared in the release post, React 18 introduces features powered by our new concurrent renderer, with a gradual adoption strategy for existing applications. — _The item is an introduction to the upgrade guide. It describes React 18 as a concurrent renderer with gradual adoption and asks readers to report issues. It names no removed API, changed behavior, or required migration step. The React Native note says only that React 18 will ship in a future React Native version and relies on the New React Native Architecture. It states no breaking impact and no action to take at this release._
- (18) There is no one-to-one replacement for the old render callback API — it depends on your use case. — _The text says the legacy render and hydrate APIs keep working in React 18 and only log a console warning: "Until you switch to the new API, your app will behave as if it's running React 17." The render callback has no one-to-one replacement, and hydrate should move to hydrateRoot. Both are migration steps needed only when the app opts into the new root API (createRoot/hydrateRoot), so no action is required at the 18 upgrade itself._
- (18) In the React 18 Working Group we worked with library maintainers to create new APIs needed to support concurrent rendering for use cases specific to their use case in areas like styles, and external stores. — _The item is an introduction to new, additive APIs (useSyncExternalStore, useInsertionEffect) that libraries may adopt to support concurrent rendering in React 18. It states no breakage or required action for applications, and says only that some libraries may need to switch. The text says useInsertionEffect is not expected to be used unless you have built a CSS-in-JS library. It describes no removed API, no changed default and no operational impact._
- (18) Components can now render undefined: React no longer warns if you return undefined from a component. — _React 18 only stops warning when a component returns undefined, so components can now render undefined without a warning. The text describes no breakage or required migration, only a suggestion to use a linter to catch a forgotten return statement before JSX._
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
