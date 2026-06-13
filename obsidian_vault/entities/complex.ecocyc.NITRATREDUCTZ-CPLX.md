---
entity_id: "complex.ecocyc.NITRATREDUCTZ-CPLX"
entity_type: "complex"
name: "nitrate reductase Z"
source_database: "EcoCyc"
source_id: "NITRATREDUCTZ-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "NRZ"
  - "quinol:nitrate oxidoreductase"
---

# nitrate reductase Z

`complex.ecocyc.NITRATREDUCTZ-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:NITRATREDUCTZ-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P19318|protein.P19318]], [[protein.P19319|protein.P19319]], [[protein.P0AF32|protein.P0AF32]]

## Enriched Summary

Nitrate reductase Z (NRZ) is a membrane bound molybdoenzyme responsible for the weak nitrate reductase activity present when cells are grown aerobically in a nitrate containing medium . By homology whith nitrate reductase A, nitrate reductase Z is a heterotrimer composed of the α (NarZ), β (NarY) and γ (NarV) chains. A fourth polypeptide, encoded by EG10645 "narW", is required for the incorporation of the molybdenum cofactor into the α subunit . NRZ is constitutively expressed in a strain which carries the operon on a multicopy plasmid ; NRZ is repressed by Fnr in anaerobiosis; NRZ is only slightly induced by nitrate; NRZ may function during the aerobic to anaerobic transition when cells are growing in the presence of nitrate . During entry into stationary phase, transcription of the narZYWV operon is induced, and induction is mainly dependent on the alternative sigma factor RpoS . Nitrate reductase Z also has tellurite reductase activity in wild-type E. coli . E. coli K-12 contains three nitrate reductases. Two of them, NITRATREDUCTA-CPLX (NRA) and nitrate reductase Z (NRZ), are membrane bound and biochemically similar but differentially regulated (reviewed by . The third nitrate reductase, NAP-CPLX "Nap" is located in the periplasm...

## Biological Role

Catalyzes RXN-15119 (reaction.ecocyc.RXN-15119), RXN0-3501 (reaction.ecocyc.RXN0-3501). Bound by Heme (molecule.C00032), bis(guanylyl molybdopterin) cofactor (molecule.ecocyc.CPD-15873), an iron-sulfur cluster (molecule.ecocyc.FeS-Centers).

## Annotation

Nitrate reductase Z (NRZ) is a membrane bound molybdoenzyme responsible for the weak nitrate reductase activity present when cells are grown aerobically in a nitrate containing medium . By homology whith nitrate reductase A, nitrate reductase Z is a heterotrimer composed of the α (NarZ), β (NarY) and γ (NarV) chains. A fourth polypeptide, encoded by EG10645 "narW", is required for the incorporation of the molybdenum cofactor into the α subunit . NRZ is constitutively expressed in a strain which carries the operon on a multicopy plasmid ; NRZ is repressed by Fnr in anaerobiosis; NRZ is only slightly induced by nitrate; NRZ may function during the aerobic to anaerobic transition when cells are growing in the presence of nitrate . During entry into stationary phase, transcription of the narZYWV operon is induced, and induction is mainly dependent on the alternative sigma factor RpoS . Nitrate reductase Z also has tellurite reductase activity in wild-type E. coli . E. coli K-12 contains three nitrate reductases. Two of them, NITRATREDUCTA-CPLX (NRA) and nitrate reductase Z (NRZ), are membrane bound and biochemically similar but differentially regulated (reviewed by . The third nitrate reductase, NAP-CPLX "Nap" is located in the periplasm.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-15119|reaction.ecocyc.RXN-15119]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-3501|reaction.ecocyc.RXN0-3501]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (6)

- `binds` <-- [[molecule.C00032|molecule.C00032]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-15873|molecule.ecocyc.CPD-15873]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.FeS-Centers|molecule.ecocyc.FeS-Centers]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AF32|protein.P0AF32]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P19318|protein.P19318]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P19319|protein.P19319]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:NITRATREDUCTZ-CPLX`
- `QSPROTEOME:QS00176185`

## Notes

1*protein.P19318|1*protein.P19319|1*protein.P0AF32
