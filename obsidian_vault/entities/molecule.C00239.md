---
entity_id: "molecule.C00239"
entity_type: "small_molecule"
name: "dCMP"
source_database: "KEGG"
source_id: "C00239"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "dCMP"
  - "Deoxycytidylic acid"
  - "Deoxycytidine monophosphate"
  - "Deoxycytidylate"
  - "2'-Deoxycytidine 5'-monophosphate"
---

# dCMP

`molecule.C00239`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00239`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: dCMP; Deoxycytidylic acid; Deoxycytidine monophosphate; Deoxycytidylate; 2'-Deoxycytidine 5'-monophosphate

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Annotation

KEGG compound: dCMP; Deoxycytidylic acid; Deoxycytidine monophosphate; Deoxycytidylate; 2'-Deoxycytidine 5'-monophosphate

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.DCTP-PYROPHOSPHATASE-RXN|reaction.ecocyc.DCTP-PYROPHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-7913|reaction.ecocyc.RXN-7913]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5292|reaction.ecocyc.RXN0-5292]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00239`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
