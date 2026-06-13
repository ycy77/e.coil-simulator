---
entity_id: "complex.ecocyc.CPLX0-10308"
entity_type: "complex"
name: "carbon-phosphorus lyase ATP-binding protein PhnL"
source_database: "EcoCyc"
source_id: "CPLX0-10308"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# carbon-phosphorus lyase ATP-binding protein PhnL

`complex.ecocyc.CPLX0-10308`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-10308`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P16679|protein.P16679]]

## Enriched Summary

The phnL gene is part of a 14-gene phnCDEFGHIJKLMNOP operon that is involved in phosphonate uptake and metabolism and is a member of the phosphate regulon . Sequence analysis showed that PhnL is a non-transporter member of the ATP-binding cassette (ABC) protein family. PhnL was shown to be a component of the carbon-phosphorus lyase system and is required for carbon-phosphorous lyase activity . A phnL mutant accumulates presumed intermediates of the C-P lyase pathway of phosphonate degradation . A mixture of PhnL, PhnG, PhnH and PhnI catalyzed the nucleophilic attack of CPD0-1068 on the anomeric carbon of ATP to form adenine and CPD0-2479 . PhnL forms a homodimer that binds to the PHNK-MONOMER "PhnK homodimer", which itself binds to the CPLX0-10309. Both PhnK and PhnL dimers are able to bind and hydrolyze ATP, leading to opening of the core complex, exposing and rearranging the Zn2+ active site. The authors hypothesize that PhnL could potentially function to inhibit phosphate release from PhnK post hydrolysis, thus controlling when the energy generated from ATP hydrolysis is released . The phnL gene is part of a 14-gene phnCDEFGHIJKLMNOP operon that is involved in phosphonate uptake and metabolism and is a member of the phosphate regulon . Sequence analysis showed that PhnL is a non-transporter member of the ATP-binding cassette (ABC) protein family...

## Biological Role

Component of carbon-phosphorus lyase system (complex.ecocyc.CPLX0-7958).

## Annotation

The phnL gene is part of a 14-gene phnCDEFGHIJKLMNOP operon that is involved in phosphonate uptake and metabolism and is a member of the phosphate regulon . Sequence analysis showed that PhnL is a non-transporter member of the ATP-binding cassette (ABC) protein family. PhnL was shown to be a component of the carbon-phosphorus lyase system and is required for carbon-phosphorous lyase activity . A phnL mutant accumulates presumed intermediates of the C-P lyase pathway of phosphonate degradation . A mixture of PhnL, PhnG, PhnH and PhnI catalyzed the nucleophilic attack of CPD0-1068 on the anomeric carbon of ATP to form adenine and CPD0-2479 . PhnL forms a homodimer that binds to the PHNK-MONOMER "PhnK homodimer", which itself binds to the CPLX0-10309. Both PhnK and PhnL dimers are able to bind and hydrolyze ATP, leading to opening of the core complex, exposing and rearranging the Zn2+ active site. The authors hypothesize that PhnL could potentially function to inhibit phosphate release from PhnK post hydrolysis, thus controlling when the energy generated from ATP hydrolysis is released .

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7958|complex.ecocyc.CPLX0-7958]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P16679|protein.P16679]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-10308`
- `QSPROTEOME:QS00198643`

## Notes

2*protein.P16679
