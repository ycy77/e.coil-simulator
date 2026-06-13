---
entity_id: "protein.P07639"
entity_type: "protein"
name: "aroB"
source_database: "UniProt"
source_id: "P07639"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00110}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aroB b3389 JW3352"
---

# aroB

`protein.P07639`

## Static

- Type: `protein`
- Source: `UniProt:P07639`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00110}.

## Enriched Summary

FUNCTION: Catalyzes the conversion of 3-deoxy-D-arabino-heptulosonate 7-phosphate (DAHP) to dehydroquinate (DHQ). {ECO:0000255|HAMAP-Rule:MF_00110, ECO:0000269|PubMed:2514789}. Dehydroquinate synthase (DHQ synthase) is involved in the second step of the chorismate pathway, which leads to the biosynthesis of aromatic amino acids. DHQ synthase catalyzes the cyclization of 3-deoxy-D-arabino-heptulosonic acid 7-phosphate (DAHP) to dehydroquinate (DHQ) . In the course of this conversion the synthase apparently catalyzes an oxidation, a β-elimination, an intramolecular aldol condensation, and a reduction . DHQ synthase is a metalloenzyme that uses either Co2+ or Zn2+ as its metal cofactor. Although the Co2+ form of the enzyme has been reported have a higher specific activity, the bioavailability of Zn2+ in nature is much greater than Co2+. The presence of NAD+ as a cofactor is essential for catalytic activity. DHQ synthase appears to be synthesized constitutively and is not repressed by chorismate, any of the aromatic amino acids or by the regulator genes trpR and tyrR . The sequence for aroB has been determined and the protein overexpressed .

## Biological Role

Catalyzes 3-DEHYDROQUINATE-SYNTHASE-RXN (reaction.ecocyc.3-DEHYDROQUINATE-SYNTHASE-RXN). Bound by NAD+ (molecule.C00003), Zinc cation (molecule.C00038), Cobalt ion (molecule.C00175).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of 3-deoxy-D-arabino-heptulosonate 7-phosphate (DAHP) to dehydroquinate (DHQ). {ECO:0000255|HAMAP-Rule:MF_00110, ECO:0000269|PubMed:2514789}.

## Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3-DEHYDROQUINATE-SYNTHASE-RXN|reaction.ecocyc.3-DEHYDROQUINATE-SYNTHASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `binds` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3389|gene.b3389]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07639`
- `KEGG:ecj:JW3352;eco:b3389;ecoc:C3026_18390;`
- `GeneID:947927;`
- `GO:GO:0003856; GO:0005737; GO:0008270; GO:0008652; GO:0009073; GO:0009423; GO:0070403`
- `EC:4.2.3.4`

## Notes

3-dehydroquinate synthase (DHQS) (EC 4.2.3.4)
