---
entity_id: "reaction.ecocyc.GCVT-RXN"
entity_type: "reaction"
name: "GCVT-RXN"
source_database: "EcoCyc"
source_id: "GCVT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Tetrahydrofolate aminomethyltransferase"
  - "Glycine-cleavage system T-protein"
---

# GCVT-RXN

`reaction.ecocyc.GCVT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GCVT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

One of three reactions of the glycine cleavage system. The aminomethyl group is split to ammonia and a C1 unit is transferred to the tetrahydrofolate cofactor. EcoCyc reaction equation: AMINOMETHYLDIHYDROLIPOYL-GCVH + THF-GLU-N -> DIHYDROLIPOYL-GCVH + METHYLENE-THF-GLU-N + AMMONIUM; direction=REVERSIBLE. One of three reactions of the glycine cleavage system. The aminomethyl group is split to ammonia and a C1 unit is transferred to the tetrahydrofolate cofactor.

## Biological Role

Catalyzed by gcvT (protein.P27248). Substrates: THF-polyglutamate (molecule.C03541), a [glycine-cleavage complex H protein] N6-aminomethyldihydrolipoyl-L-lysine (molecule.ecocyc.AMINOMETHYLDIHYDROLIPOYL-GCVH). Products: ammonium (molecule.ecocyc.AMMONIUM), a [glycine-cleavage complex H protein] N6-dihydrolipoyl-L-lysine (molecule.ecocyc.DIHYDROLIPOYL-GCVH), a 5,10-methylenetetrahydrofolate (molecule.ecocyc.METHYLENE-THF-GLU-N).

## Enriched Pathways

- `ecocyc.GLYCLEAV-PWY` glycine cleavage (EcoCyc)

## Annotation

One of three reactions of the glycine cleavage system. The aminomethyl group is split to ammonia and a C1 unit is transferred to the tetrahydrofolate cofactor.

## Pathways

- `ecocyc.GLYCLEAV-PWY` glycine cleavage (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P27248|protein.P27248]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.DIHYDROLIPOYL-GCVH|molecule.ecocyc.DIHYDROLIPOYL-GCVH]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.METHYLENE-THF-GLU-N|molecule.ecocyc.METHYLENE-THF-GLU-N]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C03541|molecule.C03541]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.AMINOMETHYLDIHYDROLIPOYL-GCVH|molecule.ecocyc.AMINOMETHYLDIHYDROLIPOYL-GCVH]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GCVT-RXN`

## Notes

AMINOMETHYLDIHYDROLIPOYL-GCVH + THF-GLU-N -> DIHYDROLIPOYL-GCVH + METHYLENE-THF-GLU-N + AMMONIUM; direction=REVERSIBLE
