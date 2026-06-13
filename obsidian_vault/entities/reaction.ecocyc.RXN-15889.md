---
entity_id: "reaction.ecocyc.RXN-15889"
entity_type: "reaction"
name: "RXN-15889"
source_database: "EcoCyc"
source_id: "RXN-15889"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15889

`reaction.ecocyc.RXN-15889`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15889`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Apo-EntF + CO-A -> Holo-EntF + 3-5-ADP + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Apo-EntF + CO-A -> Holo-EntF + 3-5-ADP + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by entD (protein.P19925). Substrates: CoA (molecule.C00010). Products: Adenosine 3',5'-bisphosphate (molecule.C00054), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.ENTBACSYN-PWY` enterobactin biosynthesis (EcoCyc)

## Annotation

Apo-EntF + CO-A -> Holo-EntF + 3-5-ADP + PROTON; direction=LEFT-TO-RIGHT

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

- `EcoCyc:RXN-15889`

## Notes

Apo-EntF + CO-A -> Holo-EntF + 3-5-ADP + PROTON; direction=LEFT-TO-RIGHT
