---
entity_id: "gene.b1919"
entity_type: "gene"
name: "dcyD"
source_database: "NCBI RefSeq"
source_id: "gene-b1919"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1919"
  - "dcyD"
---

# dcyD

`gene.b1919`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1919`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dcyD (gene.b1919) is a gene entity. It encodes dcyD (protein.P76316). Encoded protein function: FUNCTION: Catalyzes the alpha,beta-elimination reaction of D-cysteine and of several D-cysteine derivatives. It could be a defense mechanism against D-cysteine. Can also catalyze the degradation of 3-chloro-D-alanine. {ECO:0000255|HAMAP-Rule:MF_01045, ECO:0000269|PubMed:3908101}. EcoCyc product frame: DCYSDESULF-MONOMER. EcoCyc synonyms: yedO. Genomic coordinates: 1998494-1999480. EcoCyc protein note: D-cysteine desulfhydrase (DcyD) is involved in utilization of D-cysteine as a source of sulfur. The enzyme also protects the cell from growth inhibition caused by D-cysteine, which interferes with isoleucine, leucine, and valine biosynthesis via inhibition of THREDEHYDSYN-CPLX . DcyD has similarity to 1-aminocyclopropane-carboxylate deaminases, but does not exhibit activity toward this substrate . 3-Chloro-D-alanine is an effective antibacterial agent. Although the purified enzyme catalyzes the α,β elimination reaction with 3-chloro-D-alanine, the reaction does not appear to occur in vivo . Of the strains originally tested, the mutant W3110 ΔtrpED102/F'ΔtrpED102 contained the highest amount of D-cysteine desulfhydrase . A dcyD mutant exhibits decreased resistance to D-cysteine, while overexpression causes increased resistance to D-cysteine compared to wild type...

## Biological Role

Activated by nac (protein.Q47005).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76316|protein.P76316]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=dcyD; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006389,ECOCYC:G7038,GeneID:946831`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1998494-1999480:-; feature_type=gene
