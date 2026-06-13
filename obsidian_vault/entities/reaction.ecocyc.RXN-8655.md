---
entity_id: "reaction.ecocyc.RXN-8655"
entity_type: "reaction"
name: "RXN-8655"
source_database: "EcoCyc"
source_id: "RXN-8655"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-8655

`reaction.ecocyc.RXN-8655`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-8655`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

LIPOYL-AMP + Lipoyl-Protein-L-Lysine -> Lipoyl-Protein-N6-lipoyllysine + AMP + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: LIPOYL-AMP + Lipoyl-Protein-L-Lysine -> Lipoyl-Protein-N6-lipoyllysine + AMP + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: Lipoyl-AMP (molecule.C16238), a [lipoyl-carrier protein]-L-lysine (molecule.ecocyc.Lipoyl-Protein-L-Lysine). Products: AMP (molecule.C00020), H+ (molecule.C00080), a [lipoyl-carrier protein]-N6-[(R)-lipoyl]-L-lysine (molecule.ecocyc.Lipoyl-Protein-N6-lipoyllysine).

## Enriched Pathways

- `ecocyc.PWY0-522` lipoate salvage I (EcoCyc)

## Annotation

LIPOYL-AMP + Lipoyl-Protein-L-Lysine -> Lipoyl-Protein-N6-lipoyllysine + AMP + PROTON; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-522` lipoate salvage I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Lipoyl-Protein-N6-lipoyllysine|molecule.ecocyc.Lipoyl-Protein-N6-lipoyllysine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C16238|molecule.C16238]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Lipoyl-Protein-L-Lysine|molecule.ecocyc.Lipoyl-Protein-L-Lysine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-8655`

## Notes

LIPOYL-AMP + Lipoyl-Protein-L-Lysine -> Lipoyl-Protein-N6-lipoyllysine + AMP + PROTON; direction=LEFT-TO-RIGHT
