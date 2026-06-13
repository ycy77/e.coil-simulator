---
entity_id: "reaction.ecocyc.2-ISOPROPYLMALATESYN-RXN"
entity_type: "reaction"
name: "2-ISOPROPYLMALATESYN-RXN"
source_database: "EcoCyc"
source_id: "2-ISOPROPYLMALATESYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2-ISOPROPYLMALATESYN-RXN

`reaction.ecocyc.2-ISOPROPYLMALATESYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2-ISOPROPYLMALATESYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first step in the biosynthesis of leucine, beyond a fork with the valine pathway. EcoCyc reaction equation: 2-KETO-ISOVALERATE + ACETYL-COA + WATER -> PROTON + 3-CARBOXY-3-HYDROXY-ISOCAPROATE + CO-A; direction=LEFT-TO-RIGHT. This is the first step in the biosynthesis of leucine, beyond a fork with the valine pathway.

## Biological Role

Catalyzed by leuA (protein.P09151). Substrates: H2O (molecule.C00001), Acetyl-CoA (molecule.C00024), 3-Methyl-2-oxobutanoic acid (molecule.C00141). Products: CoA (molecule.C00010), H+ (molecule.C00080), alpha-Isopropylmalate (molecule.C02504).

## Enriched Pathways

- `ecocyc.LEUSYN-PWY` L-leucine biosynthesis (EcoCyc)

## Annotation

This is the first step in the biosynthesis of leucine, beyond a fork with the valine pathway.

## Pathways

- `ecocyc.LEUSYN-PWY` L-leucine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P09151|protein.P09151]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02504|molecule.C02504]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00141|molecule.C00141]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00123|molecule.C00123]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:2-ISOPROPYLMALATESYN-RXN`

## Notes

2-KETO-ISOVALERATE + ACETYL-COA + WATER -> PROTON + 3-CARBOXY-3-HYDROXY-ISOCAPROATE + CO-A; direction=LEFT-TO-RIGHT
