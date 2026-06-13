---
entity_id: "molecule.C02426"
entity_type: "small_molecule"
name: "L-Glyceraldehyde"
source_database: "KEGG"
source_id: "C02426"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Glyceraldehyde"
  - "L-2,3-Dihydroxypropionaldehyde"
  - "L-2,3-Dihydroxypropanal"
  - "L-Glycerose"
  - "L-Aldotriose"
---

# L-Glyceraldehyde

`molecule.C02426`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02426`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Glyceraldehyde; L-2,3-Dihydroxypropionaldehyde; L-2,3-Dihydroxypropanal; L-Glycerose; L-Aldotriose

## Biological Role

Produced in 1 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)

## Annotation

KEGG compound: L-Glyceraldehyde; L-2,3-Dihydroxypropionaldehyde; L-2,3-Dihydroxypropanal; L-Glycerose; L-Aldotriose

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.RXN0-7251|reaction.ecocyc.RXN0-7251]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `represses` --> [[reaction.ecocyc.TRANSALDOL-RXN|reaction.ecocyc.TRANSALDOL-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C02426`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
