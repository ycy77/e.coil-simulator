---
entity_id: "gene.b2420"
entity_type: "gene"
name: "yfeS"
source_database: "NCBI RefSeq"
source_id: "gene-b2420"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2420"
  - "yfeS"
---

# yfeS

`gene.b2420`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2420`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfeS (gene.b2420) is a gene entity. It encodes yfeS (protein.P78271). Encoded protein function: Uncharacterized protein YfeS EcoCyc product frame: G7261-MONOMER. Genomic coordinates: 2537749-2538483. EcoCyc protein note: A knockout mutant of this gene was sensitive to boric acid exposure; a complementation assay restored its intrinsic boric acid resistance. Double and triple knockout mutants (ΔG6253ΔEG12760ΔyfeS, ΔG6994ΔyfeS and ΔyfeSΔyoaCΔgarP) exhibited increasing sensitivity, respectively .

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P78271|protein.P78271]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=yfeS; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yfeS; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007979,ECOCYC:G7261,GeneID:946887`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2537749-2538483:+; feature_type=gene
