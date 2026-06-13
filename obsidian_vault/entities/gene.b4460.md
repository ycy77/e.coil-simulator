---
entity_id: "gene.b4460"
entity_type: "gene"
name: "araH"
source_database: "NCBI RefSeq"
source_id: "gene-b4460"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4460"
  - "araH"
---

# araH

`gene.b4460`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4460`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

araH (gene.b4460) is a gene entity. It encodes araH (protein.P0AE26). Encoded protein function: FUNCTION: Part of the binding-protein-dependent transport system for L-arabinose. Probably responsible for the translocation of the substrate across the membrane. EcoCyc product frame: ARAH-MONOMER. EcoCyc synonyms: b1898, b1899. Genomic coordinates: 1982554-1983540. EcoCyc protein note: araH is predicted to encode a hydrophobic protein

## Biological Role

Activated by rpoD (protein.P00579), araC (protein.P0A9E0), crp (protein.P0ACJ8), rpoS (protein.P13445).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE26|protein.P0AE26]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=araH; function=+
- `activates` <-- [[protein.P0A9E0|protein.P0A9E0]] `RegulonDB` `S` - regulator=AraC; target=araH; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=araH; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=araH; function=+

## External IDs

- `Dbxref:ASAP:ABE-0174093,ECOCYC:EG10059,GeneID:948923`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1982554-1983540:-; feature_type=gene
