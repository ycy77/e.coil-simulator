---
entity_id: "molecule.C02739"
entity_type: "small_molecule"
name: "1-(5-Phospho-D-ribosyl)-ATP"
source_database: "KEGG"
source_id: "C02739"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "1-(5-Phospho-D-ribosyl)-ATP"
  - "Phosphoribosyl-ATP"
  - "N1-(5-Phospho-D-ribosyl)-ATP"
  - "1-(5-Phosphoribosyl)-ATP"
  - "1-(5-Phospho-beta-D-ribosyl)-ATP"
---

# 1-(5-Phospho-D-ribosyl)-ATP

`molecule.C02739`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02739`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 1-(5-Phospho-D-ribosyl)-ATP; Phosphoribosyl-ATP; N1-(5-Phospho-D-ribosyl)-ATP; 1-(5-Phosphoribosyl)-ATP; 1-(5-Phospho-beta-D-ribosyl)-ATP EcoCyc common name: 1-(5-phospho-β-D-ribosyl)-ATP.

## Biological Role

Consumed as substrate in 2 reaction(s).

## Enriched Pathways

- `eco00340` Histidine metabolism (KEGG)

## Annotation

KEGG compound: 1-(5-Phospho-D-ribosyl)-ATP; Phosphoribosyl-ATP; N1-(5-Phospho-D-ribosyl)-ATP; 1-(5-Phosphoribosyl)-ATP; 1-(5-Phospho-beta-D-ribosyl)-ATP

## Pathways

- `eco00340` Histidine metabolism (KEGG)

## Outgoing Edges (2)

- `is_substrate_of` --> [[reaction.ecocyc.ATPPHOSPHORIBOSYLTRANS-RXN|reaction.ecocyc.ATPPHOSPHORIBOSYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.HISTPRATPHYD-RXN|reaction.ecocyc.HISTPRATPHYD-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C02739`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
