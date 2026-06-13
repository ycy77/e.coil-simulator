---
entity_id: "gene.b3261"
entity_type: "gene"
name: "fis"
source_database: "NCBI RefSeq"
source_id: "gene-b3261"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3261"
  - "fis"
---

# fis

`gene.b3261`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3261`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fis (gene.b3261) is a gene entity. It encodes fis (protein.P0A6R3). Encoded protein function: FUNCTION: Activates ribosomal RNA transcription, as well other genes. Plays a direct role in upstream activation of rRNA promoters. Binds to a recombinational enhancer sequence that is required to stimulate hin-mediated DNA inversion. Prevents initiation of DNA replication from oriC. Binds to hundreds of transcriptionally active and inactive AT-rich sites, approximately half its binding sites are in non-coding DNA, which only accounts for about 10% of the genome (PubMed:16963779). {ECO:0000269|PubMed:16963779, ECO:0000269|PubMed:2209559, ECO:0000269|PubMed:8836178}. EcoCyc product frame: PD00196. EcoCyc synonyms: nbp. Genomic coordinates: 3411271-3411567.

## Biological Role

Repressed by fis (protein.P0A6R3). Activated by rpoD (protein.P00579), rpsA (protein.P0AG67).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6R3|protein.P0A6R3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=fis; function=+
- `activates` <-- [[protein.P0AG67|protein.P0AG67]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=fis; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010703,ECOCYC:EG10317,GeneID:947697`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3411271-3411567:+; feature_type=gene
