---
entity_id: "gene.b4478"
entity_type: "gene"
name: "dgoD"
source_database: "NCBI RefSeq"
source_id: "gene-b4478"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4478"
  - "dgoD"
---

# dgoD

`gene.b4478`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4478`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dgoD (gene.b4478) is a gene entity. It encodes dgoD (protein.Q6BF17). Encoded protein function: FUNCTION: Catalyzes the dehydration of D-galactonate to 2-keto-3-deoxy-D-galactonate. {ECO:0000269|PubMed:324806, ECO:0000269|Ref.7}. EcoCyc product frame: GALACTONATE-DEHYDRATASE-MONOMER. EcoCyc synonyms: b3692, yidU. Genomic coordinates: 3871850-3872998. EcoCyc protein note: D-galactonate dehydratase catalyzes the first step in the degradation of D-galactonate, the dehydration of D-galactonate to form 2-dehydro-3-deoxygalactonate . D-galactonate dehydratase belongs to the mandelate racemase (MR) subgroup of the enolase superfamily . A reaction mechanism for the β-elimination of OH- involving His185 as a general acid/base catalyst has been proposed and is supported by analysis of point mutants . Production of galactonate dehydratase is induced by growth on galactonate . The inducer is D-galactonate, and expression is subject to catabolite repression . The enantiomer CPD-12349 alone cannot be used by E. coli as a sole carbon source, however a mixture of 2-dehydro-3-deoxy-L-galactonate and D-GALACTURONATE enables the utilization of both compounds .

## Biological Role

Repressed by dgoR (protein.P31460). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q6BF17|protein.Q6BF17]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=dgoD; function=+
- `represses` <-- [[protein.P31460|protein.P31460]] `RegulonDB` `C` - regulator=DgoR; target=dgoD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0174106,ECOCYC:GB4478,GeneID:2847765`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3871850-3872998:-; feature_type=gene
