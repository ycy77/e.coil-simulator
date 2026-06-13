---
entity_id: "protein.P0ABE5"
entity_type: "protein"
name: "cybB"
source_database: "UniProt"
source_id: "P0ABE5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:29915379, ECO:0000269|PubMed:3510204, ECO:0000269|PubMed:6097799}; Multi-pass membrane protein {ECO:0000269|PubMed:29915379}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cybB b1418 JW5224"
---

# cybB

`protein.P0ABE5`

## Static

- Type: `protein`
- Source: `UniProt:P0ABE5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:29915379, ECO:0000269|PubMed:3510204, ECO:0000269|PubMed:6097799}; Multi-pass membrane protein {ECO:0000269|PubMed:29915379}.

## Enriched Summary

FUNCTION: B-type di-heme cytochrome (PubMed:29915379, PubMed:3510204, PubMed:35671795). Catalyzes the oxidation of superoxide to molecular oxygen and transfers the extracted electrons to ubiquinone through the two hemes (PubMed:29915379, PubMed:35671795). Can also use menaquinone (PubMed:35671795). The enzyme may be responsible for the detoxification of the superoxide anion produced in the membrane or at its surface (PubMed:29915379). However, it can also efficiently catalyze the formation of superoxide from ubiquinol under physiological conditions (PubMed:35671795). {ECO:0000269|PubMed:29915379, ECO:0000269|PubMed:3510204, ECO:0000269|PubMed:35671795}. CybB or cytochrome b561 is a membrane bound superoxide:ubiquinone oxidoreductase which catalyses the direct oxidation of superoxide to oxygen concomitant with the reduction of ubiquinone to ubiquinol; the primary function of CybB may be to quench superoxide produced by respiratory chain enzymes in or at the membrane surface . CybB is a small inner membrane protein forming a four-helix bundle; it contains two b-type hemes, one of which has the edge of the porphyrin ring exposed to the periplasm...

## Biological Role

Catalyzes RXN-20148 (reaction.ecocyc.RXN-20148). Bound by Heme (molecule.C00032).

## Annotation

FUNCTION: B-type di-heme cytochrome (PubMed:29915379, PubMed:3510204, PubMed:35671795). Catalyzes the oxidation of superoxide to molecular oxygen and transfers the extracted electrons to ubiquinone through the two hemes (PubMed:29915379, PubMed:35671795). Can also use menaquinone (PubMed:35671795). The enzyme may be responsible for the detoxification of the superoxide anion produced in the membrane or at its surface (PubMed:29915379). However, it can also efficiently catalyze the formation of superoxide from ubiquinol under physiological conditions (PubMed:35671795). {ECO:0000269|PubMed:29915379, ECO:0000269|PubMed:3510204, ECO:0000269|PubMed:35671795}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-20148|reaction.ecocyc.RXN-20148]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00032|molecule.C00032]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1418|gene.b1418]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABE5`
- `KEGG:ecj:JW5224;eco:b1418;ecoc:C3026_08260;`
- `GeneID:947241;`
- `GO:GO:0005886; GO:0009055; GO:0016491; GO:0019430; GO:0020037; GO:0022904; GO:0046872`
- `EC:1.10.3.17`

## Notes

Superoxide oxidase CybB (SOO) (EC 1.10.3.17) (Cytochrome b-561) (Cytochrome b561) (Superoxide:quinone oxidoreductase) (Superoxide:ubiquinone oxidoreductase)
