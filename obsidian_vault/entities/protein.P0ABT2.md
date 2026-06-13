---
entity_id: "protein.P0ABT2"
entity_type: "protein"
name: "dps"
source_database: "UniProt"
source_id: "P0ABT2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm, nucleoid."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dps pexB vtm b0812 JW0797"
---

# dps

`protein.P0ABT2`

## Static

- Type: `protein`
- Source: `UniProt:P0ABT2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm, nucleoid.

## Enriched Summary

FUNCTION: During stationary phase, binds the chromosome non-specifically, forming a highly ordered and stable dps-DNA co-crystal within which chromosomal DNA is condensed and protected from diverse damages. It protects DNA from oxidative damage by sequestering intracellular Fe(2+) ion and storing it in the form of Fe(3+) oxyhydroxide mineral, which can be released after reduction. One hydrogen peroxide oxidizes two Fe(2+) ions, which prevents hydroxyl radical production by the Fenton reaction. Dps also protects the cell from UV and gamma irradiation, iron and copper toxicity, thermal stress and acid and base shocks. Also shows a weak catalase activity. {ECO:0000269|PubMed:10403254, ECO:0000269|PubMed:1340475, ECO:0000269|PubMed:15205421, ECO:0000269|PubMed:15534364}.

## Biological Role

Component of stationary phase nucleoid component that sequesters Fe and protects DNA from damage (complex.ecocyc.CPLX0-1521).

## Annotation

FUNCTION: During stationary phase, binds the chromosome non-specifically, forming a highly ordered and stable dps-DNA co-crystal within which chromosomal DNA is condensed and protected from diverse damages. It protects DNA from oxidative damage by sequestering intracellular Fe(2+) ion and storing it in the form of Fe(3+) oxyhydroxide mineral, which can be released after reduction. One hydrogen peroxide oxidizes two Fe(2+) ions, which prevents hydroxyl radical production by the Fenton reaction. Dps also protects the cell from UV and gamma irradiation, iron and copper toxicity, thermal stress and acid and base shocks. Also shows a weak catalase activity. {ECO:0000269|PubMed:10403254, ECO:0000269|PubMed:1340475, ECO:0000269|PubMed:15205421, ECO:0000269|PubMed:15534364}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1521|complex.ecocyc.CPLX0-1521]] `EcoCyc` `database` - EcoCyc component coefficient=12 | EcoCyc protcplxs.col coefficient=12

## Incoming Edges (1)

- `encodes` <-- [[gene.b0812|gene.b0812]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABT2`
- `KEGG:ecj:JW0797;eco:b0812;ecoc:C3026_05115;`
- `GeneID:86863322;93776616;945101;`
- `GO:GO:0003677; GO:0005737; GO:0006879; GO:0006950; GO:0008199; GO:0009295; GO:0016020; GO:0016722; GO:0030261; GO:0032297; GO:0042594; GO:0042802; GO:1990084`
- `EC:1.16.-.-`

## Notes

DNA protection during starvation protein (EC 1.16.-.-)
