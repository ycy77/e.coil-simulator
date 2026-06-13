---
entity_id: "gene.b3903"
entity_type: "gene"
name: "rhaA"
source_database: "NCBI RefSeq"
source_id: "gene-b3903"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3903"
  - "rhaA"
---

# rhaA

`gene.b3903`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3903`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rhaA (gene.b3903) is a gene entity. It encodes rhaA (protein.P32170). Encoded protein function: FUNCTION: Catalyzes the interconversion of L-rhamnose and L-rhamnulose (PubMed:14243758, PubMed:1650346, PubMed:2558952, PubMed:8564401). Can also catalyze the isomerization of L-lyxose to L-xylulose (PubMed:1650346). {ECO:0000269|PubMed:14243758, ECO:0000269|PubMed:1650346, ECO:0000269|PubMed:2558952, ECO:0000269|PubMed:8564401}. EcoCyc product frame: RHAMNISOM-MONOMER. Genomic coordinates: 4094723-4095982. EcoCyc protein note: L-rhamnose isomerase (RhaA) catalyzes the first step in the utilization of the deoxyhexose sugar rhamnose. L-rhamnose isomerase is also capable of using L-lyxose as a substrate . Conditioned on activation of LYXK-CPLX, RhaA contributes to E. coli's ability to metabolize the uncommon sugar, L-lyxose . Crystal structures of L-rhamnose isomerase have been determined. Despite low sequence similarity, the enzyme shows structural similarity to xylose isomerase from Streptomyces rubiginosus. The data suggests the possibility of a metal-mediated hydride shift reaction mechanism . Expression of rhaA is induced by L-rhamnose . L-lyxose can also induce expression of rhaA . rhaA mutants can not utilize rhamnose as a source of carbon .

## Biological Role

Activated by rpoD (protein.P00579), rhaS (protein.P09377), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32170|protein.P32170]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rhaA; function=+
- `activates` <-- [[protein.P09377|protein.P09377]] `RegulonDB` `C` - regulator=RhaS; target=rhaA; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=rhaA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012736,ECOCYC:EG11867,GeneID:948400`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4094723-4095982:-; feature_type=gene
