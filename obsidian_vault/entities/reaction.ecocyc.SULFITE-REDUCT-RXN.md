---
entity_id: "reaction.ecocyc.SULFITE-REDUCT-RXN"
entity_type: "reaction"
name: "SULFITE-REDUCT-RXN"
source_database: "EcoCyc"
source_id: "SULFITE-REDUCT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# SULFITE-REDUCT-RXN

`reaction.ecocyc.SULFITE-REDUCT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:SULFITE-REDUCT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The fourth and final reaction in the conversion of sulfate to sulfide. This reaction catalyzes the conversion of sulfite to sulfide, leading to the synthesis of cysteine. EcoCyc reaction equation: WATER + NADP + HS -> PROTON + NADPH + SO3; direction=PHYSIOL-RIGHT-TO-LEFT. The fourth and final reaction in the conversion of sulfate to sulfide. This reaction catalyzes the conversion of sulfite to sulfide, leading to the synthesis of cysteine.

## Biological Role

Catalyzed by assimilatory sulfite reductase (NADPH) (complex.ecocyc.SULFITE-REDUCT-CPLX). Substrates: H2O (molecule.C00001), NADP+ (molecule.C00006), Hydrogen sulfide (molecule.C00283). Products: NADPH (molecule.C00005), H+ (molecule.C00080), Sulfite (molecule.C00094).

## Enriched Pathways

- `ecocyc.SO4ASSIM-PWY` assimilatory sulfate reduction I (EcoCyc)

## Annotation

The fourth and final reaction in the conversion of sulfate to sulfide. This reaction catalyzes the conversion of sulfite to sulfide, leading to the synthesis of cysteine.

## Pathways

- `ecocyc.SO4ASSIM-PWY` assimilatory sulfate reduction I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[complex.ecocyc.SULFITE-REDUCT-CPLX|complex.ecocyc.SULFITE-REDUCT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00094|molecule.C00094]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00283|molecule.C00283]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01326|molecule.C01326]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-5401|molecule.ecocyc.CPD-5401]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-763|molecule.ecocyc.CPD-763]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:SULFITE-REDUCT-RXN`

## Notes

WATER + NADP + HS -> PROTON + NADPH + SO3; direction=PHYSIOL-RIGHT-TO-LEFT
