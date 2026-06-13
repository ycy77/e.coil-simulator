---
entity_id: "gene.b1800"
entity_type: "gene"
name: "dmlA"
source_database: "NCBI RefSeq"
source_id: "gene-b1800"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1800"
  - "dmlA"
---

# dmlA

`gene.b1800`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1800`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dmlA (gene.b1800) is a gene entity. It encodes dmlA (protein.P76251). Encoded protein function: FUNCTION: Catalyzes the NAD(+)-dependent oxidative decarboxylation of D-malate into pyruvate. Is essential for aerobic growth on D-malate as the sole carbon source. But is not required for anaerobic D-malate utilization, although DmlA is expressed and active in those conditions. Appears to be not able to use L-tartrate as a substrate for dehydrogenation instead of D-malate. {ECO:0000269|PubMed:20233924}. EcoCyc product frame: G6986-MONOMER. EcoCyc synonyms: ttuC, yeaU. Genomic coordinates: 1881912-1882997. EcoCyc protein note: DmlA is a D-malate dehydrogenase that is essential for aerobic growth on D-malate as the sole carbon source . DmlA also catalyses the oxidative decarboxylation of 3-isopropylmalate in vitro and in vivo and the non-decarboxylating oxidation of L(+)-tartrate in vitro. DmlA is a generalist enzyme and displays relatively high activity on 3 differing substrates . Expression of dmlA is increased more than 500-fold during growth on D-malate compared to growth on L-lactate , L-malate, glucose or glycerol . Under anaerobic conditions, expression of dmlA is increased even further by the presence of D-malate; however, anaerobic growth on D-malate requires the presence of an additional electron donor such as glycerol...

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76251|protein.P76251]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005991,ECOCYC:G6986,GeneID:946319`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1881912-1882997:+; feature_type=gene
