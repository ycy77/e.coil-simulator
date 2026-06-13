---
entity_id: "reaction.ecocyc.RXN-22002"
entity_type: "reaction"
name: "RXN-22002"
source_database: "EcoCyc"
source_id: "RXN-22002"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22002

`reaction.ecocyc.RXN-22002`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22002`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

BCCP-L-lysine + BIO-5-AMP -> BCCP-biotin-L-lysine + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: BCCP-L-lysine + BIO-5-AMP -> BCCP-biotin-L-lysine + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Biotinyl-5'-AMP (molecule.C05921), a [biotin carboxyl-carrier protein]-L-lysine (molecule.ecocyc.BCCP-L-lysine). Products: AMP (molecule.C00020), H+ (molecule.C00080), a [biotin carboxyl-carrier protein]-N6-biotinyl-L-lysine (molecule.ecocyc.BCCP-biotin-L-lysine).

## Annotation

BCCP-L-lysine + BIO-5-AMP -> BCCP-biotin-L-lysine + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.BCCP-biotin-L-lysine|molecule.ecocyc.BCCP-biotin-L-lysine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C05921|molecule.C05921]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.BCCP-L-lysine|molecule.ecocyc.BCCP-L-lysine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22002`

## Notes

BCCP-L-lysine + BIO-5-AMP -> BCCP-biotin-L-lysine + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
