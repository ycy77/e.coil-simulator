---
entity_id: "molecule.C00431"
entity_type: "small_molecule"
name: "5-Aminopentanoate"
source_database: "KEGG"
source_id: "C00431"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "5-Aminopentanoate"
  - "5-Aminopentanoic acid"
  - "5-Aminovaleric acid"
---

# 5-Aminopentanoate

`molecule.C00431`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00431`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 5-Aminopentanoate; 5-Aminopentanoic acid; 5-Aminovaleric acid

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)

## Annotation

KEGG compound: 5-Aminopentanoate; 5-Aminopentanoic acid; 5-Aminovaleric acid

## Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.RXN0-7318|reaction.ecocyc.RXN0-7318]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-384|reaction.ecocyc.TRANS-RXN-384]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-384|reaction.ecocyc.TRANS-RXN-384]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.VAGL-RXN|reaction.ecocyc.VAGL-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.TRANS-RXN-57|reaction.ecocyc.TRANS-RXN-57]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P25527|protein.P25527]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00431`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
