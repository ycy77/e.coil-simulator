---
entity_id: "gene.b0521"
entity_type: "gene"
name: "ybcF"
source_database: "NCBI RefSeq"
source_id: "gene-b0521"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0521"
  - "ybcF"
---

# ybcF

`gene.b0521`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0521`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybcF (gene.b0521) is a gene entity. It encodes allK (protein.P37306). Encoded protein function: FUNCTION: Kinase involved in the anaerobic nitrogen utilization via the assimilation of allantoin (PubMed:36384810). Catalyzes the transfer of a phosphate group from carbamoyl phosphate to ADP to produce ATP and leave carbamate, which spontaneously hydrolyzes to ammonia and hydrogencarbonate (PubMed:36384810). {ECO:0000269|PubMed:36384810}. EcoCyc product frame: EG12384-MONOMER. EcoCyc synonyms: arcC, ybcF, UTCase (transcarbamylase with unknown function), AllK. Genomic coordinates: 550439-551332. EcoCyc protein note: This gene is the last gene within the TU0-12962 operon whose first three genes encode subunits of the CPLX0-12207 complex . Using sequence orthology and genome and metabolic context methods, ybcF is predicted to encode the catabolic carbamate kinase activity of the anaerobic allantoin degradation pathway . Using both inactivation and overexpression mutants, and purified AllK in vitro, the carbamate kinase activity was verified in anaerobic conditions with allantoin as the sole nitrogen source. This activity is also referred to as oxamic transcarbamylase (OXTCase) .

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00230` Purine metabolism (KEGG)
- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37306|protein.P37306]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001791,ECOCYC:EG12384,GeneID:944972`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:550439-551332:+; feature_type=gene
