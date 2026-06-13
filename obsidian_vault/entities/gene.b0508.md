---
entity_id: "gene.b0508"
entity_type: "gene"
name: "hyi"
source_database: "NCBI RefSeq"
source_id: "gene-b0508"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0508"
  - "hyi"
---

# hyi

`gene.b0508`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0508`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hyi (gene.b0508) is a gene entity. It encodes hyi (protein.P30147). Encoded protein function: FUNCTION: Catalyzes the reversible isomerization between hydroxypyruvate and 2-hydroxy-3-oxopropanoate (also termed tartronate semialdehyde). Does not catalyze the isomerization of D-fructose to D-glucose or that of D-xylulose to D-xylose. Also does not catalyze racemization of serine, alanine, glycerate or lactate. {ECO:0000269|PubMed:10561547}. EcoCyc product frame: G6277-MONOMER. EcoCyc synonyms: ybbG, gip. Genomic coordinates: 535710-536486. EcoCyc protein note: Hydroxypyruvate isomerase is a cofactor-independent racemase that catalyzes the reversible isomerization between hydroxypyruvate and tartronate semialdehyde .

## Biological Role

Repressed by allR (protein.P0ACN4).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30147|protein.P30147]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACN4|protein.P0ACN4]] `RegulonDB` `C` - regulator=AllR; target=hyi; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001756,ECOCYC:G6277,GeneID:946186`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:535710-536486:+; feature_type=gene
