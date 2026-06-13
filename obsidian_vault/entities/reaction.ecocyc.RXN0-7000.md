---
entity_id: "reaction.ecocyc.RXN0-7000"
entity_type: "reaction"
name: "RXN0-7000"
source_database: "EcoCyc"
source_id: "RXN0-7000"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7000

`reaction.ecocyc.RXN0-7000`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7000`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

EF-P-lysyl-lysine + OXYGEN-MOLECULE + NADPH + PROTON -> EF-P-lysyl-hydroxylysine + WATER + NADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: EF-P-lysyl-lysine + OXYGEN-MOLECULE + NADPH + PROTON -> EF-P-lysyl-hydroxylysine + WATER + NADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by epmC (protein.P76938). Substrates: NADPH (molecule.C00005), Oxygen (molecule.C00007), H+ (molecule.C00080), [a protein chain elongation factor EF-P]-N-(β-L-lysyl)-L-lysine34 (molecule.ecocyc.EF-P-lysyl-lysine). Products: H2O (molecule.C00001), NADP+ (molecule.C00006), a [protein chain elongation factor EF-P]-N-(β-lysyl)-5-hydroxy-L-lysine34 (molecule.ecocyc.EF-P-lysyl-hydroxylysine).

## Annotation

EF-P-lysyl-lysine + OXYGEN-MOLECULE + NADPH + PROTON -> EF-P-lysyl-hydroxylysine + WATER + NADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P76938|protein.P76938]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.EF-P-lysyl-hydroxylysine|molecule.ecocyc.EF-P-lysyl-hydroxylysine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.EF-P-lysyl-lysine|molecule.ecocyc.EF-P-lysyl-lysine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7000`

## Notes

EF-P-lysyl-lysine + OXYGEN-MOLECULE + NADPH + PROTON -> EF-P-lysyl-hydroxylysine + WATER + NADP; direction=PHYSIOL-LEFT-TO-RIGHT
