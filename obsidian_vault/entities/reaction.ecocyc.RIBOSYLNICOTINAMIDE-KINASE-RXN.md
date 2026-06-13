---
entity_id: "reaction.ecocyc.RIBOSYLNICOTINAMIDE-KINASE-RXN"
entity_type: "reaction"
name: "RIBOSYLNICOTINAMIDE-KINASE-RXN"
source_database: "EcoCyc"
source_id: "RIBOSYLNICOTINAMIDE-KINASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RIBOSYLNICOTINAMIDE-KINASE-RXN

`reaction.ecocyc.RIBOSYLNICOTINAMIDE-KINASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:RIBOSYLNICOTINAMIDE-KINASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NICOTINAMIDE_RIBOSE + ATP -> PROTON + NICOTINAMIDE_NUCLEOTIDE + ADP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: NICOTINAMIDE_RIBOSE + ATP -> PROTON + NICOTINAMIDE_NUCLEOTIDE + ADP; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by DNA-binding transcriptional repressor/NMN adenylyltransferase NadR (complex.ecocyc.CPLX0-7975). Substrates: ATP (molecule.C00002), Nicotinamide-beta-riboside (molecule.C03150). Products: ADP (molecule.C00008), H+ (molecule.C00080), Nicotinamide D-ribonucleotide (molecule.C00455).

## Enriched Pathways

- `ecocyc.PWY3O-4106` NAD salvage pathway IV (from nicotinamide riboside) (EcoCyc)

## Annotation

NICOTINAMIDE_RIBOSE + ATP -> PROTON + NICOTINAMIDE_NUCLEOTIDE + ADP; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY3O-4106` NAD salvage pathway IV (from nicotinamide riboside) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7975|complex.ecocyc.CPLX0-7975]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00455|molecule.C00455]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03150|molecule.C03150]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RIBOSYLNICOTINAMIDE-KINASE-RXN`

## Notes

NICOTINAMIDE_RIBOSE + ATP -> PROTON + NICOTINAMIDE_NUCLEOTIDE + ADP; direction=LEFT-TO-RIGHT
