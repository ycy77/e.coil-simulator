---
entity_id: "reaction.ecocyc.RXN-24992"
entity_type: "reaction"
name: "RXN-24992"
source_database: "EcoCyc"
source_id: "RXN-24992"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-24992

`reaction.ecocyc.RXN-24992`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24992`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Protein-Tyrosines -> ADP + Protein-tyrosine-phosphates + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + Protein-Tyrosines -> ADP + Protein-tyrosine-phosphates + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by etk (protein.P38134), wzc (protein.P76387). Substrates: ATP (molecule.C00002), a [protein]-L-tyrosine (molecule.ecocyc.Protein-Tyrosines). Products: ADP (molecule.C00008), H+ (molecule.C00080), a [protein]-L-tyrosine phosphate (molecule.ecocyc.Protein-tyrosine-phosphates).

## Annotation

ATP + Protein-Tyrosines -> ADP + Protein-tyrosine-phosphates + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P38134|protein.P38134]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76387|protein.P76387]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Protein-tyrosine-phosphates|molecule.ecocyc.Protein-tyrosine-phosphates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-Tyrosines|molecule.ecocyc.Protein-Tyrosines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24992`

## Notes

ATP + Protein-Tyrosines -> ADP + Protein-tyrosine-phosphates + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
