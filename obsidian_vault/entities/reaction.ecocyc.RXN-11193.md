---
entity_id: "reaction.ecocyc.RXN-11193"
entity_type: "reaction"
name: "RXN-11193"
source_database: "EcoCyc"
source_id: "RXN-11193"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11193

`reaction.ecocyc.RXN-11193`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11193`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

WATER + D-Amino-Acids + ETR-Quinones -> AMMONIUM + 2-Oxo-carboxylates + ETR-Quinols; direction=LEFT-TO-RIGHT EcoCyc reaction equation: WATER + D-Amino-Acids + ETR-Quinones -> AMMONIUM + 2-Oxo-carboxylates + ETR-Quinols; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by D-amino acid dehydrogenase (complex.ecocyc.DALADEHYDROG-CPLX). Substrates: H2O (molecule.C00001), a D-amino acid (molecule.ecocyc.D-Amino-Acids). Products: a 2-oxo carboxylate (molecule.ecocyc.2-Oxo-carboxylates), ammonium (molecule.ecocyc.AMMONIUM).

## Annotation

WATER + D-Amino-Acids + ETR-Quinones -> AMMONIUM + 2-Oxo-carboxylates + ETR-Quinols; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.DALADEHYDROG-CPLX|complex.ecocyc.DALADEHYDROG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.2-Oxo-carboxylates|molecule.ecocyc.2-Oxo-carboxylates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.D-Amino-Acids|molecule.ecocyc.D-Amino-Acids]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11193`

## Notes

WATER + D-Amino-Acids + ETR-Quinones -> AMMONIUM + 2-Oxo-carboxylates + ETR-Quinols; direction=LEFT-TO-RIGHT
