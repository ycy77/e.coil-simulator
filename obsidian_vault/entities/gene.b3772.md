---
entity_id: "gene.b3772"
entity_type: "gene"
name: "ilvA"
source_database: "NCBI RefSeq"
source_id: "gene-b3772"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3772"
  - "ilvA"
---

# ilvA

`gene.b3772`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3772`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ilvA (gene.b3772) is a gene entity. It encodes ilvA (protein.P04968). Encoded protein function: FUNCTION: Catalyzes the anaerobic formation of alpha-ketobutyrate and ammonia from threonine in a two-step reaction. The first step involved a dehydration of threonine and a production of enamine intermediates (aminocrotonate), which tautomerizes to its imine form (iminobutyrate). Both intermediates are unstable and short-lived. The second step is the nonenzymatic hydrolysis of the enamine/imine intermediates to form 2-ketobutyrate and free ammonia. In the low water environment of the cell, the second step is accelerated by RidA. {ECO:0000269|PubMed:13405870}. EcoCyc product frame: THREDEHYDSYN-MONOMER. EcoCyc synonyms: ile. Genomic coordinates: 3955331-3956875.

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P04968|protein.P04968]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ilvA; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `C` - regulator=Lrp; target=ilvA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012321,ECOCYC:EG10493,GeneID:948287`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3955331-3956875:+; feature_type=gene
