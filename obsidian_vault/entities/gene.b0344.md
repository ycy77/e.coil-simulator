---
entity_id: "gene.b0344"
entity_type: "gene"
name: "lacZ"
source_database: "NCBI RefSeq"
source_id: "gene-b0344"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0344"
  - "lacZ"
---

# lacZ

`gene.b0344`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0344`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lacZ (gene.b0344) is a gene entity. It encodes lacZ (protein.P00722). Encoded protein function: Beta-galactosidase (Beta-gal) (EC 3.2.1.23) (Lactase) EcoCyc product frame: BETAGALACTOSID-MONOMER. Genomic coordinates: 363231-366305.

## Biological Role

Repressed by lacI (protein.P03023), hns (protein.P0ACF8), marA (protein.P0ACH5), crp (protein.P0ACJ8). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00511` Other glycan degradation (KEGG)
- `eco00600` Sphingolipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00722|protein.P00722]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=lacZ; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=lacZ; function=-+
- `represses` <-- [[protein.P03023|protein.P03023]] `RegulonDB` `C` - regulator=LacI; target=lacZ; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=lacZ; function=-
- `represses` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `C` - regulator=MarA; target=lacZ; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=lacZ; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0001183,ECOCYC:EG10527,GeneID:945006`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:363231-366305:-; feature_type=gene
