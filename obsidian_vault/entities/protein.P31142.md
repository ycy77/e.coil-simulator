---
entity_id: "protein.P31142"
entity_type: "protein"
name: "sseA"
source_database: "UniProt"
source_id: "P31142"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sseA b2521 JW2505"
---

# sseA

`protein.P31142`

## Static

- Type: `protein`
- Source: `UniProt:P31142`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the transfer of sulfur from 3-mercaptopyruvate to a thiol-containing acceptor to form an intramolecular disulfide releasing hydrogen sulfide and pyruvate (Probable). May be involved in the enhancement of bacterial growth inhibition by serine (PubMed:7982894). {ECO:0000269|PubMed:7982894, ECO:0000305|PubMed:11445076}. 3-Mercaptopyruvate sulfurtransferase (3MST) is a rhodanese-like enzyme that, in contrast to rhodanese, uses 3-mercaptopyruvate as the preferred sulfur donor; thiosulfate can be used as a less efficient donor . 3MST is the major source of hydrogen sulfide production in E. coli grown in LB medium ; H2S in turn protects the cell against DNA damage by sequestering free Fe2+, which otherwise drives hydroxyl radical generation via the Fenton reaction . A crystal structure of 3MST has been solved at 2.8 Å resolution; the structure shows differences with the structure of rhodanese enzymes, including a variation in the active site loop. The structure provides insight into the catalytic mechanism of 3MST . The Ser240 residue is important for catalytic activity . Overexpression enhances the serine sensitivity caused by serine-mediated inhibition of ASPKINIHOMOSERDEHYDROGI-CPLX homoserine dehydrogenase I activity during growth on some carbon sources and results in increased cellular rhodanese activity...

## Biological Role

Catalyzes MERCAPYSTRANS-RXN (reaction.ecocyc.MERCAPYSTRANS-RXN), THIOSULFATE-SULFURTRANSFERASE-RXN (reaction.ecocyc.THIOSULFATE-SULFURTRANSFERASE-RXN).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Annotation

FUNCTION: Catalyzes the transfer of sulfur from 3-mercaptopyruvate to a thiol-containing acceptor to form an intramolecular disulfide releasing hydrogen sulfide and pyruvate (Probable). May be involved in the enhancement of bacterial growth inhibition by serine (PubMed:7982894). {ECO:0000269|PubMed:7982894, ECO:0000305|PubMed:11445076}.

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.MERCAPYSTRANS-RXN|reaction.ecocyc.MERCAPYSTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.THIOSULFATE-SULFURTRANSFERASE-RXN|reaction.ecocyc.THIOSULFATE-SULFURTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2521|gene.b2521]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31142`
- `KEGG:ecj:JW2505;eco:b2521;ecoc:C3026_13975;`
- `GeneID:93774615;946993;`
- `GO:GO:0004792; GO:0005829; GO:0006979; GO:0016784; GO:0042262; GO:0046677`
- `EC:2.8.1.2`

## Notes

3-mercaptopyruvate sulfurtransferase (MST) (EC 2.8.1.2) (Rhodanese-like protein)
