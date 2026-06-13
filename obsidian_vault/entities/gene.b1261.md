---
entity_id: "gene.b1261"
entity_type: "gene"
name: "trpB"
source_database: "NCBI RefSeq"
source_id: "gene-b1261"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1261"
  - "trpB"
---

# trpB

`gene.b1261`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1261`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

trpB (gene.b1261) is a gene entity. It encodes trpB (protein.P0A879). Encoded protein function: FUNCTION: The beta subunit is responsible for the synthesis of L-tryptophan from indole and L-serine. EcoCyc product frame: TRYPSYN-BPROTEIN. Genomic coordinates: 1317222-1318415.

## Biological Role

Repressed by trpR (protein.P0A881). Activated by rydC (gene.b4597), rpoD (protein.P00579).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A879|protein.P0A879]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[gene.b4597|gene.b4597]] `RegulonDB` `S` - regulator=RydC; target=trpB; function=+
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=trpB; function=+
- `represses` <-- [[protein.P0A881|protein.P0A881]] `RegulonDB` `C` - regulator=TrpR; target=trpB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004234,ECOCYC:EG11025,GeneID:945768`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1317222-1318415:-; feature_type=gene
