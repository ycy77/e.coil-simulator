---
entity_id: "molecule.C00526"
entity_type: "small_molecule"
name: "Deoxyuridine"
source_database: "KEGG"
source_id: "C00526"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Deoxyuridine"
  - "2-Deoxyuridine"
  - "2'-Deoxyuridine"
---

# Deoxyuridine

`molecule.C00526`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00526`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Deoxyuridine; 2-Deoxyuridine; 2'-Deoxyuridine EcoCyc common name: 2'-deoxyuridine.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Deoxyuridine; 2-Deoxyuridine; 2'-Deoxyuridine

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (7)

- `is_product_of` --> [[reaction.ecocyc.CYTIDEAM-RXN|reaction.ecocyc.CYTIDEAM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14143|reaction.ecocyc.RXN-14143]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14523|reaction.ecocyc.RXN-14523]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-108F|reaction.ecocyc.TRANS-RXN-108F]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.DURIDKI-RXN|reaction.ecocyc.DURIDKI-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-108F|reaction.ecocyc.TRANS-RXN-108F]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.URA-PHOSPH-RXN|reaction.ecocyc.URA-PHOSPH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.P0AFF2|protein.P0AFF2]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00526`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
