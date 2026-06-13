---
entity_id: "molecule.C00077"
entity_type: "small_molecule"
name: "L-Ornithine"
source_database: "KEGG"
source_id: "C00077"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Ornithine"
  - "(S)-2,5-Diaminovaleric acid"
  - "(S)-2,5-Diaminopentanoic acid"
  - "(S)-2,5-Diaminopentanoate"
---

# L-Ornithine

`molecule.C00077`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00077`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Ornithine; (S)-2,5-Diaminovaleric acid; (S)-2,5-Diaminopentanoic acid; (S)-2,5-Diaminopentanoate

## Biological Role

Consumed as substrate in 8 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: L-Ornithine; (S)-2,5-Diaminovaleric acid; (S)-2,5-Diaminopentanoic acid; (S)-2,5-Diaminopentanoate

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (16)

- `activates` --> [[reaction.ecocyc.CARBPSYN-RXN|reaction.ecocyc.CARBPSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.R00669|reaction.R00669]] `KEGG` `database` - C00437 + C00001 <=> C00033 + C00077
- `is_product_of` --> [[reaction.ecocyc.ABC-37-RXN|reaction.ecocyc.ABC-37-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ACETYLORNDEACET-RXN|reaction.ecocyc.ACETYLORNDEACET-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-211|reaction.ecocyc.TRANS-RXN0-211]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00670|reaction.R00670]] `KEGG` `database` - C00077 <=> C00134 + C00011
- `is_substrate_of` --> [[reaction.R00672|reaction.R00672]] `KEGG` `database` - C00077 <=> C00515
- `is_substrate_of` --> [[reaction.ecocyc.ABC-37-RXN|reaction.ecocyc.ABC-37-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ORNCARBAMTRANSFER-RXN|reaction.ecocyc.ORNCARBAMTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ORNDECARBOX-RXN|reaction.ecocyc.ORNDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-23920|reaction.ecocyc.RXN-23920]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-23921|reaction.ecocyc.RXN-23921]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-211|reaction.ecocyc.TRANS-RXN0-211]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ACETYLORNDEACET-RXN|reaction.ecocyc.ACETYLORNDEACET-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.AGMATIN-RXN|reaction.ecocyc.AGMATIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ARGDECARBOX-RXN|reaction.ecocyc.ARGDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (2)

- `transports` <-- [[complex.ecocyc.ABC-3-CPLX|complex.ecocyc.ABC-3-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P0AAF1|protein.P0AAF1]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00077`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
