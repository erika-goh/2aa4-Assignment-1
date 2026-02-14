# Task 5 – Engineering Process Fact Extraction

> **Purpose**: Structured factual data only. No narrative reflection. All data sourced from the repository.

---

## SECTION 1 — Workload Distribution

### Contributors & Commit Counts

| Author | Commits | Email |
|--------|---------|-------|
| Shan Truong | 9 | shanjanuary@gmail.com |
| Aryan Verma | 4 | 109933196+rinnegannn@users.noreply.github.com |

### Task-to-Contributor Mapping

| Task | Commits | Contributor |
|------|---------|-------------|
| **Task 1** – Papyrus UML Model | `0cef132` (upload Papyrus files + PNG) | Aryan Verma |
| **Task 2** – Generated Java Skeletons | `fe14a8e` (upload 16 Java files) | Aryan Verma |
| **Task 3** – GenAI Experiment | `fe48a7d` (3 docs) | Shan Truong (AI-assisted) |
| **Task 4** – Simulator Core | `1e2a1d6` (5 files, 125 ins, 54 del) | Shan Truong (AI-assisted) |
| **Task 4** – Demonstrator main | `894ad67` (2 files, 97 ins, 19 del) | Shan Truong (AI-assisted) |
| **Task 4** – Engineering Docs | `342a19f` (1 file, 145 ins) | Shan Truong (AI-assisted) |

### Approximate Workload Distribution

| Contributor | Files Changed | Lines Added | Lines Removed | Scope |
|-------------|--------------|-------------|---------------|-------|
| Shan Truong | 13 files | ~589 lines | 73 lines | Project setup, Tasks 3–4: GenAI, simulator, docs |
| Aryan Verma | 24 files | ~3,063 lines | 21 lines | Tasks 1–2: UML model + Java skeletons |

---

## SECTION 2 — Timeline & Iterations

### Chronological Milestone Timeline

| Date | Commit | Author | Milestone |
|------|--------|--------|-----------|
| 2026-01-30 13:11 | `889bef5` | Shan Truong | **Initial commit** (LICENSE + README) |
| 2026-02-09 12:46 | `e4556eb` | Aryan Verma | **.gitignore** setup |
| 2026-02-09 12:46 | `e527d24` | Aryan Verma | Delete LICENSE |
| 2026-02-09 12:49 | `fe14a8e` | Aryan Verma | **Task 2**: Upload 16 Papyrus-generated Java skeletons |
| 2026-02-09 12:54 | `0cef132` | Aryan Verma | **Task 1**: Upload Papyrus UML model (PNG + XML + .aird/.di/.notation) |
| 2026-02-13 01:56 | `fe48a7d` | Shan Truong | **Task 3**: GenAI experiment (3 markdown docs) |
| 2026-02-13 01:56 | PR #6 merged | — | Task 3 branch → main |
| 2026-02-13 02:21 | `1e2a1d6` | Shan Truong | **Task 4a**: Simulator core (Agent R1.8 + Game applyAction) |
| 2026-02-13 02:21 | PR #7 merged | — | Task 4 core branch → main |
| 2026-02-13 02:37 | `894ad67` | Shan Truong | **Task 4b**: Demonstrator Main + Simulator class |
| 2026-02-13 02:37 | PR #8 merged | — | Task 4 main branch → main |
| 2026-02-13 02:49 | `342a19f` | Shan Truong | **Task 4c**: Engineering documentation + invariants |
| 2026-02-13 02:49 | PR #9 merged | — | Task 4 docs branch → main |
| 2026-02-13 | Tag `v1.0.0` | — | Release tag on `main` at `5cc41a1` |

### Evidence of Iteration

- **Modelling → Code Generation**: Aryan uploaded Java skeleton files (`fe14a8e`) *before* uploading the UML model (`0cef132`), indicating the code was generated from the Papyrus model prior to the model files being committed.
- **Skeleton → Implementation**: Task 4 core (`1e2a1d6`) modified 5 existing skeleton files (`Action.java`, `Agent.java`, `Configuration.java`, `Game.java`), adding logic to previously stub-only classes.
- **Implementation → Refactoring**: Task 4 main (`894ad67`) refactored `Main.java` (19 deletions, 44 insertions) and introduced `Simulator.java` to separate setup from orchestration.
- **No reverse iteration observed**: No commits show the UML model being updated after implementation changes.

### Files Changed During Iteration

| Phase | Files |
|-------|-------|
| Task 4 Core | `Action.java`, `Agent.java`, `Configuration.java`, `Game.java`, `Main.java` (initial) |
| Task 4 Main | `Main.java` (refactored), `Simulator.java` (new) |
| Task 4 Docs | `docs/task4-engineering.md` (new) |

---

## SECTION 3 — Technical Decisions & Engineering Evidence

### OO Mechanisms Used

| Mechanism | Evidence |
|-----------|----------|
| **Encapsulation** | All fields in all classes are `private`. State changes use methods (`addVictoryPoints()`, `applyAction()` is `private` to `Game`). |
| **Inheritance** | `Settlement extends Structure`, `City extends Settlement`. `Structure` is declared `abstract`. |
| **Polymorphism** | `Structure.getVictoryPoints()` is `abstract`. `Settlement` returns 1, `City` returns 2. Called polymorphically in `Player.addStructure()`. |
| **Composition** | `Game` composes `Player` [1..4], `Board` [1], `Agent` [4] (created in constructor). `Player` composes `ResourceHand` [1]. `Board` composes `Tile`, `Node`, `Edge`. |

### SOLID Principles Evidence

| Principle | Where |
|-----------|-------|
| **SRP** | `Agent` decides actions. `Game` applies effects. `Player` stores VP. `Simulator` sets up. `Main` orchestrates. |
| **OCP** | `Action` carries structured data via `getDescription()`. New action types can be added without modifying `Agent` or `Game` internals. `Simulator` can be extended with new factory methods. |
| **LSP** | `City` and `Settlement` are substitutable for `Structure` in all contexts (e.g., `List<Structure>`). |
| **ISP** | Not explicitly demonstrated (no interfaces defined). |
| **DIP** | Not explicitly demonstrated (concrete dependencies throughout). |

### Implemented Invariants (R1.6) and Enforcement Location

| Invariant | Enforced In |
|-----------|-------------|
| `currentRound >= 0` | `Game` constructor initializes to 0; only incremented in `playRound()` |
| `victoryPoints >= 0` for all players | `Player` constructor initializes to 0; only positive deltas added |
| Game terminates when VP ≥ 10 or round ≥ maxRounds | `Game.checkTermination()` |
| Node holds at most one Structure | `Node.structure` field (single reference, not a list), multiplicity [0..1] in UML |
| No negative resource counts | `ResourceBank.takeResource()` checks `hasResource()` before decrementing |
| `agents.size() == players.size()` | `Game` constructor creates one `Agent` per `Player` in a loop |

### R1.8 Implementation (Linear Action Scan + Random Selection)

- **Location**: `Agent.takeTurn()` (lines 43–63 of `Agent.java`)
- **Mechanism**:
  1. Creates `ArrayList<Action>` of candidates
  2. **Linear scan**: adds `BUILD_SETTLEMENT` (always), `BUILD_CITY` (if structures exist), `BUILD_ROAD` (always), `PASS` (always)
  3. Calls `chooseRandomAction(validActions)` which uses `random.nextInt(list.size())` to pick uniformly

### Confirmation Checklist

| Item | Status |
|------|--------|
| Code compiles (no lint errors) | ✅ Confirmed |
| Demonstrator `Main.main()` exists | ✅ `src-gen/catandomainmodel/Main.java` |
| Tag exists | ✅ `v1.0.0` on commit `5cc41a1` |
| Release exists | ✅ Tag `v1.0.0` present on `main` |

---

## SECTION 4 — GenAI Experiment Analysis (Task 3)

*Source: `docs/task3-genai/prompt.md`, `genai-output.md`, `analysis.md`*

| Item | Value |
|------|-------|
| **Tool used** | Claude (Anthropic) |
| **Date** | 2026-02-13 |
| **Input type** | PNG (UML class diagram) + Papyrus-exported XML (`catandomainmodel.uml`) |

### Strengths Observed
- Identified all 16 types (15 classes + 1 enum) correctly
- Captured inheritance hierarchies (`Structure → Settlement → City`)
- Mapped private field visibility correctly
- Recognized composition vs. association relationships
- Enumeration literals exactly matched
- Cross-referenced PNG and XML inputs

### Weaknesses / Mistakes Found
- Tendency to add extra methods not in the UML (e.g., `setStructure()`, `hasStructure()`, `addNode()`)
- Multiplicity details (e.g., exactly 19 tiles, 54 nodes, 72 edges) lost or generalized
- `EMap` type mapping assumed as `Map<ResourceType, Integer>` (not guaranteed correct)
- Composition semantics not enforced in generated code (no lifecycle management)
- Constructor parameter types sometimes differed from UML (e.g., `Settlement` constructor)
- Tendency to write partial implementations when asked for skeletons

### Modifications Required After Generation
- Generated output was documentation-only (Task 3 docs), not committed as replacement code
- The actual Java skeletons in `src-gen/` are Papyrus-generated, not GenAI-generated
- Task 4 implementation was done separately, modifying the Papyrus skeletons directly

### Hyperparameters Documented
- None explicitly documented in `prompt.md` or `analysis.md`

---

## SECTION 5 — Project Management & Organization

### Branches Used

| Branch | Purpose |
|--------|---------|
| `main` | Integration branch, all PRs merge here |
| `task-3-genai` | Task 3: GenAI experiment documentation |
| `task-4-core` | Task 4: Simulator core implementation |
| `task-4-main` | Task 4: Demonstrator main program |
| `task-4-docs` | Task 4: Engineering documentation |

### Pull Requests Merged

| PR # | Source Branch | Title/Commit | Status |
|------|-------------|--------------|--------|
| #6 | `task-3-genai` | Task 3: add GenAI prompt, output summary, and analysis (#1) | Merged |
| #7 | `task-4-core` | Task 4: implement simulator core with R1.8 action selection and VP updates (#2) | Merged |
| #8 | `task-4-main` | Task 4: add demonstrator main program (#3) | Merged |
| #9 | `task-4-docs` | Task 4: add engineering documentation and invariants list (#4) | Merged |

### Issue Tracking

- Commits reference issue numbers: `(#1)`, `(#2)`, `(#3)`, `(#4)`
- This indicates GitHub Issues were used to track each sub-task

### Tag & Release

| Item | Value |
|------|-------|
| **Tag name** | `v1.0.0` |
| **Tagged commit** | `5cc41a1` (HEAD of `main`) |
| **Tag type** | Lightweight (no annotated message visible in log) |
| **Release notes** | Not extractable from local repo; may exist on GitHub |
