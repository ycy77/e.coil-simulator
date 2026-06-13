---
entity_id: "gene.b1053"
entity_type: "gene"
name: "mdtG"
source_database: "NCBI RefSeq"
source_id: "gene-b1053"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1053"
  - "mdtG"
---

# mdtG

`gene.b1053`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1053`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mdtG (gene.b1053) is a gene entity. It encodes mdtG (protein.P25744). Encoded protein function: FUNCTION: Confers resistance to fosfomycin and deoxycholate. {ECO:0000269|PubMed:11566977}. EcoCyc product frame: YCEE-MONOMER. EcoCyc synonyms: yceE. Genomic coordinates: 1114264-1115490. EcoCyc protein note: Increased expression of mdtG in a K-12 strain which lacks the major efflux pump permease AcrB (E. coli KAM3; see ) results in a four-fold increase in resistance to fosfomycin and a two-fold increase in resistance to deoxycholate but does not impact the resistance to a range of other antibiotics and toxic compounds . MdtG (formerly YceE) is a member of the Drug:H+ Antiporter-1 (12 Spanner) (DHA1) family within the Major Facilitator Superfamily (MFS) . mdtG is a member of the marA-soxS-rob regulon; a SoxS binding marbox sequence is located within the mdtG promoter region; an mdtG-lacZ transcriptional fusion is induced in the presence of paraquat, sodium salicylate and 2,2'-dipyridyl . mdtG is one of 35 efflux-encoding genes that have been deleted or inactivated in 'Efflux KnockOut-35' (EKO-35) - a K-12 BW25133-derived strain that lacks 35 efflux pumps and can be used as a platform to study their function .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25744|protein.P25744]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=mdtG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003572,ECOCYC:EG11343,GeneID:945627`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1114264-1115490:-; feature_type=gene
