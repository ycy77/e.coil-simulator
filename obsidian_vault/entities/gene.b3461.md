---
entity_id: "gene.b3461"
entity_type: "gene"
name: "rpoH"
source_database: "NCBI RefSeq"
source_id: "gene-b3461"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3461"
  - "rpoH"
---

# rpoH

`gene.b3461`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3461`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpoH (gene.b3461) is a gene entity. It encodes rpoH (protein.P0AGB3). Encoded protein function: FUNCTION: Sigma factors are initiation factors that promote the attachment of RNA polymerase to specific initiation sites and are then released. This sigma factor is involved in regulation of expression of heat shock genes. Intracellular concentration of free RpoH protein increases in response to heat shock, which causes association with RNA polymerase (RNAP) and initiation of transcription of heat shock genes, including numerous global transcriptional regulators and genes involved in maintaining membrane functionality and homeostasis. RpoH is then quickly degraded, leading to a decrease in the rate of synthesis of heat shock proteins and shut-off of the heat shock response. {ECO:0000255|HAMAP-Rule:MF_00961, ECO:0000269|PubMed:15757896, ECO:0000269|PubMed:16818608, ECO:0000269|PubMed:3306410, ECO:0000269|PubMed:3315848, ECO:0000269|PubMed:6387714}. EcoCyc product frame: RPOH-MONOMER. EcoCyc synonyms: fam, hin, htpR. Genomic coordinates: 3599929-3600783. EcoCyc protein note: rpoH encodes σ32, the primary sigma factor controlling the heat shock response during log-phase growth. It is subject to tight control via a multivalent regulatory system that reponds to temperature and the abundance of misfolded proteins within the cell...

## Biological Role

Repressed by crp (protein.P0ACJ8), cytR (protein.P0ACN7). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), rpoE (protein.P0AGB6), rpoS (protein.P13445), zraR (protein.P14375), rpoN (protein.P24255).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGB3|protein.P0AGB3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (8)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rpoH; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=rpoH; function=-+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=rpoH; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=rpoH; function=+
- `activates` <-- [[protein.P14375|protein.P14375]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=rpoH; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `C` - sigma=sigma54; target=rpoH; function=+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=rpoH; function=-+
- `represses` <-- [[protein.P0ACN7|protein.P0ACN7]] `RegulonDB` `S` - regulator=CytR; target=rpoH; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011303,ECOCYC:EG10897,GeneID:947970`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3599929-3600783:-; feature_type=gene
