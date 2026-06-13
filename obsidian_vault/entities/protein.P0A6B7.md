---
entity_id: "protein.P0A6B7"
entity_type: "protein"
name: "iscS"
source_database: "UniProt"
source_id: "P0A6B7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00331, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "iscS nuvC yfhO yzzO b2530 JW2514"
---

# iscS

`protein.P0A6B7`

## Static

- Type: `protein`
- Source: `UniProt:P0A6B7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00331, ECO:0000305}.

## Enriched Summary

FUNCTION: Master enzyme that delivers sulfur to a number of partners involved in Fe-S cluster assembly, tRNA modification or cofactor biosynthesis. Catalyzes the removal of elemental sulfur from cysteine to produce alanine. Functions as a sulfur delivery protein for Fe-S cluster synthesis onto IscU, an Fe-S scaffold assembly protein, as well as other S acceptor proteins. Preferentially binds to disordered IscU on which the Fe-S is assembled, IscU converts to the structured state and then dissociates from IscS to transfer the Fe-S to an acceptor protein. Also functions as a selenium delivery protein in the pathway for the biosynthesis of selenophosphate. Transfers sulfur onto 'Cys-456' of ThiI and onto 'Cys-19' of TusA in transpersulfidation reactions. {ECO:0000269|PubMed:10544286, ECO:0000269|PubMed:10600118, ECO:0000269|PubMed:10781558, ECO:0000269|PubMed:10781607, ECO:0000269|PubMed:10829016, ECO:0000269|PubMed:10908675, ECO:0000269|PubMed:11577100, ECO:0000269|PubMed:16387657, ECO:0000269|PubMed:22203963, ECO:0000269|PubMed:8663056}.

## Biological Role

Catalyzes L-cysteine:sulfur-acceptor sulfurtransferase (reaction.R11528). Component of IscS:TusA sulfurtransferase (complex.ecocyc.CPLX0-12610), cysteine desulfurase IscS (complex.ecocyc.CPLX0-248).

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Annotation

FUNCTION: Master enzyme that delivers sulfur to a number of partners involved in Fe-S cluster assembly, tRNA modification or cofactor biosynthesis. Catalyzes the removal of elemental sulfur from cysteine to produce alanine. Functions as a sulfur delivery protein for Fe-S cluster synthesis onto IscU, an Fe-S scaffold assembly protein, as well as other S acceptor proteins. Preferentially binds to disordered IscU on which the Fe-S is assembled, IscU converts to the structured state and then dissociates from IscS to transfer the Fe-S to an acceptor protein. Also functions as a selenium delivery protein in the pathway for the biosynthesis of selenophosphate. Transfers sulfur onto 'Cys-456' of ThiI and onto 'Cys-19' of TusA in transpersulfidation reactions. {ECO:0000269|PubMed:10544286, ECO:0000269|PubMed:10600118, ECO:0000269|PubMed:10781558, ECO:0000269|PubMed:10781607, ECO:0000269|PubMed:10829016, ECO:0000269|PubMed:10908675, ECO:0000269|PubMed:11577100, ECO:0000269|PubMed:16387657, ECO:0000269|PubMed:22203963, ECO:0000269|PubMed:8663056}.

## Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R11528|reaction.R11528]] `KEGG` `database` - via EC:2.8.1.7
- `is_component_of` --> [[complex.ecocyc.CPLX0-12610|complex.ecocyc.CPLX0-12610]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-248|complex.ecocyc.CPLX0-248]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2530|gene.b2530]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6B7`
- `KEGG:ecj:JW2514;eco:b2530;ecoc:C3026_14020;`
- `GeneID:86860656;93774606;947004;`
- `GO:GO:0002143; GO:0002937; GO:0005829; GO:0009000; GO:0009228; GO:0009589; GO:0016226; GO:0016261; GO:0019448; GO:0030170; GO:0031071; GO:0044571; GO:0046872; GO:0051537; GO:0072348; GO:0097163; GO:1990221; GO:1990228; GO:1990329; GO:1990330`
- `EC:2.8.1.7`

## Notes

Cysteine desulfurase IscS (EC 2.8.1.7) (NifS protein homolog) (ThiI transpersulfidase) (TusA transpersulfidase)
