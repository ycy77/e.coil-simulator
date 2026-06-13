---
entity_id: "gene.b3526"
entity_type: "gene"
name: "kdgK"
source_database: "NCBI RefSeq"
source_id: "gene-b3526"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3526"
  - "kdgK"
---

# kdgK

`gene.b3526`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3526`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

kdgK (gene.b3526) is a gene entity. It encodes kdgK (protein.P37647). Encoded protein function: FUNCTION: Catalyzes the phosphorylation of 2-keto-3-deoxygluconate (KDG) to produce 2-keto-3-deoxy-6-phosphogluconate (KDPG). {ECO:0000269|PubMed:4944816}. EcoCyc product frame: DEOXYGLUCONOKIN-MONOMER. EcoCyc synonyms: yhjI. Genomic coordinates: 3679419-3680348. EcoCyc protein note: 2-dehydro-3-deoxygluconokinase catalyzes the ATP-dependent phosphorylation of the first common intermediate in the D-glucuronate and D-galacturonate degradation pathways, 2-dehydro-3-deoxy-D-gluconate . The activity of KdgK increases 5-fold in cells grown on galacturonate or glucoronate rather than on glucose . KdgK: "2-keto-3-deoxygluconokinase"

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37647|protein.P37647]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011519,ECOCYC:EG12253,GeneID:948041`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3679419-3680348:+; feature_type=gene
