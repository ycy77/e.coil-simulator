---
entity_id: "protein.P25536"
entity_type: "protein"
name: "yhdE"
source_database: "UniProt"
source_id: "P25536"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00528, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yhdE b3248 JW3217"
---

# yhdE

`protein.P25536`

## Static

- Type: `protein`
- Source: `UniProt:P25536`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00528, ECO:0000305}.

## Enriched Summary

FUNCTION: Nucleoside triphosphate pyrophosphatase that hydrolyzes dTTP and UTP (PubMed:24210219, PubMed:25658941, PubMed:28811554). Can also hydrolyze TTP and the modified nucleotides 5-methyl-UTP (m(5)UTP), pseudo-UTP and 5-methyl-CTP (m(5)CTP). Has weak activity with CTP (PubMed:24210219, PubMed:25658941). May have a dual role in cell division arrest and in preventing the incorporation of modified nucleotides into cellular nucleic acids (PubMed:24210219, PubMed:25658941). Important in maintenance of cell shape (PubMed:25658941). {ECO:0000269|PubMed:24210219, ECO:0000269|PubMed:25658941, ECO:0000269|PubMed:28811554}.

## Biological Role

Component of nucleoside triphosphate pyrophosphatase YhdE (complex.ecocyc.CPLX0-8106).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Nucleoside triphosphate pyrophosphatase that hydrolyzes dTTP and UTP (PubMed:24210219, PubMed:25658941, PubMed:28811554). Can also hydrolyze TTP and the modified nucleotides 5-methyl-UTP (m(5)UTP), pseudo-UTP and 5-methyl-CTP (m(5)CTP). Has weak activity with CTP (PubMed:24210219, PubMed:25658941). May have a dual role in cell division arrest and in preventing the incorporation of modified nucleotides into cellular nucleic acids (PubMed:24210219, PubMed:25658941). Important in maintenance of cell shape (PubMed:25658941). {ECO:0000269|PubMed:24210219, ECO:0000269|PubMed:25658941, ECO:0000269|PubMed:28811554}.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8106|complex.ecocyc.CPLX0-8106]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3248|gene.b3248]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25536`
- `KEGG:ecj:JW3217;eco:b3248;ecoc:C3026_17660;`
- `GeneID:947753;`
- `GO:GO:0005737; GO:0009117; GO:0030145; GO:0036218; GO:0036221; GO:0042802; GO:0042803; GO:0047429`
- `EC:3.6.1.9`

## Notes

dTTP/UTP pyrophosphatase (dTTPase/UTPase) (EC 3.6.1.9) (Nucleoside triphosphate pyrophosphatase) (Nucleotide pyrophosphatase) (Nucleotide PPase)
