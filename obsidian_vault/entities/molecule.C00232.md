---
entity_id: "molecule.C00232"
entity_type: "small_molecule"
name: "Succinate semialdehyde"
source_database: "KEGG"
source_id: "C00232"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Succinate semialdehyde"
  - "Succinic semialdehyde"
  - "4-Oxobutanoate"
---

# Succinate semialdehyde

`molecule.C00232`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00232`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Succinate semialdehyde; Succinic semialdehyde; 4-Oxobutanoate

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

KEGG compound: Succinate semialdehyde; Succinic semialdehyde; 4-Oxobutanoate

## Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (8)

- `is_product_of` --> [[reaction.ecocyc.4-HYDROXYBUTYRATE-DEHYDROGENASE-RXN|reaction.ecocyc.4-HYDROXYBUTYRATE-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GABATRANSAM-RXN|reaction.ecocyc.GABATRANSAM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-18258|reaction.ecocyc.RXN-18258]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00713|reaction.R00713]] `KEGG` `database` - C00232 + C00003 + C00001 <=> C00042 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R00714|reaction.R00714]] `KEGG` `database` - C00232 + C00006 + C00001 <=> C00042 + C00005 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.SUCCINATE-SEMIALDEHYDE-DEHYDROGENASE-RXN|reaction.ecocyc.SUCCINATE-SEMIALDEHYDE-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SUCCSEMIALDDEHYDROG-RXN|reaction.ecocyc.SUCCSEMIALDDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.DIHYDRODIPICSYN-RXN|reaction.ecocyc.DIHYDRODIPICSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00232`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
