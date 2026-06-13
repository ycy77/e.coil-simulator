---
entity_id: "gene.b3509"
entity_type: "gene"
name: "hdeB"
source_database: "NCBI RefSeq"
source_id: "gene-b3509"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3509"
  - "hdeB"
---

# hdeB

`gene.b3509`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3509`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hdeB (gene.b3509) is a gene entity. It encodes hdeB (protein.P0AET2). Encoded protein function: FUNCTION: Required for optimal acid stress protection, which is important for survival of enteric bacteria in the acidic environment of the host stomach. Exhibits a chaperone-like activity at acidic pH by preventing the aggregation of many different periplasmic proteins. {ECO:0000255|HAMAP-Rule:MF_00947, ECO:0000269|PubMed:17085547}. EcoCyc product frame: EG11399-MONOMER. EcoCyc synonyms: yhiC, yhhD. Genomic coordinates: 3655966-3656292.

## Biological Role

Repressed by hns (protein.P0ACF8), marA (protein.P0ACH5), gadX (protein.P37639), fliZ (protein.P52627). Activated by rpoD (protein.P00579), rpoS (protein.P13445), phoP (protein.P23836), gadX (protein.P37639), gadE (protein.P63204).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AET2|protein.P0AET2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (9)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=hdeB; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=hdeB; function=+
- `activates` <-- [[protein.P23836|protein.P23836]] `RegulonDB` `S` - regulator=PhoP; target=hdeB; function=+
- `activates` <-- [[protein.P37639|protein.P37639]] `RegulonDB` `S` - regulator=GadX; target=hdeB; function=-+
- `activates` <-- [[protein.P63204|protein.P63204]] `RegulonDB` `S` - regulator=GadE; target=hdeB; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `C` - regulator=H-NS; target=hdeB; function=-
- `represses` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=hdeB; function=-
- `represses` <-- [[protein.P37639|protein.P37639]] `RegulonDB` `S` - regulator=GadX; target=hdeB; function=-+
- `represses` <-- [[protein.P52627|protein.P52627]] `RegulonDB` `S` - regulator=FliZ; target=hdeB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011458,ECOCYC:EG11399,GeneID:948026`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3655966-3656292:-; feature_type=gene
