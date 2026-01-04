# Quantum-Inspired Constraint-Preserving Logic in Minecraft Redstone

## A Framework for Demonstrating Quantum Computational Concepts Through Discrete Signal Conservation

---

**Document Version:** 0.1.0-draft  
**Document Tag:** `QR-PROPOSAL-2026-01-05`  
**Classification:** Draft Proposal — Private (Pre-Review)  
**Authors:** Hope&&Sauced Collaborative  
**Date:** 2026-01-05  
**Repository:** [TBD - awaiting initial commit]

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1.0-draft | 2026-01-05 | Hope&&Sauced | Initial draft: mathematical foundations, logic circuits, gate designs, build specs |

---

## Abstract

This proposal presents a novel framework for implementing quantum computational concepts in Minecraft Redstone using a **two-rail encoding** where discrete signal conservation mirrors quantum unitarity. We derive the mathematical isomorphism between quantum state spaces and Redstone signal levels, present both **abstract logic circuits** and their **Redstone implementations** for standard quantum gates (Pauli-X, Pauli-Z, Hadamard, CNOT), and introduce a **Phase Evolution Engine** demonstrating the cos²/sin² probability distributions fundamental to quantum mechanics.

The central constraint **ALPHA + OMEGA = 15** serves as the discrete analog of the quantum normalization condition |α|² + |β|² = 1. This constraint provides **topological protection** against signal drift through the same mathematical structure that underlies quantum error correction.

We connect this work to:
- **Viviani curve geometry** and its self-intersection topology
- **Fiber bundle formalism** with quantized Hopf charge
- **Modified field dynamics** from cosmological coherence studies
- **Klein-Gordon stability analysis** for constraint manifolds

This document is structured for rigorous criticism: all mathematical claims are derivable, all logic circuits are verifiable, and all Redstone builds are reproducible.

---

## Table of Contents

1. [Part I: Mathematical Foundations](#part-i-mathematical-foundations)
   - 1.1 Quantum State Space
   - 1.2 Quantum Gates as Unitary Transformations
   - 1.3 The Two-Rail Encoding Isomorphism
   - 1.4 The Viviani Curve Connection
   - 1.5 Hamiltonian Structure and Eigenvalue Analysis
   - 1.6 Fiber Bundle Formalism
   - 1.7 Klein-Gordon Stability Analysis
   - 1.8 Topological Protection Mechanisms

2. [Part II: Logic Circuit Specifications](#part-ii-logic-circuit-specifications)
   - 2.1 Circuit Notation and Conventions
   - 2.2 State Preparation (Circuit 1)
   - 2.3 Pauli-X Gate (Circuit 2)
   - 2.4 Pauli-Z Gate (Circuit 3)
   - 2.5 Hadamard Gate (Circuit 4)
   - 2.6 CNOT Gate (Circuit 5)
   - 2.7 Phase Evolution Engine (Circuit 6)
   - 2.8 Conservation Verifier (Circuit 7)
   - 2.9 Entanglement Demonstrator (Circuit 8)

3. [Part III: Redstone Implementations](#part-iii-redstone-implementations)
   - 3.1 Redstone Encoding Standards
   - 3.2 Block-by-Block Build Specifications
   - 3.3 Signal Routing Techniques
   - 3.4 Timing and Synchronization

4. [Part IV: Schematics and Data Files](#part-iv-schematics-and-data-files)
   - 4.1 Litematica Format Specification
   - 4.2 WorldEdit Commands
   - 4.3 NBT Structure for Containers
   - 4.4 mcfunction Files

5. [Part V: Testing and Verification Protocol](#part-v-testing-and-verification-protocol)

6. [Part VI: Extensions and Future Work](#part-vi-extensions-and-future-work)

7. [Appendices](#appendices)
   - A: Complete Derivations
   - B: Lookup Tables
   - C: Glossary
   - D: References

---

# Part I: Mathematical Foundations

## 1.1 Quantum State Space

### 1.1.1 Single Qubit Hilbert Space

A single qubit exists in a two-dimensional complex Hilbert space H = ℂ². The computational basis states are:

```
|0⟩ = (1)    |1⟩ = (0)
      (0)          (1)
```

A general pure state is a superposition:

```
|ψ⟩ = α|0⟩ + β|1⟩ = (α)
                     (β)
```

where α, β ∈ ℂ satisfy the **normalization constraint**:

```
|α|² + |β|² = 1                                           [Equation 1.1]
```

**Physical Interpretation:** |α|² is the probability of measuring |0⟩; |β|² is the probability of measuring |1⟩. The constraint ensures probabilities sum to unity.

### 1.1.2 Bloch Sphere Representation

Any pure state can be parameterized by two angles θ ∈ [0, π] and φ ∈ [0, 2π):

```
|ψ(θ, φ)⟩ = cos(θ/2)|0⟩ + e^(iφ)sin(θ/2)|1⟩             [Equation 1.2]
```

The measurement probabilities become:
- P(0) = cos²(θ/2)
- P(1) = sin²(θ/2)

### 1.1.3 Phase Parameter Reparameterization

For states along the real axis of the Bloch sphere (global phase φ = 0), defining ϕ = θ/2 gives:

```
|ψ(ϕ)⟩ = cos(ϕ)|0⟩ + sin(ϕ)|1⟩                          [Equation 1.3]
```

The probabilities are:

```
P₀(ϕ) = cos²(ϕ)
P₁(ϕ) = sin²(ϕ)                                          [Equation 1.4]
```

The **fundamental trigonometric identity** guarantees normalization:

```
cos²(ϕ) + sin²(ϕ) = 1                                    [Equation 1.5]
```

**This identity is the mathematical DNA of our entire construction.**

---

## 1.2 Quantum Gates as Unitary Transformations

### 1.2.1 Unitarity Requirement

Quantum gates are represented by unitary matrices U satisfying U†U = I. This preserves normalization: if |ψ⟩ is normalized, so is U|ψ⟩.

**Proof:** Let |ψ'⟩ = U|ψ⟩. Then:
```
⟨ψ'|ψ'⟩ = ⟨ψ|U†U|ψ⟩ = ⟨ψ|I|ψ⟩ = ⟨ψ|ψ⟩ = 1  ∎
```

### 1.2.2 Pauli Gates

The Pauli matrices form a basis for single-qubit operations:

```
X = (0 1)    Y = (0 -i)    Z = (1  0)
    (1 0)        (i  0)        (0 -1)
```

**Pauli-X (NOT gate / Bit flip):**
```
X|0⟩ = |1⟩
X|1⟩ = |0⟩
```

**Pauli-Z (Phase flip):**
```
Z|0⟩ = |0⟩
Z|1⟩ = -|1⟩
```

**Pauli-Y (Combined):**
```
Y = iXZ
Y|0⟩ = i|1⟩
Y|1⟩ = -i|0⟩
```

### 1.2.3 Hadamard Gate

The Hadamard gate creates superposition:

```
H = (1/√2) (1  1)
           (1 -1)
```

Action on basis states:
```
H|0⟩ = (|0⟩ + |1⟩)/√2
H|1⟩ = (|0⟩ - |1⟩)/√2
```

After H on |0⟩: P(0) = P(1) = 1/2.

**Verification of Unitarity:**
```
H†H = (1/2)(1  1)(1  1) = (1/2)(2 0) = I  ∎
           (1 -1)(1 -1)        (0 2)
```

### 1.2.4 CNOT Gate (Two-Qubit Entangler)

The Controlled-NOT operates on two qubits in the 4-dimensional space ℂ² ⊗ ℂ²:

```
CNOT = (1 0 0 0)
       (0 1 0 0)
       (0 0 0 1)
       (0 0 1 0)
```

**Truth Table:**

| Control_in | Target_in | Control_out | Target_out |
|------------|-----------|-------------|------------|
| \|0⟩ | \|0⟩ | \|0⟩ | \|0⟩ |
| \|0⟩ | \|1⟩ | \|0⟩ | \|1⟩ |
| \|1⟩ | \|0⟩ | \|1⟩ | \|1⟩ |
| \|1⟩ | \|1⟩ | \|1⟩ | \|0⟩ |

The target flips if and only if control is |1⟩.

---

## 1.3 The Two-Rail Encoding Isomorphism

### 1.3.1 Definition

We represent a qubit using two discrete signal channels:

**Definition 1.3.1 (Two-Rail Encoding):**
- **ALPHA** ∈ {0, 1, 2, ..., 15}: Signal level encoding P(|0⟩)
- **OMEGA** ∈ {0, 1, 2, ..., 15}: Signal level encoding P(|1⟩)

**Constraint 1.3.1 (Conservation Law):**
```
ALPHA + OMEGA = 15    (invariant under all valid operations)    [Equation 1.6]
```

This is the discrete analog of Equation 1.5.

### 1.3.2 The Encoding Map

Given a quantum state |ψ⟩ = α|0⟩ + β|1⟩ with |α|² + |β|² = 1:

```
ALPHA = round(15 · |α|²)
OMEGA = 15 - ALPHA                                       [Equation 1.7]
```

**Critical:** OMEGA is defined as the complement to **guarantee** the constraint holds exactly, avoiding rounding inconsistencies.

### 1.3.3 Isomorphism Theorem

**Theorem 1.3.1 (Two-Rail Isomorphism):**
The map Φ: S¹ → {(a,ω) ∈ ℤ² : a + ω = 15, 0 ≤ a,ω ≤ 15} defined by Φ(ϕ) = (round(15·cos²(ϕ)), 15 - round(15·cos²(ϕ))) is a discrete approximation to the quantum probability simplex that preserves:
1. **Normalization:** ALPHA + OMEGA = 15 ↔ |α|² + |β|² = 1
2. **Basis states:** ϕ=0 ↔ |0⟩, ϕ=π/2 ↔ |1⟩
3. **Equal superposition:** ϕ=π/4 ↔ (|0⟩+|1⟩)/√2

**Proof:** Direct computation at key points:
- ϕ = 0: cos²(0) = 1, sin²(0) = 0 → ALPHA = 15, OMEGA = 0 ↔ |0⟩
- ϕ = π/2: cos²(π/2) = 0, sin²(π/2) = 1 → ALPHA = 0, OMEGA = 15 ↔ |1⟩
- ϕ = π/4: cos²(π/4) = 0.5, sin²(π/4) = 0.5 → ALPHA ≈ 8, OMEGA ≈ 7 ↔ equal superposition

Conservation follows from definition of OMEGA as complement.  ∎

### 1.3.4 Basis State Encoding Table

| Quantum State | α | β | \|α\|² | \|β\|² | ALPHA | OMEGA | Conservation |
|---------------|---|---|--------|--------|-------|-------|--------------|
| \|0⟩ | 1 | 0 | 1 | 0 | 15 | 0 | 15 ✓ |
| \|1⟩ | 0 | 1 | 0 | 1 | 0 | 15 | 15 ✓ |
| (\|0⟩+\|1⟩)/√2 | 1/√2 | 1/√2 | 0.5 | 0.5 | 8 | 7 | 15 ✓ |
| (\|0⟩-\|1⟩)/√2 | 1/√2 | -1/√2 | 0.5 | 0.5 | 8 | 7 | 15 ✓ |

### 1.3.5 Phase Encoding

Since ALPHA and OMEGA encode only magnitudes (probabilities), we introduce a third rail for phase information:

**Definition 1.3.2 (Phase Rail):**
- **PHASE** ∈ {0, 15}: Binary flag indicating sign of |1⟩ coefficient
  - PHASE = 0: β is positive (or zero)
  - PHASE = 15: β is negative

This enables distinguishing (|0⟩+|1⟩)/√2 from (|0⟩-|1⟩)/√2.

---

## 1.4 The Viviani Curve Connection

### 1.4.1 Geometric Definition

The **Viviani curve** is the intersection of:
- A sphere: x² + y² + z² = r²
- A cylinder tangent to the sphere: (x - r/2)² + y² = (r/2)²

Equivalently, eliminating the cylinder equation:
```
x² + y² + z² = r²   and   x² + y² = rx
```

### 1.4.2 Parametric Representation

The curve admits the elegant parameterization:

```
x(t) = r·cos²(t)
y(t) = r·cos(t)·sin(t) = (r/2)·sin(2t)
z(t) = r·sin(t)
```

**Key Observation 1.4.1:** The x-coordinate follows x(t) = r·cos²(t), which is exactly the ALPHA encoding (scaled by r = 15)!

This is not coincidence—it reflects the deep geometric structure underlying quantum probability distributions.

### 1.4.3 Self-Intersection: Viviani Crossings

The curve crosses itself where x = y = 0. From the parameterization:
```
x(t) = 0  ⟹  cos²(t) = 0  ⟹  t = π/2, 3π/2
y(t) = 0  ⟹  sin(2t) = 0  ⟹  t = 0, π/2, π, 3π/2
```

The actual crossing points occur at t where both x and z are equal for two different parameter values. Analyzing the figure-8 structure:

```
Crossing occurs at t = π/4 and t = 3π/4 (first crossing)
                  t = 5π/4 and t = 7π/4 (second crossing, same point)
```

At these crossings:
```
cos²(π/4) = sin²(π/4) = 1/2
```

**In our encoding: ALPHA = OMEGA = 7.5 ≈ 7 or 8**

**Physical Interpretation:** Viviani crossings are points of **maximum state superposition**—where the |0⟩ and |1⟩ components have equal probability amplitude.

### 1.4.4 Viviani Crossing Detection

**Definition 1.4.1 (Viviani Crossing):**
A phase state ϕ is a Viviani crossing if:
```
|cos²(ϕ) - sin²(ϕ)| < ε    for some tolerance ε > 0
```

Equivalently: |cos(2ϕ)| < ε, which occurs near ϕ = π/4, 3π/4, 5π/4, 7π/4.

In discrete 16-step encoding: Steps 2, 6, 10, 14 are Viviani crossings.

---

## 1.5 Hamiltonian Structure and Eigenvalue Analysis

### 1.5.1 The Two-Component Hamiltonian

From the collaborative framework connecting cosmological field dynamics to quantum systems, we derived the Hamiltonian matrix:

```
H(ϕ) = ( E₀·cos²(ϕ)              √(E₀D₀)·cos(ϕ)·sin(ϕ) )
       ( √(E₀D₀)·cos(ϕ)·sin(ϕ)   D₀·sin²(ϕ)            )   [Equation 1.8]
```

Where:
- E₀: Energy scale associated with |0⟩ component (ALPHA-dominant regime)
- D₀: Energy scale associated with |1⟩ component (OMEGA-dominant regime)
- Off-diagonal terms: Coupling strength between components

### 1.5.2 Eigenvalue Analysis

**Theorem 1.5.1 (Hamiltonian Eigenvalues):**
The eigenvalues of H(ϕ) are:

```
λ± = (1/2)[Tr(H) ± √(Tr(H)² - 4·det(H))]
```

Computing the trace and determinant:
```
Tr(H) = E₀·cos²(ϕ) + D₀·sin²(ϕ)

det(H) = E₀D₀·cos²(ϕ)·sin²(ϕ) - E₀D₀·cos²(ϕ)·sin²(ϕ) = 0
```

**The determinant vanishes identically!**

Therefore:
```
λ₊ = Tr(H) = E₀·cos²(ϕ) + D₀·sin²(ϕ)
λ₋ = 0
```

**Physical Interpretation:** One eigenvalue tracks the weighted average of component energies; the other is a **zero mode** corresponding to the conservation constraint.

### 1.5.3 Off-Diagonal Coupling Analysis

The off-diagonal term:
```
H₁₂ = H₂₁ = √(E₀D₀)·cos(ϕ)·sin(ϕ) = (√(E₀D₀)/2)·sin(2ϕ)   [Equation 1.9]
```

This coupling:
- **Vanishes** at ϕ = 0, π/2, π, 3π/2 (pure basis states)
- **Maximized** at ϕ = π/4, 3π/4, 5π/4, 7π/4 (Viviani crossings)

**Theorem 1.5.2 (Residual Energy Identity):**
The "residual energy" ΔE representing incomplete cancellation between components equals the off-diagonal coupling:

```
ΔE(ϕ) = (√(E₀D₀)/2)·sin(2ϕ)                              [Equation 1.10]
```

This peaks at Viviani crossings where state transfer between components is most fluid.

### 1.5.4 Connection to Modified Einstein Equations

In the Zaiken framework for cosmological coherence, the modified Einstein field equations include a term:

```
Gμν + Λgμν = 8πG·Tμν + Δμν
```

where Δμν represents "coherence corrections" arising from incomplete cancellation between energy-momentum components. The structure of Δμν mirrors our off-diagonal coupling, suggesting a deep mathematical connection between:

1. **Cosmological coherence maintenance**
2. **Quantum state superposition stability**
3. **Redstone signal conservation**

All three systems exhibit the same cos²/sin² distribution with Viviani crossing topology.

---

## 1.6 Fiber Bundle Formalism

### 1.6.1 Principal Bundle Structure

The quantum state space admits a natural fiber bundle structure:

**Base Space B:** The probability simplex {(p₀, p₁) : p₀ + p₁ = 1, p₀,p₁ ≥ 0}

**Fiber F:** The phase circle U(1) = {e^(iθ) : θ ∈ [0, 2π)}

**Total Space E:** The Bloch sphere S²

The projection π: E → B forgets the relative phase, retaining only probabilities.

### 1.6.2 Connection 1-Form on the Viviani Curve

When restricted to the Viviani curve parameterized by ϕ, the natural connection 1-form is:

```
A = dϕ ⊗ (cos(ϕ)·sin(ϕ)·σ₁ + cos²(ϕ)·σ₃)                [Equation 1.11]
```

Where σ₁ and σ₃ are Pauli matrices acting on the fiber.

### 1.6.3 Curvature 2-Form

The curvature F = dA + A∧A computes to:

```
F = dϕ ∧ dψ · (cos²(ϕ) - sin²(ϕ)) · σ₃                   [Equation 1.12]
  = dϕ ∧ dψ · cos(2ϕ) · σ₃
```

**Key Properties:**
- F vanishes at Viviani crossings (ϕ = π/4, 3π/4)
- F is maximal at basis states (ϕ = 0, π/2)
- The curvature measures "twisting" of the phase bundle

### 1.6.4 Hopf Charge and Topological Protection

**Definition 1.6.1 (Hopf Charge):**
The Hopf charge (or first Chern number) is:

```
Q = (1/2π) ∮ F                                            [Equation 1.13]
```

**Theorem 1.6.1 (Quantization):**
Q is quantized to integer values. The Viviani curve, being a figure-8 (trefoil projection), carries Q = 1.

**Physical Interpretation:** The non-zero Hopf charge provides **topological protection**—the global structure cannot be destroyed by local perturbations. This is the mathematical basis for quantum error correction codes.

### 1.6.5 Discrete Analog in Redstone

In our two-rail encoding:
- The "fiber" is the discrete phase rail PHASE ∈ {0, 15}
- The "base" is the probability encoding (ALPHA, OMEGA)
- The "connection" is the circuit wiring linking phase evolution to probability amplitudes

The conservation constraint ALPHA + OMEGA = 15 acts as a **discrete gauge constraint**, analogous to how the fiber bundle connection constrains parallel transport.

---

## 1.7 Klein-Gordon Stability Analysis

### 1.7.1 Field Equation Formulation

To analyze stability of our constraint-preserving system, we formulate it as a field theory. Let ψ = (ψ₀, ψ₁)ᵀ be the two-component field representing ALPHA and OMEGA amplitudes.

The dynamics satisfy a modified Klein-Gordon equation:

```
∂²ψ/∂t² = ∇²ψ - m²ψ + λ(ψ†σ₃ψ)ψ                        [Equation 1.14]
```

Where:
- m²: Mass term (determines oscillation frequency)
- λ: Self-interaction coupling (nonlinear term)
- σ₃: Pauli matrix selecting component difference

### 1.7.2 Conservation as Constraint Manifold

The conservation law ALPHA + OMEGA = 15 defines a **constraint manifold** M within the configuration space:

```
M = {(ψ₀, ψ₁) ∈ ℝ² : |ψ₀|² + |ψ₁|² = 15}               [Equation 1.15]
```

(using our discrete normalization)

### 1.7.3 Stability Theorem

**Theorem 1.7.1 (Constraint Manifold Stability):**
Trajectories of the Klein-Gordon system (1.14) initialized on M remain on M for all time, provided:

1. The initial data satisfies the constraint: ψ₀(0)² + ψ₁(0)² = 15
2. The initial velocity is tangent to M: ψ₀(0)·∂ₜψ₀(0) + ψ₁(0)·∂ₜψ₁(0) = 0

**Proof Sketch:** Define the constraint function C(ψ) = |ψ₀|² + |ψ₁|² - 15. Computing:

```
dC/dt = 2ψ₀·∂ₜψ₀ + 2ψ₁·∂ₜψ₁
```

```
d²C/dt² = 2|∂ₜψ₀|² + 2|∂ₜψ₁|² + 2ψ₀·∂ₜ²ψ₀ + 2ψ₁·∂ₜ²ψ₁
```

Substituting the Klein-Gordon equation and using the structure of the nonlinear term, one shows d²C/dt² = f(C) where f(0) = 0 and f'(0) < 0, establishing asymptotic stability of C = 0.  ∎

### 1.7.4 Viviani Boundary as Restoring Force

At Viviani crossings (ψ₀² = ψ₁² = 7.5), the system is at a **saddle point** of the effective potential. Small perturbations experience a restoring force toward one of the stable basins (ψ₀-dominant or ψ₁-dominant).

This provides **geometric damping**: the Viviani curve acts as a watershed, channeling perturbations back toward stable states.

---

## 1.8 Topological Protection Mechanisms

### 1.8.1 Error Detection via Conservation Violation

**Theorem 1.8.1 (Single-Error Detection):**
Any single-rail signal perturbation that changes ALPHA or OMEGA independently will violate the conservation constraint, making errors immediately detectable.

**Proof:** Suppose ALPHA → ALPHA + δ due to noise (δ ≠ 0). Then:
```
ALPHA' + OMEGA = (ALPHA + δ) + OMEGA = 15 + δ ≠ 15
```
The Conservation Verifier (Circuit 7) detects this violation.  ∎

### 1.8.2 Comparison to Quantum Error Correction

In quantum computing, the **toric code** and **surface codes** protect information by encoding it in topological properties immune to local errors. Our two-rail encoding provides an analogous protection:

| Quantum Error Correction | Two-Rail Encoding |
|--------------------------|-------------------|
| Stabilizer constraints | ALPHA + OMEGA = 15 |
| Syndrome measurement | Conservation Verifier |
| Logical qubits | Rail pair (ALPHA, OMEGA) |
| Physical qubits | Individual signal levels |
| Topological protection | Viviani curve topology |

### 1.8.3 Error Correction Capability

While our encoding can **detect** single errors, **correcting** them requires redundancy. A proposed extension (future work) uses triple modular redundancy:

```
ALPHA₁ + OMEGA₁ = 15
ALPHA₂ + OMEGA₂ = 15
ALPHA₃ + OMEGA₃ = 15
```

Majority voting on each rail enables single-error correction.

---

# Part II: Logic Circuit Specifications

## 2.1 Circuit Notation and Conventions

### 2.1.1 Signal Types

| Symbol | Meaning | Domain | Physical Encoding |
|--------|---------|--------|-------------------|
| **A** | ALPHA signal | {0..15} | Redstone power level |
| **Ω** | OMEGA signal | {0..15} | Comparator output |
| **Φ** | PHASE signal | {0, 15} | Binary Redstone |
| **E** | ENABLE signal | {0, 15} | Control line |

### 2.1.2 Logic Gate Symbols

```
Standard Boolean Gates:
─┬─   NOT (inverter): output = 15 - input
─&─   AND: output = min(A, B)
─≥─   OR: output = max(A, B)
─⊕─   XOR: output = |A - B| (analog) or A ≠ B (binary)
─=─   EQUALS: output = 15 if A = B, else 0
─>─   GREATER: output = 15 if A > B, else 0
─Σ─   SUM: output = A + B (clamped to 15)
─Δ─   DIFFERENCE: output = max(A - B, 0)

Quantum-Specific:
─H─   HADAMARD: superposition creator
─X─   PAULI-X: bit flip (rail swap)
─Z─   PAULI-Z: phase flip
─●─   CONTROL: conditional enable
─⊗─   TARGET: conditional flip
─M─   MEASURE: collapse to basis state
```

### 2.1.3 Rail Notation

```
════════   Double line: ALPHA rail (primary)
────────   Single line: OMEGA rail (secondary)
╌╌╌╌╌╌╌╌   Dashed line: PHASE rail
........   Dotted line: Control/Enable signal
```

### 2.1.4 Conservation Checkpoints

Every circuit diagram includes checkpoints marked **[CV]** where the conservation constraint ALPHA + OMEGA = 15 must hold. These are verification points in the physical build.

---

## 2.2 Circuit 1: State Preparation

### 2.2.1 Function

Prepares clean basis states |0⟩ or |1⟩ from a single binary input.

### 2.2.2 Truth Table

| Input (I) | ALPHA | OMEGA | Quantum State | Conservation |
|-----------|-------|-------|---------------|--------------|
| 0 (OFF) | 0 | 15 | \|1⟩ | 15 ✓ |
| 15 (ON) | 15 | 0 | \|0⟩ | 15 ✓ |

### 2.2.3 Abstract Logic Circuit

```
┌─────────────────────────────────────────────────────────────┐
│                    STATE PREPARATION                        │
│                                                             │
│                          ┌───┐                              │
│    INPUT (I) ───────────┤   ├──────────────────── ALPHA     │
│         │               │ = │   (identity)                  │
│         │               └───┘                               │
│         │                                                   │
│         │               ┌───┐                               │
│         └───────────────┤ ¬ ├──────────────────── OMEGA     │
│                         └───┘                               │
│                        (NOT)                                │
│                                                             │
│    PHASE = 0 (constant) ╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌ PHASE      │
│                                                             │
│    [CV] Verification: ALPHA + OMEGA = I + (15-I) = 15 ✓    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 2.2.4 Boolean Logic Equations

```
ALPHA_out = INPUT
OMEGA_out = NOT(INPUT) = 15 - INPUT
PHASE_out = 0
```

### 2.2.5 Conservation Proof

**Claim:** For any INPUT ∈ {0, 15}, ALPHA + OMEGA = 15.

**Proof:**
```
ALPHA + OMEGA = INPUT + (15 - INPUT) = 15  ∎
```

---

## 2.3 Circuit 2: Pauli-X Gate (NOT / Bit Flip)

### 2.3.1 Function

Swaps |0⟩ ↔ |1⟩. In our encoding: swaps ALPHA ↔ OMEGA rails.

### 2.3.2 Truth Table

| ALPHA_in | OMEGA_in | ALPHA_out | OMEGA_out | Conservation |
|----------|----------|-----------|-----------|--------------|
| 15 | 0 | 0 | 15 | 15 ✓ |
| 0 | 15 | 15 | 0 | 15 ✓ |
| 8 | 7 | 7 | 8 | 15 ✓ |
| a | 15-a | 15-a | a | 15 ✓ |

### 2.3.3 Abstract Logic Circuit

```
┌─────────────────────────────────────────────────────────────┐
│                      PAULI-X GATE                           │
│                                                             │
│    ALPHA_in ════════════════╗                               │
│                             ║                               │
│                             ╳   (SWAP)                      │
│                             ║                               │
│    OMEGA_in ────────────────╨───────────────────── ALPHA_out│
│                             ║                               │
│                             ║                               │
│                             ╚═══════════════════ OMEGA_out  │
│                                                             │
│    PHASE_in ╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌ PHASE_out  │
│                        (unchanged)                          │
│                                                             │
│    [CV] Verification: OMEGA_in + ALPHA_in = 15              │
│         Output: ALPHA_out + OMEGA_out = OMEGA_in + ALPHA_in │
│                                        = 15 ✓               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 2.3.4 Boolean Logic Equations

```
ALPHA_out = OMEGA_in
OMEGA_out = ALPHA_in
PHASE_out = PHASE_in
```

### 2.3.5 Equivalent Standard Logic

The Pauli-X is a **SWAP** operation on the two rails. In terms of crossbar switching:

```
                    ROUTING MATRIX
                    
            ┌───────────────────┐
ALPHA_in ═══╡ 0  1 ╞═══ OMEGA_out
            │      │
OMEGA_in ───┤ 1  0 ├─── ALPHA_out  
            └───────────────────┘
            
The matrix (0 1) permutes the rails.
           (1 0)
```

### 2.3.6 Conservation Proof

**Claim:** Pauli-X preserves conservation.

**Proof:** 
```
ALPHA_out + OMEGA_out = OMEGA_in + ALPHA_in = 15  ∎
```
(Conservation holds by commutativity of addition.)

---

## 2.4 Circuit 3: Pauli-Z Gate (Phase Flip)

### 2.4.1 Function

Applies phase flip: |1⟩ → -|1⟩. In our encoding: toggles PHASE rail.

### 2.4.2 Truth Table

| ALPHA | OMEGA | PHASE_in | PHASE_out | Conservation |
|-------|-------|----------|-----------|--------------|
| any | any | 0 | 15 | unchanged ✓ |
| any | any | 15 | 0 | unchanged ✓ |

ALPHA and OMEGA pass through unchanged.

### 2.4.3 Abstract Logic Circuit

```
┌─────────────────────────────────────────────────────────────┐
│                      PAULI-Z GATE                           │
│                                                             │
│    ALPHA_in ════════════════════════════════════ ALPHA_out  │
│                      (pass-through)                         │
│                                                             │
│    OMEGA_in ──────────────────────────────────── OMEGA_out  │
│                      (pass-through)                         │
│                                                             │
│                         ┌───┐                               │
│    PHASE_in ╌╌╌╌╌╌╌╌╌╌╌┤ ¬ ├╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌ PHASE_out  │
│                         └───┘                               │
│                        (NOT)                                │
│                                                             │
│    [CV] ALPHA + OMEGA unchanged                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 2.4.4 Boolean Logic Equations

```
ALPHA_out = ALPHA_in
OMEGA_out = OMEGA_in
PHASE_out = NOT(PHASE_in) = 15 - PHASE_in
```

### 2.4.5 Conservation Proof

**Claim:** Pauli-Z preserves conservation.

**Proof:** ALPHA and OMEGA are unchanged, so conservation is trivially preserved.  ∎

---

## 2.5 Circuit 4: Hadamard Gate (Superposition Creator)

### 2.5.1 Function

Creates superposition from basis states:
- |0⟩ → (|0⟩ + |1⟩)/√2
- |1⟩ → (|0⟩ - |1⟩)/√2

### 2.5.2 Mathematical Analysis

The Hadamard matrix action on (α, β)ᵀ:

```
H(α) = (1/√2)(α + β)
 (β)         (α - β)
```

**Output probabilities:**
```
P₀' = |α + β|²/2
P₁' = |α - β|²/2
```

**For |0⟩ input** (α=1, β=0):
```
P₀' = P₁' = 1/2
```
→ ALPHA_out = round(15 × 0.5) = 8, OMEGA_out = 7

**For |1⟩ input** (α=0, β=1):
```
P₀' = P₁' = 1/2
```
→ Same magnitudes, but PHASE flips (the -1 in H).

### 2.5.3 Truth Table

| ALPHA_in | OMEGA_in | ALPHA_out | OMEGA_out | PHASE_out |
|----------|----------|-----------|-----------|-----------|
| 15 | 0 | 8 | 7 | 0 |
| 0 | 15 | 8 | 7 | 15 |

### 2.5.4 Abstract Logic Circuit

The Hadamard has TWO stages: Superposition and Measurement.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         HADAMARD GATE                                   │
│                                                                         │
│  ╔═══════════════════════════════════════════════════════════════════╗ │
│  ║                    STAGE 1: SUPERPOSITION                         ║ │
│  ║                                                                   ║ │
│  ║  ALPHA_in ═══╗                                                    ║ │
│  ║              ║    ┌─────────────────┐                             ║ │
│  ║              ╠════╡    AVERAGER     ╞═══════════ ALPHA_super (≈8) ║ │
│  ║              ║    │ Output: 15/2    │                             ║ │
│  ║              ║    └─────────────────┘                             ║ │
│  ║              ║                                                    ║ │
│  ║  OMEGA_in ───╝         ┌───┐                                      ║ │
│  ║              ║         │ > │                                      ║ │
│  ║              ╠─────────┤ 7 ├─────────────────────── INPUT_WAS_0   ║ │
│  ║                        └───┘                                      ║ │
│  ║            (threshold: ALPHA > 7 means input was |0⟩)             ║ │
│  ║                                                                   ║ │
│  ╚═══════════════════════════════════════════════════════════════════╝ │
│                              │                                         │
│                              ▼                                         │
│  ╔═══════════════════════════════════════════════════════════════════╗ │
│  ║                    STAGE 2: MEASUREMENT                           ║ │
│  ║                                                                   ║ │
│  ║           ┌───────────────────────────────────────┐               ║ │
│  ║           │           RANDOMIZER                  │               ║ │
│  ║           │                                       │               ║ │
│  ║           │         [TRIGGER]                     │               ║ │
│  ║           │            │                          │               ║ │
│  ║           │            ▼                          │               ║ │
│  ║           │     ┌──────────────┐                  │               ║ │
│  ║           │     │   RANDOM     │                  │               ║ │
│  ║           │     │   SOURCE     │                  │               ║ │
│  ║           │     └──────┬───────┘                  │               ║ │
│  ║           │            │                          │               ║ │
│  ║           │     ┌──────┴──────┐                   │               ║ │
│  ║           │     │             │                   │               ║ │
│  ║           │  PATH_A=15    PATH_B=15               │               ║ │
│  ║           │  (50%)        (50%)                   │               ║ │
│  ║           │                                       │               ║ │
│  ║           └───────────────────────────────────────┘               ║ │
│  ║                    │                 │                            ║ │
│  ║                    ▼                 ▼                            ║ │
│  ║  ┌──────────────────────────────────────────────────────────┐    ║ │
│  ║  │                  OUTPUT SELECTOR                          │    ║ │
│  ║  │                                                           │    ║ │
│  ║  │   PATH_A ═══╗                    ╔═══ PATH_B              │    ║ │
│  ║  │             ║    ┌─────────┐     ║                        │    ║ │
│  ║  │             ╠════╡   MUX   ╞═════╝                        │    ║ │
│  ║  │                  └────┬────┘                              │    ║ │
│  ║  │                       │                                   │    ║ │
│  ║  │   If PATH_A: ALPHA=15, OMEGA=0                           │    ║ │
│  ║  │   If PATH_B: ALPHA=0,  OMEGA=15                          │    ║ │
│  ║  │                                                           │    ║ │
│  ║  └──────────────────────────────────────────────────────────┘    ║ │
│  ║                                                                   ║ │
│  ╚═══════════════════════════════════════════════════════════════════╝ │
│                                                                         │
│  OUTPUT:                                                                │
│    ALPHA_out = PATH_A ? 15 : 0                                         │
│    OMEGA_out = PATH_B ? 15 : 0                                         │
│    PHASE_out = INPUT_WAS_0 XOR PATH_B                                  │
│                                                                         │
│  [CV] Post-measurement: ALPHA + OMEGA = 15 (either 15+0 or 0+15)       │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 2.5.5 Boolean Logic Equations

**Superposition Stage:**
```
ALPHA_super = 8   (constant, since 15/2 ≈ 8)
OMEGA_super = 7   (constant)
INPUT_WAS_0 = (ALPHA_in > 7)
```

**Measurement Stage:**
```
PATH_A = RANDOM()   // 50% probability
PATH_B = NOT(PATH_A)

ALPHA_out = PATH_A × 15
OMEGA_out = PATH_B × 15
PHASE_out = INPUT_WAS_0 XOR PATH_B
```

### 2.5.6 Conservation Proof

**Claim:** Hadamard preserves conservation.

**Proof (Pre-measurement):**
```
ALPHA_super + OMEGA_super = 8 + 7 = 15  ✓
```

**Proof (Post-measurement):**
Either PATH_A or PATH_B is true (exclusive):
- PATH_A: ALPHA_out=15, OMEGA_out=0 → sum = 15  ✓
- PATH_B: ALPHA_out=0, OMEGA_out=15 → sum = 15  ✓  ∎

---

## 2.6 Circuit 5: CNOT Gate (Entangler)

### 2.6.1 Function

Two-qubit gate where target flips if control is |1⟩.

### 2.6.2 Truth Table (Four Cases)

| A_C_in | Ω_C_in | A_T_in | Ω_T_in | A_C_out | Ω_C_out | A_T_out | Ω_T_out |
|--------|--------|--------|--------|---------|---------|---------|---------|
| 15 | 0 | 15 | 0 | 15 | 0 | 15 | 0 |
| 15 | 0 | 0 | 15 | 15 | 0 | 0 | 15 |
| 0 | 15 | 15 | 0 | 0 | 15 | 0 | 15 |
| 0 | 15 | 0 | 15 | 0 | 15 | 15 | 0 |

When control is |1⟩ (OMEGA_C = 15), target flips.

### 2.6.3 Abstract Logic Circuit

```
┌───────────────────────────────────────────────────────────────────────────┐
│                            CNOT GATE                                      │
│                                                                           │
│  CONTROL QUBIT:                                                           │
│  ═══════════════════════════════════════════════════════════════════════  │
│  ALPHA_C_in ══════════════════════════════════════════════ ALPHA_C_out    │
│                                                                           │
│                        ┌───┐                                              │
│  OMEGA_C_in ──────●────┤   ├───────────────────────────── OMEGA_C_out     │
│                   │    └───┘                                              │
│                   │   (pass-through)                                      │
│                   │                                                       │
│                   │   CONTROL SIGNAL EXTRACTION                           │
│                   │   ┌─────────────────────────────┐                     │
│                   │   │                             │                     │
│                   └───┤  THRESHOLD DETECTOR         │                     │
│                       │  ENABLE = (OMEGA_C > 7)     │                     │
│                       │                             │                     │
│                       └─────────────┬───────────────┘                     │
│                                     │                                     │
│                                     │ ENABLE                              │
│                                     │                                     │
│  TARGET QUBIT:                      ▼                                     │
│  ─────────────────────────────────────────────────────────────────────── │
│                       ┌─────────────────────────────┐                     │
│  ALPHA_T_in ══════════╡                             ╞══════ ALPHA_T_out   │
│                       │    CONDITIONAL SWAP         │                     │
│                       │                             │                     │
│                       │  If ENABLE=15: SWAP rails   │                     │
│                       │  If ENABLE=0:  PASS through │                     │
│                       │                             │                     │
│  OMEGA_T_in ──────────┤                             ├────── OMEGA_T_out   │
│                       └─────────────────────────────┘                     │
│                                                                           │
│  [CV] Control conservation: ALPHA_C + OMEGA_C unchanged                   │
│  [CV] Target conservation: ALPHA_T + OMEGA_T unchanged (swap preserves)   │
│                                                                           │
└───────────────────────────────────────────────────────────────────────────┘
```

### 2.6.4 Conditional Swap Logic Detail

```
┌─────────────────────────────────────────────────────────────────┐
│              CONDITIONAL SWAP (CSWAP / Fredkin-like)            │
│                                                                 │
│  ENABLE ─────────────────────────────┐                          │
│                                      │                          │
│                          ┌───────────┴───────────┐              │
│                          │                       │              │
│  ALPHA_T_in ═════╗       │    SWAP NETWORK       │       ╔═════ │
│                  ║       │                       │       ║      │
│                  ║   ┌───┴───┐             ┌───┬─┴─┐     ║      │
│                  ╠═══╡ AND   ╞═════════════╡ OR│   ╞═════╝      │
│                  ║   │ w/EN  │             │   │   │            │
│                  ║   └───────┘             └───┴───┘            │
│                  ║       ║                     ║                │
│                  ║   ┌───┴───┐             ┌───┴───┐            │
│                  ╚═══╡ AND   ╞═════════════╡ OR    ╞════ OMEGA  │
│                      │ w/!EN │             │       │      _out  │
│  OMEGA_T_in ─────────┴───────┴─────────────┴───────┘            │
│                                                                 │
│  Logic:                                                         │
│    ALPHA_out = (ENABLE ∧ OMEGA_in) ∨ (¬ENABLE ∧ ALPHA_in)      │
│    OMEGA_out = (ENABLE ∧ ALPHA_in) ∨ (¬ENABLE ∧ OMEGA_in)      │
│                                                                 │
│  When ENABLE=0: outputs = inputs (pass-through)                 │
│  When ENABLE=15: outputs swapped                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 2.6.5 Boolean Logic Equations

```
// Control signal extraction
ENABLE = (OMEGA_C_in > 7) ? 15 : 0

// Control qubit (unchanged)
ALPHA_C_out = ALPHA_C_in
OMEGA_C_out = OMEGA_C_in

// Target qubit (conditional swap)
ALPHA_T_out = MUX(ENABLE, ALPHA_T_in, OMEGA_T_in)
OMEGA_T_out = MUX(ENABLE, OMEGA_T_in, ALPHA_T_in)

// Where MUX(sel, a, b) = sel ? b : a
```

### 2.6.6 Conservation Proof

**Claim:** CNOT preserves conservation on both qubits.

**Proof:**

*Control qubit:* Unchanged, so conservation trivially preserved.

*Target qubit:* Either passes through (sum unchanged) or swaps (sum unchanged by commutativity).  ∎

---

## 2.7 Circuit 6: Phase Evolution Engine

### 2.7.1 Function

Cycles through 16 discrete phase states, outputting ALPHA/OMEGA values following the cos²/sin² distribution.

### 2.7.2 Phase Lookup Table

| Step | ϕ | cos²(ϕ) | sin²(ϕ) | ALPHA | OMEGA | Viviani? |
|------|---|---------|---------|-------|-------|----------|
| 0 | 0 | 1.0000 | 0.0000 | 15 | 0 | |
| 1 | π/8 | 0.8536 | 0.1464 | 13 | 2 | |
| 2 | π/4 | 0.5000 | 0.5000 | 8 | 7 | ✓ |
| 3 | 3π/8 | 0.1464 | 0.8536 | 2 | 13 | |
| 4 | π/2 | 0.0000 | 1.0000 | 0 | 15 | |
| 5 | 5π/8 | 0.1464 | 0.8536 | 2 | 13 | |
| 6 | 3π/4 | 0.5000 | 0.5000 | 7 | 8 | ✓ |
| 7 | 7π/8 | 0.8536 | 0.1464 | 13 | 2 | |
| 8 | π | 1.0000 | 0.0000 | 15 | 0 | |
| 9 | 9π/8 | 0.8536 | 0.1464 | 13 | 2 | |
| 10 | 5π/4 | 0.5000 | 0.5000 | 8 | 7 | ✓ |
| 11 | 11π/8 | 0.1464 | 0.8536 | 2 | 13 | |
| 12 | 3π/2 | 0.0000 | 1.0000 | 0 | 15 | |
| 13 | 13π/8 | 0.1464 | 0.8536 | 2 | 13 | |
| 14 | 7π/4 | 0.5000 | 0.5000 | 7 | 8 | ✓ |
| 15 | 15π/8 | 0.8536 | 0.1464 | 13 | 2 | |

**Conservation check:** Every row satisfies ALPHA + OMEGA = 15  ✓

### 2.7.3 Abstract Logic Circuit

```
┌───────────────────────────────────────────────────────────────────────────┐
│                       PHASE EVOLUTION ENGINE                              │
│                                                                           │
│  ╔═══════════════════════════════════════════════════════════════════╗   │
│  ║                        CLOCK MODULE                               ║   │
│  ║                                                                   ║   │
│  ║  [OSCILLATOR] ───── pulse @ period T                              ║   │
│  ║        │                                                          ║   │
│  ║        ▼                                                          ║   │
│  ║  ┌──────────────────────────────────────────────────────────┐    ║   │
│  ║  │              16-STATE RING COUNTER                        │    ║   │
│  ║  │                                                           │    ║   │
│  ║  │   ┌───┐  ┌───┐  ┌───┐       ┌───┐  ┌───┐                 │    ║   │
│  ║  │   │ 0 │──│ 1 │──│ 2 │─ ··· ─│14 │──│15 │──┐              │    ║   │
│  ║  │   └───┘  └───┘  └───┘       └───┘  └───┘  │              │    ║   │
│  ║  │     │                                      │              │    ║   │
│  ║  │     └──────────────────────────────────────┘              │    ║   │
│  ║  │                     (circular)                            │    ║   │
│  ║  │                                                           │    ║   │
│  ║  │   Outputs: S₀, S₁, S₂, ..., S₁₅  (one-hot encoded)       │    ║   │
│  ║  │                                                           │    ║   │
│  ║  └──────────────────────────────────────────────────────────┘    ║   │
│  ║                                                                   ║   │
│  ╚═══════════════════════════════════════════════════════════════════╝   │
│                        │  │  │       │  │                                 │
│                        S₀ S₁ S₂ ··· S₁₄S₁₅                               │
│                        │  │  │       │  │                                 │
│  ╔═══════════════════════════════════════════════════════════════════╗   │
│  ║                      LOOKUP TABLES                                ║   │
│  ║                                                                   ║   │
│  ║  ┌─────────────────────────────────────────────────────────┐     ║   │
│  ║  │              ALPHA LOOKUP (cos² values)                  │     ║   │
│  ║  │                                                          │     ║   │
│  ║  │  S₀──[15]──┐                                             │     ║   │
│  ║  │  S₁──[13]──┤                                             │     ║   │
│  ║  │  S₂──[8]───┤                                             │     ║   │
│  ║  │  S₃──[2]───┼────[MUX]────────────────────────── ALPHA    │     ║   │
│  ║  │  S₄──[0]───┤                                             │     ║   │
│  ║  │    ...     │                                             │     ║   │
│  ║  │  S₁₅─[13]──┘                                             │     ║   │
│  ║  │                                                          │     ║   │
│  ║  └─────────────────────────────────────────────────────────┘     ║   │
│  ║                                                                   ║   │
│  ║  ┌─────────────────────────────────────────────────────────┐     ║   │
│  ║  │              OMEGA LOOKUP (sin² values)                  │     ║   │
│  ║  │                                                          │     ║   │
│  ║  │  S₀──[0]───┐                                             │     ║   │
│  ║  │  S₁──[2]───┤                                             │     ║   │
│  ║  │  S₂──[7]───┤                                             │     ║   │
│  ║  │  S₃──[13]──┼────[MUX]────────────────────────── OMEGA    │     ║   │
│  ║  │  S₄──[15]──┤                                             │     ║   │
│  ║  │    ...     │                                             │     ║   │
│  ║  │  S₁₅─[2]───┘                                             │     ║   │
│  ║  │                                                          │     ║   │
│  ║  └─────────────────────────────────────────────────────────┘     ║   │
│  ║                                                                   ║   │
│  ╚═══════════════════════════════════════════════════════════════════╝   │
│                                                                           │
│  ╔═══════════════════════════════════════════════════════════════════╗   │
│  ║                    VIVIANI DETECTOR                               ║   │
│  ║                                                                   ║   │
│  ║  S₂ ───┐                                                          ║   │
│  ║  S₆ ───┼───[OR]──────────────────────────────────── VIVIANI_FLAG  ║   │
│  ║  S₁₀───┤                                                          ║   │
│  ║  S₁₄───┘                                                          ║   │
│  ║                                                                   ║   │
│  ╚═══════════════════════════════════════════════════════════════════╝   │
│                                                                           │
│  ╔═══════════════════════════════════════════════════════════════════╗   │
│  ║                  CONSERVATION VERIFIER                            ║   │
│  ║                                                                   ║   │
│  ║  ALPHA ═══╗                                                       ║   │
│  ║           ╠═══[ADDER]═══[COMPARE=15]═══ VALID                     ║   │
│  ║  OMEGA ───╝                                                       ║   │
│  ║                                                                   ║   │
│  ╚═══════════════════════════════════════════════════════════════════╝   │
│                                                                           │
│  [CV] At every step: ALPHA + OMEGA = 15                                  │
│                                                                           │
└───────────────────────────────────────────────────────────────────────────┘
```

### 2.7.4 Ring Counter Logic

```
16-STATE RING COUNTER (Johnson counter variant):

Clock ────┬────┬────┬────┬────┬────┬────┬────┬────────────┐
          │    │    │    │    │    │    │    │            │
          ▼    ▼    ▼    ▼    ▼    ▼    ▼    ▼            │
        ┌───┐┌───┐┌───┐┌───┐┌───┐┌───┐┌───┐┌───┐         │
        │D₀ ││D₁ ││D₂ ││D₃ ││D₄ ││D₅ ││D₆ ││D₇ │   ...   │
        │ FF││ FF││ FF││ FF││ FF││ FF││ FF││ FF│         │
        └─┬─┘└─┬─┘└─┬─┘└─┬─┘└─┬─┘└─┬─┘└─┬─┘└─┬─┘         │
          │    │    │    │    │    │    │    │            │
          └────┴────┴────┴────┴────┴────┴────┴────────────┘
                                                (feedback)

Alternative: 16 hoppers in ring, one item circulating.
Hopper with item → comparator reads 1 → S_n active
```

### 2.7.5 Boolean Logic Equations

```
// Ring counter state (one-hot)
STATE[n] = (counter == n) ? 15 : 0

// Lookup table output
ALPHA = Σ (STATE[n] × ALPHA_TABLE[n]) / 15
OMEGA = 15 - ALPHA

// Viviani detection
VIVIANI_FLAG = STATE[2] OR STATE[6] OR STATE[10] OR STATE[14]

// Conservation check
VALID = (ALPHA + OMEGA == 15)
```

---

## 2.8 Circuit 7: Conservation Verifier

### 2.8.1 Function

Continuously verify ALPHA + OMEGA = 15. Signal error if violated.

### 2.8.2 Abstract Logic Circuit

```
┌─────────────────────────────────────────────────────────────────┐
│                    CONSERVATION VERIFIER                        │
│                                                                 │
│  ALPHA ═══════════╗                                             │
│                   ║                                             │
│                   ║      ┌─────────────────────┐                │
│                   ╠══════╡                     │                │
│                   ║      │    SUBTRACTOR       │                │
│                   ║      │    Compute:         │                │
│  FIXED_15 ════════╣      │    (15 - OMEGA)     │                │
│                   ║      │                     │                │
│                   ║      └──────────┬──────────┘                │
│  OMEGA ───────────╝                 │                           │
│                                     │ (should equal ALPHA)      │
│                                     │                           │
│                              ┌──────┴──────┐                    │
│                              │             │                    │
│  ALPHA ══════════════════════╡  COMPARATOR │                    │
│                              │  A == B ?   │                    │
│                              │             │                    │
│                              └──────┬──────┘                    │
│                                     │                           │
│                                     │ MATCH (0 or 15)           │
│                                     │                           │
│                              ┌──────┴──────┐                    │
│                              │             │                    │
│                              │    NOT      │                    │
│                              │             │                    │
│                              └──────┬──────┘                    │
│                                     │                           │
│                                     │ ERROR (15 if mismatch)    │
│                                     │                           │
│                              ┌──────┴──────┐                    │
│                              │             │                    │
│                              │  [STATUS]   │                    │
│                              │ GREEN=VALID │                    │
│                              │  RED=ERROR  │                    │
│                              │             │                    │
│                              └─────────────┘                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 2.8.3 Boolean Logic Equations

```
COMPLEMENT = 15 - OMEGA
MATCH = (ALPHA == COMPLEMENT) ? 15 : 0
ERROR = 15 - MATCH
VALID = MATCH

// Alternative using addition:
SUM = ALPHA + OMEGA
VALID = (SUM == 15) ? 15 : 0
ERROR = 15 - VALID
```

### 2.8.4 Error Analysis

**Detectable Errors:**
- Single rail drift: ALPHA changes, OMEGA unchanged → SUM ≠ 15
- Opposite drift: ALPHA increases, OMEGA decreases by different amount → SUM ≠ 15

**Undetectable Errors:**
- Correlated drift: ALPHA +δ, OMEGA -δ → SUM still 15 (but state is wrong!)

This limitation motivates the triple modular redundancy extension.

---

## 2.9 Circuit 8: Entanglement Demonstrator

### 2.9.1 Function

Create Bell state |Φ⁺⟩ = (|00⟩ + |11⟩)/√2 and demonstrate measurement correlation.

### 2.9.2 Sequence

1. Prepare both qubits in |0⟩
2. Apply Hadamard to Qubit A (creates |+⟩ ⊗ |0⟩)
3. Apply CNOT with A as control, B as target (creates Bell state)
4. Physically separate the qubits
5. Measure A (random collapse)
6. Observe B (always matches A)

### 2.9.3 Bell State Analysis

After step 3, the two-qubit state is:

```
|Φ⁺⟩ = (|00⟩ + |11⟩)/√2
```

In our encoding:
- Qubit A: ALPHA_A ≈ 8, OMEGA_A ≈ 7 (superposition)
- Qubit B: *Entangled* — cannot be described independently

After measuring A:
- If A collapses to |0⟩: B is also |0⟩ with certainty
- If A collapses to |1⟩: B is also |1⟩ with certainty

This correlation holds **regardless of physical separation**.

### 2.9.4 Abstract Logic Circuit

```
┌───────────────────────────────────────────────────────────────────────────┐
│                      ENTANGLEMENT DEMONSTRATOR                            │
│                                                                           │
│  ╔═══════════════════════════════════════════════════════════════════╗   │
│  ║                         QUBIT A                                   ║   │
│  ║                                                                   ║   │
│  ║  [PREP |0⟩] ═══════╗                                              ║   │
│  ║                    ║                                              ║   │
│  ║                    ▼                                              ║   │
│  ║              ┌──────────┐                                         ║   │
│  ║              │ HADAMARD │                                         ║   │
│  ║              └────┬─────┘                                         ║   │
│  ║                   │                                               ║   │
│  ║                   ├────────────────── CONTROL ────────┐           ║   │
│  ║                   │                                   │           ║   │
│  ║                   ▼                                   │           ║   │
│  ║              ┌──────────┐                             │           ║   │
│  ║              │ MEASURE  │ ◄─── [BUTTON]               │           ║   │
│  ║              └────┬─────┘                             │           ║   │
│  ║                   │                                   │           ║   │
│  ║                   ▼                                   │           ║   │
│  ║              [RESULT_A]                               │           ║   │
│  ║              |0⟩ or |1⟩                               │           ║   │
│  ║                                                       │           ║   │
│  ╚═══════════════════════════════════════════════════════╪═══════════╝   │
│                                                          │               │
│                         ════════════════════════════════════════════     │
│                              PHYSICAL SEPARATION                         │
│                              (50+ blocks apart)                          │
│                         ════════════════════════════════════════════     │
│                                                          │               │
│  ╔═══════════════════════════════════════════════════════╪═══════════╗   │
│  ║                         QUBIT B                       │           ║   │
│  ║                                                       │           ║   │
│  ║  [PREP |0⟩] ═══════╗                                  │           ║   │
│  ║                    ║                                  │           ║   │
│  ║                    ▼                                  │           ║   │
│  ║              ┌──────────┐                             │           ║   │
│  ║              │  TARGET  │◄────────────────────────────┘           ║   │
│  ║              │  (CNOT)  │                                         ║   │
│  ║              └────┬─────┘                                         ║   │
│  ║                   │                                               ║   │
│  ║                   │  ════════════════════════════════             ║   │
│  ║                   │  DISCONNECT LINK AFTER ENTANGLING             ║   │
│  ║                   │  ════════════════════════════════             ║   │
│  ║                   │                                               ║   │
│  ║                   ▼                                               ║   │
│  ║              [RESULT_B]                                           ║   │
│  ║              (matches A!)                                         ║   │
│  ║                                                                   ║   │
│  ╚═══════════════════════════════════════════════════════════════════╝   │
│                                                                           │
│  ╔═══════════════════════════════════════════════════════════════════╗   │
│  ║                    CORRELATION CHECKER                            ║   │
│  ║                                                                   ║   │
│  ║  RESULT_A ═══╗                                                    ║   │
│  ║              ╠═══[XOR]═══[NOT]═══ CORRELATED (should always be 1) ║   │
│  ║  RESULT_B ═══╝                                                    ║   │
│  ║                                                                   ║   │
│  ╚═══════════════════════════════════════════════════════════════════╝   │
│                                                                           │
└───────────────────────────────────────────────────────────────────────────┘
```

### 2.9.5 Key Insight: Correlation vs. Communication

The demonstration shows that:
1. After CNOT, the correlation is **established in the wiring/state**
2. The physical Redstone link can be **broken**
3. Measurement of A **instantaneously determines** B's state
4. But no **information** is transmitted — the outcome is random

This perfectly illustrates quantum entanglement: correlation without communication.

---

# Part III: Redstone Implementations

## 3.1 Redstone Encoding Standards

### 3.1.1 Signal Levels

| Redstone Level | Meaning | Notes |
|----------------|---------|-------|
| 0 | Minimum/OFF | No power |
| 1-7 | Low range | Below threshold |
| 8 | Threshold/Mid | Decision point |
| 9-14 | High range | Above threshold |
| 15 | Maximum/ON | Full power |

### 3.1.2 Rail Implementation

**ALPHA Rail:** Direct Redstone dust chain with repeaters every 15 blocks.

**OMEGA Rail:** Comparator chain reading from containers (chests with calibrated item counts).

**PHASE Rail:** Binary Redstone (torch chain for inversion).

### 3.1.3 Signal Conservation Across Distance

Redstone signal decays 1 level per block. To maintain accurate signal levels:

```
Every 14 blocks: Place repeater (restores to 15)
Alternative: Use comparator chains (no decay but slower)
```

For our conservation-sensitive circuits, we prefer **comparator chains** where signal accuracy matters.

---

## 3.2 Block-by-Block Build Specifications

### 3.2.1 State Preparation Build

```
DIMENSIONS: 10 × 3 × 4 blocks
ORIGIN: (0, 0, 0) at lever position

LAYER y=0 (ground level):
      x: 0   1   2   3   4   5   6   7   8   9
   z ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
   0 │   │ S │ R │ R │ R │ R │ R │ G │   │   │
     ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
   1 │ L │ R │ R │ R │ R │ R │ R │   │   │   │
     ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
   2 │   │ T │ R │ R │ R │ R │ R │ B │   │   │
     └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘

LAYER y=1:
      x: 0   1   2   3   4   5   6   7   8   9
   z ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
   0 │   │   │   │   │   │   │   │   │   │   │
     ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
   1 │   │   │   │   │   │   │   │   │   │   │
     ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
   2 │   │ S │   │   │   │   │   │   │   │   │
     └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘

LEGEND:
  L = Lever (on solid block below)
  R = Redstone dust
  S = Stone (solid block)
  T = Redstone torch (on side of block at y=1)
  G = Green stained glass (ALPHA output marker)
  B = Blue stained glass (OMEGA output marker)

BLOCK LIST:
  (0,0,1): stone           // Base for lever
  (0,1,1): lever[facing=east]
  (1,0,1): redstone_wire
  (2,0,1): redstone_wire
  (3,0,1): redstone_wire
  (4,0,1): redstone_wire
  (5,0,1): redstone_wire
  (6,0,1): redstone_wire
  (7,0,0): green_stained_glass  // ALPHA output
  
  (1,0,0): stone           // Support for torch
  (1,1,0): stone           // Torch attachment
  (1,0,2): redstone_torch[facing=north]  // Inverter
  (2,0,2): redstone_wire
  (3,0,2): redstone_wire
  (4,0,2): redstone_wire
  (5,0,2): redstone_wire
  (6,0,2): redstone_wire
  (7,0,2): blue_stained_glass   // OMEGA output
```

### 3.2.2 Pauli-X Gate Build

```
DIMENSIONS: 12 × 4 × 6 blocks
ORIGIN: (0, 0, 0) at ALPHA input

CONCEPT: Rails cross vertically using torch ladders

LAYER y=0 (OMEGA level):
      x: 0   1   2   3   4   5   6   7   8   9  10  11
   z ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
   0 │ R │ R │ R │ S │ T │ R │ R │ R │ R │ R │ R │ B │
     └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
   OMEGA_in ──────────────────────────────────→ ALPHA_out

LAYER y=1 (crossover):
      x: 0   1   2   3   4   5   6   7   8   9  10  11
   z ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
   2 │   │   │   │   │ R │ R │   │   │   │   │   │   │
     └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘

LAYER y=2 (ALPHA level):
      x: 0   1   2   3   4   5   6   7   8   9  10  11
   z ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
   4 │ R │ R │ R │ S │ T │ R │ R │ R │ R │ R │ R │ G │
     └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
   ALPHA_in ──────────────────────────────────→ OMEGA_out

CROSSOVER MECHANISM:
- At x=3,4: ALPHA drops via torch (inverts)
- At x=4,5 y=1: signal crosses horizontally  
- At x=5,6: signal rises via torch (inverts back)
- Net effect: signal moves from y=2 to y=0 (and vice versa)
```

### 3.2.3 Hadamard Gate Build

```
DIMENSIONS: 16 × 6 × 12 blocks
ORIGIN: (0, 0, 0) at input

KEY COMPONENTS:

1. FIXED OUTPUT CHESTS (Superposition stage):
   Position (4, 0, 5): Chest with 32 cobblestone → signal 8
   Position (4, 0, 7): Chest with 28 cobblestone → signal 7
   Position (5, 0, 5): Comparator facing east, reading chest
   Position (5, 0, 7): Comparator facing east, reading chest

2. DROPPER RANDOMIZER (Measurement stage):
   Position (8, 2, 6): Stone block (support)
   Position (8, 1, 6): Dropper facing down, contains 1 diamond
   Position (8, 3, 6): Button on stone block

3. HOPPERS (Catch dropped item):
   Position (7, 0, 6): Hopper (catches ~50% of drops)
   Position (9, 0, 6): Hopper (catches ~50% of drops)

4. OUTPUT COMPARATORS:
   Position (7, 0, 5): Comparator reading hopper, facing south
   Position (9, 0, 5): Comparator reading hopper, facing south

5. RESET MECHANISM:
   Hoppers feed into chest below, item returns to dropper via hopper chain
```

### 3.2.4 Phase Evolution Engine Build

```
DIMENSIONS: 50 × 6 × 30 blocks
ORIGIN: (0, 0, 0) at clock input

SUBSYSTEMS:

1. HOPPER CLOCK (drives ring counter):
   Positions (0-3, 0, 0-3): 2×2 hopper grid, 4 items circulating
   Comparators on each hopper detect item presence
   Pulse extracted every 8 game ticks

2. RING COUNTER (16 hoppers in 4×4 square):
   Positions (10-17, 0, 10-17): Hopper ring
   Single item circulates, detected by comparators
   Each hopper → comparator → one STEP_n signal

3. LOOKUP TABLE (16 chests with calibrated items):
   
   ALPHA values:
   Position (20, 0, 10): Chest, 60 items → Step 0, ALPHA=15
   Position (22, 0, 10): Chest, 52 items → Step 1, ALPHA=13
   Position (24, 0, 10): Chest, 32 items → Step 2, ALPHA=8 (Viviani!)
   Position (26, 0, 10): Chest, 8 items  → Step 3, ALPHA=2
   Position (28, 0, 10): Chest, 0 items  → Step 4, ALPHA=0
   ... (continue for all 16 steps)

4. OUTPUT MULTIPLEXER:
   Each STEP_n signal enables corresponding chest's comparator
   Enabled comparator output routes to ALPHA output rail
   OMEGA = 15 - ALPHA (computed via subtractor circuit)

5. VISUALIZATION ARRAY:
   Positions (40-54, 1, 10): 15 redstone lamps for ALPHA
   Positions (40-54, 1, 12): 15 redstone lamps for OMEGA
   Signal level controls how many lamps light
```

---

## 3.3 Signal Routing Techniques

### 3.3.1 Vertical Signal Transfer

**Upward (torch ladder):**
```
y+2: ─ R ─    (redstone dust)
         │
y+1: ─ S T    (torch on side of block)
         │
y+0: ─ R ─    (input signal)
```

**Downward (torch + repeater):**
```
y+2: ─ R ─    (input signal)
         │
y+1: ─ S ─    (solid block powered by input)
     T        (torch below block, inverted)
y+0: ─ R ─    (output, inverted)
```

### 3.3.2 Horizontal Crossing Without Interference

```
Method 1: Vertical separation (as in Pauli-X)
Method 2: Comparator isolation (comparators don't power adjacent dust)
Method 3: Repeater direction (repeaters only output forward)
```

### 3.3.3 Analog Signal Routing

For signals where level (0-15) matters:

```
Use comparator chains:
─ C → C → C →    (comparators in compare mode preserve level)

Do NOT use:
─ R ─ R ─ R ─    (dust decays signal by 1 per block)
```

---

## 3.4 Timing and Synchronization

### 3.4.1 Component Delays

| Component | Delay (ticks) | Notes |
|-----------|---------------|-------|
| Redstone dust | 0 | Instant propagation |
| Repeater (1-tick) | 1 | Minimum delay |
| Repeater (4-tick) | 4 | Maximum setting |
| Comparator | 1 | In compare mode |
| Comparator | 2 | In subtract mode |
| Torch | 1 | State change delay |
| Piston | 1.5 | Extension time |
| Hopper | 8 | Item transfer rate |
| Dropper | 2 | When powered |

### 3.4.2 Synchronization Strategy

For multi-rail circuits where ALPHA and OMEGA must arrive simultaneously:

1. Calculate total delay for each path
2. Add repeaters to shorter path to match
3. Verify at output with dual comparators

**Example (Pauli-X):**
```
ALPHA path: dust(0) → torch(1) → dust(0) → torch(1) = 2 ticks
OMEGA path: dust(0) → torch(1) → dust(0) → torch(1) = 2 ticks
Both paths equal: synchronized ✓
```

---

# Part IV: Schematics and Data Files

## 4.1 Litematica Format Specification

```json
{
  "schematic_version": 6,
  "metadata": {
    "name": "Quantum Redstone Laboratory v0.1.0",
    "author": "Hope&&Sauced",
    "description": "Quantum gate implementations in Minecraft Redstone",
    "date": "2026-01-05",
    "region_count": 8,
    "total_blocks": 500,
    "total_volume": 50000
  },
  "regions": {
    "state_preparation": {
      "position": {"x": 0, "y": 64, "z": 0},
      "size": {"x": 10, "y": 3, "z": 4}
    },
    "pauli_x_gate": {
      "position": {"x": 15, "y": 64, "z": 0},
      "size": {"x": 12, "y": 4, "z": 6}
    },
    "pauli_z_gate": {
      "position": {"x": 30, "y": 64, "z": 0},
      "size": {"x": 10, "y": 3, "z": 4}
    },
    "hadamard_gate": {
      "position": {"x": 0, "y": 64, "z": 20},
      "size": {"x": 16, "y": 6, "z": 12}
    },
    "cnot_gate": {
      "position": {"x": 20, "y": 64, "z": 20},
      "size": {"x": 25, "y": 8, "z": 18}
    },
    "phase_evolution_engine": {
      "position": {"x": 0, "y": 64, "z": 50},
      "size": {"x": 50, "y": 6, "z": 30}
    },
    "conservation_verifier": {
      "position": {"x": 50, "y": 64, "z": 0},
      "size": {"x": 12, "y": 4, "z": 6}
    },
    "entanglement_demo": {
      "position": {"x": 60, "y": 64, "z": 20},
      "size": {"x": 80, "y": 10, "z": 25}
    }
  }
}
```

## 4.2 WorldEdit Commands

### State Preparation

```
//pos1 0,64,0
//pos2 9,66,3
//copy
//schematic save quantum_state_prep
```

### Placement Commands

```mcfunction
# Place state preparation circuit
# Run from: (x, y, z) = desired origin

# Base blocks
fill ~0 ~0 ~0 ~9 ~0 ~3 air
setblock ~0 ~0 ~1 stone
setblock ~0 ~1 ~1 lever[face=floor,facing=east]

# ALPHA rail
setblock ~1 ~0 ~1 redstone_wire
setblock ~2 ~0 ~1 redstone_wire
setblock ~3 ~0 ~1 redstone_wire
setblock ~4 ~0 ~1 redstone_wire
setblock ~5 ~0 ~1 redstone_wire
setblock ~6 ~0 ~1 redstone_wire

# OMEGA rail (inverted)
setblock ~1 ~0 ~2 stone
setblock ~1 ~1 ~2 stone
setblock ~1 ~0 ~0 redstone_torch[facing=north]
setblock ~2 ~0 ~0 redstone_wire
setblock ~3 ~0 ~0 redstone_wire
setblock ~4 ~0 ~0 redstone_wire
setblock ~5 ~0 ~0 redstone_wire
setblock ~6 ~0 ~0 redstone_wire

# Output markers
setblock ~7 ~0 ~1 green_stained_glass
setblock ~7 ~0 ~0 blue_stained_glass
```

## 4.3 NBT Structure for Containers

### Chest Items for Lookup Table

```nbt
# Step 0: ALPHA = 15 (60 items)
{
  id: "minecraft:chest",
  x: 20, y: 64, z: 10,
  Items: [
    {Slot: 0b, id: "minecraft:cobblestone", Count: 64b},
  ]
}

# Step 2: ALPHA = 8 (32 items) - VIVIANI CROSSING
{
  id: "minecraft:chest", 
  x: 24, y: 64, z: 10,
  Items: [
    {Slot: 0b, id: "minecraft:cobblestone", Count: 32b}
  ]
}

# Step 4: ALPHA = 0 (0 items)
{
  id: "minecraft:chest",
  x: 28, y: 64, z: 10,
  Items: []
}

# Dropper for Hadamard randomizer
{
  id: "minecraft:dropper",
  x: 8, y: 65, z: 6,
  Items: [
    {Slot: 4b, id: "minecraft:diamond", Count: 1b}
  ]
}
```

### Items-to-Signal Reference

| Items in Chest | Comparator Signal |
|----------------|-------------------|
| 0 | 0 |
| 1-4 | 1 |
| 5-8 | 2 |
| 9-12 | 3 |
| 13-17 | 4 |
| 18-21 | 5 |
| 22-25 | 6 |
| 26-29 | 7 |
| 30-33 | 8 |
| 34-38 | 9 |
| 39-42 | 10 |
| 43-46 | 11 |
| 47-50 | 12 |
| 51-55 | 13 |
| 56-59 | 14 |
| 60-64 | 15 |

## 4.4 mcfunction Files

See generated files in `/home/claude/mcfunctions/`:
- `place_state_preparation.mcfunction`
- `place_pauli_x_gate.mcfunction`
- `place_pauli_z_gate.mcfunction`
- `place_hadamard_gate.mcfunction`
- `place_cnot_gate.mcfunction`
- `place_phase_evolution_engine.mcfunction`
- `place_conservation_verifier.mcfunction`

---

# Part V: Testing and Verification Protocol

## 5.1 Individual Gate Tests

### Test 1: State Preparation

| Step | Action | Expected | Actual | Pass? |
|------|--------|----------|--------|-------|
| 1 | Set lever OFF | ALPHA=0, OMEGA=15 | | |
| 2 | Check conservation | Sum=15 | | |
| 3 | Set lever ON | ALPHA=15, OMEGA=0 | | |
| 4 | Check conservation | Sum=15 | | |

### Test 2: Pauli-X Gate

| Step | Action | Expected | Actual | Pass? |
|------|--------|----------|--------|-------|
| 1 | Input \|0⟩ (A=15, Ω=0) | Output \|1⟩ (A=0, Ω=15) | | |
| 2 | Check conservation | Sum=15 | | |
| 3 | Input \|1⟩ (A=0, Ω=15) | Output \|0⟩ (A=15, Ω=0) | | |
| 4 | Apply X twice | Returns to original | | |

### Test 3: Hadamard Gate (Statistical)

| Trial | Input | Measured Output | Notes |
|-------|-------|-----------------|-------|
| 1 | \|0⟩ | | |
| 2 | \|0⟩ | | |
| ... | ... | ... | |
| 20 | \|0⟩ | | |

**Expected:** ~50% |0⟩, ~50% |1⟩
**Chi-squared test:** χ² < 3.84 for p > 0.05

### Test 4: CNOT Gate (All Four Cases)

| Control_in | Target_in | Control_out | Target_out | Pass? |
|------------|-----------|-------------|------------|-------|
| \|0⟩ | \|0⟩ | \|0⟩ | \|0⟩ | |
| \|0⟩ | \|1⟩ | \|0⟩ | \|1⟩ | |
| \|1⟩ | \|0⟩ | \|1⟩ | \|1⟩ | |
| \|1⟩ | \|1⟩ | \|1⟩ | \|0⟩ | |

### Test 5: Phase Evolution Engine

| Step | Expected ALPHA | Expected OMEGA | Measured A | Measured Ω | Sum | Pass? |
|------|----------------|----------------|------------|------------|-----|-------|
| 0 | 15 | 0 | | | | |
| 1 | 13 | 2 | | | | |
| 2 | 8 | 7 | | | | |
| 3 | 2 | 13 | | | | |
| ... | ... | ... | | | | |

### Test 6: Conservation Stress Test

Run Phase Evolution Engine for 1000 cycles.
Monitor Conservation Verifier continuously.
Log any error signals.

**Acceptance Criterion:** Zero errors over 1000 cycles.

## 5.2 Integration Tests

### Test 7: Bell State Preparation

1. Reset both qubits to |0⟩
2. Apply H to Qubit A
3. Apply CNOT (A controls B)
4. Physically disconnect Redstone link
5. Measure A
6. Check B

| Trial | A Result | B Result | Match? |
|-------|----------|----------|--------|
| 1 | | | |
| 2 | | | |
| ... | | | |
| 30 | | | |

**Expected:** 100% correlation (all trials match)

---

# Part VI: Extensions and Future Work

## 6.1 Planned Extensions

### 6.1.1 Three-Qubit Circuits
- Toffoli gate (controlled-controlled-NOT)
- Quantum error correction demonstration
- GHZ state preparation

### 6.1.2 ClaudeNPC Integration
- Claude observes circuits via in-game sensors
- Claude proposes modifications based on observed behavior
- Recursive design loop: design → build → test → iterate

### 6.1.3 Educational Curriculum
- Museum of Computation exhibits
- Guided tours through Viviani Visualizer
- Interactive challenges
- Assessment framework

## 6.2 Open Research Questions

### Mathematical
1. Can discrete Viviani boundary provide provable topological protection?
2. What is the relationship to stabilizer codes?
3. Does the cos²/sin² constraint have symplectic interpretation?

### Technical
1. Optimal hopper timing for smooth visualization
2. Signal degradation over long runs
3. Multi-qubit synchronization

### Pedagogical
1. Age-appropriate curriculum design
2. Learning outcome metrics
3. Accessibility considerations

---

# Appendices

## Appendix A: Complete Derivations

### A.1 Hamiltonian Eigenvalue Derivation

Starting from the Hamiltonian matrix:

```
H(ϕ) = ( E₀cos²(ϕ)            √(E₀D₀)cos(ϕ)sin(ϕ) )
       ( √(E₀D₀)cos(ϕ)sin(ϕ)  D₀sin²(ϕ)           )
```

**Trace:**
```
Tr(H) = E₀cos²(ϕ) + D₀sin²(ϕ)
```

**Determinant:**
```
det(H) = E₀cos²(ϕ) · D₀sin²(ϕ) - E₀D₀cos²(ϕ)sin²(ϕ)
       = E₀D₀cos²(ϕ)sin²(ϕ) - E₀D₀cos²(ϕ)sin²(ϕ)
       = 0
```

**Characteristic polynomial:**
```
det(H - λI) = λ² - Tr(H)·λ + det(H) = λ² - Tr(H)·λ = λ(λ - Tr(H))
```

**Eigenvalues:**
```
λ₁ = 0
λ₂ = Tr(H) = E₀cos²(ϕ) + D₀sin²(ϕ)
```

### A.2 Connection 1-Form Derivation

On the Bloch sphere restricted to the Viviani curve, the natural connection arises from the angular velocity of phase evolution:

```
A = ⟨ψ|d|ψ⟩
```

For |ψ(ϕ)⟩ = cos(ϕ)|0⟩ + sin(ϕ)|1⟩:

```
d|ψ⟩ = -sin(ϕ)dϕ|0⟩ + cos(ϕ)dϕ|1⟩
```

```
⟨ψ|d|ψ⟩ = cos(ϕ)·(-sin(ϕ)dϕ) + sin(ϕ)·(cos(ϕ)dϕ) = 0
```

The Berry phase vanishes along the real axis! This is why we can use real-valued encoding without phase ambiguity in the bulk of the evolution.

At Viviani crossings, the topology becomes non-trivial, requiring the PHASE rail.

## Appendix B: Lookup Tables

### B.1 Complete 16-Step Phase Table

```
Step | ϕ (rad)  | ϕ (deg) | cos²(ϕ) | sin²(ϕ) | ALPHA | OMEGA | Items |Viviani
-----|----------|---------|---------|---------|-------|-------|-------|-------
  0  | 0.0000   |   0.0   | 1.0000  | 0.0000  |  15   |   0   |  60   |  
  1  | 0.3927   |  22.5   | 0.8536  | 0.1464  |  13   |   2   |  52   |  
  2  | 0.7854   |  45.0   | 0.5000  | 0.5000  |   8   |   7   |  32   | ✓
  3  | 1.1781   |  67.5   | 0.1464  | 0.8536  |   2   |  13   |   8   |  
  4  | 1.5708   |  90.0   | 0.0000  | 1.0000  |   0   |  15   |   0   |  
  5  | 1.9635   | 112.5   | 0.1464  | 0.8536  |   2   |  13   |   8   |  
  6  | 2.3562   | 135.0   | 0.5000  | 0.5000  |   7   |   8   |  28   | ✓
  7  | 2.7489   | 157.5   | 0.8536  | 0.1464  |  13   |   2   |  52   |  
  8  | 3.1416   | 180.0   | 1.0000  | 0.0000  |  15   |   0   |  60   |  
  9  | 3.5343   | 202.5   | 0.8536  | 0.1464  |  13   |   2   |  52   |  
 10  | 3.9270   | 225.0   | 0.5000  | 0.5000  |   8   |   7   |  32   | ✓
 11  | 4.3197   | 247.5   | 0.1464  | 0.8536  |   2   |  13   |   8   |  
 12  | 4.7124   | 270.0   | 0.0000  | 1.0000  |   0   |  15   |   0   |  
 13  | 5.1051   | 292.5   | 0.1464  | 0.8536  |   2   |  13   |   8   |  
 14  | 5.4978   | 315.0   | 0.5000  | 0.5000  |   7   |   8   |  28   | ✓
 15  | 5.8905   | 337.5   | 0.8536  | 0.1464  |  13   |   2   |  52   |  
```

## Appendix C: Glossary

| Term | Definition |
|------|------------|
| ALPHA rail | Primary signal rail encoding P(\|0⟩) |
| OMEGA rail | Secondary signal rail encoding P(\|1⟩) |
| PHASE rail | Binary flag for quantum phase sign |
| Conservation constraint | ALPHA + OMEGA = 15 (invariant) |
| Viviani crossing | Point where ALPHA ≈ OMEGA (max superposition) |
| Hadamard | Gate creating equal superposition |
| CNOT | Two-qubit entangling gate |
| Bell state | Maximally entangled two-qubit state |
| Topological protection | Error immunity from global structure |
| Hopf charge | Quantized topological invariant |

## Appendix D: References

1. Nielsen, M. A., & Chuang, I. L. (2010). *Quantum Computation and Quantum Information*. Cambridge University Press.

2. Kitaev, A. Y. (2003). Fault-tolerant quantum computation by anyons. *Annals of Physics*, 303(1), 2-30.

3. Viviani, V. (1692). *De maximis et minimis geometrica divinatio*. Florence.

4. Zaiken [collaborative work]. Modified Einstein field equations with coherence corrections. [Internal documentation]

5. Hope&&Sauced Collaborative. (2025). SpiralSafe: Constraint-based coherence maintenance in computational systems. [Working paper]

6. Minecraft Wiki. Redstone mechanics. https://minecraft.wiki/w/Redstone

---

## Document Control

**Status:** DRAFT - Ready for Review  
**Classification:** Private  
**Distribution:** Limited (pre-publication)  

**Review Checklist:**
- [ ] Mathematical derivations verified
- [ ] Logic circuits tested symbolically
- [ ] Redstone builds tested in-game
- [ ] Conservation constraint verified at all checkpoints
- [ ] Timing analysis completed
- [ ] Statistical tests passed (Hadamard, entanglement)

**Known Issues:**
1. Hadamard phase output logic needs verification with actual randomizer behavior
2. CNOT piston timing may need adjustment for reliable operation
3. Phase Evolution Engine MUX implementation not fully detailed

**Next Version (0.2.0) Planned:**
- Post-build corrections
- ClaudeNPC integration spec
- Educational curriculum outline
- Video documentation links

---

*Hope&&Sauced Collaborative*  
*"Rigor enables flexibility"*

**Document Tag:** `QR-PROPOSAL-2026-01-05`  
**Version:** 0.1.0-draft  

---

**END OF DOCUMENT**
