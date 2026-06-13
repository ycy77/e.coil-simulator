---
entity_id: "molecule.C01041"
entity_type: "small_molecule"
name: "Monodehydroascorbate"
source_database: "KEGG"
source_id: "C01041"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Monodehydroascorbate"
  - "Monodehydroascorbate radical"
  - "Ascorbate radical"
  - "Semidehydroascorbic acid"
---

# Monodehydroascorbate

`molecule.C01041`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01041`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Monodehydroascorbate; Monodehydroascorbate radical; Ascorbate radical; Semidehydroascorbic acid EcoCyc common name: monodehydroascorbate radical. ASCORBATE is oxidized in cells to CPD-13907 dehydroascorbate via the radical CPD-318. CPD-13907 Dehydroascorbate can be recycled back to ascorbate by the PWY-2261, or it can be further broken down in vivo by irreversible reactions.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)

## Annotation

KEGG compound: Monodehydroascorbate; Monodehydroascorbate radical; Ascorbate radical; Semidehydroascorbic acid

## Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.RXN-10981|reaction.ecocyc.RXN-10981]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-3521|reaction.ecocyc.RXN-3521]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-3523|reaction.ecocyc.RXN-3523]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01041`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
