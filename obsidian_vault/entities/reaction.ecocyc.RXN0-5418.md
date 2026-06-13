---
entity_id: "reaction.ecocyc.RXN0-5418"
entity_type: "reaction"
name: "RXN0-5418"
source_database: "EcoCyc"
source_id: "RXN0-5418"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5418

`reaction.ecocyc.RXN0-5418`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5418`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Cytidine-34-tRNAmet + ATP + ACETYL-COA + WATER -> Elongator-tRNAMet-acetylcytidine + ADP + Pi + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Cytidine-34-tRNAmet + ATP + ACETYL-COA + WATER -> Elongator-tRNAMet-acetylcytidine + ADP + Pi + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by tmcA (protein.P76562). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), Acetyl-CoA (molecule.C00024), a cytidine34 in [elongator tRNAmet] (molecule.ecocyc.Cytidine-34-tRNAmet). Products: ADP (molecule.C00008), CoA (molecule.C00010), H+ (molecule.C00080), an N4-acetylcytidine34 in [elongator tRNAmet] (molecule.ecocyc.Elongator-tRNAMet-acetylcytidine), phosphate (molecule.ecocyc.Pi).

## Annotation

Cytidine-34-tRNAmet + ATP + ACETYL-COA + WATER -> Elongator-tRNAMet-acetylcytidine + ADP + Pi + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[protein.P76562|protein.P76562]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Elongator-tRNAMet-acetylcytidine|molecule.ecocyc.Elongator-tRNAMet-acetylcytidine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Cytidine-34-tRNAmet|molecule.ecocyc.Cytidine-34-tRNAmet]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5418`

## Notes

Cytidine-34-tRNAmet + ATP + ACETYL-COA + WATER -> Elongator-tRNAMet-acetylcytidine + ADP + Pi + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
