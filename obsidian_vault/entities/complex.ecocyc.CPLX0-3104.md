---
entity_id: "complex.ecocyc.CPLX0-3104"
entity_type: "complex"
name: "ClpAP"
source_database: "EcoCyc"
source_id: "CPLX0-3104"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ClpAP

`complex.ecocyc.CPLX0-3104`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3104`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[complex.ecocyc.CPLX0-3101|complex.ecocyc.CPLX0-3101]], [[complex.ecocyc.CPLX0-881|complex.ecocyc.CPLX0-881]]

## Enriched Summary

Intracellular proteases enforce protein quality control and modify the proteome composition in response to environmental and nutritional cues. Most targeted proteolysis in bacteria is performed by a group of proteases that was named the AAA+ family (ATPases Associated with various cellular Activities) . All of these proteins contain ring-shaped hexamers that use energy from ATP hydrolysis to unfold protein substrates, followed by translocation of the unfolded chains through a central channel into a degradation chamber, where they are degraded. TAX-562 encodes five AAA+ proteases: CPLX0-2982 FtsH, CPLX0-3107 ClpXP, CPLX0-3104 ClpAP, EG10542-MONOMER Lon, and CPLX0-1163 HslUV . ClpAP is a serine protease complex responsible for the ATP-dependent degradation of a number of proteins . EG10156-MONOMER "ClpA" functions as an ATP-dependent chaperone component and EG10158-MONOMER "ClpP" as the serine protease component. Substrates for ClpAP include the plasmid P1 replication initiator RepA, HemA and a number of carbon starvation proteins . ClpAP is also one of the proteases responsible for degradation of proteins tagged with the SsrA degradation marker, including tagged lambda repressor and tagged GFP (the latter substrate indicating that ClpAP can unfold stable, native protein in an ATP-dependent manner)...

## Biological Role

Catalyzes 3.4.21.92-RXN (reaction.ecocyc.3.4.21.92-RXN).

## Annotation

Intracellular proteases enforce protein quality control and modify the proteome composition in response to environmental and nutritional cues. Most targeted proteolysis in bacteria is performed by a group of proteases that was named the AAA+ family (ATPases Associated with various cellular Activities) . All of these proteins contain ring-shaped hexamers that use energy from ATP hydrolysis to unfold protein substrates, followed by translocation of the unfolded chains through a central channel into a degradation chamber, where they are degraded. TAX-562 encodes five AAA+ proteases: CPLX0-2982 FtsH, CPLX0-3107 ClpXP, CPLX0-3104 ClpAP, EG10542-MONOMER Lon, and CPLX0-1163 HslUV . ClpAP is a serine protease complex responsible for the ATP-dependent degradation of a number of proteins . EG10156-MONOMER "ClpA" functions as an ATP-dependent chaperone component and EG10158-MONOMER "ClpP" as the serine protease component. Substrates for ClpAP include the plasmid P1 replication initiator RepA, HemA and a number of carbon starvation proteins . ClpAP is also one of the proteases responsible for degradation of proteins tagged with the SsrA degradation marker, including tagged lambda repressor and tagged GFP (the latter substrate indicating that ClpAP can unfold stable, native protein in an ATP-dependent manner) . However, ClpXP and SspB together are responsible for the in vivo degradation of the majority of SsrA-tagged proteins . ClpAP degrades a number of substrates that are not degraded by ClpXP . ClpAP is also responsible for rapid degradation of N-end rule substrates, which are marked for degradation by the identity of their amino-terminal residue (arginine, lysine, leucine, phenylalanine, tyrosine and tryptophan all mark a protein for N-end rule degradation) . Although ClpAP alon

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.4.21.92-RXN|reaction.ecocyc.3.4.21.92-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-3101|complex.ecocyc.CPLX0-3101]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[complex.ecocyc.CPLX0-881|complex.ecocyc.CPLX0-881]] `EcoCyc` `database` - EcoCyc component coefficient=2
- `is_component_of` <-- [[protein.P0A6G7|protein.P0A6G7]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=14
- `is_component_of` <-- [[protein.P0ABH9|protein.P0ABH9]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12

## External IDs

- `EcoCyc:CPLX0-3104`
- `PDB:6W21`
- `PDB:6W20`
- `PDB:6W1Z`
- `PDB:6UQO`
- `PDB:6UQE`

## Notes

1*complex.ecocyc.CPLX0-3101|2*complex.ecocyc.CPLX0-881
