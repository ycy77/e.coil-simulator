---
entity_id: "molecule.C05984"
entity_type: "small_molecule"
name: "2-Hydroxybutanoic acid"
source_database: "KEGG"
source_id: "C05984"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2-Hydroxybutanoic acid"
  - "2-Hydroxybutyrate"
  - "2-Hydroxybutyric acid"
  - "(S)-2-Hydroxybutanoate"
  - "(2S)-2-Hydroxybutanoic acid"
---

# 2-Hydroxybutanoic acid

`molecule.C05984`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05984`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2-Hydroxybutanoic acid; 2-Hydroxybutyrate; 2-Hydroxybutyric acid; (S)-2-Hydroxybutanoate; (2S)-2-Hydroxybutanoic acid EcoCyc common name: (S)-2-hydroxybutanoate.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00640` Propanoate metabolism (KEGG)

## Annotation

KEGG compound: 2-Hydroxybutanoic acid; 2-Hydroxybutyrate; 2-Hydroxybutyric acid; (S)-2-Hydroxybutanoate; (2S)-2-Hydroxybutanoic acid

## Pathways

- `eco00640` Propanoate metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.RXN-17751|reaction.ecocyc.RXN-17751]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-622|reaction.ecocyc.TRANS-RXN0-622]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7227|reaction.ecocyc.RXN0-7227]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-622|reaction.ecocyc.TRANS-RXN0-622]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.Q46839|protein.Q46839]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C05984`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
