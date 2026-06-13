---
entity_id: "protein.P09053"
entity_type: "protein"
name: "avtA"
source_database: "UniProt"
source_id: "P09053"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "avtA b3572 JW5652"
---

# avtA

`protein.P09053`

## Static

- Type: `protein`
- Source: `UniProt:P09053`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}.

## Enriched Summary

FUNCTION: Involved in the biosynthesis of alanine. {ECO:0000269|PubMed:13034817, ECO:0000269|PubMed:20729367}. Valine-pyruvate aminotransferase (transaminase C) catalyzes the transamination reaction that converts α-keto-isovalerate to valine and alanine to pyruvate . This makes it the effective last step in potential synthetic routes to both alanine and valine. Transaminase C may also catalyze the interconversion of α-ketobutyrate and α-aminobutyrate . A homology model of the enzyme based on the crystal structure of AlaA has been generated . An ilvE avtA double mutant requires isoleucine and valine for growth . avtA is a multicopy suppressor of the isoleucine requirement of an ilvE mutant . An alaA avtA double mutant forms small colonies on agar plates. An alaA avtA alaC triple mutant has a slow growth phenotype in liquid medium. The defects of the double and triple mutants can be rescued by addition of alanine . Under competitive growth conditions in rich media, the ΔavtA mutation does not confer a disadvantage compared to wild type . AvtA expression is suppressed by excess alanine and leucine . AvtA: "alanine-valine transaminase"

## Biological Role

Catalyzes RXN0-5200 (reaction.ecocyc.RXN0-5200), VALINE-PYRUVATE-AMINOTRANSFER-RXN (reaction.ecocyc.VALINE-PYRUVATE-AMINOTRANSFER-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Enriched Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Involved in the biosynthesis of alanine. {ECO:0000269|PubMed:13034817, ECO:0000269|PubMed:20729367}.

## Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5200|reaction.ecocyc.RXN0-5200]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.VALINE-PYRUVATE-AMINOTRANSFER-RXN|reaction.ecocyc.VALINE-PYRUVATE-AMINOTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3572|gene.b3572]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09053`
- `KEGG:ecj:JW5652;eco:b3572;ecoc:C3026_19365;`
- `GeneID:948087;`
- `GO:GO:0005829; GO:0008483; GO:0009042; GO:0009099; GO:0030170; GO:0030632; GO:0042852; GO:1901605`
- `EC:2.6.1.66`

## Notes

Valine--pyruvate aminotransferase (EC 2.6.1.66) (Alanine--valine transaminase) (Transaminase C)
