---
entity_id: "gene.b4156"
entity_type: "gene"
name: "yjeM"
source_database: "NCBI RefSeq"
source_id: "gene-b4156"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4156"
  - "yjeM"
---

# yjeM

`gene.b4156`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4156`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjeM (gene.b4156) is a gene entity. It encodes yjeM (protein.P39282). Encoded protein function: Inner membrane transporter YjeM EcoCyc product frame: YJEM-MONOMER. Genomic coordinates: 4383839-4385341. EcoCyc protein note: YjeM is an uncharacterized member of the Glutamate:GABA Antiporter (GGA) Family within the Amino Acid-Polyamine-Organocation (APC) Superfamily of transporters . YjeM is predicted to contain 12 transmembrane helices; the C-terminus is located in the cytoplasm .

## Biological Role

Repressed by lrp (protein.P0ACJ0), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39282|protein.P39282]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=yjeM; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yjeM; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013613,ECOCYC:EG12475,GeneID:948679`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4383839-4385341:+; feature_type=gene
