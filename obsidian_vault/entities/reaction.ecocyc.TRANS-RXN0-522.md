---
entity_id: "reaction.ecocyc.TRANS-RXN0-522"
entity_type: "reaction"
name: "TRANS-RXN0-522"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-522"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-522

`reaction.ecocyc.TRANS-RXN0-522`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-522`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

This transport reaction was added because results from Biolog experiments suggest that E.coli K-12 can use D-galactono-1,4-lactone as a sole carbon source. Additionally there is evidence for a GLUCONOLACT-MONOMER "galactono-γ-lactonase activity" in E.coli K-12 although the enzyme responsible has not been identified and it is not clear whether this activity resides in the periplasm or the cytoplasm. If the lactonase activity resides in the periplasm the D-galactonate produced by its activity would be transported across the inner membrane by the YIDT-MONOMER "D-galactonate permease" and enter into the pathway of GALACTCAT-PWY "galactonate degradation". However, if the activity resides in the cytoplasm, D-galactono-1,4-lactone would need to be transported across the inner membrane and this is the reaction shown here. An enzyme responsible for transport has not been identified. EcoCyc reaction equation: D-GALACTONO-1-4-LACTONE -> D-GALACTONO-1-4-LACTONE; direction=LEFT-TO-RIGHT. This transport reaction was added because results from Biolog experiments suggest that E.coli K-12 can use D-galactono-1,4-lactone as a sole carbon source. Additionally there is evidence for a GLUCONOLACT-MONOMER "galactono-γ-lactonase activity" in E.coli K-12 although the enzyme responsible has not been identified and it is not clear whether this activity resides in the periplasm or the cytoplasm...

## Biological Role

Substrates: D-Galactono-1,4-lactone (molecule.C03383). Products: D-Galactono-1,4-lactone (molecule.C03383).

## Annotation

This transport reaction was added because results from Biolog experiments suggest that E.coli K-12 can use D-galactono-1,4-lactone as a sole carbon source. Additionally there is evidence for a GLUCONOLACT-MONOMER "galactono-γ-lactonase activity" in E.coli K-12 although the enzyme responsible has not been identified and it is not clear whether this activity resides in the periplasm or the cytoplasm. If the lactonase activity resides in the periplasm the D-galactonate produced by its activity would be transported across the inner membrane by the YIDT-MONOMER "D-galactonate permease" and enter into the pathway of GALACTCAT-PWY "galactonate degradation". However, if the activity resides in the cytoplasm, D-galactono-1,4-lactone would need to be transported across the inner membrane and this is the reaction shown here. An enzyme responsible for transport has not been identified.

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C03383|molecule.C03383]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C03383|molecule.C03383]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-522`

## Notes

D-GALACTONO-1-4-LACTONE -> D-GALACTONO-1-4-LACTONE; direction=LEFT-TO-RIGHT
