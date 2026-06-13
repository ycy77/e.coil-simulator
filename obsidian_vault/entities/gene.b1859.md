---
entity_id: "gene.b1859"
entity_type: "gene"
name: "znuB"
source_database: "NCBI RefSeq"
source_id: "gene-b1859"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1859"
  - "znuB"
---

# znuB

`gene.b1859`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1859`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

znuB (gene.b1859) is a gene entity. It encodes znuB (protein.P39832). Encoded protein function: FUNCTION: Involved in the high-affinity zinc uptake transport system. EcoCyc product frame: ZNUB-MONOMER. EcoCyc synonyms: yebI. Genomic coordinates: 1943414-1944199. EcoCyc protein note: znuB encodes the predicted integral membrane subunit of an ATP-dependent Zn2+ uptake system znu: Zn2+ uptake

## Biological Role

Repressed by zur (protein.P0AC51). Activated by rpoD (protein.P00579), oxyR (protein.P0ACQ4).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39832|protein.P39832]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=znuB; function=+
- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `S` - regulator=OxyR; target=znuB; function=+
- `represses` <-- [[protein.P0AC51|protein.P0AC51]] `RegulonDB` `S` - regulator=Zur; target=znuB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006201,ECOCYC:EG12368,GeneID:946372`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1943414-1944199:+; feature_type=gene
