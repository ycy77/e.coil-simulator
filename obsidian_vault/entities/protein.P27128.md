---
entity_id: "protein.P27128"
entity_type: "protein"
name: "waaO"
source_database: "UniProt"
source_id: "P27128"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "waaO rfaI b3627 JW3602"
---

# waaO

`protein.P27128`

## Static

- Type: `protein`
- Source: `UniProt:P27128`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Glucosyltransferase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:24479701, PubMed:9765561). Catalyzes the addition of a second glucose (glucose II) to the first outer-core glucose (glucose I) (PubMed:24479701, PubMed:9765561). In vitro, can add multiple glucose residues to its lipid acceptor (PubMed:24479701). Activity does not require the branched galactose added by WaaB, but it is higher in the presence of this branched galactose (PubMed:24479701). In the absence of a lipid acceptor, can hydrolyze UDP-glucose, but not UDP-galactose (PubMed:24479701). {ECO:0000269|PubMed:24479701, ECO:0000269|PubMed:9765561}. The lipopolysaccharide of E. coli K-12 consists of two major components: the hydrophobic lipid A moiety inserted into the outer membrane and the phosphorylated core oligosaccharide . WaaO is a nonprocessive α-1,3 glucosyltransferase involved in the synthesis of the R core of lipopolysaccharide . WaaO adds the second glucose (GlcII) to the first glucose (GlcI) of the outer core of LPS . Activity of WaaO requires a functional waaB gene . Note that the E. coli K-12 gene is named waaO but is also referred to in the literature by its synonyms. In Salmonella typhimurium it is named waaI (rfaI). The history of this nomenclature is explained in the comment section of the EcoGene GenePage in the Unification Link...

## Biological Role

Catalyzes RXN0-5125 (reaction.ecocyc.RXN0-5125). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Glucosyltransferase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:24479701, PubMed:9765561). Catalyzes the addition of a second glucose (glucose II) to the first outer-core glucose (glucose I) (PubMed:24479701, PubMed:9765561). In vitro, can add multiple glucose residues to its lipid acceptor (PubMed:24479701). Activity does not require the branched galactose added by WaaB, but it is higher in the presence of this branched galactose (PubMed:24479701). In the absence of a lipid acceptor, can hydrolyze UDP-glucose, but not UDP-galactose (PubMed:24479701). {ECO:0000269|PubMed:24479701, ECO:0000269|PubMed:9765561}.

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5125|reaction.ecocyc.RXN0-5125]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3627|gene.b3627]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27128`
- `KEGG:ecj:JW3602;eco:b3627;ecoc:C3026_19660;`
- `GeneID:948143;`
- `GO:GO:0008918; GO:0009244; GO:0046872; GO:0047270`
- `EC:2.4.1.73`

## Notes

Lipopolysaccharide glucosyltransferase WaaO (EC 2.4.1.73) (Lipopolysaccharide alpha-1,3 glucosyltransferase) (Lipopolysaccharide glucosyltransferase II)
