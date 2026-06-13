---
entity_id: "molecule.C02741"
entity_type: "small_molecule"
name: "Phosphoribosyl-AMP"
source_database: "KEGG"
source_id: "C02741"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Phosphoribosyl-AMP"
  - "N1-(5-Phospho-D-ribosyl)-AMP"
  - "1-(5-Phosphoribosyl)-AMP"
  - "1-(5-Phospho-beta-D-ribosyl)-AMP"
---

# Phosphoribosyl-AMP

`molecule.C02741`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02741`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Phosphoribosyl-AMP; N1-(5-Phospho-D-ribosyl)-AMP; 1-(5-Phosphoribosyl)-AMP; 1-(5-Phospho-beta-D-ribosyl)-AMP EcoCyc common name: 1-(5-phospho-β-D-ribosyl)-AMP.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00340` Histidine metabolism (KEGG)

## Annotation

KEGG compound: Phosphoribosyl-AMP; N1-(5-Phospho-D-ribosyl)-AMP; 1-(5-Phosphoribosyl)-AMP; 1-(5-Phospho-beta-D-ribosyl)-AMP

## Pathways

- `eco00340` Histidine metabolism (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.HISTPRATPHYD-RXN|reaction.ecocyc.HISTPRATPHYD-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.HISTCYCLOHYD-RXN|reaction.ecocyc.HISTCYCLOHYD-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C02741`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
