---
entity_id: "protein.P24173"
entity_type: "protein"
name: "waaC"
source_database: "UniProt"
source_id: "P24173"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:9446588}; Peripheral membrane protein {ECO:0000269|PubMed:9446588}; Cytoplasmic side {ECO:0000305|PubMed:9446588}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "waaC rfa-2 rfaC yibC b3621 JW3596"
---

# waaC

`protein.P24173`

## Static

- Type: `protein`
- Source: `UniProt:P24173`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:9446588}; Peripheral membrane protein {ECO:0000269|PubMed:9446588}; Cytoplasmic side {ECO:0000305|PubMed:9446588}.

## Enriched Summary

FUNCTION: Glycosyltransferase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:11054112, PubMed:9446588). Catalyzes the addition of the first heptose unit to one 3-deoxy-D-manno-octulosonic acid (Kdo) residue of the Kdo2-lipid A module (PubMed:11054112, PubMed:11717579, PubMed:9446588). The analog ADP-mannose can serve as an alternative donor in place of ADP-L-glycero-D-manno-heptose for the glycosylation of Kdo2-lipid A (PubMed:9446588). Displays no activity with ADP-glucose, GDP-mannose, UDP-glucose or UDP-galactose (PubMed:9446588). {ECO:0000269|PubMed:11054112, ECO:0000269|PubMed:11717579, ECO:0000269|PubMed:9446588}. ADP-heptose:LPS heptosyltransferase I (HepI) is the enzyme responsible for transfer of the first heptose sugar onto the Kdo2 moiety of the lipopolysaccharide inner core . HepI is able to catalyze heptose transfer to underacylated and fully deacylated Kdo2-lipid A analogs; this activity does not require addition of detergent. Thus, the enzyme appears to only recognize the Kdo sugar region of these acceptor molecules . Crystal structures of WaaC from the pathogenic strain RS218 have been solved, providing insight into the catalytic mechanism . WaaC is considered to be an antimicrobial drug target, and small molecule inhibitors have been identified...

## Biological Role

Catalyzes ADP-L-glycero-beta-D-manno-heptose:an alpha-Kdo-(2->4)-alpha-Kdo-(2->6)-[lipid A] 5-alpha-heptosyltransferase (reaction.R13003), RXN0-5057 (reaction.ecocyc.RXN0-5057), RXN0-5118 (reaction.ecocyc.RXN0-5118).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Glycosyltransferase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:11054112, PubMed:9446588). Catalyzes the addition of the first heptose unit to one 3-deoxy-D-manno-octulosonic acid (Kdo) residue of the Kdo2-lipid A module (PubMed:11054112, PubMed:11717579, PubMed:9446588). The analog ADP-mannose can serve as an alternative donor in place of ADP-L-glycero-D-manno-heptose for the glycosylation of Kdo2-lipid A (PubMed:9446588). Displays no activity with ADP-glucose, GDP-mannose, UDP-glucose or UDP-galactose (PubMed:9446588). {ECO:0000269|PubMed:11054112, ECO:0000269|PubMed:11717579, ECO:0000269|PubMed:9446588}.

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R13003|reaction.R13003]] `KEGG` `database` - via EC:2.4.99.23
- `catalyzes` --> [[reaction.ecocyc.RXN0-5057|reaction.ecocyc.RXN0-5057]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5118|reaction.ecocyc.RXN0-5118]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3621|gene.b3621]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24173`
- `KEGG:ecj:JW3596;eco:b3621;ecoc:C3026_19630;`
- `GeneID:948136;`
- `GO:GO:0005829; GO:0005886; GO:0008713; GO:0008920; GO:0009244`
- `EC:2.4.99.23`

## Notes

Lipopolysaccharide heptosyltransferase 1 (EC 2.4.99.23) (ADP-heptose:lipopolysaccharide heptosyltransferase I) (ADP-heptose:LPS heptosyltransferase I) (Heptosyltransferase I)
