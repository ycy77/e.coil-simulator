---
entity_id: "gene.b1620"
entity_type: "gene"
name: "malI"
source_database: "NCBI RefSeq"
source_id: "gene-b1620"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1620"
  - "malI"
---

# malI

`gene.b1620`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1620`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

malI (gene.b1620) is a gene entity. It encodes malI (protein.P18811). Encoded protein function: FUNCTION: Repressor for the malX and malY genes. Also regulates its own expression. Binds maltose as an inducer. {ECO:0000269|PubMed:1856179}. EcoCyc product frame: PD00361. Genomic coordinates: 1698152-1699180. EcoCyc protein note: "Maltose inhibitor," MalI, is a repressor that controls genes related to the maltose system. It is negatively autoregulated and coordinately represses transcription of a divergent operon that encodes a maltose-glucose PTS permease and a bifunctional protein that interacts directly with the MalT transcriptional activator . This transcription factor binds to two 12-bp-long direct repeat nucleotide sequences in tandem, overlapping the malXp and malIp simultaneously . MalI shows high similarity to GalR (28%), CytR (21%), and LacI (24%), and homology to a fragment of 30 amino acids from MalT. Additionally, the N-terminal region has a helix-turn-helix DNA-binding domain . The gene encoding this protein is homologous to transcriptional repressors of the LacI/GalR family. A negative correlation between cellular growth and the copy number of the proteins MalI has been reported .

## Biological Role

Repressed by crp (protein.P0ACJ8), malI (protein.P18811), nac (protein.Q47005). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P18811|protein.P18811]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=malI; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=malI; function=-+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=malI; function=-+
- `represses` <-- [[protein.P18811|protein.P18811]] `RegulonDB` `S` - regulator=MalI; target=malI; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=malI; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005421,ECOCYC:EG10557,GeneID:947104`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1698152-1699180:-; feature_type=gene
