---
entity_id: "molecule.C00741"
entity_type: "small_molecule"
name: "Diacetyl"
source_database: "KEGG"
source_id: "C00741"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Diacetyl"
  - "Biacetyl"
  - "Dimethylglyoxal"
  - "2,3-Butanedione"
---

# Diacetyl

`molecule.C00741`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00741`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Diacetyl; Biacetyl; Dimethylglyoxal; 2,3-Butanedione Diacetyl is an important flavor component in many fermented foods and beverages, including dairy and dairy-like products, beer and wine . It imparts a buttery aroma and flavour, and has an important stylistic role in wine. In beer, diacetyl is considered a spoilage factor. During beer maturation, 2-acetolactate is slowly converted to diacetyl by a chemical, non-enzymatic process, and the diacetyl is converted to acetoin by diacetyl reductase of the yeast cells. for this purpose, purified enzyme is sometimes added to the wort .

## Biological Role

Produced in 2 reaction(s).

## Enriched Pathways

- `eco00650` Butanoate metabolism (KEGG)

## Annotation

KEGG compound: Diacetyl; Biacetyl; Dimethylglyoxal; 2,3-Butanedione

## Pathways

- `eco00650` Butanoate metabolism (KEGG)

## Outgoing Edges (6)

- `activates` --> [[reaction.ecocyc.RXN-11496|reaction.ecocyc.RXN-11496]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.ecocyc.RXN-11032|reaction.ecocyc.RXN-11032]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-6081|reaction.ecocyc.RXN-6081]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `represses` --> [[reaction.ecocyc.AKBLIG-RXN|reaction.ecocyc.AKBLIG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-1381|reaction.ecocyc.RXN-1381]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-14249|reaction.ecocyc.RXN-14249]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00741`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
