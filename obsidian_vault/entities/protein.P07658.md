---
entity_id: "protein.P07658"
entity_type: "protein"
name: "fdhF"
source_database: "UniProt"
source_id: "P07658"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fdhF b4079 JW4040"
---

# fdhF

`protein.P07658`

## Static

- Type: `protein`
- Source: `UniProt:P07658`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Decomposes formic acid to hydrogen and carbon dioxide under anaerobic conditions in the absence of exogenous electron acceptors. Formate dehydrogenase-H is one of three membrane-associated formate dehydrogenase isoenzymes in E. coli . All are functional in the anaerobic metabolism of the organism. Formate dehydrogenase-H (FDH-H) is located in the cytoplasm and together with hydrogenase-3, FDH-H forms the formate-hydrogen lyase complex . FDH-H plays a role in the formate-dependent catabolism of urate . The enzyme is oxygen sensitive and contains selenium as selenocysteine incorporated cotranslationally at the position of an in-frame UGA stop codon in the FdhF open reading frame . fdhF mRNA contains a cis-acting element - the selenocysteine insertion sequence (SECIS) - which in combination with the specialized elongation factor CPLX0-8053 SelB is required for UGA-directed selenocysteine incorporation (and see ). A crystal structure of FDH-H has been solved at 2.3 Å resolution, confirming the presence of a [4Fe-4S] cluster, the coordination of molybdenum (Mo) to two molybdopterin guanine dinucleotide (MGD) cofactors and to selenium of selenocysteine (Sec-140), and the position of the binding site for the inhibitor nitrate...

## Biological Role

Catalyzes RXN0-3281 (reaction.ecocyc.RXN0-3281). Component of formate hydrogenlyase complex (complex.ecocyc.FHLMULTI-CPLX).

## Enriched Pathways

- `eco00680` Methane metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Decomposes formic acid to hydrogen and carbon dioxide under anaerobic conditions in the absence of exogenous electron acceptors.

## Pathways

- `eco00680` Methane metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-3281|reaction.ecocyc.RXN0-3281]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.FHLMULTI-CPLX|complex.ecocyc.FHLMULTI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4079|gene.b4079]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07658`
- `KEGG:ecj:JW4040;eco:b4079;`
- `GeneID:75169602;75203235;948584;`
- `GO:GO:0005829; GO:0006007; GO:0008863; GO:0009061; GO:0009326; GO:0015944; GO:0016020; GO:0016903; GO:0019628; GO:0019645; GO:0022904; GO:0043546; GO:0046872; GO:0051539`
- `EC:1.17.98.4`

## Notes

Formate dehydrogenase H (EC 1.17.98.4) (Formate dehydrogenase-H subunit alpha) (FDH-H) (Formate-hydrogen-lyase-linked, selenocysteine-containing polypeptide)
