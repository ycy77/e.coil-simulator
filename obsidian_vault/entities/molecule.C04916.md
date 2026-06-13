---
entity_id: "molecule.C04916"
entity_type: "small_molecule"
name: "N-(5'-Phospho-D-1'-ribulosylformimino)-5-amino-1-(5''-phospho-D-ribosyl)-4-imidazolecarboxamide"
source_database: "KEGG"
source_id: "C04916"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "N-(5'-Phospho-D-1'-ribulosylformimino)-5-amino-1-(5''-phospho-D-ribosyl)-4-imidazolecarboxamide"
  - "5-[(5-Phospho-1-deoxyribulos-1-ylamino)methylideneamino]-1-(5-phosphoribosyl)imidazole-4-carboxamide"
  - "Phosphoribulosyl-formimino-AICAR-phosphate"
  - "5-[(5-Phospho-1-deoxy-D-ribulos-1-ylamino)methylideneamino]-1-(5-phospho-beta-D-ribosyl)imidazole-4-carboxamide"
---

# N-(5'-Phospho-D-1'-ribulosylformimino)-5-amino-1-(5''-phospho-D-ribosyl)-4-imidazolecarboxamide

`molecule.C04916`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04916`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: N-(5'-Phospho-D-1'-ribulosylformimino)-5-amino-1-(5''-phospho-D-ribosyl)-4-imidazolecarboxamide; 5-[(5-Phospho-1-deoxyribulos-1-ylamino)methylideneamino]-1-(5-phosphoribosyl)imidazole-4-carboxamide; Phosphoribulosyl-formimino-AICAR-phosphate; 5-[(5-Phospho-1-deoxy-D-ribulos-1-ylamino)methylideneamino]-1-(5-phospho-beta-D-ribosyl)imidazole-4-carboxamide EcoCyc common name: phosphoribulosylformimino-AICAR-phosphate.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00340` Histidine metabolism (KEGG)

## Annotation

KEGG compound: N-(5'-Phospho-D-1'-ribulosylformimino)-5-amino-1-(5''-phospho-D-ribosyl)-4-imidazolecarboxamide; 5-[(5-Phospho-1-deoxyribulos-1-ylamino)methylideneamino]-1-(5-phosphoribosyl)imidazole-4-carboxamide; Phosphoribulosyl-formimino-AICAR-phosphate; 5-[(5-Phospho-1-deoxy-D-ribulos-1-ylamino)methylideneamino]-1-(5-phospho-beta-D-ribosyl)imidazole-4-carboxamide

## Pathways

- `eco00340` Histidine metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R04640|reaction.R04640]] `KEGG` `database` - C04896 <=> C04916
- `is_product_of` --> [[reaction.ecocyc.PRIBFAICARPISOM-RXN|reaction.ecocyc.PRIBFAICARPISOM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R12152|reaction.R12152]] `KEGG` `database` - C04916 + C00014 <=> C04677 + C04666 + C00001
- `is_substrate_of` --> [[reaction.ecocyc.GLUTAMIDOTRANS-RXN|reaction.ecocyc.GLUTAMIDOTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17900|reaction.ecocyc.RXN-17900]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04916`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
