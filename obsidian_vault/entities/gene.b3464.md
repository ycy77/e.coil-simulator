---
entity_id: "gene.b3464"
entity_type: "gene"
name: "ftsY"
source_database: "NCBI RefSeq"
source_id: "gene-b3464"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3464"
  - "ftsY"
---

# ftsY

`gene.b3464`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3464`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ftsY (gene.b3464) is a gene entity. It encodes ftsY (protein.P10121). Encoded protein function: FUNCTION: Involved in targeting and insertion of nascent membrane proteins into the cytoplasmic membrane. Acts as a receptor for the complex formed by the signal recognition particle (SRP) and the ribosome-nascent chain (RNC). Interaction with SRP-RNC leads to the transfer of the RNC complex to the Sec translocase for insertion into the membrane, the hydrolysis of GTP by both Ffh and FtsY, and the dissociation of the SRP-FtsY complex into the individual components. {ECO:0000255|HAMAP-Rule:MF_00920, ECO:0000269|PubMed:11735405, ECO:0000269|PubMed:11741850, ECO:0000269|PubMed:15148364, ECO:0000269|PubMed:17682051, ECO:0000269|PubMed:8194520, ECO:0000269|PubMed:9305630}. EcoCyc product frame: EG10346-MONOMER. Genomic coordinates: 3602750-3604243. EcoCyc protein note: FtsY is the receptor protein for the SRP-CPLX "signal recognition particle" (SRP) in a pathway which mediates the co-translational targeting and delivery of integral membrane proteins to the SEC-SECRETION-CPLX Sec translocon. FtsY is found in both the soluble and inner membrane fraction; FtsY is released from the inner membrane by treatments that solubilize peripheral membrane proteins...

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P10121|protein.P10121]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011318,ECOCYC:EG10346,GeneID:947978`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3602750-3604243:-; feature_type=gene
