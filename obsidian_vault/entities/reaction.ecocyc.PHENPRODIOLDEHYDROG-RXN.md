---
entity_id: "reaction.ecocyc.PHENPRODIOLDEHYDROG-RXN"
entity_type: "reaction"
name: "PHENPRODIOLDEHYDROG-RXN"
source_database: "EcoCyc"
source_id: "PHENPRODIOLDEHYDROG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PHENPRODIOLDEHYDROG-RXN

`reaction.ecocyc.PHENPRODIOLDEHYDROG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PHENPRODIOLDEHYDROG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second reaction in the degradation of 3-phenylpropionate. EcoCyc reaction equation: CARBOXYETHYL-3-5-CYCLOHEXADIENE-1-2-DIOL + NAD -> PROTON + 2-3-DIHYDROXYPHENYL-PROPIONATE + NADH; direction=LEFT-TO-RIGHT. This is the second reaction in the degradation of 3-phenylpropionate.

## Biological Role

Catalyzed by hcaB (protein.P0CI31). Substrates: NAD+ (molecule.C00003), cis-3-(Carboxy-ethyl)-3,5-cyclo-hexadiene-1,2-diol (molecule.C11588). Products: NADH (molecule.C00004), H+ (molecule.C00080), 3-(2,3-Dihydroxyphenyl)propanoate (molecule.C04044).

## Enriched Pathways

- `ecocyc.HCAMHPDEG-PWY` 3-phenylpropanoate and 3-(3-hydroxyphenyl)propanoate degradation to 2-hydroxypentadienoate (EcoCyc)

## Annotation

This is the second reaction in the degradation of 3-phenylpropionate.

## Pathways

- `ecocyc.HCAMHPDEG-PWY` 3-phenylpropanoate and 3-(3-hydroxyphenyl)propanoate degradation to 2-hydroxypentadienoate (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0CI31|protein.P0CI31]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04044|molecule.C04044]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C11588|molecule.C11588]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PHENPRODIOLDEHYDROG-RXN`

## Notes

CARBOXYETHYL-3-5-CYCLOHEXADIENE-1-2-DIOL + NAD -> PROTON + 2-3-DIHYDROXYPHENYL-PROPIONATE + NADH; direction=LEFT-TO-RIGHT
