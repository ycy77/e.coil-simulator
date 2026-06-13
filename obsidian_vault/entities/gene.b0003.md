---
entity_id: "gene.b0003"
entity_type: "gene"
name: "thrB"
source_database: "NCBI RefSeq"
source_id: "gene-b0003"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0003"
  - "thrB"
---

# thrB

`gene.b0003`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0003`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

thrB (gene.b0003) is a gene entity. It encodes thrB (protein.P00547). Encoded protein function: FUNCTION: Catalyzes the ATP-dependent phosphorylation of L-homoserine to L-homoserine phosphate. Is also able to phosphorylate the hydroxy group on gamma-carbon of L-homoserine analogs when the functional group at the alpha-position is a carboxyl, an ester, or even a hydroxymethyl group. Neither L-threonine nor L-serine are substrates of the enzyme. {ECO:0000269|PubMed:8973190}. EcoCyc product frame: HOMOSERKIN-MONOMER. Genomic coordinates: 2801-3733.

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00547|protein.P00547]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=thrB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000010,ECOCYC:EG10999,GeneID:947498`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2801-3733:+; feature_type=gene
