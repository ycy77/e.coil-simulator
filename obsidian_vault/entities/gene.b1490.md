---
entity_id: "gene.b1490"
entity_type: "gene"
name: "dosC"
source_database: "NCBI RefSeq"
source_id: "gene-b1490"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1490"
  - "dosC"
---

# dosC

`gene.b1490`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1490`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dosC (gene.b1490) is a gene entity. It encodes dosC (protein.P0AA89). Encoded protein function: FUNCTION: Globin-coupled heme-based oxygen sensor protein displaying diguanylate cyclase (DGC) activity in response to oxygen availability. Thus, catalyzes the synthesis of cyclic diguanylate (c-di-GMP) via the condensation of 2 GTP molecules. Is involved in the modulation of intracellular c-di-GMP levels, in association with DosP which catalyzes the degradation of c-di-GMP (PDE activity). Cyclic-di-GMP is a second messenger which controls cell surface-associated traits in bacteria. DosC regulates biofilm formation through the oxygen-dependent activation of the csgBAC operon, which encodes curli structural subunits, while not affecting the expression of the regulatory operon csgDEFG. DosC, but not the other DGCs in E.coli, also promotes the production of the exopolysaccharide poly-N-acetylglucosamine (PNAG) through up-regulation of the expression of the PNAG biosynthetic pgaABCD operon, independently of CsrA.; FUNCTION: Overexpression leads to an increased level of c-di-GMP, which leads to changes in the cell surface, to abnormal cell division, increased biofilm formation and decreased swimming (the latter 2 in strain W3110). In a strain able to produce cellulose (strain TOB1, a fecal isolate) overexpression leads to an increase in cellulose production...

## Biological Role

Repressed by hns (protein.P0ACF8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AA89|protein.P0AA89]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004965,ECOCYC:G6784,GeneID:945835`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1565758-1567140:-; feature_type=gene
