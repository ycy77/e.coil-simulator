---
entity_id: "reaction.ecocyc.GALACTURIDYLYLTRANS-RXN"
entity_type: "reaction"
name: "GALACTURIDYLYLTRANS-RXN"
source_database: "EcoCyc"
source_id: "GALACTURIDYLYLTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GALACTURIDYLYLTRANS-RXN

`reaction.ecocyc.GALACTURIDYLYLTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GALACTURIDYLYLTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Part of galactose, galactoside and glucose metabolism. EcoCyc reaction equation: CPD-12575 + GALACTOSE-1P -> CPD-14553 + GLC-1-P; direction=REVERSIBLE. Part of galactose, galactoside and glucose metabolism.

## Biological Role

Catalyzed by galactose-1-phosphate uridylyltransferase (complex.ecocyc.GALACTURIDYLYLTRANS-CPLX). Substrates: UDP-glucose (molecule.C00029), alpha-D-Galactose 1-phosphate (molecule.C00446). Products: UDP-alpha-D-galactose (molecule.C00052), α-D-glucopyranose 1-phosphate (molecule.ecocyc.GLC-1-P).

## Enriched Pathways

- `ecocyc.PWY-6317` D-galactose degradation I (Leloir pathway) (EcoCyc)

## Annotation

Part of galactose, galactoside and glucose metabolism.

## Pathways

- `ecocyc.PWY-6317` D-galactose degradation I (Leloir pathway) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.GALACTURIDYLYLTRANS-CPLX|complex.ecocyc.GALACTURIDYLYLTRANS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00052|molecule.C00052]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.GLC-1-P|molecule.ecocyc.GLC-1-P]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00029|molecule.C00029]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00446|molecule.C00446]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GALACTURIDYLYLTRANS-RXN`

## Notes

CPD-12575 + GALACTOSE-1P -> CPD-14553 + GLC-1-P; direction=REVERSIBLE
