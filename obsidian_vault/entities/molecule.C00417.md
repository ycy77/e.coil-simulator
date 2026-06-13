---
entity_id: "molecule.C00417"
entity_type: "small_molecule"
name: "cis-Aconitate"
source_database: "KEGG"
source_id: "C00417"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "cis-Aconitate"
  - "cis-Aconitic acid"
---

# cis-Aconitate

`molecule.C00417`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00417`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: cis-Aconitate; cis-Aconitic acid CIS-ACONITATE is named after the plant TAX-112591, from which it was first isolated in 1828 . The plants of the genus Aconitum (family of the Ranunculaceae) are famous for the many alkaloids they contain .

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)

## Annotation

KEGG compound: cis-Aconitate; cis-Aconitic acid

## Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)

## Outgoing Edges (7)

- `is_product_of` --> [[reaction.R01325|reaction.R01325]] `KEGG` `database` - C00158 <=> C00417 + C00001
- `is_product_of` --> [[reaction.R01900|reaction.R01900]] `KEGG` `database` - C00311 <=> C00417 + C00001
- `is_product_of` --> [[reaction.ecocyc.ACONITATE-DELTA-ISOMERASE-RXN|reaction.ecocyc.ACONITATE-DELTA-ISOMERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ACONITATEDEHYDR-RXN|reaction.ecocyc.ACONITATEDEHYDR-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.ACONITATEHYDR-RXN|reaction.ecocyc.ACONITATEHYDR-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ISOCIT-CLEAV-RXN|reaction.ecocyc.ISOCIT-CLEAV-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PREPHENATEDEHYDRAT-RXN|reaction.ecocyc.PREPHENATEDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00417`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
