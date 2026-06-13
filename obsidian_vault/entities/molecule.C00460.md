---
entity_id: "molecule.C00460"
entity_type: "small_molecule"
name: "dUTP"
source_database: "KEGG"
source_id: "C00460"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "dUTP"
  - "2'-Deoxyuridine 5'-triphosphate"
---

# dUTP

`molecule.C00460`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00460`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: dUTP; 2'-Deoxyuridine 5'-triphosphate

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Annotation

KEGG compound: dUTP; 2'-Deoxyuridine 5'-triphosphate

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R02331|reaction.R02331]] `KEGG` `database` - C00002 + C01346 <=> C00008 + C00460
- `is_product_of` --> [[reaction.ecocyc.DCTP-DEAM-RXN|reaction.ecocyc.DCTP-DEAM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.DUDPKIN-RXN|reaction.ecocyc.DUDPKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-724|reaction.ecocyc.RXN0-724]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.DUTP-PYROP-RXN|reaction.ecocyc.DUTP-PYROP-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00460`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
