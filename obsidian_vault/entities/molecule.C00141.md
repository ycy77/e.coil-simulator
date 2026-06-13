---
entity_id: "molecule.C00141"
entity_type: "small_molecule"
name: "3-Methyl-2-oxobutanoic acid"
source_database: "KEGG"
source_id: "C00141"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "3-Methyl-2-oxobutanoic acid"
  - "3-Methyl-2-oxobutyric acid"
  - "3-Methyl-2-oxobutanoate"
  - "2-Oxo-3-methylbutanoate"
  - "2-Oxoisovalerate"
  - "2-Oxoisopentanoate"
  - "alpha-Ketovaline"
  - "2-Ketovaline"
  - "2-Keto-3-methylbutyric acid"
  - "alpha-Ketoisovalerate"
---

# 3-Methyl-2-oxobutanoic acid

`molecule.C00141`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00141`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 3-Methyl-2-oxobutanoic acid; 3-Methyl-2-oxobutyric acid; 3-Methyl-2-oxobutanoate; 2-Oxo-3-methylbutanoate; 2-Oxoisovalerate; 2-Oxoisopentanoate; alpha-Ketovaline; 2-Ketovaline; 2-Keto-3-methylbutyric acid; alpha-Ketoisovalerate EcoCyc common name: 3-methyl-2-oxobutanoate.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)

## Annotation

KEGG compound: 3-Methyl-2-oxobutanoic acid; 3-Methyl-2-oxobutyric acid; 3-Methyl-2-oxobutanoate; 2-Oxo-3-methylbutanoate; 2-Oxoisovalerate; 2-Oxoisopentanoate; alpha-Ketovaline; 2-Ketovaline; 2-Keto-3-methylbutyric acid; alpha-Ketoisovalerate

## Pathways

- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)

## Outgoing Edges (8)

- `is_product_of` --> [[reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERVAL-RXN|reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERVAL-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.DIHYDROXYISOVALDEHYDRAT-RXN|reaction.ecocyc.DIHYDROXYISOVALDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.VALINE-PYRUVATE-AMINOTRANSFER-RXN|reaction.ecocyc.VALINE-PYRUVATE-AMINOTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.2-ISOPROPYLMALATESYN-RXN|reaction.ecocyc.2-ISOPROPYLMALATESYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-RXN|reaction.ecocyc.3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERLEU-RXN|reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERLEU-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-10814|reaction.ecocyc.RXN-10814]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.TYROSINE-AMINOTRANSFERASE-RXN|reaction.ecocyc.TYROSINE-AMINOTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00141`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
