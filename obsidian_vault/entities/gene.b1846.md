---
entity_id: "gene.b1846"
entity_type: "gene"
name: "yebE"
source_database: "NCBI RefSeq"
source_id: "gene-b1846"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1846"
  - "yebE"
---

# yebE

`gene.b1846`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1846`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yebE (gene.b1846) is a gene entity. It encodes yebE (protein.P33218). Encoded protein function: Inner membrane protein YebE EcoCyc product frame: EG11806-MONOMER. Genomic coordinates: 1929048-1929707. EcoCyc protein note: YebE is an inner membrane protein with one predicted transmembrane domain. The C terminus is located in the cytoplasm . A meta-analysis of E. coli K-12 MG1655 transcriptomic data sets in response to multiple stressors found 15 uncharacterized or partially characterized genes (yqfA, yhfG, yhhA, ybgS, arpA, yqaE, yfdY, yaiY, yebE, ydiE, yjcB, yiiX, ycjF, yihF, yidX) that were upregulated under all five stressors: heat, cold, oxidative stress, nitrosative stress, and antibiotic treatment, whereas 3 uncharacterized or partially characterized genes (ymfI, ydiJ, yedE) that were downregulated under all but nitrosative stress .

## Biological Role

Activated by rpoD (protein.P00579), cpxR (protein.P0AE88).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33218|protein.P33218]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yebE; function=+
- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=yebE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006137,ECOCYC:EG11806,GeneID:946355`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1929048-1929707:-; feature_type=gene
