---
entity_id: "gene.b4411"
entity_type: "gene"
name: "ecnB"
source_database: "NCBI RefSeq"
source_id: "gene-b4411"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4411"
  - "ecnB"
---

# ecnB

`gene.b4411`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4411`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ecnB (gene.b4411) is a gene entity. It encodes ecnB (protein.P0ADB7). Encoded protein function: FUNCTION: Plays a role in the bacteriolysis. Is activated under conditions of high osmolarity by the factor sigma S. Entericidin A functions as an antidote. EcoCyc product frame: MONOMER0-1563. EcoCyc synonyms: yjeU. Genomic coordinates: 4376553-4376699. EcoCyc protein note: ecnAB encodes an antidote/toxin system which may function as a starvation adaptation that supports further cell growth at the expense of dying subpopulations; the functions of EcnAB are consistent with a programmed cell death system . ecnB encodes a bacteriolytic lipoprotein that is expressed in stationary phase under high osmolarity conditions from an RPOS-MONOMER "RpoS"-dependent promoter and repressed by the PWY0-1500 "OmpR/EnvZ two component regulatory system" ecnB transcript can be detected in wild type cells grown in high salt conditions (300mM NaCl) but is absent in an rpoS transposon insertion mutant; ecnB transcript can be detected in envZ and ompR envZ transposon insertion mutants regardless of osmolarity . The MONOMER0-1562 "entericidin A lipoprotein" (EcnA) functions as an antidote to entericidin B . The EcnB lipoprotein is predicted to localise to the outer membrane; EcnB may adopt an amphipathic α-helical conformation . The entericidin locus is non-essential in E. coli K-12 .

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADB7|protein.P0ADB7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ecnB; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ecnB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0047211,ECOCYC:G0-9562,GeneID:2847737`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4376553-4376699:+; feature_type=gene
