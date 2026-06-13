---
entity_id: "reaction.ecocyc.NAD-SYNTH-NH3-RXN"
entity_type: "reaction"
name: "NAD-SYNTH-NH3-RXN"
source_database: "EcoCyc"
source_id: "NAD-SYNTH-NH3-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "NAD(+) SYNTHETASE"
---

# NAD-SYNTH-NH3-RXN

`reaction.ecocyc.NAD-SYNTH-NH3-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:NAD-SYNTH-NH3-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

A reaction in the biosynthesis of NAD. Glutamine can also serve as an amido group donor. EcoCyc reaction equation: AMMONIUM + ATP + DEAMIDO-NAD -> PROTON + AMP + PPI + NAD; direction=PHYSIOL-LEFT-TO-RIGHT. A reaction in the biosynthesis of NAD. Glutamine can also serve as an amido group donor.

## Biological Role

Catalyzed by NH3-dependent NAD+ synthetase (complex.ecocyc.NAD-SYNTH-CPLX). Substrates: ATP (molecule.C00002), Deamino-NAD+ (molecule.C00857), ammonium (molecule.ecocyc.AMMONIUM). Products: NAD+ (molecule.C00003), Diphosphate (molecule.C00013), AMP (molecule.C00020), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.PWY-7761` NAD salvage pathway II (PNC IV cycle) (EcoCyc)
- `ecocyc.PYRIDNUCSAL-PWY` NAD salvage pathway I (PNC VI cycle) (EcoCyc)
- `ecocyc.PYRIDNUCSYN-PWY` NAD de novo biosynthesis I (EcoCyc)

## Annotation

A reaction in the biosynthesis of NAD. Glutamine can also serve as an amido group donor.

## Pathways

- `ecocyc.PWY-7761` NAD salvage pathway II (PNC IV cycle) (EcoCyc)
- `ecocyc.PYRIDNUCSAL-PWY` NAD salvage pathway I (PNC VI cycle) (EcoCyc)
- `ecocyc.PYRIDNUCSYN-PWY` NAD de novo biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.NAD-SYNTH-CPLX|complex.ecocyc.NAD-SYNTH-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00857|molecule.C00857]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:NAD-SYNTH-NH3-RXN`

## Notes

AMMONIUM + ATP + DEAMIDO-NAD -> PROTON + AMP + PPI + NAD; direction=PHYSIOL-LEFT-TO-RIGHT
