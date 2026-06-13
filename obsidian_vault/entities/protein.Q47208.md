---
entity_id: "protein.Q47208"
entity_type: "protein"
name: "allF"
source_database: "UniProt"
source_id: "Q47208"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "allF fdrA ylbD b0518 JW0506"
---

# allF

`protein.Q47208`

## Static

- Type: `protein`
- Source: `UniProt:Q47208`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Component of a carbamoyltransferase involved in the anaerobic nitrogen utilization via the assimilation of allantoin (PubMed:34494882, PubMed:38888336). Catalyzes the conversion of oxalurate (N-carbamoyl-2-oxoglycine) to oxamate and carbamoyl phosphate (PubMed:38888336). {ECO:0000269|PubMed:34494882, ECO:0000269|PubMed:38888336}. Using genome and metabolic context methods, hypothesize that fdrA encodes an oxamate:CoA ligase which continues the degradation of oxamate produced by the PWY0-41 "anaerobic allantoin degradation pathway". The fate of oxamate is not clear; suggest that oxamate is not degraded further and they provide evidence that FdrA is critical for oxamate production during anaerobic allantoin degradation and may be the orphan enzyme OXAMATE-CARBAMOYLTRANSFERASE-RXN oxamate carbomoyltransferase (OXTCase). The OXTCase activity was subsequently found to require the first 3 genes in the TU0-12962 operon; all three of which are required to complement the triple mutant, ΔallFGH . The complex of three distinct subunits has not been observed for other enzymes of the transcarbamylase family in other organisms; also, the protein sequences for all three enzymes lack similarity to others in the transcarbamylase family . In contrast to the wild-type, a ΔfdrA mutant does not produce oxamate during glycerol fermentation with allantoin as the sole nitrogen source...

## Biological Role

Component of oxamate carbamoyltransferase (complex.ecocyc.CPLX0-12207).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Component of a carbamoyltransferase involved in the anaerobic nitrogen utilization via the assimilation of allantoin (PubMed:34494882, PubMed:38888336). Catalyzes the conversion of oxalurate (N-carbamoyl-2-oxoglycine) to oxamate and carbamoyl phosphate (PubMed:38888336). {ECO:0000269|PubMed:34494882, ECO:0000269|PubMed:38888336}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-12207|complex.ecocyc.CPLX0-12207]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0518|gene.b0518]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q47208`
- `KEGG:ecj:JW0506;eco:b0518;ecoc:C3026_02540;`
- `GeneID:946298;`
- `GO:GO:0000256; GO:0004775; GO:0004776; GO:0005829; GO:0006099; GO:0009361; GO:0050205; GO:0071973`
- `EC:2.1.3.5`

## Notes

Oxamate carbamoyltransferase subunit AllF (OXTCase subunit AllF) (EC 2.1.3.5) (Oxamic transcarbamylase subunit AllF)
