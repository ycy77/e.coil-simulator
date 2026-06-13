---
entity_id: "protein.P0ACM2"
entity_type: "protein"
name: "rspR"
source_database: "UniProt"
source_id: "P0ACM2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rspR ydfH b1540 JW1533"
---

# rspR

`protein.P0ACM2`

## Static

- Type: `protein`
- Source: `UniProt:P0ACM2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Repressor of the rspAB operon. Acts by binding directly to the upstream region of rspA. {ECO:0000269|PubMed:22972332}. YdfH belongs to the GntR transcription factor family , for which the consensus sequence is reported to be tnGTnnnACna . Although only one site was determined in a gel shift assay, it is possible that YfdH binds as a complex of flanking regions of the core sequence (-65 to -50) . It was determined by Genomic SELEX screening that a site located upstream of rspAB is the only target of RspR . The RspR binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data . The resulting ChIP-seq binding regions are available in RegulonDB (Galagan collection), and the corresponding energy matrix and genomic binding profiles can be accessed at boltznet.bu.edu .

## Annotation

FUNCTION: Repressor of the rspAB operon. Acts by binding directly to the upstream region of rspA. {ECO:0000269|PubMed:22972332}.

## Outgoing Edges (2)

- `represses` --> [[gene.b1580|gene.b1580]] `RegulonDB` `S` - regulator=YdfH; target=rspB; function=-
- `represses` --> [[gene.b1581|gene.b1581]] `RegulonDB` `S` - regulator=YdfH; target=rspA; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1540|gene.b1540]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACM2`
- `KEGG:ecj:JW1533;eco:b1540;ecoc:C3026_08895;`
- `GeneID:93775704;946087;`
- `GO:GO:0000987; GO:0003677; GO:0003700; GO:0006355`

## Notes

HTH-type transcriptional repressor RspR
