---
entity_id: "gene.b2910"
entity_type: "gene"
name: "zapA"
source_database: "NCBI RefSeq"
source_id: "gene-b2910"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2910"
  - "zapA"
---

# zapA

`gene.b2910`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2910`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

zapA (gene.b2910) is a gene entity. It encodes zapA (protein.P0ADS2). Encoded protein function: FUNCTION: Activator of cell division through the inhibition of FtsZ GTPase activity, therefore promoting FtsZ assembly into bundles of protofilaments necessary for the formation of the division Z ring. It is recruited early at mid-cell but it is not essential for cell division. {ECO:0000269|PubMed:15060045}. EcoCyc product frame: EG12878-MONOMER. EcoCyc synonyms: ygfE. Genomic coordinates: 3055612-3055941. EcoCyc protein note: ZapA binds to FtsZ polymers and promotes the coherence of the Z-ring by cross-linking FtsZ polymers and stabilizing longitudinal interactions between FtsZ molecules . This effect is counteracted by ZapB . In the absence of functional Min and nucleoid exclusion (SlmA) systems, the MatP-ZapB-ZapA system positions the Z ring over the nucleoid in mid-cell . The protein network formed by the divisome proteins FtsZ, ZapA, ZapB and MatP has been studied using superresolution imaging, showing that these proteins form a multi-layered protein network that extends from the cell membrane to the chromosome and that stabilizes the FtsZ ring . The ZapA and ZapB proteins are able to form an FtsZ-independent structure at midcell which appears to provide positional information to FtsZ...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADS2|protein.P0ADS2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009554,ECOCYC:EG12878,GeneID:947404`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3055612-3055941:+; feature_type=gene
