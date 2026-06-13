---
entity_id: "gene.b1021"
entity_type: "gene"
name: "pgaD"
source_database: "NCBI RefSeq"
source_id: "gene-b1021"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1021"
  - "pgaD"
---

# pgaD

`gene.b1021`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1021`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pgaD (gene.b1021) is a gene entity. It encodes pgaD (protein.P69432). Encoded protein function: FUNCTION: Required for the synthesis of poly-beta-1,6-N-acetyl-D-glucosamine (PGA), a biofilm adhesin polysaccharide. May assist the glycosyltransferase PgaC in the polymerization of PGA. {ECO:0000269|PubMed:15090514, ECO:0000269|PubMed:18359807, ECO:0000269|PubMed:19460094}. EcoCyc product frame: G6528-MONOMER. EcoCyc synonyms: hmsS, ycdP. Genomic coordinates: 1086106-1086519.

## Biological Role

Repressed by ompR (protein.P0AA16), csrA (protein.P69913). Activated by nhaR (protein.P0A9G2).

## Enriched Pathways

- `eco00543` Exopolysaccharide biosynthesis (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69432|protein.P69432]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9G2|protein.P0A9G2]] `RegulonDB` `S` - regulator=NhaR; target=pgaD; function=+
- `represses` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=pgaD; function=-
- `represses` <-- [[protein.P69913|protein.P69913]] `RegulonDB` `C` - regulator=carbon storage regulator CsrA; target=pgaD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003460,ECOCYC:G6528,GeneID:947503`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1086106-1086519:-; feature_type=gene
