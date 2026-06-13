---
entity_id: "molecule.C00086"
entity_type: "small_molecule"
name: "Urea"
source_database: "KEGG"
source_id: "C00086"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Urea"
  - "Carbamide"
---

# Urea

`molecule.C00086`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00086`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Urea; Carbamide

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 5 reaction(s).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00780` Biotin metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Urea; Carbamide

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00780` Biotin metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.R00776|reaction.R00776]] `KEGG` `database` - C00603 <=> C00048 + C00086
- `is_product_of` --> [[reaction.R01157|reaction.R01157]] `KEGG` `database` - C00179 + C00001 <=> C00134 + C00086
- `is_product_of` --> [[reaction.ecocyc.AGMATIN-RXN|reaction.ecocyc.AGMATIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-460|reaction.ecocyc.TRANS-RXN0-460]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.UREIDOGLYCOLATE-LYASE-RXN|reaction.ecocyc.UREIDOGLYCOLATE-LYASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-460|reaction.ecocyc.TRANS-RXN0-460]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00086`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
