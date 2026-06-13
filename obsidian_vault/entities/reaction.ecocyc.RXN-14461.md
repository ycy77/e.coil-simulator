---
entity_id: "reaction.ecocyc.RXN-14461"
entity_type: "reaction"
name: "RXN-14461"
source_database: "EcoCyc"
source_id: "RXN-14461"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14461

`reaction.ecocyc.RXN-14461`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14461`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCI-PERI-BAC-GN

## Enriched Summary

FAD + Proteins-L-Threonines -> Protein-flavinated-threonines + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: FAD + Proteins-L-Threonines -> Protein-flavinated-threonines + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by apbE (protein.P0AB85). Substrates: FAD (molecule.C00016), a [protein]-L-threonine (molecule.ecocyc.Proteins-L-Threonines). Products: AMP (molecule.C00020), a [protein]-FMN-L-threonine (molecule.ecocyc.Protein-flavinated-threonines).

## Annotation

FAD + Proteins-L-Threonines -> Protein-flavinated-threonines + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AB85|protein.P0AB85]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Protein-flavinated-threonines|molecule.ecocyc.Protein-flavinated-threonines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Proteins-L-Threonines|molecule.ecocyc.Proteins-L-Threonines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14461`

## Notes

FAD + Proteins-L-Threonines -> Protein-flavinated-threonines + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
