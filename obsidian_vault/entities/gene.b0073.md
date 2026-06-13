---
entity_id: "gene.b0073"
entity_type: "gene"
name: "leuB"
source_database: "NCBI RefSeq"
source_id: "gene-b0073"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0073"
  - "leuB"
---

# leuB

`gene.b0073`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0073`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

leuB (gene.b0073) is a gene entity. It encodes leuB (protein.P30125). Encoded protein function: FUNCTION: Catalyzes the oxidation of 3-carboxy-2-hydroxy-4-methylpentanoate (3-isopropylmalate) to 3-carboxy-4-methyl-2-oxopentanoate. The product decarboxylates to 4-methyl-2 oxopentanoate. {ECO:0000255|HAMAP-Rule:MF_01033, ECO:0000269|PubMed:9003442}. EcoCyc product frame: 3-ISOPROPYLMALDEHYDROG-MONOMER. Genomic coordinates: 80867-81958.

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30125|protein.P30125]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=leuB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000265,ECOCYC:EG11577,GeneID:944798`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:80867-81958:-; feature_type=gene
