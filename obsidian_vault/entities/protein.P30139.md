---
entity_id: "protein.P30139"
entity_type: "protein"
name: "thiG"
source_database: "UniProt"
source_id: "P30139"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "thiG b3991 JW5549"
---

# thiG

`protein.P30139`

## Static

- Type: `protein`
- Source: `UniProt:P30139`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the rearrangement of 1-deoxy-D-xylulose 5-phosphate (DXP) to produce the thiazole phosphate moiety of thiamine. Sulfur is provided by the thiocarboxylate moiety of the carrier protein ThiS. In vitro, sulfur can be provided by H(2)S. {ECO:0000269|PubMed:12650933}. 1-deoxy-D-xylulose 5-phosphate:thiol sulfurtransferase (ThiG) participates in the synthesis of the thiazole moiety of thiamine . ThiG is responsible for a complex cyclization reaction; formation of CPD-13575 requires 1-deoxyxylulose 5-phosphate, a sulfur atom from cysteine which is transferred via ThiS, and CPD-12279 (dehydroglycine) produced by the tyrosine lyase ThiH . ThiG purifies in a large multimeric complex with ThiH . Because CPD-12279 is unstable and undergoes hydrolysis to glyoxylate and ammonium, complex formation between ThiG and ThiH may ensure that it is passed directly from ThiH to ThiG . Growth of a thiG insertion mutant requires the presence of thiazole or thiamine . A computational screen for potential suppressors of a ΔG0-9461 pdxB mutation identified ThiG as an enzyme with similarity to Bacillus subtilis PdxS, the glutamine amidotransferase component of the pyridoxal 5'-phosphate synthase complex. Overexpression of thiG in a ΔpdxB mutant can indeed suppress the growth defect on minimal medium, and mutations in predicted active site residues of ThiG eliminate suppression...

## Biological Role

Catalyzes 1-deoxy-D-xylulose 5-phosphate:thiol sulfurtransferase (reaction.R10247), THIAZOLSYN2-RXN (reaction.ecocyc.THIAZOLSYN2-RXN). Component of thiazole synthase (complex.ecocyc.CPLX0-3949).

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the rearrangement of 1-deoxy-D-xylulose 5-phosphate (DXP) to produce the thiazole phosphate moiety of thiamine. Sulfur is provided by the thiocarboxylate moiety of the carrier protein ThiS. In vitro, sulfur can be provided by H(2)S. {ECO:0000269|PubMed:12650933}.

## Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R10247|reaction.R10247]] `KEGG` `database` - via EC:2.8.1.10
- `catalyzes` --> [[reaction.ecocyc.THIAZOLSYN2-RXN|reaction.ecocyc.THIAZOLSYN2-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-3949|complex.ecocyc.CPLX0-3949]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b3991|gene.b3991]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30139`
- `KEGG:ecj:JW5549;eco:b3991;ecoc:C3026_21555;`
- `GeneID:948493;`
- `GO:GO:0005829; GO:0009228; GO:0009229; GO:1902508; GO:1990107`
- `EC:2.8.1.10`

## Notes

Thiazole synthase (EC 2.8.1.10)
