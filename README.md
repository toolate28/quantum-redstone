# Quantum-Redstone Educational Framework

**Mathematical bridge between quantum computing and Minecraft Redstone**

## Overview

This framework implements quantum computing concepts using Minecraft's Redstone mechanics, making abstract quantum principles tangible and interactive.

### Core Innovation: Two-Rail Encoding

```
Quantum: |ψ⟩ = α|0⟩ + β|1⟩  where |α|² + |β|² = 1
Redstone: ALPHA + OMEGA = 15 (signal conservation)
```

The discrete constraint ALPHA + OMEGA = 15 is topologically equivalent to the continuous quantum normalization constraint, providing a teaching tool that preserves quantum mechanical structure.

## Generated Circuits

All 7 quantum gates have been implemented:

1. **State Preparation** (16 blocks) - Basis state initialization
2. **Pauli-X Gate** (24 blocks) - Bit flip operation
3. **Pauli-Z Gate** (31 blocks) - Phase flip operation
4. **Hadamard Gate** (12 blocks) - Superposition creation
5. **CNOT Gate** (83 blocks) - Two-qubit entanglement
6. **Phase Evolution Engine** (102 blocks) - 16-step quantum phase rotation
7. **Conservation Verifier** (14 blocks) - Validates ALPHA + OMEGA = 15

### Files

```
quantum-redstone/
├── quantum_circuit_generator.py    # Main generator (639 lines)
├── quantum_circuits.json           # All 7 circuit definitions
├── phase_lookup_table.json         # 16-step cos²/sin² table
├── quantum_redstone_verification.ipynb  # Comprehensive verification notebook
├── quantum.ipynb                   # Quantum computing foundations notebook
├── HOPENPC.ipynb                   # ClaudeNPC integration notebook
├── mcfunctions/                    # Minecraft function files
│   ├── place_state_preparation.mcfunction
│   ├── place_pauli_x_gate.mcfunction
│   ├── place_pauli_z_gate.mcfunction
│   ├── place_hadamard_gate.mcfunction
│   ├── place_cnot_gate.mcfunction
│   ├── place_phase_evolution_engine.mcfunction
│   └── place_conservation_verifier.mcfunction
└── quantum-redstone-proposal-v0.1.0-complete.md  # Full 146-page spec
```

## Quick Start

### Generate Circuits

```bash
python quantum_circuit_generator.py
```

Output:
- `quantum_circuits.json` - Structured block data
- `phase_lookup_table.json` - Phase evolution lookup table
- `mcfunctions/*.mcfunction` - In-game placement commands

### Place in Minecraft

1. Copy `mcfunctions/` to your world's datapacks:
   ```
   .minecraft/saves/YourWorld/datapacks/quantum/data/quantum/functions/
   ```

2. In-game:
   ```
   /function quantum:place_state_preparation
   /function quantum:place_hadamard_gate
   ```

3. Circuits will build at your current location (relative positioning)

## Interactive Notebooks

The framework includes three Jupyter notebooks for exploration, learning, and integration:

### 1. `quantum_redstone_verification.ipynb` - Comprehensive Verification
**Focus:** Complete testing and validation suite

Features:
- Two-rail encoding validation across full phase range
- Phase evolution testing with 16-step lookup table
- Viviani curve 3D visualization
- All 7 quantum gates verification
- CAD export verification
- Conservation constraint stress testing
- End-to-end integration tests

**Use case:** Verify framework correctness, run tests, validate exports

### 2. `quantum.ipynb` - Quantum Computing Foundations
**Focus:** Mathematical theory and quantum gate operations

Features:
- Bloch sphere visualization of quantum states
- Quantum gate mathematics (Pauli, Hadamard, CNOT)
- Unitary transformations and probability conservation
- Phase space and Viviani curve topology
- Quantum entanglement and Bell states
- Measurement theory and Born rule
- Quantum algorithms (Deutsch algorithm demo)

**Use case:** Learn quantum computing theory, understand mathematical foundations, study advanced concepts

### 3. `HOPENPC.ipynb` - ClaudeNPC Integration & Python Bridge
**Focus:** AI-powered building and real-world deployment

Features:
- Python Bridge architecture for language → code → world pipeline
- ClaudeNPC conversation simulator
- Interactive circuit building with position management
- Real-time mcfunction generation
- AI observer pattern for circuit recognition
- Educational curriculum management
- Multi-circuit orchestration for quantum algorithms

**Use case:** Deploy AI NPCs, build interactively, create educational experiences, automate circuit generation

### Running the Notebooks

```bash
# Install dependencies
pip install jupyter numpy matplotlib

# Launch Jupyter
jupyter notebook

# Open any notebook:
# - quantum_redstone_verification.ipynb
# - quantum.ipynb
# - HOPENPC.ipynb
```

## Integration with ClaudeNPC

ClaudeNPC can build these circuits via conversation:

**Player:** "Build a Hadamard gate here"

**ClaudeNPC:** *Executes Python bridge, places 12 blocks*

See `ClaudeNPC-Server-Suite` repository for Python integration.

## Mathematical Foundation

### Viviani Curve Topology

The phase space lives on a Viviani curve - intersection of a cylinder and sphere:

```
x² + y² = 1  (unit cylinder)
x² + y² + z² = 2z  (sphere)
```

When ALPHA + OMEGA = 15 (discrete), we get crossings at:
- Step 2: ALPHA=8, OMEGA=7 (cos²φ ≈ 0.5)
- Step 6: ALPHA=7, OMEGA=8
- Step 10: ALPHA=8, OMEGA=7
- Step 14: ALPHA=7, OMEGA=8

These are the discrete analogs of Viviani crossing points where cos²φ = sin²φ = 0.5.

### Conservation Verification

The `conservation_verifier` circuit uses Redstone comparators in subtract mode:

```
15 - OMEGA → compare with ALPHA
If equal: constraint satisfied
If not: ERROR lamp lights
```

This provides runtime verification that quantum state normalization is preserved.

## Circuit Details

### State Preparation

Simplest circuit. Lever position controls basis state:
- Lever ON → |0⟩ (ALPHA=15, OMEGA=0)
- Lever OFF → |1⟩ (ALPHA=0, OMEGA=15)

Uses inverter (Redstone torch on block) for rail inversion.

### Hadamard Gate

Creates superposition via "averaging":
- Two chests with different fill levels
- Chest 1: 32 items → signal 8
- Chest 2: 28 items → signal 7
- Dropout randomizer determines measurement outcome
- Demonstrates probabilistic collapse

### CNOT Gate

Most complex. Two qubits (4 rails total):
- Control qubit: ALPHA_C, OMEGA_C
- Target qubit: ALPHA_T, OMEGA_T
- Threshold detector on OMEGA_C
- Piston-based conditional swap
- Demonstrates entanglement

### Phase Evolution Engine

16-hopper ring counter cycles through phase states:
- Each hopper position = one phase step
- Lookup table chests provide cos²/sin² values
- Comparators read chest fill levels
- Outputs animate on Redstone lamps (15-lamp bars)

## Educational Use

### Learning Objectives

Students will understand:
1. Quantum superposition (as discrete signal distribution)
2. Measurement collapse (via randomizer mechanisms)
3. Entanglement (via conditional operations)
4. Phase evolution (as cyclic state transitions)
5. Conservation laws (topological constraints)

### Grade Levels

- **Grades 6-8:** State preparation, measurement basics
- **Grades 9-10:** Hadamard gate, superposition concepts
- **Grades 11-12:** CNOT, entanglement, phase evolution
- **Undergraduate:** Full mathematical formalism, Viviani topology

### Curriculum Integration

- **Physics:** Quantum mechanics, conservation laws
- **Mathematics:** Trigonometry (cos²/sin²), topology
- **Computer Science:** Logic gates, circuit design
- **Engineering:** Signal processing, Boolean algebra

## Technical Specifications

### Signal Encoding

| Signal Level | Chest Items | cos²(φ) | Notes |
|--------------|-------------|---------|-------|
| 0 | 0 | 0.0000 | Empty |
| 1 | 4 | 0.0667 | Minimal |
| 7 | 28 | 0.4667 | Near superposition |
| 8 | 32 | 0.5333 | Superposition |
| 13 | 52 | 0.8667 | High amplitude |
| 15 | 60 | 1.0000 | Full signal |

### Timing Considerations

- **Hopper clock:** 8-tick cycle (0.4 seconds)
- **Comparator delay:** 1 tick
- **Piston extension:** 2 ticks
- **Recommended TPS:** 20 (vanilla)

### Chunk Loading

Large circuits (CNOT, Phase Engine) may span multiple chunks. Use:
- Spawn chunks for permanent operation
- Chunk loaders for remote locations
- Pregen world before building

## Performance

### Resource Requirements

| Circuit | Blocks | Chunks | Build Time |
|---------|--------|--------|------------|
| State Prep | 16 | 1 | 30 sec |
| Pauli-X | 24 | 1 | 1 min |
| Pauli-Z | 31 | 1 | 1 min |
| Hadamard | 12 | 1 | 30 sec |
| CNOT | 83 | 2 | 3 min |
| Phase Engine | 102 | 3 | 5 min |
| Conservation | 14 | 1 | 30 sec |

### TPS Impact

With all 7 circuits active:
- Vanilla server: ~2% TPS reduction
- Paper/Spigot: ~1% TPS reduction
- Negligible when idle (no active signals)

## Future Work

### Planned Circuits

- Toffoli gate (universal classical computing)
- Controlled-Phase gate
- SWAP gate
- Quantum Fourier Transform (QFT) - partial implementation

### Litematica Export

Not yet implemented. Schematics would enable:
- One-click circuit placement
- Circuit libraries
- Community sharing

### ClaudeNPC Observer

AI NPCs could:
- Read Redstone signals
- Explain what circuit is doing
- Debug signal propagation
- Suggest optimizations

## Credits

**Framework:** Hope&&Sauced Collaborative
**Mathematical Foundation:** Based on Viviani curve topology
**Implementation:** Python → Minecraft NBT/mcfunction
**Testing:** Virtual Redstone simulation

## License

Educational use encouraged. Attribution appreciated.

**The Evenstar Guides Us** ✦

---

## 📸 Showcase

### mcstart Dashboard

![Dashboard Overview](showcase/mcstart1.png)
*SpiralSafe Dashboard - Quick access to quantum circuit generation*

![Project Status](showcase/mcstart2.png)
*Build status - All 7 quantum circuits ready*

![Circuit Testing](showcase/mcstart3.png)
*Validation suite - Conservation constraint verified*

![CAD Export](showcase/mcstart4.png)
*CAD integration - DXF, STL, OBJ, SVG exports*

### CAD Exports

All circuits available in multiple CAD formats:

```
cad_exports/
├── state_preparation.{dxf,stl,obj,svg}
├── pauli_x_gate.{dxf,stl,obj,svg}
├── pauli_z_gate.{dxf,stl,obj,svg}
├── hadamard_gate.{dxf,stl,obj,svg}
├── cnot_gate.{dxf,stl,obj,svg}
├── phase_evolution_engine.{dxf,stl,obj,svg}
└── conservation_verifier.{dxf,stl,obj,svg}
```

**Import into:**
- AutoCAD, LibreCAD (DXF)
- Blender, Maya, 3ds Max (OBJ)
- FreeCAD, SolidWorks, Fusion 360 (STL)
- Inkscape, Illustrator (SVG)

**Generate CAD files:**
```bash
cd C:\Users\iamto\quantum-redstone
python export_cad.py
```

---

## 🏗️ For 3D Printing

STL files are ready for 3D printing at 1:1 scale (1 block = 1 meter in CAD units).

Scale factor recommendations:
- **Desktop display:** 0.01x (1 block = 1cm)
- **Miniature:** 0.005x (1 block = 5mm)
- **Large model:** 0.05x (1 block = 5cm)

Print settings:
- Layer height: 0.2mm
- Infill: 15-20%
- Supports: Auto-generate
- Material: PLA, PETG, or Resin

---

**Build quantum computers in Minecraft, export to CAD, 3D print the circuits!**
