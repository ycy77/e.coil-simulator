---
entity_id: "protein.P39288"
entity_type: "protein"
name: "queG"
source_database: "UniProt"
source_id: "P39288"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00916}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "queG yjeS b4166 JW4124"
---

# queG

`protein.P39288`

## Static

- Type: `protein`
- Source: `UniProt:P39288`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00916}.

## Enriched Summary

FUNCTION: Catalyzes the conversion of epoxyqueuosine (oQ) to queuosine (Q), which is a hypermodified base found in the wobble positions of tRNA(Asp), tRNA(Asn), tRNA(His) and tRNA(Tyr). {ECO:0000255|HAMAP-Rule:MF_00916}. Epoxyqueuosine reductase catalyzes the final step in the de novo synthesis of queuosine, the anticodon loop modification found in tRNA(Asp), tRNA(Asn), tRNA(His), and tRNA(Tyr) . The enzyme was identified by screening the Keio collection of single-gene knockouts for the presence of epoxyqueuosine (oQ) and lack of queuosine (Q) in tRNAs by tandem UV-visible spectrophotometry and mass spectroscopy .

## Biological Role

Catalyzes RXN-12104 (reaction.ecocyc.RXN-12104). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7), a cobamide (molecule.ecocyc.Cobamides).

## Annotation

FUNCTION: Catalyzes the conversion of epoxyqueuosine (oQ) to queuosine (Q), which is a hypermodified base found in the wobble positions of tRNA(Asp), tRNA(Asn), tRNA(His) and tRNA(Tyr). {ECO:0000255|HAMAP-Rule:MF_00916}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-12104|reaction.ecocyc.RXN-12104]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.Cobamides|molecule.ecocyc.Cobamides]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b4166|gene.b4166]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39288`
- `KEGG:ecj:JW4124;eco:b4166;ecoc:C3026_22515;`
- `GeneID:75202400;948686;`
- `GO:GO:0005737; GO:0008616; GO:0046872; GO:0051539; GO:0052693`
- `EC:1.17.99.6`

## Notes

Epoxyqueuosine reductase (EC 1.17.99.6) (Queuosine biosynthesis protein QueG)
