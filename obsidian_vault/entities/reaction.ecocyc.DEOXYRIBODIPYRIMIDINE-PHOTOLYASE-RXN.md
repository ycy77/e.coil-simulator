---
entity_id: "reaction.ecocyc.DEOXYRIBODIPYRIMIDINE-PHOTOLYASE-RXN"
entity_type: "reaction"
name: "DEOXYRIBODIPYRIMIDINE-PHOTOLYASE-RXN"
source_database: "EcoCyc"
source_id: "DEOXYRIBODIPYRIMIDINE-PHOTOLYASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "DNA PHOTOLYASE"
  - "PHOTOREACTIVATING ENZYME"
---

# DEOXYRIBODIPYRIMIDINE-PHOTOLYASE-RXN

`reaction.ecocyc.DEOXYRIBODIPYRIMIDINE-PHOTOLYASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DEOXYRIBODIPYRIMIDINE-PHOTOLYASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

A SIMILAR REACTIVATION OF IRRADIATED RNA IS PROBABLY DUE TO A SEPARATE ENZYME. EcoCyc reaction equation: DNA-deoxycytidine-thymidine-dimer + Light -> DNA-Cytidines + DNA-thymidines; direction=PHYSIOL-LEFT-TO-RIGHT. A SIMILAR REACTIVATION OF IRRADIATED RNA IS PROBABLY DUE TO A SEPARATE ENZYME.

## Biological Role

Substrates: hν (molecule.ecocyc.Light). Products: a 2'-deoxycytidine in DNA (molecule.ecocyc.DNA-Cytidines), a thymidine in DNA (molecule.ecocyc.DNA-thymidines).

## Annotation

A SIMILAR REACTIVATION OF IRRADIATED RNA IS PROBABLY DUE TO A SEPARATE ENZYME.

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.ecocyc.DNA-Cytidines|molecule.ecocyc.DNA-Cytidines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.DNA-thymidines|molecule.ecocyc.DNA-thymidines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DEOXYRIBODIPYRIMIDINE-PHOTOLYASE-RXN`

## Notes

DNA-deoxycytidine-thymidine-dimer + Light -> DNA-Cytidines + DNA-thymidines; direction=PHYSIOL-LEFT-TO-RIGHT
