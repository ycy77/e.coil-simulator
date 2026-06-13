---
entity_id: "protein.P24183"
entity_type: "protein"
name: "fdnG"
source_database: "UniProt"
source_id: "P24183"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:11884747}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fdnG b1474 JW1470"
---

# fdnG

`protein.P24183`

## Static

- Type: `protein`
- Source: `UniProt:P24183`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:11884747}.

## Enriched Summary

FUNCTION: Formate dehydrogenase allows E.coli to use formate as major electron donor during anaerobic respiration, when nitrate is used as electron acceptor. The alpha subunit FdnG contains the formate oxidation site. Electrons are transferred from formate to menaquinone in the gamma subunit (FdnI), through the 4Fe-4S clusters in the beta subunit (FdnH). Formate dehydrogenase-N is part of a system that generates proton motive force, together with the dissimilatory nitrate reductase (Nar). {ECO:0000269|PubMed:11884747}. fdnG encodes the α subunit of formate dehydrogenase N (Fdh-N). The α subunit is the site of formate oxidation; it contains a CPD-15873 (bis-MGD) cofactor, a selenocysteine residue and a (4Fe-4S) cluster (FS0). Electrons are transferred from formate to the molybdenum cofactor and then passed to the β subunit possibly via the FS0 cluster . FdnG is translocated to the periplasm via the Tat system; interaction with the FdnI subunit localizes the protein to the periplasmic face of the cytoplasmic membrane . Production of FdnG is regulated at the translational level...

## Biological Role

Component of formate dehydrogenase N, subcomplex (complex.ecocyc.ALPHA-SUBUNIT-CPLX), formate dehydrogenase N (complex.ecocyc.FORMATEDEHYDROGN-CPLX).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Formate dehydrogenase allows E.coli to use formate as major electron donor during anaerobic respiration, when nitrate is used as electron acceptor. The alpha subunit FdnG contains the formate oxidation site. Electrons are transferred from formate to menaquinone in the gamma subunit (FdnI), through the 4Fe-4S clusters in the beta subunit (FdnH). Formate dehydrogenase-N is part of a system that generates proton motive force, together with the dissimilatory nitrate reductase (Nar). {ECO:0000269|PubMed:11884747}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.ALPHA-SUBUNIT-CPLX|complex.ecocyc.ALPHA-SUBUNIT-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.FORMATEDEHYDROGN-CPLX|complex.ecocyc.FORMATEDEHYDROGN-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b1474|gene.b1474]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24183`
- `KEGG:ecj:JW1470;eco:b1474;`
- `GeneID:946035;`
- `GO:GO:0006788; GO:0008430; GO:0008863; GO:0009055; GO:0009061; GO:0009326; GO:0015944; GO:0016020; GO:0019645; GO:0030151; GO:0030288; GO:0036397; GO:0043546; GO:0047111; GO:0051539`
- `EC:1.17.5.3`

## Notes

Formate dehydrogenase, nitrate-inducible, major subunit (EC 1.17.5.3) (Anaerobic formate dehydrogenase major subunit) (Formate dehydrogenase-N subunit alpha) (FDH-N subunit alpha)
