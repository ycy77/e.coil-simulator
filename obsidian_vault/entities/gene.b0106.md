---
entity_id: "gene.b0106"
entity_type: "gene"
name: "hofC"
source_database: "NCBI RefSeq"
source_id: "gene-b0106"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0106"
  - "hofC"
---

# hofC

`gene.b0106`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0106`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hofC (gene.b0106) is a gene entity. It encodes hofC (protein.P36646). Encoded protein function: Protein transport protein HofC homolog EcoCyc product frame: EG11798-MONOMER. EcoCyc synonyms: yacD, hopC. Genomic coordinates: 114522-115724. EcoCyc protein note: HopC (now called HofC) is predicted to be a polytopic inner membrane protein; hofC is part of a putative three gene operon (ppdD hofB hofC) whose members all show sequence similarity to genes involved in type IV fimbrial assembly systems of pathogenic bacteria . ppdD hofB hofC has sequence similarity to the type IV piliation genes (pilABC) of Pseudomonas aeruginosa . The ppdD hofB hofC genes are poorly expressed; overexpression of ppdD, hofB and hofC in E. coli K-12 does not result in the production of detectable type IV pili . The HopC (host function of plasmid maintenance) mutation characterized by is unrelated to the hofC/hopC gene sequenced by . The hopC mutation characterized by maps in the thr-dnaC region. hop: homology to pil

## Biological Role

Repressed by nac (protein.Q47005). Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36646|protein.P36646]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=hofC; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=hofC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000366,ECOCYC:EG11798,GeneID:945806`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:114522-115724:-; feature_type=gene
