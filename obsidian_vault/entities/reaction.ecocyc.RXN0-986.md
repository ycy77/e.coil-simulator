---
entity_id: "reaction.ecocyc.RXN0-986"
entity_type: "reaction"
name: "RXN0-986"
source_database: "EcoCyc"
source_id: "RXN0-986"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-986

`reaction.ecocyc.RXN0-986`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-986`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

AlkB catalyzes repair of DNA lesions caused by SN2 methylating compounds, rather than lesions caused by SN1 methylating compounds or ionizing radiation . AlkB preferentially binds to and repairs methylation lesions in single-stranded DNA rather than double-stranded DNA, suggesting that AlkB repair activity may be specific for the single-stranded DNA present during transcription and DNA replication . AlkB also catalyzes repair of methylated RNA . EcoCyc reaction equation: N1-ETHYLADENINE-IN-DNA + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> DNA-Adenines + ACETALD + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT. AlkB catalyzes repair of DNA lesions caused by SN2 methylating compounds, rather than lesions caused by SN1 methylating compounds or ionizing radiation . AlkB preferentially binds to and repairs methylation lesions in single-stranded DNA rather than double-stranded DNA, suggesting that AlkB repair activity may be specific for the single-stranded DNA present during transcription and DNA replication . AlkB also catalyzes repair of methylated RNA .

## Biological Role

Catalyzed by alkB (protein.P05050). Substrates: Oxygen (molecule.C00007), 2-Oxoglutarate (molecule.C00026), an N1-ethyladenine in DNA (molecule.ecocyc.N1-ETHYLADENINE-IN-DNA). Products: CO2 (molecule.C00011), Succinate (molecule.C00042), Acetaldehyde (molecule.C00084), an adenine in DNA (molecule.ecocyc.DNA-Adenines).

## Annotation

AlkB catalyzes repair of DNA lesions caused by SN2 methylating compounds, rather than lesions caused by SN1 methylating compounds or ionizing radiation . AlkB preferentially binds to and repairs methylation lesions in single-stranded DNA rather than double-stranded DNA, suggesting that AlkB repair activity may be specific for the single-stranded DNA present during transcription and DNA replication . AlkB also catalyzes repair of methylated RNA .

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P05050|protein.P05050]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00084|molecule.C00084]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.DNA-Adenines|molecule.ecocyc.DNA-Adenines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.N1-ETHYLADENINE-IN-DNA|molecule.ecocyc.N1-ETHYLADENINE-IN-DNA]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-986`

## Notes

N1-ETHYLADENINE-IN-DNA + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> DNA-Adenines + ACETALD + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
