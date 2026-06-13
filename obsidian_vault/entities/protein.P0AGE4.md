---
entity_id: "protein.P0AGE4"
entity_type: "protein"
name: "sstT"
source_database: "UniProt"
source_id: "P0AGE4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01582, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01582}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sstT ygjU b3089 JW3060"
---

# sstT

`protein.P0AGE4`

## Static

- Type: `protein`
- Source: `UniProt:P0AGE4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01582, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01582}.

## Enriched Summary

FUNCTION: Involved in the import of serine and threonine into the cell, with the concomitant import of sodium (symport system). {ECO:0000255|HAMAP-Rule:MF_01582, ECO:0000269|PubMed:12097162, ECO:0000269|PubMed:9852024}. Early studies characterized a Na+-dependent serine-threonine transport system in the K-12 derived E. coli strain W3133-2 . Purified His-tagged SstT, reconstituted into liposomes mediates serine uptake which is dependent on an inwardly directed Na+ gradient and membrane potential . Serine transport in reconstituted proteoliposomes is inhibited by L-threonine, but not by other amino acids . In the Transporter Classification Database SstT is a member of the Dicarboxylate/Amino Acid:Cation Symporter (DAACS) Family.

## Biological Role

Catalyzes L-threonine:Na+ symport (reaction.ecocyc.RXN-22449), L-serine:Na+ symport (reaction.ecocyc.RXN0-4083). Transports L-Serine (molecule.C00065), L-Threonine (molecule.C00188), Sodium cation (molecule.C01330).

## Annotation

FUNCTION: Involved in the import of serine and threonine into the cell, with the concomitant import of sodium (symport system). {ECO:0000255|HAMAP-Rule:MF_01582, ECO:0000269|PubMed:12097162, ECO:0000269|PubMed:9852024}.

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.RXN-22449|reaction.ecocyc.RXN-22449]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-4083|reaction.ecocyc.RXN0-4083]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00188|molecule.C00188]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b3089|gene.b3089]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGE4`
- `KEGG:ecj:JW3060;eco:b3089;ecoc:C3026_16870;`
- `GeneID:93778898;947605;`
- `GO:GO:0005295; GO:0005886; GO:0006865; GO:0015175; GO:0015194; GO:0015195; GO:0015825; GO:0015826; GO:0032329`

## Notes

Serine/threonine transporter SstT (Na(+)/serine-threonine symporter)
