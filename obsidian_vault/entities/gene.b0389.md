---
entity_id: "gene.b0389"
entity_type: "gene"
name: "yaiA"
source_database: "NCBI RefSeq"
source_id: "gene-b0389"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0389"
  - "yaiA"
---

# yaiA

`gene.b0389`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0389`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yaiA (gene.b0389) is a gene entity. It encodes yaiA (protein.P0AAN5). Encoded protein function: Uncharacterized protein YaiA EcoCyc product frame: EG11093-MONOMER. Genomic coordinates: 406979-407170. EcoCyc protein note: Expression of yaiA is induced by hydrogen peroxide; increased expression is partly dependent on OxyR .

## Biological Role

Repressed by tyrR (protein.P07604), trpR (protein.P0A881). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAN5|protein.P0AAN5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yaiA; function=+
- `represses` <-- [[protein.P07604|protein.P07604]] `RegulonDB` `C` - regulator=TyrR; target=yaiA; function=-
- `represses` <-- [[protein.P0A881|protein.P0A881]] `RegulonDB` `C` - regulator=TrpR; target=yaiA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001355,ECOCYC:EG11093,GeneID:945043`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:406979-407170:+; feature_type=gene
