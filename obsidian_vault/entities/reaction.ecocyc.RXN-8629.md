---
entity_id: "reaction.ecocyc.RXN-8629"
entity_type: "reaction"
name: "RXN-8629"
source_database: "EcoCyc"
source_id: "RXN-8629"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-8629

`reaction.ecocyc.RXN-8629`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-8629`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DIHYDROLIPOYL-GCVH + NAD -> PROTEIN-LIPOYLLYSINE + NADH + PROTON; direction=REVERSIBLE EcoCyc reaction equation: DIHYDROLIPOYL-GCVH + NAD -> PROTEIN-LIPOYLLYSINE + NADH + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by lipoamide dehydrogenase (complex.ecocyc.E3-CPLX). Substrates: NAD+ (molecule.C00003), a [glycine-cleavage complex H protein] N6-dihydrolipoyl-L-lysine (molecule.ecocyc.DIHYDROLIPOYL-GCVH). Products: NADH (molecule.C00004), H+ (molecule.C00080), a [glycine-cleavage complex H protein] N6-[(R)-lipoyl]-L-lysine (molecule.ecocyc.PROTEIN-LIPOYLLYSINE).

## Enriched Pathways

- `ecocyc.GLYCLEAV-PWY` glycine cleavage (EcoCyc)

## Annotation

DIHYDROLIPOYL-GCVH + NAD -> PROTEIN-LIPOYLLYSINE + NADH + PROTON; direction=REVERSIBLE

## Pathways

- `ecocyc.GLYCLEAV-PWY` glycine cleavage (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.E3-CPLX|complex.ecocyc.E3-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.PROTEIN-LIPOYLLYSINE|molecule.ecocyc.PROTEIN-LIPOYLLYSINE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.DIHYDROLIPOYL-GCVH|molecule.ecocyc.DIHYDROLIPOYL-GCVH]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-8629`

## Notes

DIHYDROLIPOYL-GCVH + NAD -> PROTEIN-LIPOYLLYSINE + NADH + PROTON; direction=REVERSIBLE
