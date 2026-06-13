---
entity_id: "gene.b3731"
entity_type: "gene"
name: "atpC"
source_database: "NCBI RefSeq"
source_id: "gene-b3731"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3731"
  - "atpC"
---

# atpC

`gene.b3731`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3731`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

atpC (gene.b3731) is a gene entity. It encodes atpC (protein.P0A6E6). Encoded protein function: FUNCTION: Produces ATP from ADP in the presence of a proton gradient across the membrane. EcoCyc product frame: ATPC-MONOMER. EcoCyc synonyms: papG, uncC. Genomic coordinates: 3915553-3915972. EcoCyc protein note: The epsilon subunit appears to play an important role in coupling the catalytic site events with proton translocation in association with the gamma subunit. The coupling involves conformational changes and probable translocations of one or both subunits. This subunit is also required for binding of the F1 complex to the Fo complex.

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6E6|protein.P0A6E6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=atpC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012206,ECOCYC:EG10100,GeneID:948245`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3915553-3915972:-; feature_type=gene
