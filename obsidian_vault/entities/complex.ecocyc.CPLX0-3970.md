---
entity_id: "complex.ecocyc.CPLX0-3970"
entity_type: "complex"
name: "murein tripeptide ABC transporter"
source_database: "EcoCyc"
source_id: "CPLX0-3970"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# murein tripeptide ABC transporter

`complex.ecocyc.CPLX0-3970`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3970`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AFH2|protein.P0AFH2]], [[protein.P0AFH6|protein.P0AFH6]], [[protein.P76027|protein.P76027]], [[protein.P77737|protein.P77737]], [[protein.P77348|protein.P77348]]

## Enriched Summary

OppBCDFMppA is a high affinity murein tripeptide transporter that is a member of the ATP-binding cassette (ABC) superfamily of transporters. oppBC and oppDF encode two ATP binding subunits and two integral membrane proteins respectively, of an ABC transport system that interacts with either of two periplasmic peptide binding proteins, MppA - which has affinity for murein tripeptides and OppA - with a preference for positively charged tripeptides and tetrapeptides . The uptake of labeled cell wall peptide is abolished in E. coli strains that contain a complete opp deletion (ΔoppABCDF467) and in a strain with a non-polar oppA mutation ; this non-polar oppA mutation (oppA462) was later reported to be a polar mutation . MppA - the periplasmic binding protein - has been implicated in the uptake of murein tripeptide under nitrogen starvation conditions . Unlike AMPG-MONOMER AmpG, OppBCDFMppA is unable to transport anhydro-MurNAc-linked muropeptides . OppBCDFMppA-mediated import of muropeptides is beneficial when nutrients are low and OppBCDFMppA appears uniquely capable of scavenging muropeptides from the environment . Related reviews: . OppBCDFMppA is a high affinity murein tripeptide transporter that is a member of the ATP-binding cassette (ABC) superfamily of transporters...

## Biological Role

Catalyzes TRANS-RXN0-268 (reaction.ecocyc.TRANS-RXN0-268). Transports hν (molecule.ecocyc.Light).

## Annotation

OppBCDFMppA is a high affinity murein tripeptide transporter that is a member of the ATP-binding cassette (ABC) superfamily of transporters. oppBC and oppDF encode two ATP binding subunits and two integral membrane proteins respectively, of an ABC transport system that interacts with either of two periplasmic peptide binding proteins, MppA - which has affinity for murein tripeptides and OppA - with a preference for positively charged tripeptides and tetrapeptides . The uptake of labeled cell wall peptide is abolished in E. coli strains that contain a complete opp deletion (ΔoppABCDF467) and in a strain with a non-polar oppA mutation ; this non-polar oppA mutation (oppA462) was later reported to be a polar mutation . MppA - the periplasmic binding protein - has been implicated in the uptake of murein tripeptide under nitrogen starvation conditions . Unlike AMPG-MONOMER AmpG, OppBCDFMppA is unable to transport anhydro-MurNAc-linked muropeptides . OppBCDFMppA-mediated import of muropeptides is beneficial when nutrients are low and OppBCDFMppA appears uniquely capable of scavenging muropeptides from the environment . Related reviews: .

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-268|reaction.ecocyc.TRANS-RXN0-268]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (5)

- `is_component_of` <-- [[protein.P0AFH2|protein.P0AFH2]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AFH6|protein.P0AFH6]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P76027|protein.P76027]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P77348|protein.P77348]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P77737|protein.P77737]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:CPLX0-3970`
- `QSPROTEOME:QS00049425`

## Notes

1*protein.P0AFH2|1*protein.P0AFH6|1*protein.P76027|1*protein.P77737|1*protein.P77348
