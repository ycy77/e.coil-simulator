---
entity_id: "gene.b3765"
entity_type: "gene"
name: "yifB"
source_database: "NCBI RefSeq"
source_id: "gene-b3765"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3765"
  - "yifB"
---

# yifB

`gene.b3765`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3765`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yifB (gene.b3765) is a gene entity. It encodes yifB (protein.P22787). Encoded protein function: Uncharacterized protein YifB EcoCyc product frame: EG11260-MONOMER. Genomic coordinates: 3948449-3949969. EcoCyc protein note: YifB belongs to the Helix 2 insert clade of the AAA+ ATPases. It contains an N-terminal Lon protease domain, which may function as an ATP-dependent protease, and a unique Zn2+ cluster inserted downstream of strand 4 of the AAA+ domain .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P22787|protein.P22787]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yifB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012300,ECOCYC:EG11260,GeneID:948282`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3948449-3949969:-; feature_type=gene
