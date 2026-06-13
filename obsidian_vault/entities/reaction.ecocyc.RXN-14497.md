---
entity_id: "reaction.ecocyc.RXN-14497"
entity_type: "reaction"
name: "RXN-14497"
source_database: "EcoCyc"
source_id: "RXN-14497"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14497

`reaction.ecocyc.RXN-14497`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14497`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

In E. coli K-12 the major route for cystine metabolism involves reductive cleavage of the cystine disulfide bond to form cysteine. The reducing environment of the cytoplasm is maintained by thioredoxins (RED-THIOREDOXIN-MONOMER "thioredoxin 1", RED-THIOREDOXIN2-MONOMER "thioredoxin 2") and glutaredoxins (RED-GLUTAREDOXIN "glutaredoxin 1", GRXB-MONOMER "glutaredoxin 2" and GRXC-MONOMER "glutaredoxin 3"). Glutathione-dependent reduction of imported cystine is an enzyme-catalyzed process; a single route of cystine reduction has not been identified but glutaredoxins 2 and 3 are implicated in the process . Reviews: EcoCyc reaction equation: CPD0-1564 + GLUTATHIONE -> OXIDIZED-GLUTATHIONE + D-CYSTEINE; direction=PHYSIOL-LEFT-TO-RIGHT. In E. coli K-12 the major route for cystine metabolism involves reductive cleavage of the cystine disulfide bond to form cysteine. The reducing environment of the cytoplasm is maintained by thioredoxins (RED-THIOREDOXIN-MONOMER "thioredoxin 1", RED-THIOREDOXIN2-MONOMER "thioredoxin 2") and glutaredoxins (RED-GLUTAREDOXIN "glutaredoxin 1", GRXB-MONOMER "glutaredoxin 2" and GRXC-MONOMER "glutaredoxin 3"). Glutathione-dependent reduction of imported cystine is an enzyme-catalyzed process; a single route of cystine reduction has not been identified but glutaredoxins 2 and 3 are implicated in the process . Reviews:

## Biological Role

Substrates: Glutathione (molecule.C00051), D-cystine (molecule.ecocyc.CPD0-1564). Products: Glutathione disulfide (molecule.C00127), D-Cysteine (molecule.C00793).

## Annotation

In E. coli K-12 the major route for cystine metabolism involves reductive cleavage of the cystine disulfide bond to form cysteine. The reducing environment of the cytoplasm is maintained by thioredoxins (RED-THIOREDOXIN-MONOMER "thioredoxin 1", RED-THIOREDOXIN2-MONOMER "thioredoxin 2") and glutaredoxins (RED-GLUTAREDOXIN "glutaredoxin 1", GRXB-MONOMER "glutaredoxin 2" and GRXC-MONOMER "glutaredoxin 3"). Glutathione-dependent reduction of imported cystine is an enzyme-catalyzed process; a single route of cystine reduction has not been identified but glutaredoxins 2 and 3 are implicated in the process . Reviews:

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00127|molecule.C00127]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00793|molecule.C00793]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1564|molecule.ecocyc.CPD0-1564]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14497`

## Notes

CPD0-1564 + GLUTATHIONE -> OXIDIZED-GLUTATHIONE + D-CYSTEINE; direction=PHYSIOL-LEFT-TO-RIGHT
