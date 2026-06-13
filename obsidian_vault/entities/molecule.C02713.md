---
entity_id: "molecule.C02713"
entity_type: "small_molecule"
name: "N-Acetylmuramate"
source_database: "KEGG"
source_id: "C02713"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "N-Acetylmuramate"
  - "N-Acetylmuramic acid"
  - "N-Acetyl-D-muramoate"
---

# N-Acetylmuramate

`molecule.C02713`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02713`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: N-Acetylmuramate; N-Acetylmuramic acid; N-Acetyl-D-muramoate EcoCyc common name: N-acetyl-D-muramate.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: N-Acetylmuramate; N-Acetylmuramic acid; N-Acetyl-D-muramoate

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R04112|reaction.R04112]] `KEGG` `database` - C02999 + C00001 <=> C02713 + C00041
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-17|reaction.ecocyc.RXN0-17]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.2.3.1.157-RXN|reaction.ecocyc.2.3.1.157-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-5226|reaction.ecocyc.RXN0-5226]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C02713`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
