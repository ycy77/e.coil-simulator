---
entity_id: "complex.ecocyc.CPLX0-8165"
entity_type: "complex"
name: "ssDNA-binding protein"
source_database: "EcoCyc"
source_id: "CPLX0-8165"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "SSB"
---

# ssDNA-binding protein

`complex.ecocyc.CPLX0-8165`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8165`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0AGE0|protein.P0AGE0]]

## Enriched Summary

The product of the essential ssb gene, the highly stable, single-stranded DNA binding protein known as SSB, functions during DNA metabolism in E. coli K-12. SSB binding protects ssDNA from degradation; SSB interacts directly with numerous enzymes of DNA metabolism and is believed to have a central role in organising the nucleoprotein complexes and processes involved in DNA replication (and replication restart), recombination, and repair (see reviews by ). Purified SSB (from E. coli strains B and D10) is a homotetramer that binds tightly and cooperatively to ssDNA to form long protein clusters . SSB (also called DNA unwinding protein) stimulates DNA polymerase II and DNA polymerase III holoenzyme activity in vitro. The SSB monomer consists of three domains: an N-terminal ssDNA binding domain that contains an oligonucleotide-oligosaccharide binding fold (OB-fold), an intrinsically disordered linker (IDL) and a C-terminal acidic tip (and see ). The role of each domain in mediating SSB function has been widely investigated (see for example: ). SSB undergoes liquid-liquid phase separation (LLPS); the formation of phase-separated protein condensates containing SSB and SSB-interacting proteins promotes a timely response to genomic stress (see also )...

## Biological Role

Component of replisome (complex.ecocyc.CPLX0-13320).

## Annotation

The product of the essential ssb gene, the highly stable, single-stranded DNA binding protein known as SSB, functions during DNA metabolism in E. coli K-12. SSB binding protects ssDNA from degradation; SSB interacts directly with numerous enzymes of DNA metabolism and is believed to have a central role in organising the nucleoprotein complexes and processes involved in DNA replication (and replication restart), recombination, and repair (see reviews by ). Purified SSB (from E. coli strains B and D10) is a homotetramer that binds tightly and cooperatively to ssDNA to form long protein clusters . SSB (also called DNA unwinding protein) stimulates DNA polymerase II and DNA polymerase III holoenzyme activity in vitro. The SSB monomer consists of three domains: an N-terminal ssDNA binding domain that contains an oligonucleotide-oligosaccharide binding fold (OB-fold), an intrinsically disordered linker (IDL) and a C-terminal acidic tip (and see ). The role of each domain in mediating SSB function has been widely investigated (see for example: ). SSB undergoes liquid-liquid phase separation (LLPS); the formation of phase-separated protein condensates containing SSB and SSB-interacting proteins promotes a timely response to genomic stress (see also ). SSB displays multiple modes of binding to single-stranded DNA (ssDNA) templates; binding modes are differentiated by the number of SSB subunits (within a functional tetramer) interacting with substrate and the average number of nucleotides occluded by each bound tetramer (reviewed by . Although the various binding modes display different properties, their physiological relevance remains unclear (see ). Atomic force microscopic investigation of SSB binding properties to various ssDNA molecules reveals distinct binding affinities fo

## Outgoing Edges (2)

- `activates` --> [[reaction.ecocyc.ATPASE-RXN|reaction.ecocyc.ATPASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_component_of` --> [[complex.ecocyc.CPLX0-13320|complex.ecocyc.CPLX0-13320]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AGE0|protein.P0AGE0]] `EcoCyc` `database` - EcoCyc component coefficient=7 | EcoCyc protcplxs.col coefficient=7

## External IDs

- `EcoCyc:CPLX0-8165`
- `QSPROTEOME:QS00093300`

## Notes

7*protein.P0AGE0
