---
entity_id: "protein.P24186"
entity_type: "protein"
name: "folD"
source_database: "UniProt"
source_id: "P24186"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "folD ads b0529 JW0518"
---

# folD

`protein.P24186`

## Static

- Type: `protein`
- Source: `UniProt:P24186`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the oxidation of 5,10-methylenetetrahydrofolate to 5,10-methenyltetrahydrofolate and then the hydrolysis of 5,10-methenyltetrahydrofolate to 10-formyltetrahydrofolate. This enzyme is specific for NADP. {ECO:0000255|HAMAP-Rule:MF_01576, ECO:0000269|PubMed:1748668}. The folD gene product is a bifunctional enzyme that catalyzes the NADP+-dependent dehydrogenation of N5,N10-methylenetetrahydrofolate and the subsequent cyclohydrolysis reaction that generates N10-formyltetrahydrofolate . N10-formyltetrahydrofolates are involved in tetrahydrofolate and purine biosynthesis and supply the formyl group for the initiator tRNAfMet. The macrolide carboxylate carolacton inhibits both activities of FolD; mutant enzymes that confer resistance to carolacton have been isolated . Crystal structures of FolD and the FolD-carolacton complex have been solved . Each monomer comprises two domains that form an interdomain cleft. The homodimeric form appears to be stabilized by an intersubunit disulfide bond between the Cys132 residues of each subunit...

## Biological Role

Component of bifunctional methylenetetrahydrofolate dehydrogenase / methenyltetrahydrofolate cyclohydrolase (complex.ecocyc.FOLD-CPLX).

## Enriched Pathways

- `eco00670` One carbon pool by folate (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the oxidation of 5,10-methylenetetrahydrofolate to 5,10-methenyltetrahydrofolate and then the hydrolysis of 5,10-methenyltetrahydrofolate to 10-formyltetrahydrofolate. This enzyme is specific for NADP. {ECO:0000255|HAMAP-Rule:MF_01576, ECO:0000269|PubMed:1748668}.

## Pathways

- `eco00670` One carbon pool by folate (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.FOLD-CPLX|complex.ecocyc.FOLD-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0529|gene.b0529]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24186`
- `KEGG:ecj:JW0518;eco:b0529;ecoc:C3026_02595;`
- `GeneID:945221;`
- `GO:GO:0000105; GO:0004477; GO:0004488; GO:0005829; GO:0006164; GO:0009086; GO:0035999; GO:0042803`
- `EC:1.5.1.5; 3.5.4.9`

## Notes

Bifunctional protein FolD [Includes: Methylenetetrahydrofolate dehydrogenase (EC 1.5.1.5); Methenyltetrahydrofolate cyclohydrolase (EC 3.5.4.9)]
