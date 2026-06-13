---
entity_id: "protein.P69922"
entity_type: "protein"
name: "fucI"
source_database: "UniProt"
source_id: "P69922"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fucI b2802 JW2773"
---

# fucI

`protein.P69922`

## Static

- Type: `protein`
- Source: `UniProt:P69922`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Converts the aldose L-fucose into the corresponding ketose L-fuculose (PubMed:13319278, PubMed:4632320, PubMed:4928018, PubMed:8564401, PubMed:9367760). Also converts D-arabinose into D-ribulose (PubMed:13319278, PubMed:4632320, PubMed:4928018). In addition, catalyzes the isomerization of L-xylulose to L-xylose (PubMed:22133443). {ECO:0000269|PubMed:13319278, ECO:0000269|PubMed:22133443, ECO:0000269|PubMed:4632320, ECO:0000269|PubMed:4928018, ECO:0000269|PubMed:8564401, ECO:0000269|PubMed:9367760}. FucI can function as both an L-fucose isomerase and a D-arabinose isomerase, the first enzymes of the L-fucose and D-arabinose degradation pathways, respectively. However, production of FucI is only induced by L-fucose . Between the two anomers of L-fucose,only the α-form adopts a position suitable for the ring opening reaction . A crystal structure of the enzyme has been solved at 2.5 Å resolution . An amber mutation has been generated .

## Biological Role

Catalyzes L-fucose aldose-ketose-isomerase (reaction.R03163). Component of L-fucose isomerase (complex.ecocyc.CPLX0-7631).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Converts the aldose L-fucose into the corresponding ketose L-fuculose (PubMed:13319278, PubMed:4632320, PubMed:4928018, PubMed:8564401, PubMed:9367760). Also converts D-arabinose into D-ribulose (PubMed:13319278, PubMed:4632320, PubMed:4928018). In addition, catalyzes the isomerization of L-xylulose to L-xylose (PubMed:22133443). {ECO:0000269|PubMed:13319278, ECO:0000269|PubMed:22133443, ECO:0000269|PubMed:4632320, ECO:0000269|PubMed:4928018, ECO:0000269|PubMed:8564401, ECO:0000269|PubMed:9367760}.

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R03163|reaction.R03163]] `KEGG` `database` - via EC:5.3.1.25
- `is_component_of` --> [[complex.ecocyc.CPLX0-7631|complex.ecocyc.CPLX0-7631]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b2802|gene.b2802]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69922`
- `KEGG:ecj:JW2773;eco:b2802;ecoc:C3026_15405;`
- `GeneID:75172886;946195;`
- `GO:GO:0005829; GO:0008736; GO:0008790; GO:0019571; GO:0030145; GO:0042355; GO:0042802`
- `EC:5.3.1.25; 5.3.1.3`

## Notes

L-fucose isomerase (FucIase) (FucIso) (EC 5.3.1.25) (6-deoxy-L-galactose isomerase) (D-arabinose isomerase) (EC 5.3.1.3)
