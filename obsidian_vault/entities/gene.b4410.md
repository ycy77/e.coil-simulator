---
entity_id: "gene.b4410"
entity_type: "gene"
name: "ecnA"
source_database: "NCBI RefSeq"
source_id: "gene-b4410"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4410"
  - "ecnA"
---

# ecnA

`gene.b4410`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4410`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ecnA (gene.b4410) is a gene entity. It encodes ecnA (protein.P0ADB4). Encoded protein function: FUNCTION: Acts as antidote to the effect of entericidin B. EcoCyc product frame: MONOMER0-1562. Genomic coordinates: 4376317-4376442. EcoCyc protein note: ecnAB encodes an antidote/toxin system which may function as a starvation adaptation that supports further cell growth at the expense of dying subpopulations; the functions of EcnAB are consistent with a programmed cell death system . The EcnA lipoprotein is predicted to localise to the outer membrane; EcnA may adopt an amphipathic α-helical conformation . The entericidin A lipoprotein (EcnA) functions as an antidote to the bacteriolytic MONOMER0-1563 "entericidin B" lipoprotein. Deregulated expression of ecnB results in stationary phase bacteriolysis; this phenotype is eliminated upon expression of ecnA . ecnA does not appear to have an assoicated promoter but a Rho-independent terminator, located upstream of ecnA may attenuate EcnA production . The entericidin locus is non-essential in E. coli K-12 .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADB4|protein.P0ADB4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ecnA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0047210,ECOCYC:G0-41,GeneID:2847736`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4376317-4376442:+; feature_type=gene
