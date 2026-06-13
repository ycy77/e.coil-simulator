---
entity_id: "reaction.ecocyc.1.8.4.4-RXN"
entity_type: "reaction"
name: "1.8.4.4-RXN"
source_database: "EcoCyc"
source_id: "1.8.4.4-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 1.8.4.4-RXN

`reaction.ecocyc.1.8.4.4-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:1.8.4.4-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

In E. coli K-12 the major route for cystine metabolism involves reductive cleavage of the cystine disulfide bond to form cysteine. The reducing environment of the cytoplasm is maintained by thioredoxins (RED-THIOREDOXIN-MONOMER "thioredoxin 1", RED-THIOREDOXIN2-MONOMER "thioredoxin 2") and glutaredoxins (RED-GLUTAREDOXIN "glutaredoxin 1", GRXB-MONOMER "glutaredoxin 2" and GRXC-MONOMER "glutaredoxin 3"). Glutathione-dependent reduction of imported cystine is an enzyme-catalyzed process; a single route of cystine reduction has not been identified but glutaredoxins 2 and 3 are implicated in the process (see also ). Reviews: EcoCyc reaction equation: L-CYSTINE + GLUTATHIONE -> OXIDIZED-GLUTATHIONE + CYS; direction=PHYSIOL-LEFT-TO-RIGHT. In E. coli K-12 the major route for cystine metabolism involves reductive cleavage of the cystine disulfide bond to form cysteine. The reducing environment of the cytoplasm is maintained by thioredoxins (RED-THIOREDOXIN-MONOMER "thioredoxin 1", RED-THIOREDOXIN2-MONOMER "thioredoxin 2") and glutaredoxins (RED-GLUTAREDOXIN "glutaredoxin 1", GRXB-MONOMER "glutaredoxin 2" and GRXC-MONOMER "glutaredoxin 3"). Glutathione-dependent reduction of imported cystine is an enzyme-catalyzed process; a single route of cystine reduction has not been identified but glutaredoxins 2 and 3 are implicated in the process (see also ). Reviews:

## Biological Role

Substrates: Glutathione (molecule.C00051), L-Cystine (molecule.C00491). Products: L-Cysteine (molecule.C00097), Glutathione disulfide (molecule.C00127).

## Annotation

In E. coli K-12 the major route for cystine metabolism involves reductive cleavage of the cystine disulfide bond to form cysteine. The reducing environment of the cytoplasm is maintained by thioredoxins (RED-THIOREDOXIN-MONOMER "thioredoxin 1", RED-THIOREDOXIN2-MONOMER "thioredoxin 2") and glutaredoxins (RED-GLUTAREDOXIN "glutaredoxin 1", GRXB-MONOMER "glutaredoxin 2" and GRXC-MONOMER "glutaredoxin 3"). Glutathione-dependent reduction of imported cystine is an enzyme-catalyzed process; a single route of cystine reduction has not been identified but glutaredoxins 2 and 3 are implicated in the process (see also ). Reviews:

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00127|molecule.C00127]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00491|molecule.C00491]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:1.8.4.4-RXN`

## Notes

L-CYSTINE + GLUTATHIONE -> OXIDIZED-GLUTATHIONE + CYS; direction=PHYSIOL-LEFT-TO-RIGHT
