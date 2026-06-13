---
entity_id: "molecule.C02593"
entity_type: "small_molecule"
name: "Tetradecanoyl-CoA"
source_database: "KEGG"
source_id: "C02593"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Tetradecanoyl-CoA"
  - "Myristoyl-CoA"
---

# Tetradecanoyl-CoA

`molecule.C02593`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02593`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Tetradecanoyl-CoA; Myristoyl-CoA EcoCyc common name: myristoyl-CoA.

## Biological Role

Consumed as substrate in 2 reaction(s).

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)

## Annotation

KEGG compound: Tetradecanoyl-CoA; Myristoyl-CoA

## Pathways

- `eco00071` Fatty acid degradation (KEGG)

## Outgoing Edges (2)

- `is_substrate_of` --> [[reaction.ecocyc.RXN-17021|reaction.ecocyc.RXN-17021]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17023|reaction.ecocyc.RXN-17023]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C02593`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
