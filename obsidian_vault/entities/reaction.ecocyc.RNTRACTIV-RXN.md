---
entity_id: "reaction.ecocyc.RNTRACTIV-RXN"
entity_type: "reaction"
name: "anaerobic ribonucleoside-triphosphate reductase activating enzyme"
source_database: "EcoCyc"
source_id: "RNTRACTIV-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# anaerobic ribonucleoside-triphosphate reductase activating enzyme

`reaction.ecocyc.RNTRACTIV-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:RNTRACTIV-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

A part of the process of activation of ribonucleoside triphosphate reductase enzyme by generation of glycyl radical. EcoCyc reaction equation: S-ADENOSYLMETHIONINE + Ribonuc-tri-P-reductases-inactive + Reduced-flavodoxins -> Ribonuc-tri-P-reductases-active + CH33ADO + MET + Flavodoxins-Semiquinones + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. A part of the process of activation of ribonucleoside triphosphate reductase enzyme by generation of glycyl radical.

## Biological Role

Catalyzed by anaerobic ribonucleoside-triphosphate reductase activating protein (complex.ecocyc.CPLX0-229). Substrates: S-Adenosyl-L-methionine (molecule.C00019). Products: L-Methionine (molecule.C00073), H+ (molecule.C00080), 5'-deoxyadenosine (molecule.ecocyc.CH33ADO).

## Annotation

A part of the process of activation of ribonucleoside triphosphate reductase enzyme by generation of glycyl radical.

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-229|complex.ecocyc.CPLX0-229]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CH33ADO|molecule.ecocyc.CH33ADO]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RNTRACTIV-RXN`

## Notes

S-ADENOSYLMETHIONINE + Ribonuc-tri-P-reductases-inactive + Reduced-flavodoxins -> Ribonuc-tri-P-reductases-active + CH33ADO + MET + Flavodoxins-Semiquinones + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
