---
entity_id: "protein.P0AAJ3"
entity_type: "protein"
name: "fdnH"
source_database: "UniProt"
source_id: "P0AAJ3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:11884747}; Single-pass membrane protein {ECO:0000269|PubMed:11884747}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fdnH b1475 JW1471"
---

# fdnH

`protein.P0AAJ3`

## Static

- Type: `protein`
- Source: `UniProt:P0AAJ3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:11884747}; Single-pass membrane protein {ECO:0000269|PubMed:11884747}.

## Enriched Summary

FUNCTION: Formate dehydrogenase allows E.coli to use formate as major electron donor during anaerobic respiration, when nitrate is used as electron acceptor. The beta subunit FdnH is an electron transfer unit containing 4 iron-sulfur clusters; it serves as a conduit for electrons that are transferred from the formate oxidation site in the alpha subunit (FdnG) to the menaquinone associated with the gamma subunit (FdnI) of formate dehydrogenase-N. Formate dehydrogenase-N is part of a system that generates proton motive force, together with the dissimilatory nitrate reductase (Nar). {ECO:0000269|PubMed:11884747}. fdnH encodes the β subunit of formate dehydrogenase N (Fdh-N); it contains four [4Fe-4S] clusters (FS1, FS2, FS3 and FS4) and one C-terminal transmembrane helix . FdnH serves as a conduit for electrons that are transferred from the formate oxidation site in the α subunit (FdnG) to the menaquinone associated with the γ subunit (FdnI) . FdnH is a putative C-tail-anchored (TA) membrane protein .

## Biological Role

Component of formate dehydrogenase N, subcomplex (complex.ecocyc.ALPHA-SUBUNIT-CPLX), formate dehydrogenase N (complex.ecocyc.FORMATEDEHYDROGN-CPLX).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Formate dehydrogenase allows E.coli to use formate as major electron donor during anaerobic respiration, when nitrate is used as electron acceptor. The beta subunit FdnH is an electron transfer unit containing 4 iron-sulfur clusters; it serves as a conduit for electrons that are transferred from the formate oxidation site in the alpha subunit (FdnG) to the menaquinone associated with the gamma subunit (FdnI) of formate dehydrogenase-N. Formate dehydrogenase-N is part of a system that generates proton motive force, together with the dissimilatory nitrate reductase (Nar). {ECO:0000269|PubMed:11884747}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.ALPHA-SUBUNIT-CPLX|complex.ecocyc.ALPHA-SUBUNIT-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.FORMATEDEHYDROGN-CPLX|complex.ecocyc.FORMATEDEHYDROGN-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b1475|gene.b1475]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAJ3`
- `KEGG:ecj:JW1471;eco:b1475;ecoc:C3026_08555;`
- `GeneID:86859779;948794;`
- `GO:GO:0005886; GO:0006788; GO:0009055; GO:0009061; GO:0009326; GO:0015944; GO:0016020; GO:0019645; GO:0036397; GO:0046872; GO:0051539`

## Notes

Formate dehydrogenase, nitrate-inducible, iron-sulfur subunit (Anaerobic formate dehydrogenase iron-sulfur subunit) (Formate dehydrogenase-N subunit beta) (FDH-N subunit beta)
