---
entity_id: "reaction.ecocyc.PHENDEHYD-RXN"
entity_type: "reaction"
name: "PHENDEHYD-RXN"
source_database: "EcoCyc"
source_id: "PHENDEHYD-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PHENDEHYD-RXN

`reaction.ecocyc.PHENDEHYD-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PHENDEHYD-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second reaction in the degradation of 2-phenylethylamine. EcoCyc reaction equation: WATER + NAD + PHENYLACETALDEHYDE -> PROTON + NADH + PHENYLACETATE; direction=LEFT-TO-RIGHT. This is the second reaction in the degradation of 2-phenylethylamine.

## Biological Role

Catalyzed by phenylacetaldehyde dehydrogenase (complex.ecocyc.PHENDEHYD-CPLX). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), Phenylacetaldehyde (molecule.C00601). Products: NADH (molecule.C00004), H+ (molecule.C00080), Phenylacetic acid (molecule.C07086).

## Enriched Pathways

- `ecocyc.2PHENDEG-PWY` phenylethylamine degradation I (EcoCyc)

## Annotation

This is the second reaction in the degradation of 2-phenylethylamine.

## Pathways

- `ecocyc.2PHENDEG-PWY` phenylethylamine degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.PHENDEHYD-CPLX|complex.ecocyc.PHENDEHYD-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C07086|molecule.C07086]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00601|molecule.C00601]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00601|molecule.C00601]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PHENDEHYD-RXN`

## Notes

WATER + NAD + PHENYLACETALDEHYDE -> PROTON + NADH + PHENYLACETATE; direction=LEFT-TO-RIGHT
