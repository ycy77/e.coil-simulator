---
entity_id: "gene.b3356"
entity_type: "gene"
name: "yhfA"
source_database: "NCBI RefSeq"
source_id: "gene-b3356"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3356"
  - "yhfA"
---

# yhfA

`gene.b3356`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3356`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhfA (gene.b3356) is a gene entity. It encodes yhfA (protein.P0ADX1). Encoded protein function: Protein YhfA EcoCyc product frame: EG11182-MONOMER. Genomic coordinates: 3485414-3485818. EcoCyc protein note: No information about this protein was found by a literature search conducted on November 16 2018. Some published disagreement exists regarding a putative gene called crpT; some studies suggest that it may encode a small regulatory RNA, whereas other studies find that it is likely to be only the yhfA 5' untranslated leader sequence .

## Biological Role

Repressed by crp (protein.P0ACJ8). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADX1|protein.P0ADX1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yhfA; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=yhfA; function=-+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=yhfA; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0010964,ECOCYC:EG11182,GeneID:947860`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3485414-3485818:-; feature_type=gene
