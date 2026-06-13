---
entity_id: "complex.ecocyc.CPLX0-0"
entity_type: "complex"
name: "replication restart protein DnaT"
source_database: "EcoCyc"
source_id: "CPLX0-0"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "primosomal protein i"
  - "primosomal protein DnaT"
---

# replication restart protein DnaT

`complex.ecocyc.CPLX0-0`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-0`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A8J2|protein.P0A8J2]]

## Enriched Summary

DnaT is required for chromosomal DNA replication, specifically for the restart of stalled replication forks . DnaT is specifically required for primosome function in the PriA-dependent restart reaction when replication stalls with a nascent leading strand end rather than a gapped fork. The function of PriA, PriB, and DnaT appears to be to load the replicative helicase DnaB onto a stalled replication fork for assembly of the replisome . Origin-independent loading of the replisome may be regulated by the dynamic assembly of the primosome; a model has been proposed . Early biochemical and genetic data showed that DnaT is required for induction of replication in the absence of protein synthesis during the SOS response and is a required component for assembly of the primosome complex that is capable of priming ΦX174 DNA replication in vitro . The inherently weak interaction between DnaT and PriB is stimulated by single-stranded DNA . The N-terminal domain of DnaT interacts with PriB; the interaction leads to dissociation from ssDNA. The Asp70 and Glu76 residues and the entire linker region (Asp66-Glu76) between the N- and C-terminal domains of DnaT are involved in PriB interaction and ssDNA dissociation . DnaT exists in a monomer-homotrimer equilibrium in the cell. At the estimated intracellular concentration of DnaT, the monomer:trimer ratio is approximately 3:1...

## Biological Role

Component of DNA replication restart primosome (complex.ecocyc.CPLX0-3922).

## Annotation

DnaT is required for chromosomal DNA replication, specifically for the restart of stalled replication forks . DnaT is specifically required for primosome function in the PriA-dependent restart reaction when replication stalls with a nascent leading strand end rather than a gapped fork. The function of PriA, PriB, and DnaT appears to be to load the replicative helicase DnaB onto a stalled replication fork for assembly of the replisome . Origin-independent loading of the replisome may be regulated by the dynamic assembly of the primosome; a model has been proposed . Early biochemical and genetic data showed that DnaT is required for induction of replication in the absence of protein synthesis during the SOS response and is a required component for assembly of the primosome complex that is capable of priming ΦX174 DNA replication in vitro . The inherently weak interaction between DnaT and PriB is stimulated by single-stranded DNA . The N-terminal domain of DnaT interacts with PriB; the interaction leads to dissociation from ssDNA. The Asp70 and Glu76 residues and the entire linker region (Asp66-Glu76) between the N- and C-terminal domains of DnaT are involved in PriB interaction and ssDNA dissociation . DnaT exists in a monomer-homotrimer equilibrium in the cell. At the estimated intracellular concentration of DnaT, the monomer:trimer ratio is approximately 3:1 . Binding of Mg2+ changes the thermodynamics of the DnaT trimerization . Within the N-terminal domain, the 24-residue region between Phe42 and Asp66 is required for trimerization . A crystal structure of the DnaT84-153-ssDNA ternary complex has been solved . The structure of the C-terminal domain (DnaT89-179) has been determined by NMR spectroscopy . Amino acid residues critical for DNA binding were confirmed by sit

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3922|complex.ecocyc.CPLX0-3922]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A8J2|protein.P0A8J2]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:CPLX0-0`
- `QSPROTEOME:QS00049398`

## Notes

3*protein.P0A8J2
