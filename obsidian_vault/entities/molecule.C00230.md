---
entity_id: "molecule.C00230"
entity_type: "small_molecule"
name: "3,4-Dihydroxybenzoate"
source_database: "KEGG"
source_id: "C00230"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "3,4-Dihydroxybenzoate"
  - "3,4-Dihydroxybenzoic acid"
  - "Protocatechuate"
  - "Protocatechuic acid"
---

# 3,4-Dihydroxybenzoate

`molecule.C00230`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00230`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 3,4-Dihydroxybenzoate; 3,4-Dihydroxybenzoic acid; Protocatechuate; Protocatechuic acid EcoCyc common name: protocatechuate. 4-Carboxy-1,2-dihydroxybenzene

## Enriched Pathways

- `eco00362` Benzoate degradation (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00623` Toluene degradation (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)

## Annotation

KEGG compound: 3,4-Dihydroxybenzoate; 3,4-Dihydroxybenzoic acid; Protocatechuate; Protocatechuic acid

## Pathways

- `eco00362` Benzoate degradation (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00623` Toluene degradation (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)

## Outgoing Edges (1)

- `represses` --> [[reaction.ecocyc.GLUTDECARBOX-RXN|reaction.ecocyc.GLUTDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00230`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
