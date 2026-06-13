---
entity_id: "molecule.C03589"
entity_type: "small_molecule"
name: "4-Hydroxy-2-oxopentanoate"
source_database: "KEGG"
source_id: "C03589"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "4-Hydroxy-2-oxopentanoate"
  - "4-Hydroxy-2-oxovalerate"
---

# 4-Hydroxy-2-oxopentanoate

`molecule.C03589`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03589`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 4-Hydroxy-2-oxopentanoate; 4-Hydroxy-2-oxovalerate EcoCyc common name: (S)-4-hydroxy-2-oxopentanoate.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00621` Dioxin degradation (KEGG)
- `eco00622` Xylene degradation (KEGG)

## Annotation

KEGG compound: 4-Hydroxy-2-oxopentanoate; 4-Hydroxy-2-oxovalerate

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00621` Dioxin degradation (KEGG)
- `eco00622` Xylene degradation (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R00750|reaction.R00750]] `KEGG` `database` - C00084 + C00022 <=> C03589
- `is_product_of` --> [[reaction.R02601|reaction.R02601]] `KEGG` `database` - C00596 + C00001 <=> C03589
- `is_substrate_of` --> [[reaction.ecocyc.2-OXOPENT-4-ENOATE-HYDRATASE-RXN|reaction.ecocyc.2-OXOPENT-4-ENOATE-HYDRATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.MHPELY-RXN|reaction.ecocyc.MHPELY-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-13460|reaction.ecocyc.RXN-13460]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03589`
- `EcoCyc:CPD-21382`
- `PUBCHEM:9543038`
- `CHEBI:58222`
- `canonicalized_from:molecule.ecocyc.CPD-21382`

## Notes

Included because it appears in at least one E. coli KEGG pathway. | molecule.ecocyc.CPD-21382: EcoCyc:CPD-21382
