---
entity_id: "gene.b0742"
entity_type: "gene"
name: "cpoB"
source_database: "NCBI RefSeq"
source_id: "gene-b0742"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0742"
  - "cpoB"
---

# cpoB

`gene.b0742`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0742`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cpoB (gene.b0742) is a gene entity. It encodes cpoB (protein.P45955). Encoded protein function: FUNCTION: Mediates coordination of peptidoglycan synthesis and outer membrane constriction during cell division. Promotes physical and functional coordination of the PBP1B-LpoB and Tol machines, and regulates PBP1B activity in response to Tol energy state. {ECO:0000269|PubMed:25951518}. EcoCyc product frame: EG12854-MONOMER. EcoCyc synonyms: ybgF. Genomic coordinates: 779598-780389. EcoCyc protein note: CpoB is a periplasmic protein that mediates physical and functional coordination between the peptidoglycan (PG) synthase CPLX0-3951 "PBP1B-LpoB" and the energy transducing Tol system; this coordination is required to properly synchronize PG synthesis and outer membrane (OM) constriction during cell division. CpoB, PBP1B-LpoB and the Tol proteins are recruited to the septum at the later stages of cell division and form a higher order complex that spatially links PG synthesis and OM invagination . CpoB interacts with TolA in vivo and in vitro . CpoB forms stable trimers in solution ; TolA binding disrupts trimeric CpoB to form CpoB-TolA heterodimers CpoB localizes to sites of envelope constriction in pre-divisional cellls; CpoB interacts with PBP1B in vivo; CpoB forms a ternery complex with TolA and PBP1B; CpoB forms a ternary compex with LpoB and PBP1B...

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45955|protein.P45955]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002523,ECOCYC:EG12854,GeneID:947227`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:779598-780389:+; feature_type=gene
