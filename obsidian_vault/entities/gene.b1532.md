---
entity_id: "gene.b1532"
entity_type: "gene"
name: "marB"
source_database: "NCBI RefSeq"
source_id: "gene-b1532"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1532"
  - "marB"
---

# marB

`gene.b1532`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1532`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

marB (gene.b1532) is a gene entity. It encodes marB (protein.P31121). Encoded protein function: Multiple antibiotic resistance protein MarB EcoCyc product frame: EG11599-MONOMER. Genomic coordinates: 1619989-1620207. EcoCyc protein note: marB is part of the marRAB operon, which is known to have a role in multiple antibiotic resistance . MarB is located in the periplasm . Deletion of marB results in increased expression of marA .

## Biological Role

Repressed by cra (protein.P0ACP1), acrR (protein.P0ACS9), marR (protein.P27245). Activated by fis (protein.P0A6R3), soxS (protein.P0A9E2), marA (protein.P0ACH5), rob (protein.P0ACI0), cpxR (protein.P0AE88).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31121|protein.P31121]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (8)

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=marB; function=+
- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `S` - regulator=SoxS; target=marB; function=+
- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `C` - regulator=MarA; target=marB; function=+
- `activates` <-- [[protein.P0ACI0|protein.P0ACI0]] `RegulonDB` `C` - regulator=Rob; target=marB; function=+
- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=marB; function=+
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=marB; function=-
- `represses` <-- [[protein.P0ACS9|protein.P0ACS9]] `RegulonDB` `S` - regulator=AcrR; target=marB; function=-
- `represses` <-- [[protein.P27245|protein.P27245]] `RegulonDB` `C` - regulator=MarR; target=marB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005114,ECOCYC:EG11599,GeneID:946184`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1619989-1620207:+; feature_type=gene
