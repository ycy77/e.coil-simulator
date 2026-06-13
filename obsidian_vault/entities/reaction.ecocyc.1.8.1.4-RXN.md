---
entity_id: "reaction.ecocyc.1.8.1.4-RXN"
entity_type: "reaction"
name: "1.8.1.4-RXN"
source_database: "EcoCyc"
source_id: "1.8.1.4-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 1.8.1.4-RXN

`reaction.ecocyc.1.8.1.4-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:1.8.1.4-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Dihydro-Lipoyl-Proteins + NAD -> Lipoyl-Protein-N6-lipoyllysine + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Dihydro-Lipoyl-Proteins + NAD -> Lipoyl-Protein-N6-lipoyllysine + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lipoamide dehydrogenase (complex.ecocyc.E3-CPLX). Substrates: NAD+ (molecule.C00003), a [lipoyl-carrier protein]-N6-[(R)-dihydrolipoyl]-L-lysine (molecule.ecocyc.Dihydro-Lipoyl-Proteins). Products: NADH (molecule.C00004), H+ (molecule.C00080), a [lipoyl-carrier protein]-N6-[(R)-lipoyl]-L-lysine (molecule.ecocyc.Lipoyl-Protein-N6-lipoyllysine).

## Annotation

Dihydro-Lipoyl-Proteins + NAD -> Lipoyl-Protein-N6-lipoyllysine + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.E3-CPLX|complex.ecocyc.E3-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Lipoyl-Protein-N6-lipoyllysine|molecule.ecocyc.Lipoyl-Protein-N6-lipoyllysine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Dihydro-Lipoyl-Proteins|molecule.ecocyc.Dihydro-Lipoyl-Proteins]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:1.8.1.4-RXN`

## Notes

Dihydro-Lipoyl-Proteins + NAD -> Lipoyl-Protein-N6-lipoyllysine + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
