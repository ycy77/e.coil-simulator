---
entity_id: "protein.P0AEK7"
entity_type: "protein"
name: "fdnI"
source_database: "UniProt"
source_id: "P0AEK7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:11884747}; Multi-pass membrane protein {ECO:0000269|PubMed:11884747}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fdnI b1476 JW1472"
---

# fdnI

`protein.P0AEK7`

## Static

- Type: `protein`
- Source: `UniProt:P0AEK7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:11884747}; Multi-pass membrane protein {ECO:0000269|PubMed:11884747}.

## Enriched Summary

FUNCTION: Formate dehydrogenase allows E.coli to use formate as major electron donor during anaerobic respiration, when nitrate is used as electron acceptor. Subunit gamma is the cytochrome b556 component of the formate dehydrogenase-N, and also contains a menaquinone reduction site that receives electrons from the beta subunit (FdnH), through its hemes. Formate dehydrogenase-N is part of a system that generates proton motive force, together with the dissimilatory nitrate reductase (Nar). {ECO:0000269|PubMed:11884747}. fdnI encodes the γ subunit of formate dehydrogenase-N (Fhd-N); it is an integral membrane protein with four transmembrane helices, which, together with the single transmembrane helix of FdnH and a cardiolipin molecule, form a tightly packed trimer in the inner membrane. The γ subunit contains two heme b groups - heme bP located towards the periplasmic side of the membrane and heme bC located towards the cytoplasmic face of the membrane - and a site for menaquinone reduction .

## Biological Role

Component of formate dehydrogenase N, subcomplex (complex.ecocyc.ALPHA-SUBUNIT-CPLX), formate dehydrogenase N (complex.ecocyc.FORMATEDEHYDROGN-CPLX).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Formate dehydrogenase allows E.coli to use formate as major electron donor during anaerobic respiration, when nitrate is used as electron acceptor. Subunit gamma is the cytochrome b556 component of the formate dehydrogenase-N, and also contains a menaquinone reduction site that receives electrons from the beta subunit (FdnH), through its hemes. Formate dehydrogenase-N is part of a system that generates proton motive force, together with the dissimilatory nitrate reductase (Nar). {ECO:0000269|PubMed:11884747}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.ALPHA-SUBUNIT-CPLX|complex.ecocyc.ALPHA-SUBUNIT-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.FORMATEDEHYDROGN-CPLX|complex.ecocyc.FORMATEDEHYDROGN-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b1476|gene.b1476]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEK7`
- `KEGG:ecj:JW1472;eco:b1476;ecoc:C3026_08560;`
- `GeneID:86859778;93775635;946038;`
- `GO:GO:0005886; GO:0006788; GO:0008863; GO:0009055; GO:0009061; GO:0009326; GO:0015944; GO:0016020; GO:0019645; GO:0020037; GO:0036397; GO:0046872`

## Notes

Formate dehydrogenase, nitrate-inducible, cytochrome b556(Fdn) subunit (Anaerobic formate dehydrogenase cytochrome b556 subunit) (Formate dehydrogenase-N subunit gamma) (FDH-N subunit gamma)
