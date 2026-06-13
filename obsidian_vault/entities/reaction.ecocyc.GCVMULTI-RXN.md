---
entity_id: "reaction.ecocyc.GCVMULTI-RXN"
entity_type: "reaction"
name: "GCVMULTI-RXN"
source_database: "EcoCyc"
source_id: "GCVMULTI-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GCVMULTI-RXN

`reaction.ecocyc.GCVMULTI-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GCVMULTI-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Degradation of glycine to ammonia, CO2 and a C1 unit. EcoCyc reaction equation: GLY + THF-GLU-N + NAD -> METHYLENE-THF-GLU-N + AMMONIUM + CARBON-DIOXIDE + NADH; direction=LEFT-TO-RIGHT. Degradation of glycine to ammonia, CO2 and a C1 unit.

## Biological Role

Catalyzed by glycine cleavage system (complex.ecocyc.GCVMULTI-CPLX). Substrates: NAD+ (molecule.C00003), Glycine (molecule.C00037), THF-polyglutamate (molecule.C03541). Products: NADH (molecule.C00004), CO2 (molecule.C00011), ammonium (molecule.ecocyc.AMMONIUM), a 5,10-methylenetetrahydrofolate (molecule.ecocyc.METHYLENE-THF-GLU-N).

## Enriched Pathways

- `ecocyc.1CMET2-PWY` folate transformations III (E. coli) (EcoCyc)
- `ecocyc.PWY0-1608` glycine degradation (EcoCyc)

## Annotation

Degradation of glycine to ammonia, CO2 and a C1 unit.

## Pathways

- `ecocyc.1CMET2-PWY` folate transformations III (E. coli) (EcoCyc)
- `ecocyc.PWY0-1608` glycine degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.GCVMULTI-CPLX|complex.ecocyc.GCVMULTI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.METHYLENE-THF-GLU-N|molecule.ecocyc.METHYLENE-THF-GLU-N]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03541|molecule.C03541]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GCVMULTI-RXN`

## Notes

GLY + THF-GLU-N + NAD -> METHYLENE-THF-GLU-N + AMMONIUM + CARBON-DIOXIDE + NADH; direction=LEFT-TO-RIGHT
