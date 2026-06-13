---
entity_id: "molecule.C01412"
entity_type: "small_molecule"
name: "Butanal"
source_database: "KEGG"
source_id: "C01412"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Butanal"
  - "Butyraldehyde"
---

# Butanal

`molecule.C01412`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01412`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Butanal; Butyraldehyde EcoCyc common name: 1-butanal.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00650` Butanoate metabolism (KEGG)

## Annotation

KEGG compound: Butanal; Butyraldehyde

## Pathways

- `eco00650` Butanoate metabolism (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.RXN0-6973|reaction.ecocyc.RXN0-6973]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9562|reaction.ecocyc.RXN-9562]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01412`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
