---
entity_id: "reaction.ecocyc.3.4.19.12-RXN"
entity_type: "reaction"
name: "3.4.19.12-RXN"
source_database: "EcoCyc"
source_id: "3.4.19.12-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Ubiquitin thiolesterase"
  - "Ubiquitin C-terminal hydrolase"
  - "Ubiquitin carboxyl-terminal hydrolase"
---

# 3.4.19.12-RXN

`reaction.ecocyc.3.4.19.12-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.4.19.12-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTEIN-N-UBIQUITYL-LYSINE + WATER -> Protein-L-lysine + Ubiquitin-C-Terminal-Glycine; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PROTEIN-N-UBIQUITYL-LYSINE + WATER -> Protein-L-lysine + Ubiquitin-C-Terminal-Glycine; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by elaD (protein.Q47013). Substrates: H2O (molecule.C00001), a [protein]-N6-monoubiquitinyl-L-lysine (molecule.ecocyc.PROTEIN-N-UBIQUITYL-LYSINE). Products: Protein lysine (molecule.C02188), a [ubiquitin] C-terminal glycine (molecule.ecocyc.Ubiquitin-C-Terminal-Glycine).

## Annotation

PROTEIN-N-UBIQUITYL-LYSINE + WATER -> Protein-L-lysine + Ubiquitin-C-Terminal-Glycine; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.Q47013|protein.Q47013]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C02188|molecule.C02188]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Ubiquitin-C-Terminal-Glycine|molecule.ecocyc.Ubiquitin-C-Terminal-Glycine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.PROTEIN-N-UBIQUITYL-LYSINE|molecule.ecocyc.PROTEIN-N-UBIQUITYL-LYSINE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.4.19.12-RXN`

## Notes

PROTEIN-N-UBIQUITYL-LYSINE + WATER -> Protein-L-lysine + Ubiquitin-C-Terminal-Glycine; direction=PHYSIOL-LEFT-TO-RIGHT
