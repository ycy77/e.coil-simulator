---
entity_id: "gene.b2752"
entity_type: "gene"
name: "cysD"
source_database: "NCBI RefSeq"
source_id: "gene-b2752"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2752"
  - "cysD"
---

# cysD

`gene.b2752`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2752`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cysD (gene.b2752) is a gene entity. It encodes cysD (protein.P21156). Encoded protein function: FUNCTION: With CysN forms the ATP sulfurylase (ATPS) that catalyzes the adenylation of sulfate producing adenosine 5'-phosphosulfate (APS) and diphosphate, the first enzymatic step in sulfur assimilation pathway. APS synthesis involves the formation of a high-energy phosphoric-sulfuric acid anhydride bond driven by GTP hydrolysis by CysN coupled to ATP hydrolysis by CysD. {ECO:0000255|HAMAP-Rule:MF_00064, ECO:0000269|PubMed:2828368, ECO:0000269|PubMed:8003495}. EcoCyc product frame: CYSD-MONOMER. Genomic coordinates: 2875421-2876329. EcoCyc protein note: CysD along with CysN are the two subunits which form sulfate adenylyltransferase . This enzyme is involved in the assimilation of sulfate and catalyzes two reactions, GTP hydrolysis and activation of intracellular sulfate to APS (APS) which generates a sulfate-phosphate anhydride linkage. This linkage facilitates an energetically-downhill entry into the subsequent metabolic fates of reduction and group transfer. The rate of APS formation is enhanced by both a protein activator and by GTP hydrolysis . Mutations in the cysD gene prevent the anabolic utilization of sulfate . cysD, along with cysN and cysC, resides in the sulfate activation operon...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00450` Selenocompound metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01320` Sulfur cycle (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P21156|protein.P21156]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cysD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009029,ECOCYC:EG10186,GeneID:947217`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2875421-2876329:-; feature_type=gene
