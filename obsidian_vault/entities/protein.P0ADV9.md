---
entity_id: "protein.P0ADV9"
entity_type: "protein"
name: "lptC"
source_database: "UniProt"
source_id: "P0ADV9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01915, ECO:0000269|PubMed:18424520, ECO:0000269|PubMed:20720015}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01915, ECO:0000269|PubMed:18424520, ECO:0000269|PubMed:20720015}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lptC yrbK b3199 JW3166"
---

# lptC

`protein.P0ADV9`

## Static

- Type: `protein`
- Source: `UniProt:P0ADV9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01915, ECO:0000269|PubMed:18424520, ECO:0000269|PubMed:20720015}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01915, ECO:0000269|PubMed:18424520, ECO:0000269|PubMed:20720015}.

## Enriched Summary

FUNCTION: Involved in the assembly of lipopolysaccharide (LPS). Required for the translocation of LPS from the inner membrane to the outer membrane. Facilitates the transfer of LPS from the inner membrane to the periplasmic protein LptA. Could be a docking site for LptA. {ECO:0000255|HAMAP-Rule:MF_01915, ECO:0000269|PubMed:16765569, ECO:0000269|PubMed:18424520, ECO:0000269|PubMed:20720015, ECO:0000269|PubMed:21169485, ECO:0000269|PubMed:21195693}. LptC is a component of the Lpt lipopolysaccharide (LPS) transport system in E. coli K-12. lptC is essential for growth . Depletion of lptC leads to growth arrest and irreversible cell damage; sensitivity to SDS and bile salts indicates a defective outer membrane . LptC contains a single N-terminal membrane spanning domain and a large soluble periplasmic domain . LptC forms a complex with LptF, LptG and LptB ; LptC interacts with LptA . LptC lacking the transmembrane (TM) region is functional and can bind the LptBFG inner membrane complex . LptC binds rough and smooth LPS in vitro (see also ). LptA can displace LPS from the purified periplasmic domain of LptC in vitro but not vice versa . The soluble domain of LptC is a dimer in vitro . LptC inhibits the ATPase activity of LptB2FG complexes in vitro...

## Biological Role

Component of lipopolysaccharide transport system (complex.ecocyc.CPLX0-7992).

## Annotation

FUNCTION: Involved in the assembly of lipopolysaccharide (LPS). Required for the translocation of LPS from the inner membrane to the outer membrane. Facilitates the transfer of LPS from the inner membrane to the periplasmic protein LptA. Could be a docking site for LptA. {ECO:0000255|HAMAP-Rule:MF_01915, ECO:0000269|PubMed:16765569, ECO:0000269|PubMed:18424520, ECO:0000269|PubMed:20720015, ECO:0000269|PubMed:21169485, ECO:0000269|PubMed:21195693}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7992|complex.ecocyc.CPLX0-7992]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3199|gene.b3199]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ADV9`
- `KEGG:ecj:JW3166;eco:b3199;ecoc:C3026_17410;`
- `GeneID:75173373;75206055;947722;`
- `GO:GO:0005886; GO:0015221; GO:0015920; GO:0016020; GO:0017089; GO:0030288; GO:0042802; GO:0043165; GO:1990351`

## Notes

Lipopolysaccharide export system protein LptC
