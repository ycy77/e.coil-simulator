---
entity_id: "gene.b2836"
entity_type: "gene"
name: "aas"
source_database: "NCBI RefSeq"
source_id: "gene-b2836"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2836"
  - "aas"
---

# aas

`gene.b2836`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2836`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aas (gene.b2836) is a gene entity. It encodes aas (protein.P31119). Encoded protein function: FUNCTION: Plays a role in lysophospholipid acylation. Transfers fatty acids to the 1-position via an enzyme-bound acyl-ACP intermediate in the presence of ATP and magnesium. Its physiological function is to regenerate phosphatidylethanolamine from 2-acyl-glycero-3-phosphoethanolamine (2-acyl-GPE) formed by transacylation reactions or degradation by phospholipase A1. {ECO:0000255|HAMAP-Rule:MF_01162, ECO:0000269|PubMed:1649829}. EcoCyc product frame: AAS-MONOMER. Genomic coordinates: 2973855-2976014. EcoCyc protein note: 2-acylglycerophosphoethanolamine (2-acyl-GPE) acyltransferase and acyl-acyl carrier protein (acyl-ACP) synthetase are dual catalytic activities encoded by the aas gene. Both enzymatic activities participate in membrane phospholipid turnover and the uptake and incorporation of exogenous 2-acyllysophospholipids. The function of 2-acyl-GPE acyltransferase is to regenerate phosphatidylethanolamine (PtdEtn) from 2-acyl-GPE formed by transacylation reactions or phospholipase A1 action. In the process enzyme-bound ACP is also regenerated . Acyl-ACP synthetase functions to ligate free fatty acids, with lengths of C-8 to C-18, to ACP . The protein contains bound ACP . Based on sequence similarity, Aas has been predicted to be a hydroxycinnamate-CoA ligase . Review:

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31119|protein.P31119]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009302,ECOCYC:EG11679,GeneID:947315`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2973855-2976014:-; feature_type=gene
