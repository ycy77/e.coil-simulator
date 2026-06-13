---
entity_id: "molecule.C00180"
entity_type: "small_molecule"
name: "Benzoate"
source_database: "KEGG"
source_id: "C00180"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Benzoate"
  - "Benzoic acid"
  - "Benzenecarboxylic acid"
  - "Phenylformic acid"
  - "Dracylic acid"
---

# Benzoate

`molecule.C00180`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00180`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Benzoate; Benzoic acid; Benzenecarboxylic acid; Phenylformic acid; Dracylic acid

## Biological Role

Produced in 1 reaction(s).

## Enriched Pathways

- `eco00362` Benzoate degradation (KEGG)
- `eco00621` Dioxin degradation (KEGG)
- `eco00623` Toluene degradation (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)

## Annotation

KEGG compound: Benzoate; Benzoic acid; Benzenecarboxylic acid; Phenylformic acid; Dracylic acid

## Pathways

- `eco00362` Benzoate degradation (KEGG)
- `eco00621` Dioxin degradation (KEGG)
- `eco00623` Toluene degradation (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.RXN-24038|reaction.ecocyc.RXN-24038]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `represses` --> [[reaction.ecocyc.RXN-19492|reaction.ecocyc.RXN-19492]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-301|reaction.ecocyc.RXN0-301]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.TRANS-RXN0-571|reaction.ecocyc.TRANS-RXN0-571]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00180`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
