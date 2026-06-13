---
entity_id: "molecule.C00558"
entity_type: "small_molecule"
name: "D-Tagaturonate"
source_database: "KEGG"
source_id: "C00558"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Tagaturonate"
  - "D-Tagaturonic acid"
---

# D-Tagaturonate

`molecule.C00558`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00558`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Tagaturonate; D-Tagaturonic acid

## Biological Role

Produced in 4 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00562` Inositol phosphate metabolism (KEGG)

## Annotation

KEGG compound: D-Tagaturonate; D-Tagaturonic acid

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00562` Inositol phosphate metabolism (KEGG)

## Outgoing Edges (5)

- `activates` --> [[reaction.ecocyc.MANNONDEHYDRAT-RXN|reaction.ecocyc.MANNONDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.R12146|reaction.R12146]] `KEGG` `database` - C15930 + C00003 <=> C00558 + C00004 + C00080
- `is_product_of` --> [[reaction.ecocyc.ALTRO-OXIDOREDUCT-RXN|reaction.ecocyc.ALTRO-OXIDOREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GALACTUROISOM-RXN|reaction.ecocyc.GALACTUROISOM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5229|reaction.ecocyc.RXN0-5229]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00558`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
