---
entity_id: "molecule.C00266"
entity_type: "small_molecule"
name: "Glycolaldehyde"
source_database: "KEGG"
source_id: "C00266"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Glycolaldehyde"
  - "Hydroxyacetaldehyde"
---

# Glycolaldehyde

`molecule.C00266`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00266`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Glycolaldehyde; Hydroxyacetaldehyde

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 8 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco00790` Folate biosynthesis (KEGG)

## Annotation

KEGG compound: Glycolaldehyde; Hydroxyacetaldehyde

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco00790` Folate biosynthesis (KEGG)

## Outgoing Edges (11)

- `is_product_of` --> [[reaction.ecocyc.4.1.2.28-RXN|reaction.ecocyc.4.1.2.28-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.DARABALDOL-RXN|reaction.ecocyc.DARABALDOL-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLYCOLALDREDUCT-RXN|reaction.ecocyc.GLYCOLALDREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.H2NEOPTERINALDOL-RXN|reaction.ecocyc.H2NEOPTERINALDOL-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-13418|reaction.ecocyc.RXN-13418]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14023|reaction.ecocyc.RXN-14023]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-18376|reaction.ecocyc.RXN-18376]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6563|reaction.ecocyc.RXN0-6563]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.GLYCOLALD-DEHYDROG-RXN|reaction.ecocyc.GLYCOLALD-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14642|reaction.ecocyc.RXN-14642]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.GLYCOLALD-DEHYDROG-RXN|reaction.ecocyc.GLYCOLALD-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00266`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
