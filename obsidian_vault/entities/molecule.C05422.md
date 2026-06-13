---
entity_id: "molecule.C05422"
entity_type: "small_molecule"
name: "Dehydroascorbate"
source_database: "KEGG"
source_id: "C05422"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Dehydroascorbate"
  - "Dehydroascorbic acid"
  - "L-Dehydroascorbate"
  - "L-Dehydroascorbic acid"
---

# Dehydroascorbate

`molecule.C05422`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05422`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Dehydroascorbate; Dehydroascorbic acid; L-Dehydroascorbate; L-Dehydroascorbic acid ASCORBATE is oxidized in cells to CPD-13907 dehydroascorbate via the radical CPD-318. CPD-13907 Dehydroascorbate can be recycled back to ascorbate by the PWY-2261, or it can be further broken down in vivo by irreversible reactions. The structure shown here is the one found in most text books. However, it appears to be incorrect. Dehydroascorbic acid in solution absorbs a single water molecule and forms a CPD-13907 "bicyclic monohydrate" structure .

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)

## Annotation

KEGG compound: Dehydroascorbate; Dehydroascorbic acid; L-Dehydroascorbate; L-Dehydroascorbic acid

## Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.ecocyc.RXN-12440|reaction.ecocyc.RXN-12440]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-12876|reaction.ecocyc.RXN-12876]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-3523|reaction.ecocyc.RXN-3523]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12862|reaction.ecocyc.RXN-12862]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12869|reaction.ecocyc.RXN-12869]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21400|reaction.ecocyc.RXN-21400]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05422`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
