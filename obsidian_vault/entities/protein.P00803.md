---
entity_id: "protein.P00803"
entity_type: "protein"
name: "lepB"
source_database: "UniProt"
source_id: "P00803"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:21778229}; Multi-pass membrane protein {ECO:0000269|PubMed:21778229}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lepB b2568 JW2552"
---

# lepB

`protein.P00803`

## Static

- Type: `protein`
- Source: `UniProt:P00803`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:21778229}; Multi-pass membrane protein {ECO:0000269|PubMed:21778229}.

## Enriched Summary

Signal peptidase I (SPase I) (EC 3.4.21.89) (Leader peptidase I) Signal peptidase catalyzes the cleavage of the amino-terminal leader or signal peptide from membrane-tethered secretory pre-proteins . The action of signal peptidase releases the mature secretory protein into the periplasm and retains the signal peptide in the membrane where it is further degraded by the inner membrane protease EG12436-MONOMER "RseP". Signal peptidase cleaves pre-proteins translocated by both the general Sec-system and the twin-arginine translocation (Tat) system . Signal peptidase also cleaves the signal peptide from bacteriophage M13 procoat protein . Signal peptidase is required for import of the bacterial toxin, colicin D Signal peptidase has two N-terminal transmembrane segments separated by a small cytoplasmic domain and a large C-terminal catalytic domain that is located in the periplasm. The second transmembrane segment is believed to function as a non-cleavable signal sequence . A soluble form of leader peptidase which lacks residues 2-76 is catalytically active in vitro and has been crystallised on its own and in complex with inhibitors...

## Biological Role

Catalyzes 3.4.21.89-RXN (reaction.ecocyc.3.4.21.89-RXN).

## Enriched Pathways

- `eco03060` Protein export (KEGG)

## Annotation

Signal peptidase I (SPase I) (EC 3.4.21.89) (Leader peptidase I)

## Pathways

- `eco03060` Protein export (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.4.21.89-RXN|reaction.ecocyc.3.4.21.89-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2568|gene.b2568]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00803`
- `KEGG:ecj:JW2552;eco:b2568;ecoc:C3026_14225;`
- `GeneID:947040;`
- `GO:GO:0004175; GO:0004252; GO:0005886; GO:0006465; GO:0006508; GO:0008233; GO:0009003; GO:0016485`
- `EC:3.4.21.89`

## Notes

Signal peptidase I (SPase I) (EC 3.4.21.89) (Leader peptidase I)
