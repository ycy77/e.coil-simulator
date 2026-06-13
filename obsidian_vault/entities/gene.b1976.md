---
entity_id: "gene.b1976"
entity_type: "gene"
name: "mtfA"
source_database: "NCBI RefSeq"
source_id: "gene-b1976"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1976"
  - "mtfA"
---

# mtfA

`gene.b1976`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1976`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mtfA (gene.b1976) is a gene entity. It encodes mtfA (protein.P76346). Encoded protein function: FUNCTION: Involved in the modulation of the activity of the glucose-phosphotransferase system (glucose-PTS) (PubMed:16855233). Interacts with the transcriptional repressor Mlc, preventing its interaction with DNA and leading to the modulation of expression of genes regulated by Mlc, including ptsG, which encodes the PTS system glucose-specific EIICB component (PubMed:16855233, PubMed:22178967). {ECO:0000269|PubMed:16855233, ECO:0000269|PubMed:22178967}.; FUNCTION: Shows zinc-dependent metallopeptidase activity (By similarity). In vitro, can cleave several artificial substrates (PubMed:22178967). The greatest activity and specificity is observed for L-alanine fused to 4-nitroanilide (L-alanine-pNA) (PubMed:22178967). Shows significantly lower activity towards L-arginine-pNA, L-proline-pNA, hippuryl-L-phenylalanine and hippuryl-L-arginine, and cannot use FTC-casein (PubMed:22178967). Mlc does not appear to be a biologically relevant peptidase substrate (PubMed:22178967). Biologically relevant targets may have a function in growth transition under changing environmental conditions (PubMed:22178967). {ECO:0000250|UniProtKB:A6TB83, ECO:0000269|PubMed:22178967}. EcoCyc product frame: G7063-MONOMER. EcoCyc synonyms: yeeI. Genomic coordinates: 2043651-2044448...

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76346|protein.P76346]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=mtfA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006558,ECOCYC:G7063,GeneID:946489`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2043651-2044448:+; feature_type=gene
