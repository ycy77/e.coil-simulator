---
entity_id: "reaction.ecocyc.RXN0-2301"
entity_type: "reaction"
name: "RXN0-2301"
source_database: "EcoCyc"
source_id: "RXN0-2301"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2301

`reaction.ecocyc.RXN0-2301`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2301`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ISOVALERYL-COA + ETF-Oxidized + PROTON -> 3-METHYL-CROTONYL-COA + ETF-Reduced; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ISOVALERYL-COA + ETF-Oxidized + PROTON -> 3-METHYL-CROTONYL-COA + ETF-Reduced; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by isovaleryl-CoA dehydrogenase and DNA-binding transcriptional repressor (complex.ecocyc.CPLX0-7691). Substrates: H+ (molecule.C00080), 3-Methylbutanoyl-CoA (molecule.C02939). Products: 3-Methylcrotonyl-CoA (molecule.C03069).

## Annotation

ISOVALERYL-COA + ETF-Oxidized + PROTON -> 3-METHYL-CROTONYL-COA + ETF-Reduced; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7691|complex.ecocyc.CPLX0-7691]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C03069|molecule.C03069]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C02939|molecule.C02939]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-2301`

## Notes

ISOVALERYL-COA + ETF-Oxidized + PROTON -> 3-METHYL-CROTONYL-COA + ETF-Reduced; direction=PHYSIOL-LEFT-TO-RIGHT
