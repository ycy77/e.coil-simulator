---
entity_id: "complex.ecocyc.CPLX0-3"
entity_type: "complex"
name: "replication restart protein PriB"
source_database: "EcoCyc"
source_id: "CPLX0-3"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "PriB"
  - "primosomal replication protein N"
---

# replication restart protein PriB

`complex.ecocyc.CPLX0-3`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P07013|protein.P07013]]

## Enriched Summary

PriB is a component of the primosome, a multiprotein complex that is believed to be involved in restart of stalled replication forks. Based on genetic studies, some EG10763-MONOMER PriA-dependent restart pathways require PriB . Other research shows that a pathway dependent on both PriA and PriB is used when stalled replication forks have no leading strand gaps, alternately turning to a EG10765 PriC pathway when there are large gaps . PriB is a core component of the primosome, binding to PriA and single-stranded DNA (ssDNA) shortly after PriA binds DNA, stabilizing the PriA-DNA interaction . It has been shown that interactions between PriA and both arms of the branched DNA at replication forks trigger structural changes in PriA that, in addition to creating a pore encircling the lagging DNA strand, expose a surface of PriA to which PriB docks . PriB also assists in subsequent binding of DnaT to PriA . In the case of phiX174 phage, PriB interacts directly with single-strand binding protein (SSB) . While it is bound, PriB stimulates the helicase activity and processivity of PriA . Several crystal structures have been determined for PriB, all to around 2 Å resolution. Based on these structures, PriB exists as a dimer and is very structurally similar to SSB . Based on sequence comparison and operon organization PriB appears to have evolved from SSB via gene duplication . A 2...

## Biological Role

Component of DNA replication restart primosome (complex.ecocyc.CPLX0-3922).

## Annotation

PriB is a component of the primosome, a multiprotein complex that is believed to be involved in restart of stalled replication forks. Based on genetic studies, some EG10763-MONOMER PriA-dependent restart pathways require PriB . Other research shows that a pathway dependent on both PriA and PriB is used when stalled replication forks have no leading strand gaps, alternately turning to a EG10765 PriC pathway when there are large gaps . PriB is a core component of the primosome, binding to PriA and single-stranded DNA (ssDNA) shortly after PriA binds DNA, stabilizing the PriA-DNA interaction . It has been shown that interactions between PriA and both arms of the branched DNA at replication forks trigger structural changes in PriA that, in addition to creating a pore encircling the lagging DNA strand, expose a surface of PriA to which PriB docks . PriB also assists in subsequent binding of DnaT to PriA . In the case of phiX174 phage, PriB interacts directly with single-strand binding protein (SSB) . While it is bound, PriB stimulates the helicase activity and processivity of PriA . Several crystal structures have been determined for PriB, all to around 2 Å resolution. Based on these structures, PriB exists as a dimer and is very structurally similar to SSB . Based on sequence comparison and operon organization PriB appears to have evolved from SSB via gene duplication . A 2.7 Å-resolution crystal structure of PriB complexed with a short oligo shows that although PriB is structurally similar to SSB, it binds ssDNA differently . By shift assay, PriB binds both ssDNA and ssRNA equally well . PriB is required for "constitutive stable DNA replication," that is DNA replication that occurs in the absence of protein synthesis in an rnha mutant . Though priB nulls have very little p

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3922|complex.ecocyc.CPLX0-3922]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P07013|protein.P07013]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-3`
- `QSPROTEOME:QS00183173`
- `PDB:1V1Q`
- `PDB:1WOC`
- `PDB:1TXY`
- `PDB:2CCZ`

## Notes

2*protein.P07013
