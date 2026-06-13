---
entity_id: "reaction.ecocyc.ENTDB-RXN"
entity_type: "reaction"
name: "ENTDB-RXN"
source_database: "EcoCyc"
source_id: "ENTDB-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ENTDB-RXN

`reaction.ecocyc.ENTDB-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ENTDB-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

In this reaction the phosphopantetheine moiety of coenzyme A is transferred to a probable serine residue in the ArCP domain of apo-EntB. EcoCyc reaction equation: Apo-EntB + CO-A -> Holo-EntB + 3-5-ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. In this reaction the phosphopantetheine moiety of coenzyme A is transferred to a probable serine residue in the ArCP domain of apo-EntB.

## Biological Role

Catalyzed by entD (protein.P19925). Substrates: CoA (molecule.C00010). Products: Adenosine 3',5'-bisphosphate (molecule.C00054), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.ENTBACSYN-PWY` enterobactin biosynthesis (EcoCyc)

## Annotation

In this reaction the phosphopantetheine moiety of coenzyme A is transferred to a probable serine residue in the ArCP domain of apo-EntB.

## Pathways

- `ecocyc.ENTBACSYN-PWY` enterobactin biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P19925|protein.P19925]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00054|molecule.C00054]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[protein.P0ADI4|protein.P0ADI4]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ENTDB-RXN`

## Notes

Apo-EntB + CO-A -> Holo-EntB + 3-5-ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
