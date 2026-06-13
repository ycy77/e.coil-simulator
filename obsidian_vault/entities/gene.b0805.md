---
entity_id: "gene.b0805"
entity_type: "gene"
name: "fiu"
source_database: "NCBI RefSeq"
source_id: "gene-b0805"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0805"
  - "fiu"
---

# fiu

`gene.b0805`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0805`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fiu (gene.b0805) is a gene entity. It encodes fiu (protein.P75780). Encoded protein function: FUNCTION: Involved in the active transport across the outer membrane of iron complexed with catecholate siderophores such as dihydroxybenzoylserine and dihydroxybenzoate. It derives its energy for transport by interacting with the trans-periplasmic membrane protein TonB. Can also transport catechol-substituted cephalosporins. Receptor for microcins M, H47 and E492. {ECO:0000269|PubMed:12949180, ECO:0000269|PubMed:16718603, ECO:0000269|PubMed:2139424, ECO:0000269|PubMed:2407721, ECO:0000269|PubMed:3072926}. EcoCyc product frame: G6414-MONOMER. EcoCyc synonyms: ybiL. Genomic coordinates: 839249-841531. EcoCyc protein note: Fiu is an integral outer membrane protein which mediates the TonB-dependent import of iron-catecholate complexes. Early work characterized an fiu mutant and identified an 83 kDa protein, produced in large amounts under iron limiting conditions which mediated the TonB dependent uptake of dihydroxybenzoylserine-iron complexes and 2-3-DIHYDROXYBENZOATE "dihydroxybenzoate" (an enterobactin precursor) (see also ). The physiological function of Fiu may be to recapture enterobactin hydrolysis products such as 2,3-dihydroxybenzoylserine and dihydroxybenzoate...

## Biological Role

Repressed by rybB (gene.b4417), fur (protein.P0A9A9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75780|protein.P75780]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[gene.b4417|gene.b4417]] `RegulonDB` `S` - regulator=RybB; target=fiu; function=-
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=fiu; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002749,ECOCYC:G6414,GeneID:946246`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:839249-841531:-; feature_type=gene
