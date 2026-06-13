---
entity_id: "complex.ecocyc.CPLX0-3107"
entity_type: "complex"
name: "ClpXP"
source_database: "EcoCyc"
source_id: "CPLX0-3107"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ClpXP

`complex.ecocyc.CPLX0-3107`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3107`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[complex.ecocyc.CPLX0-3101|complex.ecocyc.CPLX0-3101]], [[complex.ecocyc.CPLX0-3102|complex.ecocyc.CPLX0-3102]]

## Enriched Summary

Intracellular proteases enforce protein quality control and modify the proteome composition in response to environmental and nutritional cues. Most targeted proteolysis in bacteria is performed by a group of proteases that was named the AAA+ family (ATPases Associated with various cellular Activities) . All of these proteins contain ring-shaped hexamers that use energy from ATP hydrolysis to unfold protein substrates, followed by translocation of the unfolded chains through a central channel into a degradation chamber, where they are degraded. TAX-562 encodes five AAA+ proteases: CPLX0-2982 FtsH, CPLX0-3107 ClpXP, CPLX0-3104 ClpAP, EG10542-MONOMER Lon, and CPLX0-1163 HslUV . ClpXP is a serine protease complex responsible for the ATP-dependent degradation of a wide range of proteins . ClpXP consists of a ClpP tetradecamer capped at one or both ends by ClpX hexamers . ClpXP degrades the altered Mu immunity repressor, Vir. When Vir is present, the normal immunity repressor, Rep, becomes more vulnerable to ClpXP-mediated degradation as well . ClpXP can also degrade MuA, although it does not degrade it all, allowing ClpX to act in its chaperone capacity to assist MuA function . ClpXP is partially responsible for degradation of proteins with the SsrA degradation tag, produced as a consequence of SSRA-RNA-mediated ribosome rescue, including SsrA-tagged lambda repressor...

## Biological Role

Catalyzes 3.4.21.92-RXN (reaction.ecocyc.3.4.21.92-RXN).

## Annotation

Intracellular proteases enforce protein quality control and modify the proteome composition in response to environmental and nutritional cues. Most targeted proteolysis in bacteria is performed by a group of proteases that was named the AAA+ family (ATPases Associated with various cellular Activities) . All of these proteins contain ring-shaped hexamers that use energy from ATP hydrolysis to unfold protein substrates, followed by translocation of the unfolded chains through a central channel into a degradation chamber, where they are degraded. TAX-562 encodes five AAA+ proteases: CPLX0-2982 FtsH, CPLX0-3107 ClpXP, CPLX0-3104 ClpAP, EG10542-MONOMER Lon, and CPLX0-1163 HslUV . ClpXP is a serine protease complex responsible for the ATP-dependent degradation of a wide range of proteins . ClpXP consists of a ClpP tetradecamer capped at one or both ends by ClpX hexamers . ClpXP degrades the altered Mu immunity repressor, Vir. When Vir is present, the normal immunity repressor, Rep, becomes more vulnerable to ClpXP-mediated degradation as well . ClpXP can also degrade MuA, although it does not degrade it all, allowing ClpX to act in its chaperone capacity to assist MuA function . ClpXP is partially responsible for degradation of proteins with the SsrA degradation tag, produced as a consequence of SSRA-RNA-mediated ribosome rescue, including SsrA-tagged lambda repressor . ClpXP degrades stably folded SsrA proteins efficiently, but only poorly degrades proteins bearing SsrA tags artificially attached in the middle of their sequences via cysteine linkages . ClpXP can degrade DNA-bound lambda O protein when transcription is possible, otherwise, it is stable . ClpXP-mediated degradation of lambda O protein can affect the lysis/lysogeny decision under certain growth conditions . Clp

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.4.21.92-RXN|reaction.ecocyc.3.4.21.92-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-3101|complex.ecocyc.CPLX0-3101]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[complex.ecocyc.CPLX0-3102|complex.ecocyc.CPLX0-3102]] `EcoCyc` `database` - EcoCyc component coefficient=2
- `is_component_of` <-- [[protein.P0A6G7|protein.P0A6G7]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=14
- `is_component_of` <-- [[protein.P0A6H1|protein.P0A6H1]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12

## External IDs

- `EcoCyc:CPLX0-3107`
- `PDB:6WSG`
- `PDB:6WRF`
- `PDB:6WR2`
- `PDB:6PPE`
- `PDB:6POS`
- `PDB:6POD`
- `PDB:6PO3`
- `PDB:6PO1`

## Notes

1*complex.ecocyc.CPLX0-3101|2*complex.ecocyc.CPLX0-3102
