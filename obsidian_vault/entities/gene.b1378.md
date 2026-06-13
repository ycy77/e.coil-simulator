---
entity_id: "gene.b1378"
entity_type: "gene"
name: "ydbK"
source_database: "NCBI RefSeq"
source_id: "gene-b1378"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1378"
  - "ydbK"
---

# ydbK

`gene.b1378`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1378`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydbK (gene.b1378) is a gene entity. It encodes ydbK (protein.P52647). Encoded protein function: FUNCTION: Oxidoreductase required for the transfer of electrons from pyruvate to flavodoxin. {ECO:0000305}. EcoCyc product frame: G6701-MONOMER. EcoCyc synonyms: pfo. Genomic coordinates: 1437260-1440784. EcoCyc protein note: Based on sequence similarity, YdbK is predicted to function as a pyruvate:flavodoxin oxidoreductase and/or pyruvate synthase . The activity has been assayed in crude extracts with methyl viologen as the electron acceptor . Coexpression of YdbK with a heterologous hydrogenase enzyme enhances the production of hydrogen; the effect depends on the coexpression of an E. coli flavodoxin or a heterologous ferredoxin . Overexpression of YdbK in an engineered strain that utilizes ethanol aerobically as the sole source of carbon and secretes valine enables better growth and higher valine production, suggesting enhanced availability of pyruvate . The authors of suggest that YdbK is most likely the enzyme characterized by , PYRUFLAVREDUCT-MONOMER. Under the conditions employed by , the enzyme may function in the direction of pyruvate synthesis. A ydbK mutant is unable to grow on glucose under oxidative stress conditions . ydbK is needed for superoxide resistance during growth on minimal medium , and a ydbK fpr double mutant is sensitive to methyl viologen...

## Biological Role

Activated by soxS (protein.P0A9E2).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52647|protein.P52647]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `C` - regulator=SoxS; target=ydbK; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004613,ECOCYC:G6701,GeneID:946587`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1437260-1440784:-; feature_type=gene
