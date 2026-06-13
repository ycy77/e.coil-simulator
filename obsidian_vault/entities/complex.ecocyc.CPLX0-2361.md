---
entity_id: "complex.ecocyc.CPLX0-2361"
entity_type: "complex"
name: "DNA polymerase III, core enzyme"
source_database: "EcoCyc"
source_id: "CPLX0-2361"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-CYTOSOL-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# DNA polymerase III, core enzyme

`complex.ecocyc.CPLX0-2361`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-2361`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-CYTOSOL-GN
- Complex type: `structural`
- Components: [[protein.P10443|protein.P10443]], [[protein.P03007|protein.P03007]], [[protein.P0ABS8|protein.P0ABS8]]

## Enriched Summary

The DNA polymerase III core enzyme contains one each of the alpha, epsilon and theta subunits and can carry out the basic polymerase and exonuclease activities of polymerase III . Based on yeast two-hybrid data, both alpha and theta interact with epsilon, but not each other . The interaction between epsilon and theta has been examined via lanthanide-labeling NMR . In a cell-free translation system, theta is required for the generation of soluble epsilon. An NMR analysis of cell-free DNA core enzyme shows epsilon connects to alpha via a flexible linker region . The DNA polymerase III core enzyme contains one each of the alpha, epsilon and theta subunits and can carry out the basic polymerase and exonuclease activities of polymerase III . Based on yeast two-hybrid data, both alpha and theta interact with epsilon, but not each other . The interaction between epsilon and theta has been examined via lanthanide-labeling NMR . In a cell-free translation system, theta is required for the generation of soluble epsilon. An NMR analysis of cell-free DNA core enzyme shows epsilon connects to alpha via a flexible linker region .

## Biological Role

Component of DNA polymerase III, holoenzyme (complex.ecocyc.CPLX0-3803).

## Annotation

The DNA polymerase III core enzyme contains one each of the alpha, epsilon and theta subunits and can carry out the basic polymerase and exonuclease activities of polymerase III . Based on yeast two-hybrid data, both alpha and theta interact with epsilon, but not each other . The interaction between epsilon and theta has been examined via lanthanide-labeling NMR . In a cell-free translation system, theta is required for the generation of soluble epsilon. An NMR analysis of cell-free DNA core enzyme shows epsilon connects to alpha via a flexible linker region .

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3803|complex.ecocyc.CPLX0-3803]] `EcoCyc` `database` - EcoCyc component coefficient=3

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P03007|protein.P03007]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0ABS8|protein.P0ABS8]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P10443|protein.P10443]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-2361`
- `PDB:4GX9`
- `PDB:4GX8`
- `PDB:5FKW`
- `PDB:5FKV`
- `PDB:5FKU`
- `PDB:5M1S`
- `QSPROTEOME:QS00049416`

## Notes

1*protein.P10443|1*protein.P03007|1*protein.P0ABS8
