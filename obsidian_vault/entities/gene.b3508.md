---
entity_id: "gene.b3508"
entity_type: "gene"
name: "yhiD"
source_database: "NCBI RefSeq"
source_id: "gene-b3508"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3508"
  - "yhiD"
---

# yhiD

`gene.b3508`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3508`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhiD (gene.b3508) is a gene entity. It encodes yhiD (protein.P0AFV2). Encoded protein function: FUNCTION: Could be involved in magnesium uptake. {ECO:0000269|PubMed:19798051}. EcoCyc product frame: EG11400-MONOMER. EcoCyc synonyms: yhhE. Genomic coordinates: 3655255-3655902. EcoCyc protein note: yhiD, hdeD, or gadE mutants have reduced viability at high cell density (~108 CFU per mL) at pH 2.1 compared to wild-type .

## Biological Role

Repressed by hns (protein.P0ACF8), marA (protein.P0ACH5), gadX (protein.P37639), fliZ (protein.P52627), gadW (protein.P63201). Activated by rpoD (protein.P00579), rpoS (protein.P13445), phoP (protein.P23836), gadX (protein.P37639), gadW (protein.P63201), gadE (protein.P63204).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFV2|protein.P0AFV2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (11)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yhiD; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=yhiD; function=+
- `activates` <-- [[protein.P23836|protein.P23836]] `RegulonDB` `S` - regulator=PhoP; target=yhiD; function=+
- `activates` <-- [[protein.P37639|protein.P37639]] `RegulonDB` `S` - regulator=GadX; target=yhiD; function=-+
- `activates` <-- [[protein.P63201|protein.P63201]] `RegulonDB` `S` - regulator=GadW; target=yhiD; function=-+
- `activates` <-- [[protein.P63204|protein.P63204]] `RegulonDB` `C` - regulator=GadE; target=yhiD; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `C` - regulator=H-NS; target=yhiD; function=-
- `represses` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=yhiD; function=-
- `represses` <-- [[protein.P37639|protein.P37639]] `RegulonDB` `S` - regulator=GadX; target=yhiD; function=-+
- `represses` <-- [[protein.P52627|protein.P52627]] `RegulonDB` `S` - regulator=FliZ; target=yhiD; function=-
- `represses` <-- [[protein.P63201|protein.P63201]] `RegulonDB` `S` - regulator=GadW; target=yhiD; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0011456,ECOCYC:EG11400,GeneID:948019`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3655255-3655902:-; feature_type=gene
