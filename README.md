# Simplex Solver

## Architecture

```mermaid
stateDiagram-v2
    [*] --> SimplexProblem
    [*] --> GomoryCut
    SimplexProblem --> DualSimplexProblem
    SimplexProblem --> TwoPhaseSimplexProblem
    SimplexProblem --> SimplexAnswer
    GomoryCut --> TwoPhaseSimplexProblem
    TwoPhaseSimplexProblem --> SimplexAnswer
    DualSimplexProblem --> SimplexAnswer
```
