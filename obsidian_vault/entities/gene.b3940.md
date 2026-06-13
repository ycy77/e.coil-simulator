---
entity_id: "gene.b3940"
entity_type: "gene"
name: "metL"
source_database: "NCBI RefSeq"
source_id: "gene-b3940"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3940"
  - "metL"
---

# metL

`gene.b3940`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3940`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

metL (gene.b3940) is a gene entity. It encodes metL (protein.P00562). Encoded protein function: FUNCTION: Bifunctional aspartate kinase and homoserine dehydrogenase that catalyzes the first and the third steps toward the synthesis of lysine, methionine and threonine from aspartate. {ECO:0000250|UniProtKB:Q9SA18}. EcoCyc product frame: ASPKINIIHOMOSERDEHYDROGII-MONOMER. EcoCyc synonyms: metM. Genomic coordinates: 4129835-4132267.

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00300` Lysine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00562|protein.P00562]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=metL; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012889,ECOCYC:EG10590,GeneID:948433`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4129835-4132267:+; feature_type=gene
