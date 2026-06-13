---
entity_id: "protein.P46022"
entity_type: "protein"
name: "mtgA"
source_database: "UniProt"
source_id: "P46022"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00766, ECO:0000269|PubMed:8772200}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00766}. Note=Localizes to the cell division site. {ECO:0000269|PubMed:18165305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mtgA mgt yrbM b3208 JW3175"
---

# mtgA

`protein.P46022`

## Static

- Type: `protein`
- Source: `UniProt:P46022`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00766, ECO:0000269|PubMed:8772200}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00766}. Note=Localizes to the cell division site. {ECO:0000269|PubMed:18165305}.

## Enriched Summary

FUNCTION: Peptidoglycan polymerase that catalyzes glycan chain elongation from lipid-linked precursors (PubMed:18165305, PubMed:6368264, PubMed:8772200). May play a role in peptidoglycan assembly during cell division in collaboration with other cell division proteins (PubMed:18165305). {ECO:0000269|PubMed:18165305, ECO:0000269|PubMed:6368264, ECO:0000269|PubMed:8772200}. MtgA is a monofunctional murein glycosyltransferase involved in polymerization of lipid II molecules into glycan strands of peptidoglycan. GFP-MtgA fusions localize to the division site in mrcA(ts) mrcB mutants . Bacterial two-hybrid experiments reveal MtgA interacts with PBP3, FtsW, and FtsN . Assays for peptidoglycan synthesis activity revealed that MtgA has glycosyltransferase activity and polymerizes glycan strands with lipid II as substrate at an optimum pH of 6.0 to 6.5 . This differs from the optimum of 7.5 to 8.0 for PBP1B, which is the major bifunctional glycosyltransferase for peptidoglycan synthesis in E. coli . The glycan strands were then shown to act as substrate for lysozyme . Inhibition assays show that MOENOMYCIN moenomycin A does not inhibit this activity as it does with the high-molecular-weight penicillin-binding proteins that have glycosyltransferase activity . Induction of this gene from an expression vector in wild-type W3110 caused cells to immediately stop growing, but not to lyse...

## Biological Role

Catalyzes R06177 (reaction.R06177), [poly-N-acetyl-D-glucosaminyl-(1->4)-(N-acetyl-D-muramoylpentapeptide)]-diphosphoundecaprenol:[N-acetyl-D-glucosaminyl-(1->4)-N-acetyl-D-muramoylpentapeptide]-diphosphoundecaprenol polysaccharidetransferase (reaction.R06178), R06179 (reaction.R06179), RXN-16650 (reaction.ecocyc.RXN-16650). Bound by Cobalt ion (molecule.C00175), Ca2+ (molecule.ecocyc.CA_2), Mn2+ (molecule.ecocyc.MN_2).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Peptidoglycan polymerase that catalyzes glycan chain elongation from lipid-linked precursors (PubMed:18165305, PubMed:6368264, PubMed:8772200). May play a role in peptidoglycan assembly during cell division in collaboration with other cell division proteins (PubMed:18165305). {ECO:0000269|PubMed:18165305, ECO:0000269|PubMed:6368264, ECO:0000269|PubMed:8772200}.

## Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R06177|reaction.R06177]] `KEGG` `database` - via EC:2.4.99.28
- `catalyzes` --> [[reaction.R06178|reaction.R06178]] `KEGG` `database` - via EC:2.4.99.28
- `catalyzes` --> [[reaction.R06179|reaction.R06179]] `KEGG` `database` - via EC:2.4.99.28
- `catalyzes` --> [[reaction.ecocyc.RXN-16650|reaction.ecocyc.RXN-16650]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `binds` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3208|gene.b3208]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P46022`
- `KEGG:ecj:JW3175;eco:b3208;ecoc:C3026_17455;`
- `GeneID:75206064;947728;`
- `GO:GO:0005886; GO:0008360; GO:0008955; GO:0009252; GO:0009274; GO:0016763; GO:0043164; GO:0071555`
- `EC:2.4.99.28`

## Notes

Biosynthetic peptidoglycan transglycosylase (EC 2.4.99.28) (Glycan polymerase) (Monofunctional biosynthetic peptidoglycan transglycosylase) (Monofunctional glycosyltransferase) (Monofunctional GTase) (Peptidoglycan glycosyltransferase MtgA) (PGT)
