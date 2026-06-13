---
entity_id: "gene.b3117"
entity_type: "gene"
name: "tdcB"
source_database: "NCBI RefSeq"
source_id: "gene-b3117"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3117"
  - "tdcB"
---

# tdcB

`gene.b3117`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3117`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tdcB (gene.b3117) is a gene entity. It encodes tdcB (protein.P0AGF6). Encoded protein function: FUNCTION: Catalyzes the anaerobic formation of alpha-ketobutyrate and ammonia from threonine in a two-step reaction. The first step involved a dehydration of threonine and a production of enamine intermediates (aminocrotonate), which tautomerizes to its imine form (iminobutyrate). Both intermediates are unstable and short-lived. The second step is the nonenzymatic hydrolysis of the enamine/imine intermediates to form 2-ketobutyrate and free ammonia. In the low water environment of the cell, the second step is accelerated by RidA. TdcB also dehydrates serine to yield pyruvate via analogous enamine/imine intermediates. {ECO:0000269|PubMed:10388709, ECO:0000269|PubMed:13405870, ECO:0000269|PubMed:15390404}. EcoCyc product frame: THREDEHYDCAT-MONOMER. EcoCyc synonyms: tdc. Genomic coordinates: 3265039-3266028.

## Biological Role

Activated by crp (protein.P0ACJ8), tdcA (protein.P0ACQ7), tdcR (protein.P11866).

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

- `encodes` --> [[protein.P0AGF6|protein.P0AGF6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=tdcB; function=+
- `activates` <-- [[protein.P0ACQ7|protein.P0ACQ7]] `RegulonDB` `S` - regulator=TdcA; target=tdcB; function=+
- `activates` <-- [[protein.P11866|protein.P11866]] `RegulonDB` `S` - regulator=TdcR; target=tdcB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010249,ECOCYC:EG10990,GeneID:947633`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3265039-3266028:-; feature_type=gene
