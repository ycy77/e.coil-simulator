---
entity_id: "reaction.ecocyc.CITLY-RXN"
entity_type: "reaction"
name: "CITLY-RXN"
source_database: "EcoCyc"
source_id: "CITLY-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CITLY-RXN

`reaction.ecocyc.CITLY-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CITLY-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This overall reaction is carried out by the citrate lyase multienzyme complex. The reaction proceeds in two steps, each one catalyzed by a separate subunit of the enzyme complex. EcoCyc reaction equation: CIT -> ACET + OXALACETIC_ACID; direction=PHYSIOL-LEFT-TO-RIGHT. This overall reaction is carried out by the citrate lyase multienzyme complex. The reaction proceeds in two steps, each one catalyzed by a separate subunit of the enzyme complex.

## Biological Role

Catalyzed by citrate lyase (complex.ecocyc.ACECITLY-CPLX). Substrates: Citrate (molecule.C00158). Products: Acetate (molecule.C00033), Oxaloacetate (molecule.C00036).

## Annotation

This overall reaction is carried out by the citrate lyase multienzyme complex. The reaction proceeds in two steps, each one catalyzed by a separate subunit of the enzyme complex.

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.ACECITLY-CPLX|complex.ecocyc.ACECITLY-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00036|molecule.C00036]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00158|molecule.C00158]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00036|molecule.C00036]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C18237|molecule.C18237]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:CITLY-RXN`

## Notes

CIT -> ACET + OXALACETIC_ACID; direction=PHYSIOL-LEFT-TO-RIGHT
