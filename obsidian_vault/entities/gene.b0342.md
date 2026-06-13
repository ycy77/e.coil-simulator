---
entity_id: "gene.b0342"
entity_type: "gene"
name: "lacA"
source_database: "NCBI RefSeq"
source_id: "gene-b0342"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0342"
  - "lacA"
---

# lacA

`gene.b0342`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0342`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lacA (gene.b0342) is a gene entity. It encodes lacA (protein.P07464). Encoded protein function: FUNCTION: Catalyzes the CoA-dependent transfer of an acetyl group to the 6-O-methyl position of a range of galactosides, glucosides, and lactosides (PubMed:14009486, PubMed:4630409, PubMed:7592843). May assist cellular detoxification by acetylating non-metabolizable pyranosides, thereby preventing their reentry into the cell (Probable). {ECO:0000269|PubMed:14009486, ECO:0000269|PubMed:4630409, ECO:0000269|PubMed:7592843, ECO:0000305|PubMed:11937062}. EcoCyc product frame: GALACTOACETYLTRAN-MONOMER. Genomic coordinates: 361249-361860.

## Biological Role

Repressed by lacI (protein.P03023), hns (protein.P0ACF8), marA (protein.P0ACH5), crp (protein.P0ACJ8). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07464|protein.P07464]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=lacA; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=lacA; function=-+
- `represses` <-- [[protein.P03023|protein.P03023]] `RegulonDB` `C` - regulator=LacI; target=lacA; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=lacA; function=-
- `represses` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `C` - regulator=MarA; target=lacA; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=lacA; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0001177,ECOCYC:EG10524,GeneID:945674`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:361249-361860:-; feature_type=gene
