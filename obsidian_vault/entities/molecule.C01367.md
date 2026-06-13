---
entity_id: "molecule.C01367"
entity_type: "small_molecule"
name: "3'-AMP"
source_database: "KEGG"
source_id: "C01367"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "3'-AMP"
  - "3'-Adenylic acid"
  - "3'-Adenosine monophosphate"
  - "Adenosine-3'-monophosphate"
  - "Adenosine 3'-phosphate"
  - "AMP 3'-phosphate"
---

# 3'-AMP

`molecule.C01367`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01367`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 3'-AMP; 3'-Adenylic acid; 3'-Adenosine monophosphate; Adenosine-3'-monophosphate; Adenosine 3'-phosphate; AMP 3'-phosphate EcoCyc common name: adenosine 3'-monophosphate.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)

## Annotation

KEGG compound: 3'-AMP; 3'-Adenylic acid; 3'-Adenosine monophosphate; Adenosine-3'-monophosphate; Adenosine 3'-phosphate; AMP 3'-phosphate

## Pathways

- `eco00230` Purine metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.RXN-14113|reaction.ecocyc.RXN-14113]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14126|reaction.ecocyc.RXN-14126]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.CITSYN-RXN|reaction.ecocyc.CITSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01367`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
