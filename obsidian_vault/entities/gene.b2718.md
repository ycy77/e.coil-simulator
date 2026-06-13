---
entity_id: "gene.b2718"
entity_type: "gene"
name: "hycH"
source_database: "NCBI RefSeq"
source_id: "gene-b2718"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2718"
  - "hycH"
---

# hycH

`gene.b2718`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2718`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hycH (gene.b2718) is a gene entity. It encodes hycH (protein.P0AEV7). Encoded protein function: FUNCTION: Seems to be required for the conversion of a precursor form of the large subunit of hydrogenlyase (HycE) into a mature form. {ECO:0000269|PubMed:1625581}. EcoCyc product frame: EG10481-MONOMER. EcoCyc synonyms: hevH. Genomic coordinates: 2843036-2843446. EcoCyc protein note: The HycH protein is implicated in assembly of the FHLMULTI-CPLX "formate hydrogenlyase (FHL) complex" and more specifically in the attachment and stability of the electron transfer subunit HycG; HycH interacts with unprocessed HycE . Deletion of hycH results in a significant reduction in FHL activity compared to wild type, although residual activity can still be detected . Deletion of hycH reduces the stability of the FHL complex . HycH shares 45% overall amino acid sequence identity with G7307-MONOMER "HyfJ" and the two proteins may share overlapping functions . HycH was initially implicated in 'processing' of HycE- the catalytic subunit of hydrogenase 3 - a function later ascribed to G7414-MONOMER "HycI" (and see ).

## Biological Role

Activated by modE (protein.P0A9G8), fhlA (protein.P19323), rpoN (protein.P24255).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEV7|protein.P0AEV7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `S` - regulator=ModE; target=hycH; function=+
- `activates` <-- [[protein.P19323|protein.P19323]] `RegulonDB` `S` - regulator=FhlA; target=hycH; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=hycH; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008933,ECOCYC:EG10481,GeneID:947438`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2843036-2843446:-; feature_type=gene
