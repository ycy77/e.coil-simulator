---
entity_id: "gene.b1317"
entity_type: "gene"
name: "ycjU"
source_database: "NCBI RefSeq"
source_id: "gene-b1317"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1317"
  - "ycjU"
---

# ycjU

`gene.b1317`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1317`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycjU (gene.b1317) is a gene entity. It encodes ycjU (protein.P77366). Encoded protein function: FUNCTION: Catalyzes the conversion of beta D-glucose 1-phosphate (G1P) to D-glucose 6-phosphate (G6P), forming beta-D-glucose 1,6-(bis)phosphate (beta-G16P) as an intermediate (Probable) (PubMed:16990279, PubMed:29684280). Phosphatase activity with the reaction intermediate beta-G16P has been measured (PubMed:25848029). In vitro interconverts beta D-glucose 1-phosphate, beta-D-allose 1-phosphate, beta-D-galactose 1-phosphate and beta-D-mannose 1-phosphate to their corresponding sugar 6-phosphate product. The beta-D-glucose 1-phosphate substrate may be furnished by YcjT (AC P77154), the apparent upstream enzyme in the putative biochemical pathway encoded in this locus (yjcM to ycjW) (PubMed:29684280). It may play a key role in the regulation of the flow of carbohydrate intermediates in glycolysis and the formation of the sugar nucleotide UDP-glucose. {ECO:0000269|PubMed:16990279, ECO:0000269|PubMed:25848029, ECO:0000269|PubMed:29684280, ECO:0000305|PubMed:25848029}. EcoCyc product frame: G6655-MONOMER. EcoCyc synonyms: pgmB. Genomic coordinates: 1380148-1380807. EcoCyc protein note: YcjU is a β-phosphoglucomutase belonging to the superfamily of haloacid dehalogenase (HAD)-like hydrolases...

## Biological Role

Repressed by ycjW (protein.P77615).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77366|protein.P77366]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P77615|protein.P77615]] `RegulonDB` `S` - regulator=YcjW; target=ycjU; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004420,ECOCYC:G6655,GeneID:945891`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1380148-1380807:+; feature_type=gene
