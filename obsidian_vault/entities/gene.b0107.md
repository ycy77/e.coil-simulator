---
entity_id: "gene.b0107"
entity_type: "gene"
name: "hofB"
source_database: "NCBI RefSeq"
source_id: "gene-b0107"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0107"
  - "hofB"
---

# hofB

`gene.b0107`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0107`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hofB (gene.b0107) is a gene entity. It encodes hofB (protein.P36645). Encoded protein function: Protein transport protein HofB homolog EcoCyc product frame: EG12106-MONOMER. EcoCyc synonyms: hopB. Genomic coordinates: 115714-117099. EcoCyc protein note: hopB (now called hofB) contains a Walker A motif and two pairs of conserved Cys residues located in CXXC motifs; hofB is part of a putative three gene operon (ppdD hofB hofC) whose members all show sequence similarity to genes involved in type IV fimbrial assembly systems of pathogenic bacteria . A hofB mutant (hofB::kan) has no obvious phenotype . ppdD hofB hofC has sequence similarity to the type IV piliation genes (pilABC) of Pseudomonas aeruginosa . The ppdD hofB hofC genes are poorly expressed; overexpression of ppdD, hofB and hofC in E. coli K-12 does not result in the production of detectable type IV pili . The HopB (host function of plasmid maintenance) mutation characterized by is unrelated to the hofB/hopB gene sequenced by . The hopB mutation characterized by maps in the bglB-oriC region. hop: homology to pil

## Biological Role

Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36645|protein.P36645]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=hofB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000370,ECOCYC:EG12106,GeneID:947481`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:115714-117099:-; feature_type=gene
