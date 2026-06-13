---
entity_id: "protein.P0ABL3"
entity_type: "protein"
name: "napB"
source_database: "UniProt"
source_id: "P0ABL3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:10234835, ECO:0000269|PubMed:10548535, ECO:0000269|PubMed:17130127}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "napB yejY b2203 JW5367"
---

# napB

`protein.P0ABL3`

## Static

- Type: `protein`
- Source: `UniProt:P0ABL3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:10234835, ECO:0000269|PubMed:10548535, ECO:0000269|PubMed:17130127}.

## Enriched Summary

FUNCTION: Electron transfer subunit of the periplasmic nitrate reductase complex NapAB. Receives electrons from the membrane-anchored tetraheme c-type NapC protein and transfers these to NapA subunit, thus allowing electron flow between membrane and periplasm. Essential for periplasmic nitrate reduction with nitrate as the terminal electron acceptor. {ECO:0000269|PubMed:10234835, ECO:0000269|PubMed:10548535, ECO:0000269|PubMed:17130127}. The EG12061 gene encodes the periplasmic diheme cytochrome c550 component of the periplasmic nitrate reductase. It receives electrons from the membrane-bound EG12060 NapC protein and passes them to the EG12067 NapA catalytic subunit (and see . E. coli NapA and NapB proteins do not purify as a heterodimeric complex .

## Biological Role

Component of periplasmic nitrate reductase (complex.ecocyc.NAP-CPLX).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)

## Annotation

FUNCTION: Electron transfer subunit of the periplasmic nitrate reductase complex NapAB. Receives electrons from the membrane-anchored tetraheme c-type NapC protein and transfers these to NapA subunit, thus allowing electron flow between membrane and periplasm. Essential for periplasmic nitrate reduction with nitrate as the terminal electron acceptor. {ECO:0000269|PubMed:10234835, ECO:0000269|PubMed:10548535, ECO:0000269|PubMed:17130127}.

## Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.NAP-CPLX|complex.ecocyc.NAP-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2203|gene.b2203]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABL3`
- `KEGG:ecj:JW5367;eco:b2203;ecoc:C3026_12310;`
- `GeneID:86947142;93774975;946698;`
- `GO:GO:0009061; GO:0009325; GO:0042128; GO:0042597; GO:0046872`

## Notes

Periplasmic nitrate reductase, electron transfer subunit (Diheme cytochrome c NapB)
