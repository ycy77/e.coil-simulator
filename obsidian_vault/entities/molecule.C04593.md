---
entity_id: "molecule.C04593"
entity_type: "small_molecule"
name: "(2S,3R)-3-Hydroxybutane-1,2,3-tricarboxylate"
source_database: "KEGG"
source_id: "C04593"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(2S,3R)-3-Hydroxybutane-1,2,3-tricarboxylate"
  - "Methylisocitrate"
  - "Methylisocitric acid"
---

# (2S,3R)-3-Hydroxybutane-1,2,3-tricarboxylate

`molecule.C04593`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04593`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (2S,3R)-3-Hydroxybutane-1,2,3-tricarboxylate; Methylisocitrate; Methylisocitric acid EcoCyc common name: (2R,3S)-2-methylisocitrate.

## Biological Role

Consumed as substrate in 4 reaction(s).

## Enriched Pathways

- `eco00640` Propanoate metabolism (KEGG)

## Annotation

KEGG compound: (2S,3R)-3-Hydroxybutane-1,2,3-tricarboxylate; Methylisocitrate; Methylisocitric acid

## Pathways

- `eco00640` Propanoate metabolism (KEGG)

## Outgoing Edges (4)

- `is_substrate_of` --> [[reaction.R00409|reaction.R00409]] `KEGG` `database` - C04593 <=> C00022 + C00042
- `is_substrate_of` --> [[reaction.R04425|reaction.R04425]] `KEGG` `database` - C04593 <=> C04225 + C00001
- `is_substrate_of` --> [[reaction.ecocyc.4.2.1.99-RXN|reaction.ecocyc.4.2.1.99-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.METHYLISOCITRATE-LYASE-RXN|reaction.ecocyc.METHYLISOCITRATE-LYASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04593`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
