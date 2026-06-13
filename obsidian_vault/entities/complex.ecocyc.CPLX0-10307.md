---
entity_id: "complex.ecocyc.CPLX0-10307"
entity_type: "complex"
name: "carbon-phosphorus lyase ATP-binding protein PhnK"
source_database: "EcoCyc"
source_id: "CPLX0-10307"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# carbon-phosphorus lyase ATP-binding protein PhnK

`complex.ecocyc.CPLX0-10307`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-10307`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P16678|protein.P16678]]

## Enriched Summary

The phnK gene is part of a 14-gene phnCDEFGHIJKLMNOP operon that is involved in phosphonate uptake and metabolism and is a member of the phosphate regulon . PhnK is required for carbon-phosphorous lyase (C-P lyase) activity , and a phnK mutant accumulates presumed intermediates of the C-P lyase pathway of phosphonate degradation . Sequence analysis showed that PhnK is a non-transporter member of the ATP-binding cassette (ABC) protein family. PhnK was shown to be a component of the carbon-phosphorus lyase system and to interact with the CPLX0-10309 . PhnK interacts with the PhnJ subunit of the core complex via its α helices 3 and 4; the interaction exposes the Gly32 active site residue of PhnJ . Later research has shown that PhnK binds to the CPLX0-10309 as a homodimer. Furthermore, it also binds a dimer of PHNL-MONOMER PhnL, a second non-transporter ABC protein encoded by the phn operon. Both the PhnK and the PhnL dimers are able to bind and hydrolyze ATP, leading to opening of the core complex, exposing and rearranging the Zn2+ active site. The authors hypothesize that PhnL could potentially function to inhibit phosphate release from PhnK post hydrolysis, thus controlling when the energy generated from ATP hydrolysis is released...

## Biological Role

Component of carbon-phosphorus lyase system (complex.ecocyc.CPLX0-7958).

## Annotation

The phnK gene is part of a 14-gene phnCDEFGHIJKLMNOP operon that is involved in phosphonate uptake and metabolism and is a member of the phosphate regulon . PhnK is required for carbon-phosphorous lyase (C-P lyase) activity , and a phnK mutant accumulates presumed intermediates of the C-P lyase pathway of phosphonate degradation . Sequence analysis showed that PhnK is a non-transporter member of the ATP-binding cassette (ABC) protein family. PhnK was shown to be a component of the carbon-phosphorus lyase system and to interact with the CPLX0-10309 . PhnK interacts with the PhnJ subunit of the core complex via its α helices 3 and 4; the interaction exposes the Gly32 active site residue of PhnJ . Later research has shown that PhnK binds to the CPLX0-10309 as a homodimer. Furthermore, it also binds a dimer of PHNL-MONOMER PhnL, a second non-transporter ABC protein encoded by the phn operon. Both the PhnK and the PhnL dimers are able to bind and hydrolyze ATP, leading to opening of the core complex, exposing and rearranging the Zn2+ active site. The authors hypothesize that PhnL could potentially function to inhibit phosphate release from PhnK post hydrolysis, thus controlling when the energy generated from ATP hydrolysis is released .

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7958|complex.ecocyc.CPLX0-7958]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P16678|protein.P16678]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-10307`
- `QSPROTEOME:QS00195963`

## Notes

2*protein.P16678
