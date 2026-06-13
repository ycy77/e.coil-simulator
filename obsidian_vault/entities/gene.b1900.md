---
entity_id: "gene.b1900"
entity_type: "gene"
name: "araG"
source_database: "NCBI RefSeq"
source_id: "gene-b1900"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1900"
  - "araG"
---

# araG

`gene.b1900`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1900`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

araG (gene.b1900) is a gene entity. It encodes araG (protein.P0AAF3). Encoded protein function: FUNCTION: Part of the ABC transporter complex AraFGH involved in arabinose import. Responsible for energy coupling to the transport system (Probable). {ECO:0000305|PubMed:2656640, ECO:0000305|PubMed:7028715}. EcoCyc product frame: ARAG-MONOMER. Genomic coordinates: 1983555-1985069. EcoCyc protein note: araG is predicted to encode a soluble protein. Sequence analysis indicates the presence of putative ATP binding sites .

## Biological Role

Activated by rpoD (protein.P00579), araC (protein.P0A9E0), crp (protein.P0ACJ8), rpoS (protein.P13445).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAF3|protein.P0AAF3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=araG; function=+
- `activates` <-- [[protein.P0A9E0|protein.P0A9E0]] `RegulonDB` `C` - regulator=AraC; target=araG; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=araG; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=araG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006328,ECOCYC:EG10058,GeneID:946408`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1983555-1985069:-; feature_type=gene
