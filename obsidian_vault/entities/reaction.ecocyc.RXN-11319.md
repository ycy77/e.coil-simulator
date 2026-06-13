---
entity_id: "reaction.ecocyc.RXN-11319"
entity_type: "reaction"
name: "RXN-11319"
source_database: "EcoCyc"
source_id: "RXN-11319"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11319

`reaction.ecocyc.RXN-11319`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11319`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + TYR + NADPH -> CPD-12279 + CPD-108 + CH33ADO + MET + NADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + TYR + NADPH -> CPD-12279 + CPD-108 + CH33ADO + MET + NADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by thiH (protein.P30140). Substrates: NADPH (molecule.C00005), S-Adenosyl-L-methionine (molecule.C00019), L-Tyrosine (molecule.C00082). Products: NADP+ (molecule.C00006), L-Methionine (molecule.C00073), H+ (molecule.C00080), 4-Cresol (molecule.C01468), Iminoglycine (molecule.C15809), 5'-deoxyadenosine (molecule.ecocyc.CH33ADO).

## Enriched Pathways

- `ecocyc.PWY-6892` thiazole component of thiamine diphosphate biosynthesis I (EcoCyc)

## Annotation

S-ADENOSYLMETHIONINE + TYR + NADPH -> CPD-12279 + CPD-108 + CH33ADO + MET + NADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6892` thiazole component of thiamine diphosphate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[protein.P30140|protein.P30140]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01468|molecule.C01468]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C15809|molecule.C15809]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CH33ADO|molecule.ecocyc.CH33ADO]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00082|molecule.C00082]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00048|molecule.C00048]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-11319`

## Notes

S-ADENOSYLMETHIONINE + TYR + NADPH -> CPD-12279 + CPD-108 + CH33ADO + MET + NADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
