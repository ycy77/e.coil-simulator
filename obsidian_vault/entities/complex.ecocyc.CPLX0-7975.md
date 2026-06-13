---
entity_id: "complex.ecocyc.CPLX0-7975"
entity_type: "complex"
name: "DNA-binding transcriptional repressor/NMN adenylyltransferase NadR"
source_database: "EcoCyc"
source_id: "CPLX0-7975"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# DNA-binding transcriptional repressor/NMN adenylyltransferase NadR

`complex.ecocyc.CPLX0-7975`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7975`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P27278|protein.P27278]]

## Enriched Summary

The multifunctional protein NadR has enzymatic as well as regulatory activity. Initially thought to only function as a transcriptional regulator that represses genes involved in transport and de novo synthesis of NAD , NadR was later shown to have nicotinamide mononucleotide (NMN) adenylyltransferase activity and predicted to have ribosylnicotinamide kinase activity . Experiments in which XANTHOSINEPHOSPHORY-MONOMER was shown to be possibly involved in PWY3O-4106 also indicated this NAD salvage pathway was deficient in nadR deletion mutants . NadR is composed of three different domains: an N-terminal helix-turn-helix domain for DNA binding, a central NMN adenylyltransferase domain that contains an ATP-binding site, and a C-terminal ribosylnicotinamide kinase domain . NadR is often found to be mutated in long-term evolution experiments; interestingly, mutations are usually only found in the N- and C-terminal domains . It has been proposed that NadR recognizes and binds to two palindromic sequences of 6 bp separated by six less conserved nucleotides. This site is conserved in some NadR ortholog target genes in some enterobacteria, and it was also identified upstream of the nadR gene itself in E. carotovora, S. marcescens, Y. pestis, and Y. enterocolitica , but not in Escherichia coli . Mutations in nadR have been observed in cells tolerant to the chemical p-coumarate...

## Biological Role

Catalyzes 2.7.7.1-RXN (reaction.ecocyc.2.7.7.1-RXN), RIBOSYLNICOTINAMIDE-KINASE-RXN (reaction.ecocyc.RIBOSYLNICOTINAMIDE-KINASE-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

The multifunctional protein NadR has enzymatic as well as regulatory activity. Initially thought to only function as a transcriptional regulator that represses genes involved in transport and de novo synthesis of NAD , NadR was later shown to have nicotinamide mononucleotide (NMN) adenylyltransferase activity and predicted to have ribosylnicotinamide kinase activity . Experiments in which XANTHOSINEPHOSPHORY-MONOMER was shown to be possibly involved in PWY3O-4106 also indicated this NAD salvage pathway was deficient in nadR deletion mutants . NadR is composed of three different domains: an N-terminal helix-turn-helix domain for DNA binding, a central NMN adenylyltransferase domain that contains an ATP-binding site, and a C-terminal ribosylnicotinamide kinase domain . NadR is often found to be mutated in long-term evolution experiments; interestingly, mutations are usually only found in the N- and C-terminal domains . It has been proposed that NadR recognizes and binds to two palindromic sequences of 6 bp separated by six less conserved nucleotides. This site is conserved in some NadR ortholog target genes in some enterobacteria, and it was also identified upstream of the nadR gene itself in E. carotovora, S. marcescens, Y. pestis, and Y. enterocolitica , but not in Escherichia coli . Mutations in nadR have been observed in cells tolerant to the chemical p-coumarate . Review:

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.2.7.7.1-RXN|reaction.ecocyc.2.7.7.1-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RIBOSYLNICOTINAMIDE-KINASE-RXN|reaction.ecocyc.RIBOSYLNICOTINAMIDE-KINASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P27278|protein.P27278]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-7975`
- `QSPROTEOME:QS00049684`

## Notes

4*protein.P27278
