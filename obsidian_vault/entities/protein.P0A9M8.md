---
entity_id: "protein.P0A9M8"
entity_type: "protein"
name: "pta"
source_database: "UniProt"
source_id: "P0A9M8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pta b2297 JW2294"
---

# pta

`protein.P0A9M8`

## Static

- Type: `protein`
- Source: `UniProt:P0A9M8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Involved in acetate metabolism (PubMed:16080684). Catalyzes the reversible interconversion of acetyl-CoA and acetyl phosphate (PubMed:16080684). The direction of the overall reaction changes depending on growth conditions (PubMed:16080684). On minimal medium acetyl-CoA is generated. In rich medium acetyl-CoA is converted to acetate and allowing the cell to dump the excess of acetylation potential in exchange for energy in the form of ATP (PubMed:15687190). The main pathway for acetate production during exponential phase (PubMed:16080684). {ECO:0000269|PubMed:15687190, ECO:0000269|PubMed:16080684}. Phosphate acetyltransferase (Pta) catalyzes the reversible conversion between acetyl-CoA and acetylphosphate, a step in the metabolism of acetate. Both pyruvate and phosphoenolpyruvate activate the enzyme in the direction of acetylphosphate synthesis and inhibit the enzyme in the direction of acetyl-CoA synthesis . Pta is composed of three domains; only the C-terminal domain is required for phosphate acetyltransferase activity. The N-terminal domain is involved in stabilization of the native quarternary structure and metabolic regulation . Pta may be able to utilize both acetyl-CoA and propionyl-CoA...

## Biological Role

Catalyzes acetyl-CoA:phosphate acetyltransferase (reaction.R00230). Component of phosphate acetyltransferase (complex.ecocyc.PHOSACETYLTRANS-CPLX).

## Enriched Pathways

- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Involved in acetate metabolism (PubMed:16080684). Catalyzes the reversible interconversion of acetyl-CoA and acetyl phosphate (PubMed:16080684). The direction of the overall reaction changes depending on growth conditions (PubMed:16080684). On minimal medium acetyl-CoA is generated. In rich medium acetyl-CoA is converted to acetate and allowing the cell to dump the excess of acetylation potential in exchange for energy in the form of ATP (PubMed:15687190). The main pathway for acetate production during exponential phase (PubMed:16080684). {ECO:0000269|PubMed:15687190, ECO:0000269|PubMed:16080684}.

## Pathways

- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00230|reaction.R00230]] `KEGG` `database` - via EC:2.3.1.8
- `is_component_of` --> [[complex.ecocyc.PHOSACETYLTRANS-CPLX|complex.ecocyc.PHOSACETYLTRANS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b2297|gene.b2297]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9M8`
- `KEGG:ecj:JW2294;eco:b2297;ecoc:C3026_12815;`
- `GeneID:93774877;946778;`
- `GO:GO:0005829; GO:0006083; GO:0008270; GO:0008959; GO:0016746; GO:0019413; GO:0019427; GO:0045733; GO:0070689`
- `EC:2.3.1.8`

## Notes

Phosphate acetyltransferase (EC 2.3.1.8) (Phosphotransacetylase)
