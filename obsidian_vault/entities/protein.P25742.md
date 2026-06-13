---
entity_id: "protein.P25742"
entity_type: "protein"
name: "waaQ"
source_database: "UniProt"
source_id: "P25742"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "waaQ rfaQ b3632 JW3607"
---

# waaQ

`protein.P25742`

## Static

- Type: `protein`
- Source: `UniProt:P25742`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Glycosyltransferase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:25957775). Catalyzes the addition of the third heptose unit (HepIII) to the second heptose unit (HepII) of the phospho-Hep2-Kdo2-lipid A module (PubMed:25957775). {ECO:0000269|PubMed:25957775}. WaaQ is a heptosyltransferase that is responsible for addition of the side-branch heptose of the inner core of LPS . It catalyzes the transfer of L-glycero-D-manno-heptose to the second Hep of Hep2-Kdo2-Lipid A via an α(1→7) glycosidic linkage . A non-polar waaQ mutant lacks the HepIII sugar of the inner core region of LPS as well as phosphorylation at HepII . WaaP activity (phosphorylation at HepI) is a prerequisite for the efficient addition of the HepIII residue to the inner core by WaaQ . A waaQ transposon insertion mutant was shown to grow in mouse cecal mucus, but cell clumping appeared to prevent it from colonizing mouse large intestine. The mutant was also hypersensitive to sodium dodecyl sulfate, bile salts and novobiocin, as expected for deep-rough mutants . Transposon insertion mutants in waaQ showed increased tolerance to lactoperoxidase and more sensitivity than wild-type to the antibacterial plant-derived compound thymol . In the facultative pathogen E...

## Biological Role

Catalyzes ADP-L-glycero-beta-D-manno-heptose:an alpha-Hep-(1->3)-4-O-phospho-alpha-Hep-(1->5)-[alpha-Kdo-(2->4)]-alpha-Kdo-(2->6)-[lipid A] heptoseI 7-alpha-heptosyltransferase (reaction.R13005), RXN-22462 (reaction.ecocyc.RXN-22462), RXN0-5122 (reaction.ecocyc.RXN0-5122).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Glycosyltransferase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:25957775). Catalyzes the addition of the third heptose unit (HepIII) to the second heptose unit (HepII) of the phospho-Hep2-Kdo2-lipid A module (PubMed:25957775). {ECO:0000269|PubMed:25957775}.

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R13005|reaction.R13005]] `KEGG` `database` - via EC:2.4.99.25
- `catalyzes` --> [[reaction.ecocyc.RXN-22462|reaction.ecocyc.RXN-22462]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5122|reaction.ecocyc.RXN0-5122]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3632|gene.b3632]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25742`
- `KEGG:ecj:JW3607;eco:b3632;ecoc:C3026_19685;`
- `GeneID:948155;`
- `GO:GO:0005829; GO:0008713; GO:0009244; GO:0071967`
- `EC:2.4.99.25`

## Notes

Lipopolysaccharide heptosyltransferase 3 (EC 2.4.99.25) (ADP-heptose:lipopolysaccharide heptosyltransferase III) (ADP-heptose:LPS heptosyltransferase III) (Heptosyltransferase III)
