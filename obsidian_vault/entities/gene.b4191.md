---
entity_id: "gene.b4191"
entity_type: "gene"
name: "ulaR"
source_database: "NCBI RefSeq"
source_id: "gene-b4191"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4191"
  - "ulaR"
---

# ulaR

`gene.b4191`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4191`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ulaR (gene.b4191) is a gene entity. It encodes ulaR (protein.P0A9W0). Encoded protein function: FUNCTION: Represses ulaG and the ulaABCDEF operon. Two ulaR binding sites have been identified in each promoter. Full activity requires simultaneous interaction of UlaR with both divergent promoters and seems to be dependent on repressor-mediated DNA loop formation, which is helped by the action of integration host factor. {ECO:0000269|PubMed:12374842, ECO:0000269|PubMed:12644495, ECO:0000269|PubMed:14996803}. EcoCyc product frame: G7854-MONOMER. EcoCyc synonyms: yjfQ. Genomic coordinates: 4417698-4418453. EcoCyc protein note: UlaR is a DNA-binding transcription factor of 251 amino acids that is expressed constitutively and that coordinately represses transcription of a divergent operon (ula) involved in transport and utilization of L-ascorbate catabolism . Synthesis of these genes is induced when Escherichia coli is grown in the absence of glucose, and under anaerobic conditions it can ferment L-ascorbate; under aerobic conditions it is functional in the presence of casein acid hydrolysate . L-Ascorbate-6-P is the effector of the UlaR transcriptional repressor, and when this small molecule binds to UlaR, it severely impairs the formation of UlaR cognate operator sites, since they form a stable complex...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9W0|protein.P0A9W0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013713,ECOCYC:G7854,GeneID:948706`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4417698-4418453:-; feature_type=gene
