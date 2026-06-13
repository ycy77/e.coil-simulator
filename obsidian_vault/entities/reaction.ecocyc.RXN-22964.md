---
entity_id: "reaction.ecocyc.RXN-22964"
entity_type: "reaction"
name: "RXN-22964"
source_database: "EcoCyc"
source_id: "RXN-22964"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22964

`reaction.ecocyc.RXN-22964`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22964`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Lipoyl-Protein-N6-lipoyllysine + NAD + WATER -> Lipoyl-Protein-L-Lysine + CPD-25444 + NIACINAMIDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Lipoyl-Protein-N6-lipoyllysine + NAD + WATER -> Lipoyl-Protein-L-Lysine + CPD-25444 + NIACINAMIDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by protein-lysine deacetylase/desuccinylase/delipoylase (complex.ecocyc.CPLX0-8550). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), a [lipoyl-carrier protein]-N6-[(R)-lipoyl]-L-lysine (molecule.ecocyc.Lipoyl-Protein-N6-lipoyllysine). Products: Nicotinamide (molecule.C00153), 2''-O-lipoyl-ADP-D-ribose (molecule.ecocyc.CPD-25444), a [lipoyl-carrier protein]-L-lysine (molecule.ecocyc.Lipoyl-Protein-L-Lysine).

## Annotation

Lipoyl-Protein-N6-lipoyllysine + NAD + WATER -> Lipoyl-Protein-L-Lysine + CPD-25444 + NIACINAMIDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8550|complex.ecocyc.CPLX0-8550]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00153|molecule.C00153]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-25444|molecule.ecocyc.CPD-25444]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Lipoyl-Protein-L-Lysine|molecule.ecocyc.Lipoyl-Protein-L-Lysine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Lipoyl-Protein-N6-lipoyllysine|molecule.ecocyc.Lipoyl-Protein-N6-lipoyllysine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22964`

## Notes

Lipoyl-Protein-N6-lipoyllysine + NAD + WATER -> Lipoyl-Protein-L-Lysine + CPD-25444 + NIACINAMIDE; direction=PHYSIOL-LEFT-TO-RIGHT
