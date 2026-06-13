---
entity_id: "protein.P39361"
entity_type: "protein"
name: "sgcR"
source_database: "UniProt"
source_id: "P39361"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sgcR yjhJ b4300 JW4262"
---

# sgcR

`protein.P39361`

## Static

- Type: `protein`
- Source: `UniProt:P39361`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Putative transcriptional regulator for the sgcREAQCX region. SgcR, which contains a helix-turn-helix motif to bind DNA in its N-terminal domain, was predicted to regulate genes related to metabolism . Upstream of the sgcR gene, a sequence was found that could work as a transcriptional promoter, and the transcription of the sgcR gene is affected by glucose-lactose shift and glucose-acetate shift . The SgcR binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data . The resulting ChIP-seq binding regions are available in RegulonDB (Galagan collection), and the corresponding energy matrix and genomic binding profiles can be accessed at boltznet.bu.edu .

## Annotation

FUNCTION: Putative transcriptional regulator for the sgcREAQCX region.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b4300|gene.b4300]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39361`
- `KEGG:ecj:JW4262;eco:b4300;ecoc:C3026_23200;`
- `GeneID:946830;`
- `GO:GO:0000987; GO:0006355; GO:0098531`

## Notes

Putative sgc region transcriptional regulator
