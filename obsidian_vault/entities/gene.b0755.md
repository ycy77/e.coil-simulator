---
entity_id: "gene.b0755"
entity_type: "gene"
name: "gpmA"
source_database: "NCBI RefSeq"
source_id: "gene-b0755"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0755"
  - "gpmA"
---

# gpmA

`gene.b0755`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0755`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gpmA (gene.b0755) is a gene entity. It encodes gpmA (protein.P62707). Encoded protein function: FUNCTION: Catalyzes the interconversion of 2-phosphoglycerate and 3-phosphoglycerate. {ECO:0000255|HAMAP-Rule:MF_01039, ECO:0000269|PubMed:10437801}. EcoCyc product frame: GPMA-MONOMER. EcoCyc synonyms: gpm. Genomic coordinates: 786843-787595.

## Biological Role

Repressed by fnrS (gene.b4699), fur (protein.P0A9A9). Activated by rpoD (protein.P00579), rpoS (protein.P13445).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P62707|protein.P62707]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gpmA; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=gpmA; function=+
- `represses` <-- [[gene.b4699|gene.b4699]] `RegulonDB` `S` - regulator=FnrS; target=gpmA; function=-
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=gpmA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002563,ECOCYC:EG11699,GeneID:945068`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:786843-787595:-; feature_type=gene
