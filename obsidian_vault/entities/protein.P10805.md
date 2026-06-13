---
entity_id: "protein.P10805"
entity_type: "protein"
name: "envY"
source_database: "UniProt"
source_id: "P10805"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "envY b0566 JW0555"
---

# envY

`protein.P10805`

## Static

- Type: `protein`
- Source: `UniProt:P10805`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Influences the temperature-dependent expression of several E.coli envelope proteins, most notably the porins OmpF and OmpC and the lambda receptor, LamB. EnvY is a DNA-binding transcriptional regulator that participates in the control of several genes that encode cellular envelope proteins at low temperatures and during stationary phase . This protein is an envelope protein that contains a putative membrane-spanning region, and as for the members of the family of transcriptional regulators (AraC/XylS) that it pertains to , it also contains a helix-turn-helix motif for DNA binding in the C-terminal region . The transcriptional regulators of E. coli that show higher similarity to EnvR are AppY and AdiY . The latter, like EnvY, also has a putative transmembrane region . No research has been done to determine the DNA-binding sites for EnvY. The regulation of envY has not been described yet, but a region of dyad symmetry has been found upstream of this gene . EnvY was transcriptionally upregulated in iron excess over iron limitation at 6.3% dissolved oxygen as determined by RNA-seq . The EnvY binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data...

## Annotation

FUNCTION: Influences the temperature-dependent expression of several E.coli envelope proteins, most notably the porins OmpF and OmpC and the lambda receptor, LamB.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b0566|gene.b0566]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P10805`
- `KEGG:ecj:JW0555;eco:b0566;ecoc:C3026_02810;`
- `GeneID:949114;`
- `GO:GO:0000976; GO:0003700; GO:0006355; GO:0009266; GO:0016020`

## Notes

Porin thermoregulatory protein EnvY
