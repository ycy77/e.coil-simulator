---
entity_id: "gene.b2453"
entity_type: "gene"
name: "eutG"
source_database: "NCBI RefSeq"
source_id: "gene-b2453"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2453"
  - "eutG"
---

# eutG

`gene.b2453`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2453`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

eutG (gene.b2453) is a gene entity. It encodes eutG (protein.P76553). Encoded protein function: FUNCTION: May act on the acetaldehyde produced from the degradation of ethanolamine, producing ethanol (By similarity). Active on acetaldehyde and isobutyraldehyde in vitro. In vitro works equally well with NADH or NADPH (PubMed:22731523). {ECO:0000250|UniProtKB:P41795, ECO:0000269|PubMed:22731523}. EcoCyc product frame: G7283-MONOMER. EcoCyc synonyms: yffV. Genomic coordinates: 2568324-2569511. EcoCyc protein note: EutG is a predicted alcohol dehydrogenase whose activity contributes slightly to the conversion of isobutyraldehyde to isobutanol in an engineered strain . EutG: "ethanolamine utilization" (in Salmonella typhimurium)

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76553|protein.P76553]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008087,ECOCYC:G7283,GeneID:946233`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2568324-2569511:-; feature_type=gene
