---
entity_id: "protein.P28904"
entity_type: "protein"
name: "treC"
source_database: "UniProt"
source_id: "P28904"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:8083158}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "treC olgH b4239 JW4198"
---

# treC

`protein.P28904`

## Static

- Type: `protein`
- Source: `UniProt:P28904`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:8083158}.

## Enriched Summary

FUNCTION: Hydrolyzes trehalose-6-phosphate to glucose and glucose 6-phosphate. Can also very effectively hydrolyze p-nitrophenyl-alpha-D-glucopyranoside, but it does not recognize trehalose, sucrose, maltose, isomaltose, or maltodextrins. {ECO:0000269|PubMed:8083158}. E. coli can utilize trehalose as the sole source of carbon. Under low-osmolarity conditions, trehalose is imported into the cytoplasm by the trehalose-specific PTS transporter, converting it into trehalose-6-phoshate. Trehalose-6-phosphate hydrolase (TreC) then hydrolyzes trehalose-6-phosphate into glucose and glucose-6-phosphate . TreC may be able to catalyze the conversion of maltose to maltose-1-phosphate, which may act as an inducer of malK expression . Expression of TreC is induced by trehalose, but only under low-osmolarity conditions .

## Biological Role

Catalyzes alpha,alpha-trehalose-6-phosphate phosphoglucohydrolase (reaction.R00837), TRE6PHYDRO-RXN (reaction.ecocyc.TRE6PHYDRO-RXN).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Hydrolyzes trehalose-6-phosphate to glucose and glucose 6-phosphate. Can also very effectively hydrolyze p-nitrophenyl-alpha-D-glucopyranoside, but it does not recognize trehalose, sucrose, maltose, isomaltose, or maltodextrins. {ECO:0000269|PubMed:8083158}.

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00837|reaction.R00837]] `KEGG` `database` - via EC:3.2.1.93
- `catalyzes` --> [[reaction.ecocyc.TRE6PHYDRO-RXN|reaction.ecocyc.TRE6PHYDRO-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4239|gene.b4239]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P28904`
- `KEGG:ecj:JW4198;eco:b4239;ecoc:C3026_22880;`
- `GeneID:948762;`
- `GO:GO:0004556; GO:0005829; GO:0005993; GO:0006974; GO:0008788; GO:0009313`
- `EC:3.2.1.93`

## Notes

Trehalose-6-phosphate hydrolase (EC 3.2.1.93) (Alpha,alpha-phosphotrehalase)
