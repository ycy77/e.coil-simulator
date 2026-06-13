---
entity_id: "reaction.ecocyc.PROTEIN-TYROSINE-PHOSPHATASE-RXN"
entity_type: "reaction"
name: "PROTEIN-TYROSINE-PHOSPHATASE-RXN"
source_database: "EcoCyc"
source_id: "PROTEIN-TYROSINE-PHOSPHATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "PTPASE"
  - "PHOSPHOTYROSINE PHOSPHATASE"
---

# PROTEIN-TYROSINE-PHOSPHATASE-RXN

`reaction.ecocyc.PROTEIN-TYROSINE-PHOSPHATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PROTEIN-TYROSINE-PHOSPHATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DEPHOSPHORYLATES O-PHOSPHOTYROSINE GROUPS IN PHOSPHOPROTEINS, SUCH AS THE PRODUCTS OF EC 2.7.1.112. EcoCyc reaction equation: Protein-tyrosine-phosphates + WATER -> Pi + Protein-Tyrosines; direction=PHYSIOL-LEFT-TO-RIGHT. DEPHOSPHORYLATES O-PHOSPHOTYROSINE GROUPS IN PHOSPHOPROTEINS, SUCH AS THE PRODUCTS OF EC 2.7.1.112.

## Biological Role

Catalyzed by wzb (protein.P0AAB2), etp (protein.P0ACZ2), pphA (protein.P55798), pphB (protein.P55799). Substrates: H2O (molecule.C00001), a [protein]-L-tyrosine phosphate (molecule.ecocyc.Protein-tyrosine-phosphates). Products: phosphate (molecule.ecocyc.Pi), a [protein]-L-tyrosine (molecule.ecocyc.Protein-Tyrosines).

## Annotation

DEPHOSPHORYLATES O-PHOSPHOTYROSINE GROUPS IN PHOSPHOPROTEINS, SUCH AS THE PRODUCTS OF EC 2.7.1.112.

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P0AAB2|protein.P0AAB2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0ACZ2|protein.P0ACZ2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P55798|protein.P55798]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P55799|protein.P55799]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Protein-Tyrosines|molecule.ecocyc.Protein-Tyrosines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-tyrosine-phosphates|molecule.ecocyc.Protein-tyrosine-phosphates]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PROTEIN-TYROSINE-PHOSPHATASE-RXN`

## Notes

Protein-tyrosine-phosphates + WATER -> Pi + Protein-Tyrosines; direction=PHYSIOL-LEFT-TO-RIGHT
