---
entity_id: "molecule.C00363"
entity_type: "small_molecule"
name: "dTDP"
source_database: "KEGG"
source_id: "C00363"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "dTDP"
  - "Deoxythymidine 5'-diphosphate"
---

# dTDP

`molecule.C00363`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00363`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: dTDP; Deoxythymidine 5'-diphosphate

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Annotation

KEGG compound: dTDP; Deoxythymidine 5'-diphosphate

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.DTMPKI-RXN|reaction.ecocyc.DTMPKI-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.FUC4NACTRANS-RXN|reaction.ecocyc.FUC4NACTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5129|reaction.ecocyc.RXN0-5129]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.DTDPKIN-RXN|reaction.ecocyc.DTDPKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.PHOSPHOGLUCMUT-RXN|reaction.ecocyc.PHOSPHOGLUCMUT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00363`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
