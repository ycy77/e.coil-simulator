---
entity_id: "molecule.C01185"
entity_type: "small_molecule"
name: "Nicotinate D-ribonucleotide"
source_database: "KEGG"
source_id: "C01185"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Nicotinate D-ribonucleotide"
  - "beta-Nicotinate D-ribonucleotide"
  - "Nicotinate ribonucleotide"
  - "Nicotinic acid ribonucleotide"
---

# Nicotinate D-ribonucleotide

`molecule.C01185`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01185`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Nicotinate D-ribonucleotide; beta-Nicotinate D-ribonucleotide; Nicotinate ribonucleotide; Nicotinic acid ribonucleotide EcoCyc common name: β-nicotinate D-ribonucleotide.

## Biological Role

Consumed as substrate in 5 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)

## Annotation

KEGG compound: Nicotinate D-ribonucleotide; beta-Nicotinate D-ribonucleotide; Nicotinate ribonucleotide; Nicotinic acid ribonucleotide

## Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)

## Outgoing Edges (8)

- `is_product_of` --> [[reaction.ecocyc.NICOTINATEPRIBOSYLTRANS-RXN|reaction.ecocyc.NICOTINATEPRIBOSYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.NMNAMIDOHYDRO-RXN|reaction.ecocyc.NMNAMIDOHYDRO-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R01724|reaction.R01724]] `KEGG` `database` - C01185 + C00013 + C00008 + C00009 <=> C00253 + C00119 + C00002 + C00001 + C00080
- `is_substrate_of` --> [[reaction.R04148|reaction.R04148]] `KEGG` `database` - C01185 + C03114 <=> C00253 + C04778 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.DMBPPRIBOSYLTRANS-RXN|reaction.ecocyc.DMBPPRIBOSYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.NICONUCADENYLYLTRAN-RXN|reaction.ecocyc.NICONUCADENYLYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.QUINOPRIBOTRANS-RXN|reaction.ecocyc.QUINOPRIBOTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.QUINOPRIBOTRANS-RXN|reaction.ecocyc.QUINOPRIBOTRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01185`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
