---
entity_id: "gene.b0641"
entity_type: "gene"
name: "lptE"
source_database: "NCBI RefSeq"
source_id: "gene-b0641"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0641"
  - "lptE"
---

# lptE

`gene.b0641`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0641`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lptE (gene.b0641) is a gene entity. It encodes lptE (protein.P0ADC1). Encoded protein function: FUNCTION: Together with LptD, is involved in the assembly of lipopolysaccharide (LPS) at the surface of the outer membrane. Required for the proper assembly of LptD. Binds LPS and may serve as the LPS recognition site at the outer membrane. {ECO:0000255|HAMAP-Rule:MF_01186, ECO:0000269|PubMed:16861298, ECO:0000269|PubMed:18424520, ECO:0000269|PubMed:20203010}. EcoCyc product frame: EG10855-MONOMER. EcoCyc synonyms: rlpB. Genomic coordinates: 671605-672186. EcoCyc protein note: LptE is part of the outer membrane LptDE complex that functions to assemble lipopolysaccharide (LPS) at the cell surface . lptE (formerly rlpB) encodes a minor lipoprotein; in vitro expression of the mature protein is inhibited by treatment with the signal peptidase II inhibitor, globomycin; the protein incorporates 3H-labeled palmitate and 3H-labeled glycerol in vitro . Purifed LptE binds LPS specifically . LptE binds LPS, disrupts LPS-LPS interactions and affects LPS aggregation propensity in vitro. LptE binds and solubilizes surface bound LPS in vitro. LptE containing the double mutation R91D K136D is able to bind, but cannot solubilize, surface bound LPS. These two amino acids may form part of an LPS interaction site that functions to disaggregate LPS and aid insertion into the outer membrane...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADC1|protein.P0ADC1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002194,ECOCYC:EG10855,GeneID:946257`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:671605-672186:-; feature_type=gene
