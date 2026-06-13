---
entity_id: "molecule.C00159"
entity_type: "small_molecule"
name: "D-Mannose"
source_database: "KEGG"
source_id: "C00159"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Mannose"
  - "Mannose"
  - "Seminose"
  - "Carubinose"
  - "D-Mannopyranose"
---

# D-Mannose

`molecule.C00159`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00159`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Mannose; Mannose; Seminose; Carubinose; D-Mannopyranose This compound class represents a reducing sugar that exists in solution in multiple configurations. The open-chain structure shown here is provided only as a schematic illustration of chirality. Consult the appropriate class instances for information on specific ring structures and their anomeric configuration.

## Biological Role

Produced in 4 reaction(s).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: D-Mannose; Mannose; Seminose; Carubinose; D-Mannopyranose

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R01329|reaction.R01329]] `KEGG` `database` - C05400 + C00001 <=> C00159 + C00124
- `is_product_of` --> [[reaction.ecocyc.GDPMANMANHYDRO-RXN|reaction.ecocyc.GDPMANMANHYDRO-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17724|reaction.ecocyc.RXN-17724]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17725|reaction.ecocyc.RXN-17725]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `represses` --> [[reaction.ecocyc.ALDOSE1EPIM-RXN|reaction.ecocyc.ALDOSE1EPIM-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00159`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
