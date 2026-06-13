---
entity_id: "molecule.C00493"
entity_type: "small_molecule"
name: "Shikimate"
source_database: "KEGG"
source_id: "C00493"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Shikimate"
  - "Shikimic acid"
  - "3,4,5-Trihydroxy-1-cyclohexenecarboxylic acid"
---

# Shikimate

`molecule.C00493`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00493`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Shikimate; Shikimic acid; 3,4,5-Trihydroxy-1-cyclohexenecarboxylic acid SHIKIMATE "Shikimate" is an important intermediate in the chorismate biosynthetic pathway. It was first isolated from Japanese star anise. Shikimate is used for the production of some antiviral drugs used to halt the spread of the flu virus, but as a biosynthetic intermediate, it is usually not found in high concentrations in organisms. Shikimate can be easily harvested from the needles of several species of pine trees, and biosynthetic pathways in TAX-562 have been enhanced to obtain sufficient amounts of the metabolite for commercial use.

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)

## Annotation

KEGG compound: Shikimate; Shikimic acid; 3,4,5-Trihydroxy-1-cyclohexenecarboxylic acid

## Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-27|reaction.ecocyc.TRANS-RXN-27]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11174|reaction.ecocyc.RXN-11174]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SHIKIMATE-5-DEHYDROGENASE-RXN|reaction.ecocyc.SHIKIMATE-5-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SHIKIMATE-KINASE-RXN|reaction.ecocyc.SHIKIMATE-KINASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-27|reaction.ecocyc.TRANS-RXN-27]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.SHIKIMATE-5-DEHYDROGENASE-RXN|reaction.ecocyc.SHIKIMATE-5-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P76350|protein.P76350]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00493`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
