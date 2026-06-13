---
entity_id: "gene.b3057"
entity_type: "gene"
name: "bacA"
source_database: "NCBI RefSeq"
source_id: "gene-b3057"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3057"
  - "bacA"
---

# bacA

`gene.b3057`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3057`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bacA (gene.b3057) is a gene entity. It encodes uppP (protein.P60932). Encoded protein function: FUNCTION: Catalyzes the dephosphorylation of undecaprenyl diphosphate (UPP). Confers resistance to bacitracin. {ECO:0000269|PubMed:15778224}. EcoCyc product frame: EG11665-MONOMER. EcoCyc synonyms: uppP. Genomic coordinates: 3203310-3204131. EcoCyc protein note: The purified BacA protein has undecaprenyl pyrophosphate (Und-PP or C55-PP) phosphatase activity, but not undecaprenol phosphokinase activity . The bacA gene product is not essential for growth, but the product of the BacA catalysed reaction, undecaprenyl phosphate, is essential for the synthesis of peptidoglycan and other cell wall components. At least three additional gene products, G6439-MONOMER "YbjG", PGPPHOSPHAB-MONOMER "PgpB", and G7146-MONOMER "LpxT", are thought to have undecaprenyl pyrophosphate phosphatase activity in E. coli . BacA accounts for approximately three quarters of the total C55-PP phosphatase activity . BacA catalyses C55-PP dephosphorylation on the periplasmic side of the inner membrane . Purified BacA dephosphorylates farnesyl pyrophosphate (FPP); the optimal pH for this assay is 6...

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco00552` Teichoic acid biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P60932|protein.P60932]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=bacA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010034,ECOCYC:EG11665,GeneID:947551`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3203310-3204131:-; feature_type=gene
