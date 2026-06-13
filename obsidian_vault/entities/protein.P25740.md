---
entity_id: "protein.P25740"
entity_type: "protein"
name: "waaG"
source_database: "UniProt"
source_id: "P25740"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:26244737, ECO:0000305|PubMed:29225173}; Peripheral membrane protein {ECO:0000269|PubMed:29225173}; Cytoplasmic side {ECO:0000305|PubMed:26244737}. Note=Binds membranes via electrostatic interactions (PubMed:26244737, PubMed:29225173). Interaction with the membrane is conferred at least in part by the N-terminal positively charged and largely alpha-helical membrane-interacting region (MIR-WaaG) (PubMed:26244737). {ECO:0000269|PubMed:26244737, ECO:0000269|PubMed:29225173}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "waaG pcsA rfaG b3631 JW3606"
---

# waaG

`protein.P25740`

## Static

- Type: `protein`
- Source: `UniProt:P25740`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:26244737, ECO:0000305|PubMed:29225173}; Peripheral membrane protein {ECO:0000269|PubMed:29225173}; Cytoplasmic side {ECO:0000305|PubMed:26244737}. Note=Binds membranes via electrostatic interactions (PubMed:26244737, PubMed:29225173). Interaction with the membrane is conferred at least in part by the N-terminal positively charged and largely alpha-helical membrane-interacting region (MIR-WaaG) (PubMed:26244737). {ECO:0000269|PubMed:26244737, ECO:0000269|PubMed:29225173}.

## Enriched Summary

FUNCTION: Glucosyltransferase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:10986272, PubMed:24479701). Catalyzes the addition of the first outer-core glucose from UDP-glucose to the inner-core heptose II (PubMed:24479701). Cannot use other sugar donors, such as UDP-galactose, UDP-glucuronic acid, UDP-galacuronic acid, GDP-mannose, ADP-glucose and GDP-glucose (PubMed:24479701). In the absence of a lipid acceptor, can slowly hydrolyze UDP-glucose (PubMed:24479701). {ECO:0000269|PubMed:10986272, ECO:0000269|PubMed:24479701}. The lipopolysaccharide of E. coli K-12 consists of two major components: the hydrophobic lipid A moiety inserted into the outer membrane and the phosphorylated core oligosaccharide . UDP-glucose:(heptosyl)lipopolysaccharide α-1,3-glucosyltransferase (WaaG) adds the first glucose (GlcI) of the outer core of LPS from UDP-glucose to the HepII residue of the inner core . WaaG is a glycosyltransferase family 4 (GT4) enzyme. Early studies characterized the rfa locus and identified the waaG gene (formerly rfaG) . waaG+ restores flagella and pili to a waaGPSBI deletion mutant . Mutation of waaG reduces phosphorylation of the inner core heptoses HepI and HepII . An E. coli DH5α waaG::Tn5 mutant has a hypervesiculation phenotype...

## Biological Role

Catalyzes RXN-22463 (reaction.ecocyc.RXN-22463), RXN0-5120 (reaction.ecocyc.RXN0-5120).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Glucosyltransferase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:10986272, PubMed:24479701). Catalyzes the addition of the first outer-core glucose from UDP-glucose to the inner-core heptose II (PubMed:24479701). Cannot use other sugar donors, such as UDP-galactose, UDP-glucuronic acid, UDP-galacuronic acid, GDP-mannose, ADP-glucose and GDP-glucose (PubMed:24479701). In the absence of a lipid acceptor, can slowly hydrolyze UDP-glucose (PubMed:24479701). {ECO:0000269|PubMed:10986272, ECO:0000269|PubMed:24479701}.

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-22463|reaction.ecocyc.RXN-22463]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5120|reaction.ecocyc.RXN0-5120]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3631|gene.b3631]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25740`
- `KEGG:ecj:JW3606;eco:b3631;ecoc:C3026_19680;`
- `GeneID:948149;`
- `GO:GO:0005886; GO:0008919; GO:0009244; GO:0016757`
- `EC:2.4.1.-`

## Notes

Lipopolysaccharide glucosyltransferase WaaG (EC 2.4.1.-) (Lipopolysaccharide glucosyltransferase I) (UDP-glucose:(heptosyl)lipopolysaccharide glucosyltransferase)
