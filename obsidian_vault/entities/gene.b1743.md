---
entity_id: "gene.b1743"
entity_type: "gene"
name: "spy"
source_database: "NCBI RefSeq"
source_id: "gene-b1743"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1743"
  - "spy"
---

# spy

`gene.b1743`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1743`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

spy (gene.b1743) is a gene entity. It encodes spy (protein.P77754). Encoded protein function: FUNCTION: An ATP-independent periplasmic chaperone, decreases protein aggregation and helps protein refolding. Binds substrate over a large region of its convex inner surface (PubMed:21317898, PubMed:24497545). Substrate protein folds while it is bound to chaperone (PubMed:26619265). Increasing Spy flexibility increases its substrate affinity and overall chaperone activity (shown for 3 different substrates) (PubMed:24497545). Protects proteins in vitro against tannin inactivation; tannins have antimicrobial activity (PubMed:21317898). Overexpression enhances the stability of otherwise unstable periplasmic proteins (PubMed:21317898). {ECO:0000269|PubMed:21317898, ECO:0000269|PubMed:24497545, ECO:0000269|PubMed:26619265}. EcoCyc product frame: G6939-MONOMER. Genomic coordinates: 1825140-1825625.

## Biological Role

Activated by rpoD (protein.P00579), cpxR (protein.P0AE88), baeR (protein.P69228).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77754|protein.P77754]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=spy; function=+
- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=spy; function=+
- `activates` <-- [[protein.P69228|protein.P69228]] `RegulonDB` `S` - regulator=BaeR; target=spy; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005812,ECOCYC:G6939,GeneID:946253`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1825140-1825625:-; feature_type=gene
