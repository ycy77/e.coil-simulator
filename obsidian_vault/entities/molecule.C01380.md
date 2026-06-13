---
entity_id: "molecule.C01380"
entity_type: "small_molecule"
name: "Ethylene glycol"
source_database: "KEGG"
source_id: "C01380"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Ethylene glycol"
  - "1,2-Ethanediol"
  - "Ethane-1,2-diol"
---

# Ethylene glycol

`molecule.C01380`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01380`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Ethylene glycol; 1,2-Ethanediol; Ethane-1,2-diol Ethylene glycol is commonly used as a coolant, as a deicing fluid, and to produce plastics such as polyethylene terephthalate. Eethylene glycol readily partitions into the aqueous phase, resulting in high mobility and rapid dispersion through the biosphere. Although the toxicity is low , acute exposure can result in kidney and brain damage and possibly teratogenesis.

## Biological Role

Consumed as substrate in 2 reaction(s).

## Enriched Pathways

- `eco00625` Chloroalkane and chloroalkene degradation (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)

## Annotation

KEGG compound: Ethylene glycol; 1,2-Ethanediol; Ethane-1,2-diol

## Pathways

- `eco00625` Chloroalkane and chloroalkene degradation (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)

## Outgoing Edges (2)

- `is_substrate_of` --> [[reaction.ecocyc.GLYCOLALDREDUCT-RXN|reaction.ecocyc.GLYCOLALDREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14023|reaction.ecocyc.RXN-14023]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01380`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
