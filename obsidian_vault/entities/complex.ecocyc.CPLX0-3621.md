---
entity_id: "complex.ecocyc.CPLX0-3621"
entity_type: "complex"
name: "replicative DNA helicase"
source_database: "EcoCyc"
source_id: "CPLX0-3621"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "DnaB"
---

# replicative DNA helicase

`complex.ecocyc.CPLX0-3621`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3621`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0ACB0|protein.P0ACB0]]

## Enriched Summary

DnaB, the replicative DNA helicase, processively unwinds DNA at replication forks in advance of DNA polymerase. Along with primase, it is responsible for the initation of chromosomal DNA replication and for the continued priming of lagging-strand synthesis . It is also required for DNA replication in a number of plasmids . DnaB is a component of the primosome, the protein complex that initiates replicative DNA synthesis at the origin of replication, G0-10506. Such initiation requires MONOMER0-160, CPLX0-2425, DnaB and EG10237-MONOMER . Four or five DnaA monomers bind to a single DnaB helicase as well as binding to oriC, loading the DnaB onto one of the DNA strands exposed at the prepared origin of replication . The resulting complex of DnaA, DnaB and DnaC binds asymmetrically along the DNA, extending fifty base pairs farther "upstream" from oriC . Formation of this initiation complex on an oriC plasmid requires supercoiled DNA . DnaB subsequently unwinds DNA bidirectionally from oriC. DNA gyrase is required for this bidirectional activity. In the absence of DNA synthesis, single-strand binding protein (SSB) binds the unwound DNA . DnaB remains continuously associated with the advancing replication forks during subsequent DNA synthesis...

## Biological Role

Catalyzes RXN0-4261 (reaction.ecocyc.RXN0-4261). Component of replisome (complex.ecocyc.CPLX0-13320), DNA replication restart primosome (complex.ecocyc.CPLX0-3922).

## Annotation

DnaB, the replicative DNA helicase, processively unwinds DNA at replication forks in advance of DNA polymerase. Along with primase, it is responsible for the initation of chromosomal DNA replication and for the continued priming of lagging-strand synthesis . It is also required for DNA replication in a number of plasmids . DnaB is a component of the primosome, the protein complex that initiates replicative DNA synthesis at the origin of replication, G0-10506. Such initiation requires MONOMER0-160, CPLX0-2425, DnaB and EG10237-MONOMER . Four or five DnaA monomers bind to a single DnaB helicase as well as binding to oriC, loading the DnaB onto one of the DNA strands exposed at the prepared origin of replication . The resulting complex of DnaA, DnaB and DnaC binds asymmetrically along the DNA, extending fifty base pairs farther "upstream" from oriC . Formation of this initiation complex on an oriC plasmid requires supercoiled DNA . DnaB subsequently unwinds DNA bidirectionally from oriC. DNA gyrase is required for this bidirectional activity. In the absence of DNA synthesis, single-strand binding protein (SSB) binds the unwound DNA . DnaB remains continuously associated with the advancing replication forks during subsequent DNA synthesis . Using a DnaA-bound forked oriC DNA in vitro system, the presence of SSB was found to stimulate DnaB unwinding at the fork and DnaB's role in releasing DnaA from the DNA; additionally SSB enhances the unwinding at the fork by DnaB when DnaC is in excessive amounts . DnaC acts as a loader for DnaB, binding to it and localizing it to duplex DNA for its role in initiating replication and to single-stranded DNA for its role in assisting primer formation by primase . Though it is required for loading DnaB onto DNA, bound DnaC directly limits D

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN0-4261|reaction.ecocyc.RXN0-4261]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-13320|complex.ecocyc.CPLX0-13320]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-3922|complex.ecocyc.CPLX0-3922]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0ACB0|protein.P0ACB0]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CPLX0-3621`
- `QSPROTEOME:QS00176215`

## Notes

6*protein.P0ACB0
