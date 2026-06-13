---
entity_id: "gene.b2751"
entity_type: "gene"
name: "cysN"
source_database: "NCBI RefSeq"
source_id: "gene-b2751"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2751"
  - "cysN"
---

# cysN

`gene.b2751`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2751`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cysN (gene.b2751) is a gene entity. It encodes cysN (protein.P23845). Encoded protein function: FUNCTION: With CysD forms the ATP sulfurylase (ATPS) that catalyzes the adenylation of sulfate producing adenosine 5'-phosphosulfate (APS) and diphosphate, the first enzymatic step in sulfur assimilation pathway. APS synthesis involves the formation of a high-energy phosphoric-sulfuric acid anhydride bond driven by GTP hydrolysis by CysN coupled to ATP hydrolysis by CysD. {ECO:0000255|HAMAP-Rule:MF_00062, ECO:0000269|PubMed:2828368, ECO:0000269|PubMed:8003495}. EcoCyc product frame: CYSN-MONOMER. Genomic coordinates: 2873992-2875419. EcoCyc protein note: CysN along with CysD are the two subunits which form sulfate adenylyltransferase . CysN contains a GTP-binding consensus sequence and stimulates the synthesis of APS (APS) by a GTPase mechanism . Sulfate adenylyltransferase is involved in the assimilation of sulfate and catalyzes two reactions, GTP hydrolysis and activation of intracellular sulfate to APS which generates a sulfate-phosphate anhydride linkage. This linkage facilitates an energetically-downhill entry into the subsequent metabolic fates of reduction and group transfer. The rate of APS formation is enhanced by both a protein activator and by GTP hydrolysis . Disruption of the cysN gene prevents sulfate activation and decreases expression of the downstream cysC gene...

## Biological Role

Activated by rpoD (protein.P00579), glaR (protein.P37338).

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

- `encodes` --> [[protein.P23845|protein.P23845]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cysN; function=+
- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=cysN; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009026,ECOCYC:EG10194,GeneID:947219`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2873992-2875419:-; feature_type=gene
