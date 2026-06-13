---
entity_id: "reaction.ecocyc.HCAMULTI-RXN"
entity_type: "reaction"
name: "HCAMULTI-RXN"
source_database: "EcoCyc"
source_id: "HCAMULTI-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# HCAMULTI-RXN

`reaction.ecocyc.HCAMULTI-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:HCAMULTI-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3-PHENYLPROPIONATE + NADH + OXYGEN-MOLECULE + PROTON -> CARBOXYETHYL-3-5-CYCLOHEXADIENE-1-2-DIOL + NAD; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 3-PHENYLPROPIONATE + NADH + OXYGEN-MOLECULE + PROTON -> CARBOXYETHYL-3-5-CYCLOHEXADIENE-1-2-DIOL + NAD; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by putative 3-phenylpropionate/cinnamate dioxygenase (complex.ecocyc.HCAMULTI-CPLX). Substrates: NADH (molecule.C00004), Oxygen (molecule.C00007), H+ (molecule.C00080), Phenylpropanoate (molecule.C05629). Products: NAD+ (molecule.C00003), cis-3-(Carboxy-ethyl)-3,5-cyclo-hexadiene-1,2-diol (molecule.C11588).

## Enriched Pathways

- `ecocyc.HCAMHPDEG-PWY` 3-phenylpropanoate and 3-(3-hydroxyphenyl)propanoate degradation to 2-hydroxypentadienoate (EcoCyc)

## Annotation

3-PHENYLPROPIONATE + NADH + OXYGEN-MOLECULE + PROTON -> CARBOXYETHYL-3-5-CYCLOHEXADIENE-1-2-DIOL + NAD; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.HCAMHPDEG-PWY` 3-phenylpropanoate and 3-(3-hydroxyphenyl)propanoate degradation to 2-hydroxypentadienoate (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.HCAMULTI-CPLX|complex.ecocyc.HCAMULTI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C11588|molecule.C11588]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05629|molecule.C05629]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:HCAMULTI-RXN`

## Notes

3-PHENYLPROPIONATE + NADH + OXYGEN-MOLECULE + PROTON -> CARBOXYETHYL-3-5-CYCLOHEXADIENE-1-2-DIOL + NAD; direction=PHYSIOL-LEFT-TO-RIGHT
