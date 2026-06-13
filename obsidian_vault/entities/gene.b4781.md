---
entity_id: "gene.b4781"
entity_type: "gene"
name: "evgL"
source_database: "NCBI RefSeq"
source_id: "gene-b4781"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4781"
  - "evgL"
---

# evgL

`gene.b4781`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4781`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

evgL (gene.b4781) is a gene entity. It encodes evgL (protein.P0DSF9). Encoded protein function: Protein EvgL EcoCyc product frame: MONOMER0-4493. Genomic coordinates: 2483729-2483758. EcoCyc protein note: EvgL was identified as a previously unannotated small protein; its expression is higher during stationary phase than during exponential phase in rich media .

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by rpoD (protein.P00579), evgA (protein.P0ACZ4), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0DSF9|protein.P0DSF9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=evgL; function=+
- `activates` <-- [[protein.P0ACZ4|protein.P0ACZ4]] `RegulonDB` `S` - regulator=EvgA; target=evgL; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=evgL; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=evgL; function=-

## External IDs

- `Dbxref:ECOCYC:G0-17027,GeneID:63925643`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2483729-2483758:+; feature_type=gene
