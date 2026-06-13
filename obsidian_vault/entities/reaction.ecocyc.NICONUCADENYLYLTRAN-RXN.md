---
entity_id: "reaction.ecocyc.NICONUCADENYLYLTRAN-RXN"
entity_type: "reaction"
name: "NICONUCADENYLYLTRAN-RXN"
source_database: "EcoCyc"
source_id: "NICONUCADENYLYLTRAN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "DEAMIDO-NAD(+) PYROPHOSPHORYLASE"
  - "Deamido-NAD(+) diphosphorylase"
---

# NICONUCADENYLYLTRAN-RXN

`reaction.ecocyc.NICONUCADENYLYLTRAN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:NICONUCADENYLYLTRAN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is known in Salmonella and a gene has been identified. It is assumed to be present in E. coli as well but no gene has yet been identified. It is the first of two reactions that synthesize NAD from nicotinic acid mononucleotide. A second reaction is catalyzed, part of the recycling pathway, which produces NAD by another route. This reaction is nicotinamide mononucleotide + ATP = NAD + PPi, E.C. 2.7.7.1. EcoCyc reaction equation: PROTON + ATP + NICOTINATE_NUCLEOTIDE -> PPI + DEAMIDO-NAD; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is known in Salmonella and a gene has been identified. It is assumed to be present in E. coli as well but no gene has yet been identified. It is the first of two reactions that synthesize NAD from nicotinic acid mononucleotide. A second reaction is catalyzed, part of the recycling pathway, which produces NAD by another route. This reaction is nicotinamide mononucleotide + ATP = NAD + PPi, E.C. 2.7.7.1.

## Biological Role

Catalyzed by nadD (protein.P0A752). Substrates: ATP (molecule.C00002), H+ (molecule.C00080), Nicotinate D-ribonucleotide (molecule.C01185). Products: Diphosphate (molecule.C00013), Deamino-NAD+ (molecule.C00857).

## Enriched Pathways

- `ecocyc.PWY-7761` NAD salvage pathway II (PNC IV cycle) (EcoCyc)
- `ecocyc.PYRIDNUCSAL-PWY` NAD salvage pathway I (PNC VI cycle) (EcoCyc)
- `ecocyc.PYRIDNUCSYN-PWY` NAD de novo biosynthesis I (EcoCyc)

## Annotation

This reaction is known in Salmonella and a gene has been identified. It is assumed to be present in E. coli as well but no gene has yet been identified. It is the first of two reactions that synthesize NAD from nicotinic acid mononucleotide. A second reaction is catalyzed, part of the recycling pathway, which produces NAD by another route. This reaction is nicotinamide mononucleotide + ATP = NAD + PPi, E.C. 2.7.7.1.

## Pathways

- `ecocyc.PWY-7761` NAD salvage pathway II (PNC IV cycle) (EcoCyc)
- `ecocyc.PYRIDNUCSAL-PWY` NAD salvage pathway I (PNC VI cycle) (EcoCyc)
- `ecocyc.PYRIDNUCSYN-PWY` NAD de novo biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `activates` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P0A752|protein.P0A752]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00857|molecule.C00857]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01185|molecule.C01185]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:NICONUCADENYLYLTRAN-RXN`

## Notes

PROTON + ATP + NICOTINATE_NUCLEOTIDE -> PPI + DEAMIDO-NAD; direction=PHYSIOL-LEFT-TO-RIGHT
