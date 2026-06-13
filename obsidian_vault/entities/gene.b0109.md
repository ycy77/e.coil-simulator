---
entity_id: "gene.b0109"
entity_type: "gene"
name: "nadC"
source_database: "NCBI RefSeq"
source_id: "gene-b0109"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0109"
  - "nadC"
---

# nadC

`gene.b0109`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0109`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nadC (gene.b0109) is a gene entity. It encodes nadC (protein.P30011). Encoded protein function: FUNCTION: Involved in the catabolism of quinolinic acid (QA). {ECO:0000269|PubMed:8561507}. EcoCyc product frame: QUINOPRIBOTRANS-MONOMER. Genomic coordinates: 117752-118645. EcoCyc protein note: Quinolinate phosphoribosyltransferase (NadC) catalyzes the third step in the de novo biosynthesis of NAD from L-aspartate . nadC mutants excrete quinolinate . NadC: "NAD biosynthesis"

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30011|protein.P30011]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=nadC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000374,ECOCYC:EG11546,GeneID:948869`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:117752-118645:-; feature_type=gene
