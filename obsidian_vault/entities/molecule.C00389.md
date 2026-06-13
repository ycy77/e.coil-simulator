---
entity_id: "molecule.C00389"
entity_type: "small_molecule"
name: "Quercetin"
source_database: "KEGG"
source_id: "C00389"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Quercetin"
  - "3,3',4,5,7-Pentahydroxyflavone"
  - "3,5,7,3',4'-Pentahydroxyflavone"
---

# Quercetin

`molecule.C00389`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00389`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Quercetin; 3,3',4,5,7-Pentahydroxyflavone; 3,5,7,3',4'-Pentahydroxyflavone Quercetin is a plant flavonol that is found in many fruits, vegetables, leaves, seeds, and grains. It was first isolated from an oak tree (genus TAX-3511) hence its name. Quercetin has a bitter flavor and is used as an ingredient in dietary supplements, beverages, and foods. It is one of the most abundant dietary flavonoids. The compound was shown to act as a competitive inhibitor of EC-4.2.1.59 (FabZ) from the pathogenic bacterium TAX-210 .

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00946` Degradation of flavonoids (KEGG)

## Annotation

KEGG compound: Quercetin; 3,3',4,5,7-Pentahydroxyflavone; 3,5,7,3',4'-Pentahydroxyflavone

## Pathways

- `eco00946` Degradation of flavonoids (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R13065|reaction.R13065]] `KEGG` `database` - C05623 + C00001 <=> C00389 + C00221
- `is_substrate_of` --> [[reaction.ecocyc.QUERCETIN-23-DIOXYGENASE-RXN|reaction.ecocyc.QUERCETIN-23-DIOXYGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ATPSYN-RXN|reaction.ecocyc.ATPSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-18737|reaction.ecocyc.RXN-18737]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00389`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
