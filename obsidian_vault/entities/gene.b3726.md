---
entity_id: "gene.b3726"
entity_type: "gene"
name: "pstA"
source_database: "NCBI RefSeq"
source_id: "gene-b3726"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3726"
  - "pstA"
---

# pstA

`gene.b3726`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3726`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pstA (gene.b3726) is a gene entity. It encodes pstA (protein.P07654). Encoded protein function: FUNCTION: Part of the binding-protein-dependent transport system for phosphate; probably responsible for the translocation of the substrate across the membrane. EcoCyc product frame: PSTA-MONOMER. EcoCyc synonyms: R2pho, phoR2, phoR2b, phoT. Genomic coordinates: 3908549-3909439. EcoCyc protein note: PstA is one of two inner membrane subunits of an ATP-dependent high affinity phosphate uptake system. Protein topology in the inner membrane has been determined .

## Biological Role

Activated by rpoD (protein.P00579), phoB (protein.P0AFJ5), rpoS (protein.P13445).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07654|protein.P07654]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=pstA; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `C` - regulator=PhoB; target=pstA; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=pstA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012184,ECOCYC:EG10782,GeneID:948239`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3908549-3909439:-; feature_type=gene
