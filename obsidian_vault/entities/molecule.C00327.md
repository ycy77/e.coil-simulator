---
entity_id: "molecule.C00327"
entity_type: "small_molecule"
name: "L-Citrulline"
source_database: "KEGG"
source_id: "C00327"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Citrulline"
  - "2-Amino-5-ureidovaleric acid"
  - "Citrulline"
---

# L-Citrulline

`molecule.C00327`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00327`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Citrulline; 2-Amino-5-ureidovaleric acid; Citrulline L-CITRULLINE is a non-standard amino acid that is not normally incorporated into proteins during protein synthesis. Citrulline was first isolated from TAX-3653 (watermelon) in 1914 . It was re-isolated in 1930, at which time its chemical formula was determined and it was named (after the Latin name of the watermelon) .

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)

## Annotation

KEGG compound: L-Citrulline; 2-Amino-5-ureidovaleric acid; Citrulline

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R09107|reaction.R09107]] `KEGG` `database` - C15532 + C00001 <=> C00033 + C00327
- `is_product_of` --> [[reaction.ecocyc.ORNCARBAMTRANSFER-RXN|reaction.ecocyc.ORNCARBAMTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.ARGSUCCINSYN-RXN|reaction.ecocyc.ARGSUCCINSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.N-ACETYLTRANSFER-RXN|reaction.ecocyc.N-ACETYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00327`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
