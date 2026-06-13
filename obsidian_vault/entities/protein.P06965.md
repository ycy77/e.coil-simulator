---
entity_id: "protein.P06965"
entity_type: "protein"
name: "dicC"
source_database: "UniProt"
source_id: "P06965"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dicC b1569 JW1561"
---

# dicC

`protein.P06965`

## Static

- Type: `protein`
- Source: `UniProt:P06965`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: This protein is a repressor of division inhibition gene dicB. DicC has similarity to the bacteriophage P22 Cro transcriptional regulator. The organization of the dicAC locus is similar to the P22 immunity region. In the dicA1 mutant, expression of the dicAC locus appears to be under the control of DicC . Overexpression of dicC from a multicopy plasmid can complement the cell division phenotype of the dicA1 mutant . Expression of dicC is repressed by DicA . The DicC binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data . The resulting ChIP-seq binding regions are available in RegulonDB (Galagan collection), and the corresponding energy matrix and genomic binding profiles can be accessed at boltznet.bu.edu . DicC: "division control C"

## Annotation

FUNCTION: This protein is a repressor of division inhibition gene dicB.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b1569|gene.b1569]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06965`
- `KEGG:ecj:JW1561;eco:b1569;ecoc:C3026_09045;`
- `GeneID:946120;`
- `GO:GO:0003677; GO:0006355; GO:0051301`

## Notes

Repressor protein of division inhibition gene dicB
