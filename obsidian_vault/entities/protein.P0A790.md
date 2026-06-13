---
entity_id: "protein.P0A790"
entity_type: "protein"
name: "panD"
source_database: "UniProt"
source_id: "P0A790"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:6767707}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "panD b0131 JW0127"
---

# panD

`protein.P0A790`

## Static

- Type: `protein`
- Source: `UniProt:P0A790`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:6767707}.

## Enriched Summary

FUNCTION: Catalyzes the pyruvoyl-dependent decarboxylation of aspartate to produce beta-alanine. {ECO:0000269|PubMed:6767707}. Aspartate 1-decarboxylase is responsible for the synthesis of β-alanine, which is needed in the biosynthesis of pantothenate. This enzyme is one of a small class of enzymes that use a covalently bound pyruvoyl prosthetic group. The pyruvoyl group is thought to act analogously to a pyridoxal phosphate cofactor by forming a Schiff base with the amino group of the substrate and then serving as an electron sink to facilitate the decarboxylation . Pyruvoyl-containing enzymes are expressed as a zymogen which is processed post-translationally by a self-maturation cleavage called serinolysis. E. coli contains two more such enzymes, PHOSPHASERDECARB-DIMER and SAMDECARB-CPLX. The PanD proenzyme (π protein) is processed at the serine residue at position 25, resulting in two subunits, α and β, which form a complex that is enzymatically active. Autocatalytic processing of purified enzyme preparations occurs slowly at room temperature or 37° C, and at a higher rate at elevated temperatures . An ester intermediate at Ser25, formed by an N->O acyl shift, facilitates autoproteolysis . β-elimination of the ester results in proteolysis and the formation of dehydroalanine, which undergoes hydrolysis to form the pyruvoyl group . Experiments in E...

## Biological Role

Catalyzes L-aspartate 1-carboxy-lyase (beta-alanine-forming) (reaction.R00489). Component of aspartate 1-decarboxylase (complex.ecocyc.CPLX0-2901).

## Enriched Pathways

- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the pyruvoyl-dependent decarboxylation of aspartate to produce beta-alanine. {ECO:0000269|PubMed:6767707}.

## Pathways

- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00489|reaction.R00489]] `KEGG` `database` - via EC:4.1.1.11
- `is_component_of` --> [[complex.ecocyc.CPLX0-2901|complex.ecocyc.CPLX0-2901]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0131|gene.b0131]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A790`
- `KEGG:ecj:JW0127;eco:b0131;ecoc:C3026_00560;`
- `GeneID:86945057;93777305;945686;`
- `GO:GO:0004068; GO:0005829; GO:0006523; GO:0015940; GO:0016540`
- `EC:4.1.1.11`

## Notes

Aspartate 1-decarboxylase (EC 4.1.1.11) (Aspartate alpha-decarboxylase) [Cleaved into: Aspartate 1-decarboxylase beta chain; Aspartate 1-decarboxylase alpha chain]
