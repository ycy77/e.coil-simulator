---
entity_id: "gene.b2571"
entity_type: "gene"
name: "rseB"
source_database: "NCBI RefSeq"
source_id: "gene-b2571"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2571"
  - "rseB"
---

# rseB

`gene.b2571`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2571`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rseB (gene.b2571) is a gene entity. It encodes rseB (protein.P0AFX9). Encoded protein function: FUNCTION: Negatively modulates the activity of sigma-E (RpoE) by stabilizing RseA under non-stress conditions. Although not essential for association of sigma-E with Rsea it increases their affinity 2- to 3-fold. When bound to RseA it prevents proteolysis by DegS, which is probably relieved by lipopolysaccharide binding (LPS). {ECO:0000269|PubMed:10500101, ECO:0000269|PubMed:17360428, ECO:0000269|PubMed:21245315, ECO:0000269|PubMed:23687042, ECO:0000269|PubMed:9159522, ECO:0000269|PubMed:9159523}. EcoCyc product frame: G7348-MONOMER. Genomic coordinates: 2707798-2708754.

## Biological Role

Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), glnG (protein.P0AFB8), glrR (protein.P0AFU4), rpoE (protein.P0AGB6), rcsB (protein.P0DMC7), rpoS (protein.P13445), rpoN (protein.P24255).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFX9|protein.P0AFX9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (8)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rseB; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=rseB; function=+
- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=rseB; function=+
- `activates` <-- [[protein.P0AFU4|protein.P0AFU4]] `RegulonDB` `S` - regulator=GlrR; target=rseB; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=rseB; function=+
- `activates` <-- [[protein.P0DMC7|protein.P0DMC7]] `RegulonDB` `C` - regulator=RcsB; target=rseB; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=rseB; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=rseB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008459,ECOCYC:G7348,GeneID:947054`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2707798-2708754:-; feature_type=gene
