---
entity_id: "protein.P0A6D3"
entity_type: "protein"
name: "aroA"
source_database: "UniProt"
source_id: "P0A6D3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00210, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aroA b0908 JW0891"
---

# aroA

`protein.P0A6D3`

## Static

- Type: `protein`
- Source: `UniProt:P0A6D3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00210, ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the transfer of the enolpyruvyl moiety of phosphoenolpyruvate (PEP) to the 5-hydroxyl of shikimate-3-phosphate (S3P) to produce enolpyruvyl shikimate-3-phosphate and inorganic phosphate. {ECO:0000255|HAMAP-Rule:MF_00210, ECO:0000269|PubMed:12430021, ECO:0000269|PubMed:13129913, ECO:0000269|PubMed:16225867, ECO:0000269|PubMed:17855366, ECO:0000269|PubMed:17958399, ECO:0000269|PubMed:19211556, ECO:0000269|PubMed:6229418}. 3-Phosphoshikimate-1-carboxyvinyltransferase (EPSP synthase) is involved in the 6th step of the chorismate pathway, which leads to the biosynthesis of aromatic amino acids. EPSP synthase catalyzes the transfer of the enolpyruvoyl moiety from phosphoenolpyruvate to the hydroxyl group of carbon 5 of shikimate 3-phosphate with the elimination of phosphate to produce 5-enolpyruvoyl shikimate 3-phosphate (EPSP). This is an addition-elimination reaction. It is an ordered reaction in which shikimate 3-phosphate binds first. It involves the transfer of an enolpyruvyl group unchanged to the acceptor molecule. The reaction introduces the three carbon fragment that is destined to become the side chain of phenylalanine and tyrosine and to be removed again in the synthesis of tryptophan. Two reactive cysteines have been identified . A lysine has been designated a potential active site residue...

## Biological Role

Catalyzes 2.5.1.19-RXN (reaction.ecocyc.2.5.1.19-RXN).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the transfer of the enolpyruvyl moiety of phosphoenolpyruvate (PEP) to the 5-hydroxyl of shikimate-3-phosphate (S3P) to produce enolpyruvyl shikimate-3-phosphate and inorganic phosphate. {ECO:0000255|HAMAP-Rule:MF_00210, ECO:0000269|PubMed:12430021, ECO:0000269|PubMed:13129913, ECO:0000269|PubMed:16225867, ECO:0000269|PubMed:17855366, ECO:0000269|PubMed:17958399, ECO:0000269|PubMed:19211556, ECO:0000269|PubMed:6229418}.

## Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.5.1.19-RXN|reaction.ecocyc.2.5.1.19-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0908|gene.b0908]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6D3`
- `KEGG:ecj:JW0891;eco:b0908;ecoc:C3026_05600;`
- `GeneID:93776510;945528;`
- `GO:GO:0003866; GO:0005829; GO:0008652; GO:0009073; GO:0009423`
- `EC:2.5.1.19`

## Notes

3-phosphoshikimate 1-carboxyvinyltransferase (EC 2.5.1.19) (5-enolpyruvylshikimate-3-phosphate synthase) (EPSP synthase) (EPSPS)
