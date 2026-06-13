---
entity_id: "gene.b2788"
entity_type: "gene"
name: "gudX"
source_database: "NCBI RefSeq"
source_id: "gene-b2788"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2788"
  - "gudX"
---

# gudX

`gene.b2788`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2788`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gudX (gene.b2788) is a gene entity. It encodes gudX (protein.Q46915). Encoded protein function: FUNCTION: Does not seem to have an in-vivo activity on glucarate or idarate. Its real substrate is unknown. EcoCyc product frame: G7446-MONOMER. EcoCyc synonyms: ygcY. Genomic coordinates: 2919406-2920746. EcoCyc protein note: GudX (GlucD-related protein, GlucDRP) has similarity to the functional D-glucarate dehydratase, GudD, which is encoded in a probable operon downstream of gudX. Purified GudX has only very weak D-glucarate dehydratase and L-idarate epimerase activity; a physiological substrate has not been identified .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46915|protein.Q46915]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=gudX; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009136,ECOCYC:G7446,GeneID:947261`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2919406-2920746:-; feature_type=gene
