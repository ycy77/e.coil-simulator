---
entity_id: "molecule.C02305"
entity_type: "small_molecule"
name: "Phosphocreatine"
source_database: "KEGG"
source_id: "C02305"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Phosphocreatine"
  - "N-Phosphocreatine"
  - "Creatine phosphate"
---

# Phosphocreatine

`molecule.C02305`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02305`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Phosphocreatine; N-Phosphocreatine; Creatine phosphate EcoCyc common name: Nω-phosphocreatine.

## Biological Role

Consumed as substrate in 1 reaction(s).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)

## Annotation

KEGG compound: Phosphocreatine; N-Phosphocreatine; Creatine phosphate

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)

## Outgoing Edges (2)

- `is_substrate_of` --> [[reaction.ecocyc.PHOSPHOAMIDASE-RXN|reaction.ecocyc.PHOSPHOAMIDASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.THI-P-SYN-RXN|reaction.ecocyc.THI-P-SYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C02305`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
