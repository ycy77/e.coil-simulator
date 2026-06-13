---
entity_id: "gene.b3067"
entity_type: "gene"
name: "rpoD"
source_database: "NCBI RefSeq"
source_id: "gene-b3067"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3067"
  - "rpoD"
---

# rpoD

`gene.b3067`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3067`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpoD (gene.b3067) is a gene entity. It encodes rpoD (protein.P00579). Encoded protein function: FUNCTION: Sigma factors are initiation factors that promote the attachment of RNA polymerase to specific initiation sites and are then released. This sigma factor is the primary sigma factor during exponential growth. Preferentially transcribes genes associated with fast growth, such as ribosomal operons, other protein-synthesis related genes, rRNA- and tRNA-encoding genes and prfB. {ECO:0000255|HAMAP-Rule:MF_00963, ECO:0000269|PubMed:1643661, ECO:0000269|PubMed:1745227, ECO:0000269|PubMed:21398637, ECO:0000269|PubMed:24843001, ECO:0000269|PubMed:3543015, ECO:0000269|PubMed:8289270, ECO:0000269|PubMed:8808934}. EcoCyc product frame: RPOD-MONOMER. EcoCyc synonyms: alt. Genomic coordinates: 3213047-3214888. EcoCyc protein note: Sigma 70 is the primary sigma factor during exponential growth, targeting RNAP70-CPLX to a wide range of promoters that are essential for normal growth. Eσ70 transcribes, in the absence of any additional transcription factor, with higher efficiency genes encoding ribosomal proteins and other protein synthesis-related genes, such as rRNA- and tRNA-encoding genes and prfB, which encodes release factor 2 . Sigma 70 accounts for 60-95% of the total pool of cellular sigma factors during normal exponential growth...

## Biological Role

Repressed by lexA (protein.P0A7C2). Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3), rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00579|protein.P00579]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rpoD; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=rpoD; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=rpoD; function=+
- `represses` <-- [[protein.P0A7C2|protein.P0A7C2]] `RegulonDB` `S` - regulator=LexA; target=rpoD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010070,ECOCYC:EG10896,GeneID:947567`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3213047-3214888:+; feature_type=gene
