---
entity_id: "reaction.ecocyc.NMNAMIDOHYDRO-RXN"
entity_type: "reaction"
name: "NMNAMIDOHYDRO-RXN"
source_database: "EcoCyc"
source_id: "NMNAMIDOHYDRO-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# NMNAMIDOHYDRO-RXN

`reaction.ecocyc.NMNAMIDOHYDRO-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:NMNAMIDOHYDRO-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of NAD cycling. EcoCyc reaction equation: NICOTINAMIDE_NUCLEOTIDE + WATER -> AMMONIUM + NICOTINATE_NUCLEOTIDE; direction=LEFT-TO-RIGHT. This reaction is part of NAD cycling.

## Biological Role

Catalyzed by NMN amidohydrolase (complex.ecocyc.CPLXECOLI-7943). Substrates: H2O (molecule.C00001), Nicotinamide D-ribonucleotide (molecule.C00455). Products: Nicotinate D-ribonucleotide (molecule.C01185), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.PWY-7761` NAD salvage pathway II (PNC IV cycle) (EcoCyc)

## Annotation

This reaction is part of NAD cycling.

## Pathways

- `ecocyc.PWY-7761` NAD salvage pathway II (PNC IV cycle) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLXECOLI-7943|complex.ecocyc.CPLXECOLI-7943]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01185|molecule.C01185]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00455|molecule.C00455]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:NMNAMIDOHYDRO-RXN`

## Notes

NICOTINAMIDE_NUCLEOTIDE + WATER -> AMMONIUM + NICOTINATE_NUCLEOTIDE; direction=LEFT-TO-RIGHT
