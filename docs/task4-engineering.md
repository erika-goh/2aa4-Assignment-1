# Task 4 – Engineering Documentation & Invariants

## 1. System Overview

### Simulator Architecture

The Catan simulator follows a layered delegation pattern:

```
Main  →  Simulator  →  Game  →  Agent(s)
```

- **Main** — Minimal entry point. Prints banners and delegates to `Simulator`.
- **Simulator** — Encapsulates setup (board, players) and delegates execution to `Game.startGame()`.
- **Game** — Owns the simulation loop: iterates rounds, collects agent actions, applies effects, checks termination.
- **Agent** — Decides which action to take each turn. One agent per player.

### Game Loop

`Game.startGame()` runs a `while (!checkTermination())` loop that calls `playRound()` each iteration.

Each round:
1. Increment `currentRound`.
2. For each `Agent`: call `takeTurn()` → receive an `Action`.
3. Print the action.
4. Apply the action's effect to game state via `applyAction()`.
5. Print a round summary (all players' VP).

### Agent Action Selection (R1.8)

`Agent.takeTurn()` implements a **simple linear scan** of all candidate actions:

| Action | Validity Condition |
|---|---|
| `BUILD_SETTLEMENT` | Always available |
| `BUILD_CITY` | Player has ≥ 1 existing structure |
| `BUILD_ROAD` | Always available |
| `PASS` | Always available (fallback) |

Valid actions are collected into a list, and `chooseRandomAction()` picks one uniformly at random.

### Termination Logic

`Game.checkTermination()` returns `true` when **either**:
- A player reaches **≥ 10 victory points**, or
- `currentRound ≥ maxRounds` (safety net, default 500).

The game is designed to terminate naturally via VP accumulation.

---

## 2. Explicit Invariants (R1.6)

The following invariants must hold throughout the simulation:

### Round Counter
- **INV-1**: `currentRound >= 0` at all times.
- **INV-2**: `currentRound` increases by exactly 1 per call to `playRound()`.

### Victory Points
- **INV-3**: `victoryPoints >= 0` for every player at all times.
- **INV-4**: `victoryPoints <= 10` for all players unless the game is terminating (i.e., `checkTermination()` returns `true`).

### Resources
- **INV-5**: No resource count in `ResourceHand` or `ResourceBank` may be negative.
- **INV-6**: Total resources distributed must not exceed total resources available in `ResourceBank`.

### Board Structure
- **INV-7**: A `Node` can hold at most one `Structure` (its `structure` field is either `null` or a single `Structure`).
- **INV-8**: `Board.tiles`, `Board.nodes`, and `Board.edges` must remain non-null throughout the game.

### Game Termination
- **INV-9**: The game **must** terminate when:
  ```
  (∃ player ∈ players : player.victoryPoints >= 10) ∨ (currentRound >= maxRounds)
  ```
- **INV-10**: After termination, no further calls to `playRound()` occur.

### Agent–Player Pairing
- **INV-11**: `agents.size() == players.size()` at all times.
- **INV-12**: Each `Agent` is associated with exactly one `Player`, and this association does not change during the game.

---

## 3. SOLID & GRASP Design Rationale

### Single Responsibility Principle (SRP)

| Class | Single Responsibility |
|---|---|
| `Agent` | **Decides** which action to take (action selection logic) |
| `Game` | **Applies** action effects to game state (state mutation) |
| `Player` | **Stores** player state (VP, structures, resources) |
| `Simulator` | **Sets up** the game (board, players, Game instantiation) |
| `Main` | **Orchestrates** the demo (banners + delegation) |

The agent never mutates game state directly; the game never decides which action an agent should take.

### Open/Closed Principle (OCP)

- `Action` objects carry structured data (`roundNumber`, `playerID`, `description`) rather than relying on fragile string parsing.
- `Game.applyAction()` uses `action.getDescription()` with `equals()` checks, making it safe to extend with new action types without modifying existing action-handling logic.
- New board configurations can be introduced via new `Simulator` constructors or factory methods without changing `Game` or `Agent`.

### Encapsulation

- All state changes flow through class methods: `Player.addVictoryPoints()`, `Game.applyAction()`.
- No external class directly modifies `victoryPoints`, `currentRound`, or internal lists.
- `applyAction()` is `private` to `Game` — external code cannot bypass it.

### Information Expert (GRASP)

- **Game** is the information expert for applying action effects because it holds references to all players and the board.
- **Player** is the information expert for its own VP because it owns the `victoryPoints` field.
- **Agent** is the information expert for action selection because it knows its player's state.

### Creator (GRASP)

- **Game** creates `Agent` objects in its constructor because `Game` contains and closely uses them.
- **Simulator** creates `Board`, `Player`, and `Game` objects because it is responsible for initial setup.

---

## 4. Limitations & Future Work

### Board Placement Validation
- `Board.isValidSettlementPlacement()`, `isValidRoadPlacement()`, and `isValidCityPlacement()` return `false` (stub). The simulator does not enforce spatial placement rules.

### No Adjacency Rules
- The board has no adjacency graph connecting nodes and edges. Methods like `getAdjacentNodes()` and `getAdjacentEdges()` return empty lists.

### No Dice Simulation
- `Agent.rollDice()` exists but is not called during the game loop. Resource collection is not triggered by dice rolls.

### Simplified Resource Distribution
- Resources are not distributed based on tile numbers or dice outcomes. `ResourceHand` and `ResourceBank` exist structurally but are not actively used in the current simulation.

### Victory Points Are Action-Driven Only
- VP increases come solely from `BUILD_SETTLEMENT` (+1) and `BUILD_CITY` (+2) actions chosen randomly. There is no cost-checking or resource spending before building.

---

## 5. Conclusion

The simulator runs end-to-end: `Main` launches `Simulator`, which sets up a `Game` with 4 players. Each round, agents perform a linear scan of available actions and randomly select one. Victory points accumulate through building actions until a player reaches 10 VP, at which point the game terminates and announces a winner. The architecture respects SRP, OCP, and encapsulation, and all documented invariants (INV-1 through INV-12) are maintained throughout execution.
