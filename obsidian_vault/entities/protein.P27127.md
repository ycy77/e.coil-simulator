---
entity_id: "protein.P27127"
entity_type: "protein"
name: "waaB"
source_database: "UniProt"
source_id: "P27127"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "waaB rfaB b3628 JW3603"
---

# waaB

`protein.P27127`

## Static

- Type: `protein`
- Source: `UniProt:P27127`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Galactosyltransferase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:24479701). Catalyzes the addition of galactose from UDP-galactose to the first glucose residue of the LPS outer core (PubMed:24479701). Cannot use other sugar donors, such as UDP-glucose, UDP-glucuronic acid, UDP-galacuronic acid, GDP-mannose, ADP-glucose and GDP-glucose (PubMed:24479701). In the absence of a lipid acceptor, can hydrolyze UDP-galactose to UDP and galactose (PubMed:24479701). {ECO:0000269|PubMed:24479701}. The lipopolysaccharide (LPS) of E. coli K-12 consists of two major components: the hydrophobic lipid A moiety inserted into the outer membrane and the phosphorylated core oligosaccharide . UDP-galactose:(glucosyl)lipopolysaccharide 1,6-D-galactosyltransferase (WaaB) adds galactose from UDP-galactose to the first glucose residue (GlcI) of the outer core of LPS . Early studies characterized the waa (rfa) locus and identified the waaB gene . In the absence of the lipid acceptor, WaaB can slowly hydrolyze the UDP-galactose sugar donor. It cannot hydrolyze UDP-glucose . WaaB is not able to utilize other sugar nucleotide donors such as UDP-glucose, UDP-glucuronate, UDP-galacturonate, GDP-mannose, ADP-glucose and GDP-glucose. Unphosphorylated heptosyl2-Kdo2-lipid A cannot serve as an acceptor...

## Biological Role

Catalyzes RXN0-5124 (reaction.ecocyc.RXN0-5124).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Galactosyltransferase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:24479701). Catalyzes the addition of galactose from UDP-galactose to the first glucose residue of the LPS outer core (PubMed:24479701). Cannot use other sugar donors, such as UDP-glucose, UDP-glucuronic acid, UDP-galacuronic acid, GDP-mannose, ADP-glucose and GDP-glucose (PubMed:24479701). In the absence of a lipid acceptor, can hydrolyze UDP-galactose to UDP and galactose (PubMed:24479701). {ECO:0000269|PubMed:24479701}.

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5124|reaction.ecocyc.RXN0-5124]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3628|gene.b3628]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27127`
- `KEGG:ecj:JW3603;eco:b3628;ecoc:C3026_19665;`
- `GeneID:948144;`
- `GO:GO:0005829; GO:0008921; GO:0009244`
- `EC:2.4.1.-`

## Notes

Lipopolysaccharide 1,6-galactosyltransferase (EC 2.4.1.-) (UDP-D-galactose:(Glucosyl)lipopolysaccharide-alpha-1,3-D-galactosyltransferase)
