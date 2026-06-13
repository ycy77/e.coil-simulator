---
entity_id: "molecule.C00109"
entity_type: "small_molecule"
name: "2-Oxobutanoate"
source_database: "KEGG"
source_id: "C00109"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2-Oxobutanoate"
  - "2-Ketobutyric acid"
  - "2-Oxobutyric acid"
  - "2-Oxobutyrate"
  - "2-Oxobutanoic acid"
  - "alpha-Ketobutyric acid"
  - "alpha-Ketobutyrate"
---

# 2-Oxobutanoate

`molecule.C00109`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00109`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2-Oxobutanoate; 2-Ketobutyric acid; 2-Oxobutyric acid; 2-Oxobutyrate; 2-Oxobutanoic acid; alpha-Ketobutyric acid; alpha-Ketobutyrate

## Biological Role

Consumed as substrate in 7 reaction(s). Produced in 8 reaction(s).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)

## Annotation

KEGG compound: 2-Oxobutanoate; 2-Ketobutyric acid; 2-Oxobutyric acid; 2-Oxobutyrate; 2-Oxobutanoic acid; alpha-Ketobutyric acid; alpha-Ketobutyrate

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)

## Outgoing Edges (19)

- `activates` --> [[reaction.ecocyc.DLACTDEHYDROGNAD-RXN|reaction.ecocyc.DLACTDEHYDROGNAD-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.R00996|reaction.R00996]] `KEGG` `database` - C00188 <=> C00109 + C00014
- `is_product_of` --> [[reaction.R00999|reaction.R00999]] `KEGG` `database` - C01118 + C00001 <=> C00109 + C00042 + C00014
- `is_product_of` --> [[reaction.ecocyc.KETOBUTFORMLY-RXN|reaction.ecocyc.KETOBUTFORMLY-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.METBALT-RXN|reaction.ecocyc.METBALT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-15123|reaction.ecocyc.RXN-15123]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7227|reaction.ecocyc.RXN0-7227]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.THREDEHYD-RXN|reaction.ecocyc.THREDEHYD-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-558|reaction.ecocyc.TRANS-RXN0-558]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00994|reaction.R00994]] `KEGG` `database` - C00109 + C00011 + C00004 + C00080 <=> C06032 + C00003
- `is_substrate_of` --> [[reaction.R04673|reaction.R04673]] `KEGG` `database` - C00109 + C05125 <=> C06006 + C00068
- `is_substrate_of` --> [[reaction.R06987|reaction.R06987]] `KEGG` `database` - C00109 + C00010 <=> C00100 + C00058
- `is_substrate_of` --> [[reaction.ecocyc.ACETOOHBUTSYN-RXN|reaction.ecocyc.ACETOOHBUTSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17751|reaction.ecocyc.RXN-17751]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5200|reaction.ecocyc.RXN0-5200]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-558|reaction.ecocyc.TRANS-RXN0-558]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ACETOLACTSYN-RXN|reaction.ecocyc.ACETOLACTSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PYRUVDEH-RXN|reaction.ecocyc.PYRUVDEH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.THREDEHYD-RXN|reaction.ecocyc.THREDEHYD-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00109`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
