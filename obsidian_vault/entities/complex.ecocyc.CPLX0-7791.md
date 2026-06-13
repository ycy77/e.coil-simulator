---
entity_id: "complex.ecocyc.CPLX0-7791"
entity_type: "complex"
name: "RelB-RelE antitoxin/toxin complex / DNA-binding transcriptional repressor"
source_database: "EcoCyc"
source_id: "CPLX0-7791"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "RelBE"
  - "RelB-RelE"
---

# RelB-RelE antitoxin/toxin complex / DNA-binding transcriptional repressor

`complex.ecocyc.CPLX0-7791`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7791`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0C079|protein.P0C079]], [[protein.P0C077|protein.P0C077]]

## Enriched Summary

RelB is a DNA-binding transcriptional regulator which belongs to the ribbon-helix-helix (RHH) family of transcription factors and it is an antitoxin that prevents the lethal action of the toxin . RelB is part of the relBE-hokD operon, which specifies a toxin-antitoxin system, and it is autoregulated by its own products, RelB and RelE . On the other hand, relE encodes a cytotoxin that is lethal or inhibitory to host cells , and it also encodes a cofactor that enhances the repressor activity of RelB . The relBE-hokD operon is induced upon entering nutritional starvation conditions, such as the stringent response or acid starvation , while the level of RelB antitoxin is reduced as a result of Lon-dependent proteolysis. Consequently, RelE toxin is liberated, leading to cell growth arrest and eventually cell death . The expression of the relBE-hokD operon under these conditions may have some as-yet-uncovered beneficial function . RelB and RelE form a high-affinity complex with a 2:1 stoichiometry when RelB is in excess . This interaction of RelE with RelB is essential for regulating the expression of the relBE-hokD operon and for neutralizing the toxic activity of RelE . The ReB2-RelE complex represses transcription of the relBE-hokD operon via strong cooperative binding to the relB promoter region...

## Annotation

RelB is a DNA-binding transcriptional regulator which belongs to the ribbon-helix-helix (RHH) family of transcription factors and it is an antitoxin that prevents the lethal action of the toxin . RelB is part of the relBE-hokD operon, which specifies a toxin-antitoxin system, and it is autoregulated by its own products, RelB and RelE . On the other hand, relE encodes a cytotoxin that is lethal or inhibitory to host cells , and it also encodes a cofactor that enhances the repressor activity of RelB . The relBE-hokD operon is induced upon entering nutritional starvation conditions, such as the stringent response or acid starvation , while the level of RelB antitoxin is reduced as a result of Lon-dependent proteolysis. Consequently, RelE toxin is liberated, leading to cell growth arrest and eventually cell death . The expression of the relBE-hokD operon under these conditions may have some as-yet-uncovered beneficial function . RelB and RelE form a high-affinity complex with a 2:1 stoichiometry when RelB is in excess . This interaction of RelE with RelB is essential for regulating the expression of the relBE-hokD operon and for neutralizing the toxic activity of RelE . The ReB2-RelE complex represses transcription of the relBE-hokD operon via strong cooperative binding to the relB promoter region . The 24-bp operator contains a hexad repeat (5'-[A/T]TGT[A/C]A-3') that is repeated twice on each strand . The spacing between each half-site was found to be essential for cooperative interactions between two RelB2-RelE heterotrimers. Only RelB makes contacts to the DNA and the RHH motif of RelB recognizes the four hexad repeats within the bipartite binding site. High affinity for DNA is only achieved in the presence of RelE , which stabilizes the tetrameric form of RelB . When R

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P0C077|protein.P0C077]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4
- `is_component_of` <-- [[protein.P0C079|protein.P0C079]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-7791`
- `PDB:2KC8`
- `PDB:4FXE`
- `QSPROTEOME:QS00049440`

## Notes

4*protein.P0C079|4*protein.P0C077
