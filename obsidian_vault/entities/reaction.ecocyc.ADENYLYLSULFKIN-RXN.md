---
entity_id: "reaction.ecocyc.ADENYLYLSULFKIN-RXN"
entity_type: "reaction"
name: "ADENYLYLSULFKIN-RXN"
source_database: "EcoCyc"
source_id: "ADENYLYLSULFKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ADENYLYLSULFKIN-RXN

`reaction.ecocyc.ADENYLYLSULFKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ADENYLYLSULFKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second step in the activation of sulfate. The reaction occurs early in the sulfide branch of the cysteine synthesis pathway. EcoCyc reaction equation: APS + ATP -> PROTON + PAPS + ADP; direction=PHYSIOL-LEFT-TO-RIGHT. This is the second step in the activation of sulfate. The reaction occurs early in the sulfide branch of the cysteine synthesis pathway.

## Biological Role

Catalyzed by adenylyl-sulfate kinase (complex.ecocyc.ADENYLYLSULFKIN-CPLX). Substrates: ATP (molecule.C00002), Adenylyl sulfate (molecule.C00224). Products: ADP (molecule.C00008), 3'-Phosphoadenylyl sulfate (molecule.C00053), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.PWY-5340` sulfate activation for sulfonation (EcoCyc)

## Annotation

This is the second step in the activation of sulfate. The reaction occurs early in the sulfide branch of the cysteine synthesis pathway.

## Pathways

- `ecocyc.PWY-5340` sulfate activation for sulfonation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.ADENYLYLSULFKIN-CPLX|complex.ecocyc.ADENYLYLSULFKIN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00053|molecule.C00053]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00224|molecule.C00224]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00053|molecule.C00053]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00224|molecule.C00224]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1651|molecule.ecocyc.CPD0-1651]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ADENYLYLSULFKIN-RXN`

## Notes

APS + ATP -> PROTON + PAPS + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
