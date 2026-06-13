---
entity_id: "gene.b0439"
entity_type: "gene"
name: "lon"
source_database: "NCBI RefSeq"
source_id: "gene-b0439"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0439"
  - "lon"
---

# lon

`gene.b0439`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0439`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lon (gene.b0439) is a gene entity. It encodes lon (protein.P0A9M0). Encoded protein function: FUNCTION: ATP-dependent serine protease that mediates the selective degradation of mutant and abnormal proteins as well as certain short-lived regulatory proteins, including some antitoxins. Required for cellular homeostasis and for survival from DNA damage and developmental changes induced by stress. Degrades polypeptides processively to yield small peptide fragments that are 5 to 10 amino acids long. Binds to DNA in a double-stranded, site-specific manner. Endogenous substrates include the regulatory proteins RcsA and SulA, the transcriptional activator SoxS, UmuD and at least type II antitoxins CcdA, HipB and MazE (PubMed:16460757, PubMed:22720069, PubMed:24375411, PubMed:8022284). Its overproduction specifically inhibits translation through at least two different pathways, one of them being the YoeB-YefM toxin-antitoxin system (PubMed:15009896). {ECO:0000269|PubMed:12135363, ECO:0000269|PubMed:15009896, ECO:0000269|PubMed:16460757, ECO:0000269|PubMed:16584195, ECO:0000269|PubMed:19721064, ECO:0000269|PubMed:22720069, ECO:0000269|PubMed:24375411, ECO:0000269|PubMed:8022284}. EcoCyc product frame: EG10542-MONOMER. EcoCyc synonyms: capR, deg, dir, lopA, muc. Genomic coordinates: 458888-461242.

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9M0|protein.P0A9M0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=lon; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001521,ECOCYC:EG10542,GeneID:945085`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:458888-461242:+; feature_type=gene
