---
entity_id: "protein.P37692"
entity_type: "protein"
name: "waaF"
source_database: "UniProt"
source_id: "P37692"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "waaF rfaF b3620 JW3595"
---

# waaF

`protein.P37692`

## Static

- Type: `protein`
- Source: `UniProt:P37692`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Glycosyltransferase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:11054112). Catalyzes the addition of the second heptose unit to the heptosyl-Kdo2-lipid A module (PubMed:11054112, PubMed:11717579). The analog ADP-mannose can serve as an alternative donor in place of ADP-L-glycero-D-manno-heptose, but with lower efficiency (PubMed:11054112). {ECO:0000269|PubMed:11054112, ECO:0000269|PubMed:11717579}. ADP-heptose:LPS heptosyltransferase II (HepII, WaaF) is the enzyme responsible for transfer of the second heptose sugar onto the heptosyl-Kdo2 moiety of the lipopolysaccharide inner core . A kinetic and biophysical characterization of HepII has been reported by . Truncation of the LPS inner core by defined mutations in hldD (rfaD), hldE (rfaE) or waaF resulted in high-level gab operon expression and a mucoid colony phenotype resulting from a colanic acid capsule . Production of colanic acid in the ΔwaaF mutant is dependent on the RcsCDB phosphorelay system . In waaC, waaE, waaF and waaG mutants, biofilm formation was significantly increased relative to the parental strain . A ΔwaaF strain lacks flagella . Selection for reduced susceptibility to tigecycline results in mutations in waaF and other genes of the LPS core biosynthesis pathway...

## Biological Role

Catalyzes ADP-L-glycero-beta-D-manno-heptose:an alpha-L-glycero-D-manno-heptosyl-(1->5)-[alpha-Kdo-(2->4)]-alpha -Kdo-(2->6)-[lipid A] 3-alpha-heptosyltransferase (reaction.R13004), RXN0-5061 (reaction.ecocyc.RXN0-5061).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Glycosyltransferase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:11054112). Catalyzes the addition of the second heptose unit to the heptosyl-Kdo2-lipid A module (PubMed:11054112, PubMed:11717579). The analog ADP-mannose can serve as an alternative donor in place of ADP-L-glycero-D-manno-heptose, but with lower efficiency (PubMed:11054112). {ECO:0000269|PubMed:11054112, ECO:0000269|PubMed:11717579}.

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R13004|reaction.R13004]] `KEGG` `database` - via EC:2.4.99.24
- `catalyzes` --> [[reaction.ecocyc.RXN0-5061|reaction.ecocyc.RXN0-5061]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3620|gene.b3620]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37692`
- `KEGG:ecj:JW3595;eco:b3620;ecoc:C3026_19625;`
- `GeneID:75173816;948135;`
- `GO:GO:0005829; GO:0008713; GO:0009244`
- `EC:2.4.99.24`

## Notes

Lipopolysaccharide heptosyltransferase 2 (EC 2.4.99.24) (ADP-heptose:lipopolysaccharide heptosyltransferase II) (ADP-heptose:LPS heptosyltransferase II) (Heptosyltransferase II)
