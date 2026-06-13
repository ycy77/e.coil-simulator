---
entity_id: "gene.b3882"
entity_type: "gene"
name: "yihU"
source_database: "NCBI RefSeq"
source_id: "gene-b3882"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3882"
  - "yihU"
---

# yihU

`gene.b3882`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3882`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yihU (gene.b3882) is a gene entity. It encodes yihU (protein.P0A9V8). Encoded protein function: FUNCTION: Reduces 3-sulfolactaldehyde (SLA) to 2,3-dihydroxypropane 1-sulfonate (DHPS) (PubMed:24463506, Ref.6). Metabolite profiling studies showed that the enzyme also catalyzes in vitro the NADH-dependent reduction of succinic semialdehyde (SSA) to 4-hydroxybutyrate (GHB), and that it could be involved in the metabolism of SSA, and other potentially toxic intermediates that may accumulate under stress conditions (PubMed:19372223). However, the enzyme exhibits a 42,000-fold greater catalytic efficiency for the reduction of SLA over SSA (Ref.6). Shows no detectable activity on the analogous glycolytic intermediate glyceraldehyde-3-phosphate (Ref.6). {ECO:0000269|PubMed:19372223, ECO:0000269|PubMed:24463506, ECO:0000269|Ref.6}. EcoCyc product frame: EG11847-MONOMER. EcoCyc synonyms: squU. Genomic coordinates: 4072675-4073571.

## Biological Role

Repressed by csqR (protein.P32144). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00566` Sulfoquinovose metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9V8|protein.P0A9V8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yihU; function=+
- `represses` <-- [[protein.P32144|protein.P32144]] `RegulonDB` `S` - regulator=CsqR; target=yihU; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012678,ECOCYC:EG11847,GeneID:948372`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4072675-4073571:-; feature_type=gene
