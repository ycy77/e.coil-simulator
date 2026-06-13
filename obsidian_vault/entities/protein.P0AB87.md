---
entity_id: "protein.P0AB87"
entity_type: "protein"
name: "fucA"
source_database: "UniProt"
source_id: "P0AB87"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fucA fucC prd b2800 JW2771"
---

# fucA

`protein.P0AB87`

## Static

- Type: `protein`
- Source: `UniProt:P0AB87`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the degradation of L-fucose and D-arabinose (PubMed:13898172). Catalyzes the reversible cleavage of L-fuculose 1-phosphate (Fuc1P) to yield dihydroxyacetone phosphate (DHAP) and L-lactaldehyde (PubMed:10821675, PubMed:11054289, PubMed:13898172, Ref.8, Ref.9). Also able to catalyze the reversible cleavage of D-ribulose 1-phosphate, but FucA has a higher affinity for L-fuculose 1-phosphate and L-lactaldehyde than for D-ribulose 1-phosphate and glycolaldehyde, respectively (PubMed:4928018). FucA possesses a high specificity for the dihydroxyacetone phosphate (DHAP), but accepts a great variety of different aldehydes and has a strong preference for L-configurated alpha-hydroxy aldehydes (PubMed:10821675, PubMed:13898172, Ref.8). FucA generates a vicinal diol unit having the absolute (3R,4R)-cis configuration (D-erythro) (PubMed:10821675, Ref.8). {ECO:0000269|PubMed:10821675, ECO:0000269|PubMed:11054289, ECO:0000269|PubMed:13898172, ECO:0000269|PubMed:4928018, ECO:0000269|Ref.8, ECO:0000269|Ref.9}. FucA can function as both an L-fuculose-phosphate aldolase and a D-ribulose-phosphate aldolase, the third enzyme of the L-fucose and D-arabinose degradation pathways, respectively. However, production of FucA is only induced by L-fucose . The substrate specificity of the enzyme was tested with a partially purified preparation from an unnamed E. coli strain...

## Biological Role

Component of L-fuculose-phosphate aldolase (complex.ecocyc.CPLX0-7633).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Involved in the degradation of L-fucose and D-arabinose (PubMed:13898172). Catalyzes the reversible cleavage of L-fuculose 1-phosphate (Fuc1P) to yield dihydroxyacetone phosphate (DHAP) and L-lactaldehyde (PubMed:10821675, PubMed:11054289, PubMed:13898172, Ref.8, Ref.9). Also able to catalyze the reversible cleavage of D-ribulose 1-phosphate, but FucA has a higher affinity for L-fuculose 1-phosphate and L-lactaldehyde than for D-ribulose 1-phosphate and glycolaldehyde, respectively (PubMed:4928018). FucA possesses a high specificity for the dihydroxyacetone phosphate (DHAP), but accepts a great variety of different aldehydes and has a strong preference for L-configurated alpha-hydroxy aldehydes (PubMed:10821675, PubMed:13898172, Ref.8). FucA generates a vicinal diol unit having the absolute (3R,4R)-cis configuration (D-erythro) (PubMed:10821675, Ref.8). {ECO:0000269|PubMed:10821675, ECO:0000269|PubMed:11054289, ECO:0000269|PubMed:13898172, ECO:0000269|PubMed:4928018, ECO:0000269|Ref.8, ECO:0000269|Ref.9}.

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7633|complex.ecocyc.CPLX0-7633]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2800|gene.b2800]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AB87`
- `KEGG:ecj:JW2771;eco:b2800;ecoc:C3026_15395;`
- `GeneID:75172884;947282;`
- `GO:GO:0005829; GO:0008270; GO:0008738; GO:0016832; GO:0019323; GO:0019571; GO:0042355`
- `EC:4.1.2.17`

## Notes

L-fuculose phosphate aldolase (EC 4.1.2.17) (D-ribulose-phosphate aldolase) (L-fuculose-1-phosphate aldolase)
