---
entity_id: "molecule.C01181"
entity_type: "small_molecule"
name: "4-Trimethylammoniobutanoate"
source_database: "KEGG"
source_id: "C01181"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "4-Trimethylammoniobutanoate"
  - "Butyro-betaine"
  - "gamma-Butyrobetaine"
---

# 4-Trimethylammoniobutanoate

`molecule.C01181`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01181`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 4-Trimethylammoniobutanoate; Butyro-betaine; gamma-Butyrobetaine EcoCyc common name: γ-butyrobetaine.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: 4-Trimethylammoniobutanoate; Butyro-betaine; gamma-Butyrobetaine

## Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.RXN0-3601|reaction.ecocyc.RXN0-3601]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-100|reaction.ecocyc.TRANS-RXN-100]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-18258|reaction.ecocyc.RXN-18258]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-100|reaction.ecocyc.TRANS-RXN-100]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.CROBETREDUCT-RXN|reaction.ecocyc.CROBETREDUCT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.CPLX0-7906|complex.ecocyc.CPLX0-7906]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C01181`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
