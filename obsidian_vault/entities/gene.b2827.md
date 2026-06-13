---
entity_id: "gene.b2827"
entity_type: "gene"
name: "thyA"
source_database: "NCBI RefSeq"
source_id: "gene-b2827"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2827"
  - "thyA"
---

# thyA

`gene.b2827`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2827`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

thyA (gene.b2827) is a gene entity. It encodes thyA (protein.P0A884). Encoded protein function: FUNCTION: Catalyzes the reductive methylation of 2'-deoxyuridine-5'-monophosphate (dUMP) to 2'-deoxythymidine-5'-monophosphate (dTMP) while utilizing 5,10-methylenetetrahydrofolate (mTHF) as the methyl donor and reductant in the reaction, yielding dihydrofolate (DHF) as a by-product (PubMed:2223754, PubMed:3286637, PubMed:9826509). This enzymatic reaction provides an intracellular de novo source of dTMP, an essential precursor for DNA biosynthesis. This protein also binds to its mRNA thus repressing its own translation (PubMed:7708505). {ECO:0000269|PubMed:2223754, ECO:0000269|PubMed:3286637, ECO:0000269|PubMed:7708505, ECO:0000269|PubMed:9826509}. EcoCyc product frame: THYMIDYLATESYN-MONOMER. Genomic coordinates: 2964361-2965155.

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A884|protein.P0A884]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=thyA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009268,ECOCYC:EG11002,GeneID:949035`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2964361-2965155:-; feature_type=gene
