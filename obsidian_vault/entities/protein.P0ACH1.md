---
entity_id: "protein.P0ACH1"
entity_type: "protein"
name: "sfsB"
source_database: "UniProt"
source_id: "P0ACH1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sfsB nlp sfs7 b3188 JW3155"
---

# sfsB

`protein.P0ACH1`

## Static

- Type: `protein`
- Source: `UniProt:P0ACH1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: This protein is involved in positive regulation of the metabolism of sugars. {ECO:0000250}. This regulator participates in controlling several genes involved in maltose metabolism . It is similar to the Ner repressor protein of phage Mu. SfsB is not essential for viability . The SfsB binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data . The resulting ChIP-seq binding regions are available in RegulonDB (Galagan collection), and the corresponding energy matrix and genomic binding profiles can be accessed at boltznet.bu.edu . SfsB: "sugar fermentation stimulation" Nlp: "Ner-like protein"

## Annotation

FUNCTION: This protein is involved in positive regulation of the metabolism of sugars. {ECO:0000250}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b3188|gene.b3188]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACH1`
- `KEGG:ecj:JW3155;eco:b3188;ecoc:C3026_17355;`
- `GeneID:86862415;93778793;947960;`
- `GO:GO:0003677`

## Notes

Sugar fermentation stimulation protein B (Ner-like protein)
