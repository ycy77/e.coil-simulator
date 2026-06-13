---
entity_id: "gene.b4471"
entity_type: "gene"
name: "tdcG"
source_database: "NCBI RefSeq"
source_id: "gene-b4471"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4471"
  - "tdcG"
---

# tdcG

`gene.b4471`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4471`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tdcG (gene.b4471) is a gene entity. It encodes tdcG (protein.P42630). Encoded protein function: L-serine dehydratase TdcG (SDH) (EC 4.3.1.17) (L-serine deaminase) EcoCyc product frame: LSERINEDEAM3-MONOMER. EcoCyc synonyms: b3111, yhaQ, b3112, tdcGa, yhaP, sdhY. Genomic coordinates: 3258285-3259649.

## Biological Role

Activated by crp (protein.P0ACJ8), tdcA (protein.P0ACQ7), tdcR (protein.P11866).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P42630|protein.P42630]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=tdcG; function=+
- `activates` <-- [[protein.P0ACQ7|protein.P0ACQ7]] `RegulonDB` `S` - regulator=TdcA; target=tdcG; function=+
- `activates` <-- [[protein.P11866|protein.P11866]] `RegulonDB` `S` - regulator=TdcR; target=tdcG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0174101,ECOCYC:G7624,GeneID:2847724`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3258285-3259649:-; feature_type=gene
