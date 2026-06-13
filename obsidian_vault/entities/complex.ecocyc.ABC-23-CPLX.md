---
entity_id: "complex.ecocyc.ABC-23-CPLX"
entity_type: "complex"
name: "phosphonate/phosphate ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-23-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "PhnCDE"
---

# phosphonate/phosphate ABC transporter

`complex.ecocyc.ABC-23-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-23-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P16677|protein.P16677]], [[protein.P0DP69|protein.P0DP69]], [[protein.P16682|protein.P16682]]

## Enriched Summary

Phosphonates are compounds with direct carbon-phosphorus bonds rather than the carbon-oxygen-phosphorus bonds of phosphate esters. E. coli strains differ in their utilization of phosphonates: most strains, including E. coli B are able to metabolize phosphonates (phn+); K-12 is considered to be cryptic for phosphonate utilization - it is unable to use phosphonates as a source of phosphorous however (phn+) mutants [denoted phn (EcoK+)] can be obtained when the wild type is grown on glucose MOPS agar with phosphonates as the sole phosphorous source . Early studies characterized the phn (psiD) locus in E. coli strains that were phn+: expression of a psiD::lacZ transcriptional fusion is strongly induced upon phosphorous limitation and a psiD::lacZ strain is unable to use methylphosphonate as sole phosphorous source . phnC, phnD and phnE are part of a large gene cluster (phnCDEFGHIJKLMNOP) which is required for the use of phosphonates (and phosphite) as a phosphorous source in phn+ E. coli strains . phnC, phnD and phnE encode the components of a binding protein dependent phosphonate uptake system that can also transport phosphite, phosphoesters (phosphoserine) and inorganic phosphate (Pi) ; PhnD is the periplasmic binding protein, PhnC is the predicted ATP-binding subunit and PhnE is the predicted integral membrane subunit of the transporter complex . E...

## Biological Role

Catalyzes ABC-23-RXN (reaction.ecocyc.ABC-23-RXN), TRANS-RXN-238 (reaction.ecocyc.TRANS-RXN-238). Transports an alkylphosphonate (molecule.ecocyc.Alkylphosphonates), an (aminoalkyl)phosphonate (molecule.ecocyc.Aminoalkylphosphonates), hν (molecule.ecocyc.Light).

## Annotation

Phosphonates are compounds with direct carbon-phosphorus bonds rather than the carbon-oxygen-phosphorus bonds of phosphate esters. E. coli strains differ in their utilization of phosphonates: most strains, including E. coli B are able to metabolize phosphonates (phn+); K-12 is considered to be cryptic for phosphonate utilization - it is unable to use phosphonates as a source of phosphorous however (phn+) mutants [denoted phn (EcoK+)] can be obtained when the wild type is grown on glucose MOPS agar with phosphonates as the sole phosphorous source . Early studies characterized the phn (psiD) locus in E. coli strains that were phn+: expression of a psiD::lacZ transcriptional fusion is strongly induced upon phosphorous limitation and a psiD::lacZ strain is unable to use methylphosphonate as sole phosphorous source . phnC, phnD and phnE are part of a large gene cluster (phnCDEFGHIJKLMNOP) which is required for the use of phosphonates (and phosphite) as a phosphorous source in phn+ E. coli strains . phnC, phnD and phnE encode the components of a binding protein dependent phosphonate uptake system that can also transport phosphite, phosphoesters (phosphoserine) and inorganic phosphate (Pi) ; PhnD is the periplasmic binding protein, PhnC is the predicted ATP-binding subunit and PhnE is the predicted integral membrane subunit of the transporter complex . E. coli K-12 demonstrates reversible, phase variable phosphonate utilization estimated to occur at high frequency (>10-2 per generation in either direction, but strongly favoring the Phn- phenotype without selection for phosphonate utilization); phase variation may be mediated by a slipped-strand mispairing mechanism involving octomeric repeats in the phnE coding region. Phn- E. coli K-12 contains a triple octomer repeat in phnE

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.ABC-23-RXN|reaction.ecocyc.ABC-23-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-238|reaction.ecocyc.TRANS-RXN-238]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.Alkylphosphonates|molecule.ecocyc.Alkylphosphonates]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Aminoalkylphosphonates|molecule.ecocyc.Aminoalkylphosphonates]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P0DP69|protein.P0DP69]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P16677|protein.P16677]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P16682|protein.P16682]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:ABC-23-CPLX`
- `QSPROTEOME:QS00049309`

## Notes

2*protein.P16677|2*protein.P0DP69|1*protein.P16682
