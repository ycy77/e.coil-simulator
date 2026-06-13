---
entity_id: "reaction.ecocyc.RXN0-1842"
entity_type: "reaction"
name: "RXN0-1842"
source_database: "EcoCyc"
source_id: "RXN0-1842"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1842

`reaction.ecocyc.RXN0-1842`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1842`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The donor phospholipid has palmitate at the sn-1 position . A PagP homodimer catalyzes palmitate transfer from a phospholipid (sn-1 position) to lipid A or to a lipid A precursor (N-linked hydroxymyristate on the proximal unit) . EcoCyc reaction equation: CPD-17523 + CPD0-1283 -> HEPTA-ACYLATED-LIPID-A + 2-Acylglycero-Phosphocholines; direction=PHYSIOL-LEFT-TO-RIGHT. The donor phospholipid has palmitate at the sn-1 position . A PagP homodimer catalyzes palmitate transfer from a phospholipid (sn-1 position) to lipid A or to a lipid A precursor (N-linked hydroxymyristate on the proximal unit) .

## Biological Role

Substrates: a 1-palmitoyl-2-acyl-sn-glycero-3-phosphocholine (molecule.ecocyc.CPD-17523), lipid A (E. coli) (molecule.ecocyc.CPD0-1283). Products: 2-Acyl-sn-glycero-3-phosphocholine (molecule.C04233), a hepta-acylated lipid A (E. coli) (molecule.ecocyc.HEPTA-ACYLATED-LIPID-A).

## Annotation

The donor phospholipid has palmitate at the sn-1 position . A PagP homodimer catalyzes palmitate transfer from a phospholipid (sn-1 position) to lipid A or to a lipid A precursor (N-linked hydroxymyristate on the proximal unit) .

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C04233|molecule.C04233]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.HEPTA-ACYLATED-LIPID-A|molecule.ecocyc.HEPTA-ACYLATED-LIPID-A]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-17523|molecule.ecocyc.CPD-17523]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1283|molecule.ecocyc.CPD0-1283]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1842`

## Notes

CPD-17523 + CPD0-1283 -> HEPTA-ACYLATED-LIPID-A + 2-Acylglycero-Phosphocholines; direction=PHYSIOL-LEFT-TO-RIGHT
