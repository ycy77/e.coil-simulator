---
entity_id: "gene.b1785"
entity_type: "gene"
name: "cdgI"
source_database: "NCBI RefSeq"
source_id: "gene-b1785"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1785"
  - "cdgI"
---

# cdgI

`gene.b1785`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1785`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cdgI (gene.b1785) is a gene entity. It encodes cdgI (protein.P76236). Encoded protein function: FUNCTION: Catalyzes the synthesis of cyclic-di-GMP (c-di-GMP) via the condensation of 2 GTP molecules. {ECO:0000250|UniProtKB:P31129}. EcoCyc product frame: G6971-MONOMER. EcoCyc synonyms: yeaI. Genomic coordinates: 1870385-1871860. EcoCyc protein note: CdgI contains an N-terminal MASE4 (Membrane-Associated SEnsor) domain with eight predicted transmembrane domains followed by a C-terminal degenerate diguanylate cyclase (GGDEF) domain that is located in the cytoplasm . CdgI belongs to the core set of eight GGDEF/EAL domain proteins that is absolutely conserved in a set of 61 E. coli genomes containing pathogenic, commensal and probiotic strains . A cdgI deletion mutant shows 30-fold increased early biofilm formation and 4-fold increased swimming motility. The motility phenotype is complemented by wild type cdgI, but not a mutant where the degenerate GGDEF motif, EGEVF in CdgI, was changed to EGAVF, suggesting that CdgI may indeed be a functional diguanylate cyclase. Deletion of cdgI does not alter the concentration of c-di-GMP inside the cell . Expression of cdgI may be dependent on σS under high salt, but not other stress conditions . No expression was seen in LB medium . G6971 was significantly upregulated in simulated microgravity . CdgI: "c-di-GMP binding protein I"

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by ygfI (protein.P52044).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76236|protein.P76236]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB|EcoCyc` `C` - regulator=SrsR; target=cdgI; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005941,ECOCYC:G6971,GeneID:946366`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1870385-1871860:+; feature_type=gene
