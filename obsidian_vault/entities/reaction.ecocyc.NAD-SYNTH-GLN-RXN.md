---
entity_id: "reaction.ecocyc.NAD-SYNTH-GLN-RXN"
entity_type: "reaction"
name: "NAD-SYNTH-GLN-RXN"
source_database: "EcoCyc"
source_id: "NAD-SYNTH-GLN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Nicotinamide adenine dinucleotide synthetase (glutamine)"
  - "NAD(+) synthetase (glutamine-hydrolysing)"
---

# NAD-SYNTH-GLN-RXN

`reaction.ecocyc.NAD-SYNTH-GLN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:NAD-SYNTH-GLN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

A reaction in the biosynthesis of NAD. Ammonia can also serve as a nitrogen donor. EcoCyc reaction equation: ATP + DEAMIDO-NAD + GLN + WATER -> PROTON + AMP + PPI + NAD + GLT; direction=PHYSIOL-LEFT-TO-RIGHT. A reaction in the biosynthesis of NAD. Ammonia can also serve as a nitrogen donor.

## Biological Role

Substrates: H2O (molecule.C00001), ATP (molecule.C00002), L-Glutamine (molecule.C00064), Deamino-NAD+ (molecule.C00857). Products: NAD+ (molecule.C00003), Diphosphate (molecule.C00013), AMP (molecule.C00020), L-Glutamate (molecule.C00025), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.PWY-7761` NAD salvage pathway II (PNC IV cycle) (EcoCyc)
- `ecocyc.PYRIDNUCSAL-PWY` NAD salvage pathway I (PNC VI cycle) (EcoCyc)
- `ecocyc.PYRIDNUCSYN-PWY` NAD de novo biosynthesis I (EcoCyc)

## Annotation

A reaction in the biosynthesis of NAD. Ammonia can also serve as a nitrogen donor.

## Pathways

- `ecocyc.PWY-7761` NAD salvage pathway II (PNC IV cycle) (EcoCyc)
- `ecocyc.PYRIDNUCSAL-PWY` NAD salvage pathway I (PNC VI cycle) (EcoCyc)
- `ecocyc.PYRIDNUCSYN-PWY` NAD de novo biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `is_product_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00064|molecule.C00064]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00857|molecule.C00857]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:NAD-SYNTH-GLN-RXN`

## Notes

ATP + DEAMIDO-NAD + GLN + WATER -> PROTON + AMP + PPI + NAD + GLT; direction=PHYSIOL-LEFT-TO-RIGHT
