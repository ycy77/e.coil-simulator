---
entity_id: "gene.b1815"
entity_type: "gene"
name: "pdeD"
source_database: "NCBI RefSeq"
source_id: "gene-b1815"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1815"
  - "pdeD"
---

# pdeD

`gene.b1815`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1815`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pdeD (gene.b1815) is a gene entity. It encodes pdeD (protein.P76261). Encoded protein function: FUNCTION: Phosphodiesterase (PDE) that catalyzes the hydrolysis of cyclic-di-GMP (c-di-GMP) to 5'-pGpG (By similarity). May serve as a negative regulator of cellulose synthesis (as has been suggested for S.typhimurium); overexpression inhibits cell aggregation in strains able to produce adhesive curli fimbriae. Cyclic-di-GMP is a second messenger which controls cell surface-associated traits in bacteria (PubMed:16513732). {ECO:0000250|UniProtKB:P21514, ECO:0000269|PubMed:16513732}. EcoCyc product frame: G6996-MONOMER. EcoCyc synonyms: yoaD. Genomic coordinates: 1898427-1900025. EcoCyc protein note: PdeD is a predicted c-di-GMP phosphodiesterase ; it is predicted to be an inner membrane protein with two transmembrane domains which flank a predicted periplasmic CSS domain containing two highly conserved cysteines, followed by a cytoplasmic C-terminal EAL domain with predicted phosphodiesterase activity . PdeD is one of 5 CSS domain containing c-di-GMP phosphodiesterases in E. coli K-12; redox control and proteolysis of these enzymes is believed to modulate their activity and affect matrix production in biofilm (see ). Expression of pdeD is positively regulated by CsgD...

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76261|protein.P76261]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006043,ECOCYC:G6996,GeneID:946336`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1898427-1900025:+; feature_type=gene
