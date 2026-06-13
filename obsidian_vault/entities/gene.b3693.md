---
entity_id: "gene.b3693"
entity_type: "gene"
name: "dgoK"
source_database: "NCBI RefSeq"
source_id: "gene-b3693"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3693"
  - "dgoK"
---

# dgoK

`gene.b3693`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3693`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dgoK (gene.b3693) is a gene entity. It encodes dgoK (protein.P31459). Encoded protein function: 2-dehydro-3-deoxygalactonokinase (EC 2.7.1.58) (2-keto-3-deoxy-galactonokinase) (2-oxo-3-deoxygalactonate kinase) EcoCyc product frame: DEHYDDEOXGALACTKIN-MONOMER. EcoCyc synonyms: yidV. Genomic coordinates: 3873596-3874474. EcoCyc protein note: 2-dehydro-3-deoxygalactonate kinase catalyzes the second reaction in the degradation of D-galactonate, the ATP-dependent phosphorylation of 2-dehydro-3-deoxygalactonate . Production of 2-dehydro-3-deoxygalactonate kinase is induced by growth on galactonate . The inducer is D-galactonate, and expression is subject to catabolite repression . DgoA: "D-galactonate"

## Biological Role

Repressed by dgoR (protein.P31460). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31459|protein.P31459]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=dgoK; function=+
- `represses` <-- [[protein.P31460|protein.P31460]] `RegulonDB` `C` - regulator=DgoR; target=dgoK; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012076,ECOCYC:EG20051,GeneID:948207`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3873596-3874474:-; feature_type=gene
