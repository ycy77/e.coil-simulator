---
entity_id: "protein.P0ADC6"
entity_type: "protein"
name: "lptG"
source_database: "UniProt"
source_id: "P0ADC6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lptG yjgQ b4262 JW5760"
---

# lptG

`protein.P0ADC6`

## Static

- Type: `protein`
- Source: `UniProt:P0ADC6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex LptBFG involved in the translocation of lipopolysaccharide (LPS) from the inner membrane to the outer membrane. {ECO:0000269|PubMed:18375759}. LptG is an inner membrane component of the Lpt lipopolysaccharide transport system. LptG contains six predicted transmembrane domains and its C-terminus is located in the cytoplasm . lptG is essential in E.coli . Depletion of LptG results in increased outer membrane permeability and lipopolysaccharides do not reach the outer leaflet of the outer membrane . LptG forms a complex with LptF, LptB and LptC . LptG and LptF each contain a coupling helix which mediates their interaction with LptB; the LptFG coupling helices likely coordinate ATPase activity with LPS extraction from the inner membrane but each appears to have a distinct role (see further ). An LPS binding domain in LptG (which includes residues K34, D37, Q38, K40 and K41) has been identified .

## Biological Role

Component of lipopolysaccharide transport system (complex.ecocyc.CPLX0-7992).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex LptBFG involved in the translocation of lipopolysaccharide (LPS) from the inner membrane to the outer membrane. {ECO:0000269|PubMed:18375759}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7992|complex.ecocyc.CPLX0-7992]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4262|gene.b4262]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ADC6`
- `KEGG:ecj:JW5760;eco:b4262;ecoc:C3026_22990;`
- `GeneID:75169783;75203517;945324;`
- `GO:GO:0005886; GO:0015920; GO:0016020; GO:0043165; GO:0043190; GO:0055085; GO:1990351`

## Notes

Lipopolysaccharide export system permease protein LptG
