---
entity_id: "complex.ecocyc.CPLX-3945"
entity_type: "complex"
name: "curli secretion and assembly complex"
source_database: "EcoCyc"
source_id: "CPLX-3945"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# curli secretion and assembly complex

`complex.ecocyc.CPLX-3945`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX-3945`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0AE98|protein.P0AE98]], [[protein.P0AEA2|protein.P0AEA2]]

## Enriched Summary

Curli are extracellular amyloid fibres involved in adherence and biofilm formation in E. coli K-12 . The curli specific genes are present in two divergently transcribed operons, csgDEFG and csgBAC which encode the structural, accessory and regulatory proteins of the curli biosynthetic pathway (reviewed in ). CsgG and CsgF form a stable secretion channel complex which traverses the outer membrane; the proteins bind together at a 9:9 stoichiometric ratio . Nonameric CsgG forms a 36 stranded β-barrel in the OM with a large solvent accessible cavity located on the periplasmic side; the cavity is open to the periplasm but is constricted to form a pore at the membrane interface . The N-terminal domain of CsgF inserts into the CsgG complex to form a second pore inside the CsgG channel; the C-terminal domain of CsgF is located on the extracellular side of the CsgG channel and is responsible for binding to the minor curlin subunit G6547-MONOMER "CsgB" (and further ). G6545-MONOMER "CsgE" forms a nonameric structure which binds to the periplasmic face of the CsgG complex thus forming an enclosed chamber ; CsgE also binds to the major curlin subunit EG11489-MONOMER "CsgA" and it is proposed that CsgE may act to capture and confine CsgA into the CsgG periplasmic chamber for outward translocation (see also )...

## Biological Role

Catalyzes RXN-5068 (reaction.ecocyc.RXN-5068).

## Annotation

Curli are extracellular amyloid fibres involved in adherence and biofilm formation in E. coli K-12 . The curli specific genes are present in two divergently transcribed operons, csgDEFG and csgBAC which encode the structural, accessory and regulatory proteins of the curli biosynthetic pathway (reviewed in ). CsgG and CsgF form a stable secretion channel complex which traverses the outer membrane; the proteins bind together at a 9:9 stoichiometric ratio . Nonameric CsgG forms a 36 stranded β-barrel in the OM with a large solvent accessible cavity located on the periplasmic side; the cavity is open to the periplasm but is constricted to form a pore at the membrane interface . The N-terminal domain of CsgF inserts into the CsgG complex to form a second pore inside the CsgG channel; the C-terminal domain of CsgF is located on the extracellular side of the CsgG channel and is responsible for binding to the minor curlin subunit G6547-MONOMER "CsgB" (and further ). G6545-MONOMER "CsgE" forms a nonameric structure which binds to the periplasmic face of the CsgG complex thus forming an enclosed chamber ; CsgE also binds to the major curlin subunit EG11489-MONOMER "CsgA" and it is proposed that CsgE may act to capture and confine CsgA into the CsgG periplasmic chamber for outward translocation (see also ).

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-5068|reaction.ecocyc.RXN-5068]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P0AE98|protein.P0AE98]] `EcoCyc` `database` - EcoCyc component coefficient=9 | EcoCyc protcplxs.col coefficient=9 | EcoCyc transporter component coefficient=9
- `is_component_of` <-- [[protein.P0AEA2|protein.P0AEA2]] `EcoCyc` `database` - EcoCyc component coefficient=9 | EcoCyc protcplxs.col coefficient=9 | EcoCyc transporter component coefficient=9

## External IDs

- `EcoCyc:CPLX-3945`
- `PDB:7BRM`
- `PDB:6SI7`
- `PDB:6LQJ`
- `PDB:6LQH`
- `PDB:6L7C`
- `PDB:6L7A`
- `PDB:7BRM`
- `PDB:6LQJ`
- `QSPROTEOME:QS00182755`

## Notes

9*protein.P0AE98|9*protein.P0AEA2
