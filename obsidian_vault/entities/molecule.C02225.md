---
entity_id: "molecule.C02225"
entity_type: "small_molecule"
name: "2-Methylcitrate"
source_database: "KEGG"
source_id: "C02225"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2-Methylcitrate"
  - "(2S,3S)-2-Methylcitrate"
  - "2-Hydroxybutane-1,2,3-tricarboxylate"
  - "(2S,3S)-2-Hydroxybutane-1,2,3-tricarboxylate"
  - "(2S,3S)-2-Methylcitric acid"
  - "2-methylcitric acid"
---

# 2-Methylcitrate

`molecule.C02225`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02225`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2-Methylcitrate; (2S,3S)-2-Methylcitrate; 2-Hydroxybutane-1,2,3-tricarboxylate; (2S,3S)-2-Hydroxybutane-1,2,3-tricarboxylate; (2S,3S)-2-Methylcitric acid

## Biological Role

Consumed as substrate in 1 reaction(s).

## Enriched Pathways

- `eco00640` Propanoate metabolism (KEGG)

## Annotation

KEGG compound: 2-Methylcitrate; (2S,3S)-2-Methylcitrate; 2-Hydroxybutane-1,2,3-tricarboxylate; (2S,3S)-2-Hydroxybutane-1,2,3-tricarboxylate; (2S,3S)-2-Methylcitric acid

## Pathways

- `eco00640` Propanoate metabolism (KEGG)

## Outgoing Edges (1)

- `is_substrate_of` --> [[reaction.R04424|reaction.R04424]] `KEGG` `database` - C02225 <=> C04225 + C00001

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C02225`
- `EcoCyc:CPD-25849`
- `CHEBI:15598`
- `canonicalized_from:molecule.ecocyc.CPD-25849`

## Notes

Included because it appears in at least one E. coli KEGG pathway. | molecule.ecocyc.CPD-25849: EcoCyc:CPD-25849
