---
entity_id: "complex.ecocyc.CPLX0-7885"
entity_type: "complex"
name: "glutathione hydrolase"
source_database: "EcoCyc"
source_id: "CPLX0-7885"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "&gamma"
  - "-glutamyl transpeptidase"
---

# glutathione hydrolase

`complex.ecocyc.CPLX0-7885`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7885`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PERI-BAC-GN
- Complex type: `structural`
- Components: [[protein.P18956|protein.P18956]], [[protein.P18956|protein.P18956]]

## Enriched Summary

Represents the active glutathione hydrolase heterodimer. See EG10374-MONOMER "here" for a full description. Represents the active glutathione hydrolase heterodimer. See EG10374-MONOMER "here" for a full description.

## Biological Role

Catalyzes GAMMA-GLUTAMYLTRANSFERASE-RXN (reaction.ecocyc.GAMMA-GLUTAMYLTRANSFERASE-RXN), RXN-12618 (reaction.ecocyc.RXN-12618), RXN-18092 (reaction.ecocyc.RXN-18092), RXN-18093 (reaction.ecocyc.RXN-18093).

## Annotation

Represents the active glutathione hydrolase heterodimer. See EG10374-MONOMER "here" for a full description.

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.GAMMA-GLUTAMYLTRANSFERASE-RXN|reaction.ecocyc.GAMMA-GLUTAMYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-12618|reaction.ecocyc.RXN-12618]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-18092|reaction.ecocyc.RXN-18092]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-18093|reaction.ecocyc.RXN-18093]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P18956|protein.P18956]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-7885`
- `PDB:2DBW`
- `PDB:2EOW`
- `PDB:2DG5`
- `PDB:2DBX`
- `PDB:2DBU`
- `PDB:2Z8K`
- `PDB:2Z8J`
- `PDB:2Z8I`

## Notes

protein.P18956|protein.P18956
