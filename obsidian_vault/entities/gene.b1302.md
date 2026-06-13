---
entity_id: "gene.b1302"
entity_type: "gene"
name: "puuE"
source_database: "NCBI RefSeq"
source_id: "gene-b1302"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1302"
  - "puuE"
---

# puuE

`gene.b1302`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1302`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

puuE (gene.b1302) is a gene entity. It encodes puuE (protein.P50457). Encoded protein function: FUNCTION: Catalyzes the transfer of the amino group from gamma-aminobutyrate (GABA) to alpha-ketoglutarate (KG) to yield succinic semialdehyde (SSA). PuuE is important for utilization of putrescine as the sole nitrogen or carbon source. {ECO:0000269|PubMed:15590624, ECO:0000269|PubMed:20639325}. EcoCyc product frame: G6646-MONOMER. EcoCyc synonyms: goaG. Genomic coordinates: 1365550-1366815. EcoCyc protein note: The 4-aminobutyrate aminotransferase PuuE is the initial enzyme of one of two 4-aminobutyrate (GABA) degradation pathways. PuuE was identified as a putrescine-inducible GABA aminotransferase, which allows cells to grow on putrescine as the sole source of nitrogen even in the absence of GabT . PuuE also functions as a 5-aminovalerate aminotransferase during degradation of L-lysine . The function of genes in the puu gene cluster was initially inferred by similarity with the ipuABCDEGFH operon in Pseudomonas sp. . Site-directed mutagenesis confirmed that the K267 residue is essential for catalytic activity . PuuE activity is induced by growth on putrescine and repressed by addition of succinate and under conditions of limited oxygen availability . The three major transaminases in alanine biosynthesis are AvtA, AlaA and AlaC...

## Biological Role

Repressed by spf (gene.b3864), puuR (protein.P0A9U6).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P50457|protein.P50457]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[gene.b3864|gene.b3864]] `RegulonDB` `S` - regulator=Spf; target=puuE; function=-
- `represses` <-- [[protein.P0A9U6|protein.P0A9U6]] `RegulonDB` `C` - regulator=PuuR; target=puuE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004380,ECOCYC:G6646,GeneID:945446`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1365550-1366815:+; feature_type=gene
