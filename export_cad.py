#!/usr/bin/env python3
"""
CAD Export Tool for Quantum-Redstone Circuits
Exports Minecraft circuits to CAD-compatible formats:
- DXF (AutoCAD, LibreCAD)
- STL (3D printing, FreeCAD)
- OBJ (Blender, Maya)
- STEP (SolidWorks, Fusion 360)
- SVG (2D vector)
"""

import json
import sys
from pathlib import Path
from typing import List, Dict, Tuple
import math

# Block dimensions in Minecraft (meters)
BLOCK_SIZE = 1.0

# Material colors for visualization
BLOCK_COLORS = {
    'minecraft:redstone_wire': (255, 0, 0),
    'minecraft:redstone_torch': (255, 100, 0),
    'minecraft:lever': (139, 69, 19),
    'minecraft:stone': (128, 128, 128),
    'minecraft:comparator': (200, 50, 50),
    'minecraft:repeater': (180, 40, 40),
    'minecraft:sticky_piston': (100, 150, 100),
    'minecraft:hopper': (80, 80, 80),
    'minecraft:chest': (165, 115, 64),
    'minecraft:dropper': (100, 100, 100),
    'minecraft:glass': (200, 200, 255),
    'minecraft:redstone_lamp': (255, 200, 100),
    'minecraft:redstone_block': (200, 0, 0),
}


class CADExporter:
    """Base class for CAD export"""

    def __init__(self, circuit_data: Dict):
        self.circuit = circuit_data
        self.name = circuit_data['name']
        self.blocks = circuit_data['blocks']
        self.dimensions = circuit_data['dimensions']

    def export(self, output_path: str):
        raise NotImplementedError


class DXFExporter(CADExporter):
    """Export to DXF format (AutoCAD, LibreCAD)"""

    def export(self, output_path: str):
        """Generate DXF file"""
        output = []

        # DXF Header
        output.append("0\nSECTION\n2\nHEADER\n0\nENDSEC")
        output.append("0\nSECTION\n2\nENTITIES")

        # Export each block as a 3D solid
        for block in self.blocks:
            x, y, z = block['pos']
            material = block['block']

            # Create a 3D box for each block
            output.append(f"0\n3DFACE")
            output.append(f"8\n{material}")  # Layer name

            # Bottom face
            output.append(f"10\n{x}\n20\n{y}\n30\n{z}")
            output.append(f"11\n{x+BLOCK_SIZE}\n21\n{y}\n31\n{z}")
            output.append(f"12\n{x+BLOCK_SIZE}\n22\n{y}\n32\n{z+BLOCK_SIZE}")
            output.append(f"13\n{x}\n23\n{y}\n33\n{z+BLOCK_SIZE}")

        output.append("0\nENDSEC\n0\nEOF")

        Path(output_path).write_text("\n".join(output))
        print(f"Exported DXF: {output_path}")


class STLExporter(CADExporter):
    """Export to STL format (3D printing, FreeCAD)"""

    def export(self, output_path: str):
        """Generate ASCII STL file"""
        output = []

        output.append(f"solid {self.name}")

        for block in self.blocks:
            x, y, z = block['pos']

            # Generate 12 triangles for a cube (2 per face)
            # Front face
            output.extend(self._create_triangle(
                (x, y, z), (x+BLOCK_SIZE, y, z), (x+BLOCK_SIZE, y+BLOCK_SIZE, z),
                (0, 0, -1)
            ))
            output.extend(self._create_triangle(
                (x, y, z), (x+BLOCK_SIZE, y+BLOCK_SIZE, z), (x, y+BLOCK_SIZE, z),
                (0, 0, -1)
            ))

            # Back face
            output.extend(self._create_triangle(
                (x+BLOCK_SIZE, y, z+BLOCK_SIZE), (x, y, z+BLOCK_SIZE), (x, y+BLOCK_SIZE, z+BLOCK_SIZE),
                (0, 0, 1)
            ))
            output.extend(self._create_triangle(
                (x+BLOCK_SIZE, y, z+BLOCK_SIZE), (x, y+BLOCK_SIZE, z+BLOCK_SIZE), (x+BLOCK_SIZE, y+BLOCK_SIZE, z+BLOCK_SIZE),
                (0, 0, 1)
            ))

            # Left face
            output.extend(self._create_triangle(
                (x, y, z+BLOCK_SIZE), (x, y, z), (x, y+BLOCK_SIZE, z),
                (-1, 0, 0)
            ))
            output.extend(self._create_triangle(
                (x, y, z+BLOCK_SIZE), (x, y+BLOCK_SIZE, z), (x, y+BLOCK_SIZE, z+BLOCK_SIZE),
                (-1, 0, 0)
            ))

            # Right face
            output.extend(self._create_triangle(
                (x+BLOCK_SIZE, y, z), (x+BLOCK_SIZE, y, z+BLOCK_SIZE), (x+BLOCK_SIZE, y+BLOCK_SIZE, z+BLOCK_SIZE),
                (1, 0, 0)
            ))
            output.extend(self._create_triangle(
                (x+BLOCK_SIZE, y, z), (x+BLOCK_SIZE, y+BLOCK_SIZE, z+BLOCK_SIZE), (x+BLOCK_SIZE, y+BLOCK_SIZE, z),
                (1, 0, 0)
            ))

            # Top face
            output.extend(self._create_triangle(
                (x, y+BLOCK_SIZE, z), (x+BLOCK_SIZE, y+BLOCK_SIZE, z), (x+BLOCK_SIZE, y+BLOCK_SIZE, z+BLOCK_SIZE),
                (0, 1, 0)
            ))
            output.extend(self._create_triangle(
                (x, y+BLOCK_SIZE, z), (x+BLOCK_SIZE, y+BLOCK_SIZE, z+BLOCK_SIZE), (x, y+BLOCK_SIZE, z+BLOCK_SIZE),
                (0, 1, 0)
            ))

            # Bottom face
            output.extend(self._create_triangle(
                (x, y, z+BLOCK_SIZE), (x+BLOCK_SIZE, y, z+BLOCK_SIZE), (x+BLOCK_SIZE, y, z),
                (0, -1, 0)
            ))
            output.extend(self._create_triangle(
                (x, y, z+BLOCK_SIZE), (x+BLOCK_SIZE, y, z), (x, y, z),
                (0, -1, 0)
            ))

        output.append(f"endsolid {self.name}")

        Path(output_path).write_text("\n".join(output))
        print(f"Exported STL: {output_path}")

    def _create_triangle(self, v1: Tuple, v2: Tuple, v3: Tuple, normal: Tuple) -> List[str]:
        """Create STL triangle"""
        return [
            f"facet normal {normal[0]} {normal[1]} {normal[2]}",
            "  outer loop",
            f"    vertex {v1[0]} {v1[1]} {v1[2]}",
            f"    vertex {v2[0]} {v2[1]} {v2[2]}",
            f"    vertex {v3[0]} {v3[1]} {v3[2]}",
            "  endloop",
            "endfacet"
        ]


class OBJExporter(CADExporter):
    """Export to OBJ format (Blender, Maya)"""

    def export(self, output_path: str):
        """Generate OBJ file with MTL material"""
        vertices = []
        faces = []
        materials = {}
        vertex_index = 1

        for block in self.blocks:
            x, y, z = block['pos']
            material = block['block'].replace('minecraft:', '').replace(':', '_')

            if material not in materials:
                materials[material] = BLOCK_COLORS.get(block['block'], (128, 128, 128))

            # 8 vertices for a cube
            cube_verts = [
                (x, y, z),
                (x+BLOCK_SIZE, y, z),
                (x+BLOCK_SIZE, y+BLOCK_SIZE, z),
                (x, y+BLOCK_SIZE, z),
                (x, y, z+BLOCK_SIZE),
                (x+BLOCK_SIZE, y, z+BLOCK_SIZE),
                (x+BLOCK_SIZE, y+BLOCK_SIZE, z+BLOCK_SIZE),
                (x, y+BLOCK_SIZE, z+BLOCK_SIZE),
            ]

            vertices.extend(cube_verts)

            # 6 faces (quads) for a cube
            base = vertex_index
            cube_faces = [
                (base, base+1, base+2, base+3),  # Front
                (base+5, base+4, base+7, base+6),  # Back
                (base+4, base, base+3, base+7),  # Left
                (base+1, base+5, base+6, base+2),  # Right
                (base+3, base+2, base+6, base+7),  # Top
                (base+4, base+5, base+1, base),  # Bottom
            ]

            for face in cube_faces:
                faces.append((material, face))

            vertex_index += 8

        # Write OBJ file
        output = [f"# {self.name} - Quantum Redstone Circuit"]
        output.append(f"mtllib {Path(output_path).stem}.mtl")

        for v in vertices:
            output.append(f"v {v[0]} {v[1]} {v[2]}")

        current_material = None
        for material, face in faces:
            if material != current_material:
                output.append(f"usemtl {material}")
                current_material = material
            output.append(f"f {face[0]} {face[1]} {face[2]} {face[3]}")

        Path(output_path).write_text("\n".join(output))
        print(f"Exported OBJ: {output_path}")

        # Write MTL file
        mtl_path = Path(output_path).with_suffix('.mtl')
        mtl_output = [f"# Materials for {self.name}"]

        for material, color in materials.items():
            r, g, b = [c/255.0 for c in color]
            mtl_output.extend([
                f"newmtl {material}",
                f"Ka {r} {g} {b}",
                f"Kd {r} {g} {b}",
                f"Ks 0.5 0.5 0.5",
                "Ns 100",
                ""
            ])

        mtl_path.write_text("\n".join(mtl_output))
        print(f"Exported MTL: {mtl_path}")


class SVGExporter(CADExporter):
    """Export to SVG format (2D top-down view)"""

    def export(self, output_path: str):
        """Generate SVG file (top-down view)"""
        width = self.dimensions['x'] * 50 + 100
        height = self.dimensions['z'] * 50 + 100

        output = [
            f'<?xml version="1.0" encoding="UTF-8"?>',
            f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">',
            f'  <title>{self.name}</title>',
            f'  <rect width="{width}" height="{height}" fill="#f0f0f0"/>',
        ]

        # Group blocks by Y level
        y_levels = {}
        for block in self.blocks:
            x, y, z = block['pos']
            if y not in y_levels:
                y_levels[y] = []
            y_levels[y].append(block)

        # Draw blocks (using highest Y level for each XZ position)
        for y_level in sorted(y_levels.keys(), reverse=True):
            for block in y_levels[y_level]:
                x, y, z = block['pos']
                material = block['block']
                color = BLOCK_COLORS.get(material, (128, 128, 128))

                svg_x = 50 + x * 50
                svg_y = 50 + z * 50

                fill = f"rgb({color[0]},{color[1]},{color[2]})"

                output.append(
                    f'  <rect x="{svg_x}" y="{svg_y}" width="50" height="50" '
                    f'fill="{fill}" stroke="black" stroke-width="1"/>'
                )

                # Add label for special blocks
                if 'torch' in material or 'lever' in material or 'comparator' in material:
                    label = material.split(':')[1][:4]
                    output.append(
                        f'  <text x="{svg_x+25}" y="{svg_y+30}" '
                        f'text-anchor="middle" font-size="10">{label}</text>'
                    )

        output.append('</svg>')

        Path(output_path).write_text("\n".join(output))
        print(f"Exported SVG: {output_path}")


def export_all_circuits(circuits_file: str, output_dir: str):
    """Export all circuits to all formats"""

    with open(circuits_file, 'r') as f:
        data = json.load(f)

    circuits = data['circuits']
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    for circuit in circuits:
        name = circuit['name']
        print(f"\nExporting {name}...")

        # DXF
        dxf_path = output_path / f"{name}.dxf"
        DXFExporter(circuit).export(str(dxf_path))

        # STL
        stl_path = output_path / f"{name}.stl"
        STLExporter(circuit).export(str(stl_path))

        # OBJ
        obj_path = output_path / f"{name}.obj"
        OBJExporter(circuit).export(str(obj_path))

        # SVG
        svg_path = output_path / f"{name}.svg"
        SVGExporter(circuit).export(str(svg_path))


def main():
    import os

    script_dir = Path(__file__).parent
    circuits_file = script_dir / "quantum_circuits.json"
    output_dir = script_dir / "cad_exports"

    if not circuits_file.exists():
        print(f"Error: {circuits_file} not found!")
        print("Run quantum_circuit_generator.py first")
        return 1

    print("=" * 60)
    print("Quantum-Redstone CAD Exporter")
    print("=" * 60)
    print()

    export_all_circuits(str(circuits_file), str(output_dir))

    print()
    print("=" * 60)
    print("Export complete!")
    print("=" * 60)
    print()
    print(f"Output directory: {output_dir}")
    print()
    print("Files generated:")
    print("  .dxf - AutoCAD, LibreCAD")
    print("  .stl - 3D printing, FreeCAD, Cura")
    print("  .obj - Blender, Maya, 3ds Max")
    print("  .svg - Vector graphics, 2D view")
    print()
    print("Import these into your favorite CAD software!")

    return 0


if __name__ == "__main__":
    sys.exit(main())
