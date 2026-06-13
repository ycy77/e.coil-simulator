---
entity_id: "protein.P31992"
entity_type: "protein"
name: "pptA"
source_database: "UniProt"
source_id: "P31992"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pptA ydcE b1461 JW1456"
---

# pptA

`protein.P31992`

## Static

- Type: `protein`
- Source: `UniProt:P31992`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Can use enol isomers of phenylpyruvate, 2-hydroxy-2,4-pentadienoate and (p-hydroxyphenyl)pyruvate as substrates. {ECO:0000269|PubMed:12356301}. YdcE is a member of subfamily 5 of the 4-oxalocrotonate tautomerase (4-OT) superfamily. Although it catalyzes an efficient tautomerase reaction using 2-hydroxy-2,4-pentadienoate and related substrates, YdcE does not appear to have 4-OT-like activity with 2-hydroxymuconate or 2-oxo-3-hexenedioate . Crystal structures of YdcE alone, in complex with the inhibitor (E)-2-fluoro-p-hydroxycinnamate, and in complex with N-(2-hydroxyethyl)piperazine-N'-2-ethanesulfonic acid (HEPES) and benzoate have been solved. While many 4-OTs are hexameric, YdcE forms homodimers. The potential active sites and reaction mechanism are discussed, as are the implications of the enzyme structure with respect to the active site and the reaction mechanism . YdcE accumulates in the presence of the antifouling agent zosteric acid . Review:

## Biological Role

Catalyzes 2-hydroxy-5-methyl-cis,cis-muconate 2-oxo-5-methyl-cis-muconate isomerase (reaction.R05389). Component of tautomerase PptA (complex.ecocyc.CPLX0-902).

## Enriched Pathways

- `eco00362` Benzoate degradation (KEGG)
- `eco00621` Dioxin degradation (KEGG)
- `eco00622` Xylene degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Annotation

FUNCTION: Can use enol isomers of phenylpyruvate, 2-hydroxy-2,4-pentadienoate and (p-hydroxyphenyl)pyruvate as substrates. {ECO:0000269|PubMed:12356301}.

## Pathways

- `eco00362` Benzoate degradation (KEGG)
- `eco00621` Dioxin degradation (KEGG)
- `eco00622` Xylene degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R05389|reaction.R05389]] `KEGG` `database` - via EC:5.3.2.6
- `is_component_of` --> [[complex.ecocyc.CPLX0-902|complex.ecocyc.CPLX0-902]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1461|gene.b1461]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31992`
- `KEGG:ecj:JW1456;eco:b1461;ecoc:C3026_08485;`
- `GeneID:945731;`
- `GO:GO:0005737; GO:0016862; GO:0042803`
- `EC:5.3.2.-`

## Notes

Tautomerase PptA (EC 5.3.2.-)
