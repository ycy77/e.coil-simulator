---
entity_id: "protein.P0ABL5"
entity_type: "protein"
name: "napC"
source_database: "UniProt"
source_id: "P0ABL5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Single-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "napC yejX b2202 JW2190"
---

# napC

`protein.P0ABL5`

## Static

- Type: `protein`
- Source: `UniProt:P0ABL5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Single-pass membrane protein.

## Enriched Summary

FUNCTION: Mediates electron flow from quinones to the NapAB complex. The EG12060 gene encodes a membrane-bound tetraheme cytochrome c protein, which passes electrons either from menaquinone or from the CPLX0-3241 "NapGH ubiquinol-cytochrome c reductase complex" to the EG12061 NapB subunit of the NAP-CPLX "periplasmic nitrite reductase" . NapC is homologous to the G-55066 CymA protein of TAX-211586, which transfers electrons from menaquinol to a number of terminal oxidases. Heterologous expression of CymA in E. coli enabled growth with Fe(III) NTA as the terminal electron acceptor .

## Biological Role

Catalyzes RXN-25590 (reaction.ecocyc.RXN-25590).

## Annotation

FUNCTION: Mediates electron flow from quinones to the NapAB complex.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-25590|reaction.ecocyc.RXN-25590]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2202|gene.b2202]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABL5`
- `KEGG:ecj:JW2190;eco:b2202;ecoc:C3026_12305;`
- `GeneID:93774976;946706;`
- `GO:GO:0005886; GO:0009055; GO:0009061; GO:0019333; GO:0020037; GO:0046872`

## Notes

Cytochrome c-type protein NapC
