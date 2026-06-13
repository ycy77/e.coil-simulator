---
entity_id: "protein.P76658"
entity_type: "protein"
name: "hldE"
source_database: "UniProt"
source_id: "P76658"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hldE rfaE waaE yqiF b3052 JW3024"
---

# hldE

`protein.P76658`

## Static

- Type: `protein`
- Source: `UniProt:P76658`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the phosphorylation of D-glycero-D-manno-heptose 7-phosphate at the C-1 position to selectively form D-glycero-beta-D-manno-heptose-1,7-bisphosphate. {ECO:0000269|PubMed:11751812}.; FUNCTION: Catalyzes the ADP transfer from ATP to D-glycero-beta-D-manno-heptose 1-phosphate, yielding ADP-D-glycero-beta-D-manno-heptose. {ECO:0000269|PubMed:11751812}. HldE catalyzes two reactions in the PWY0-1241 pathway, which provides one of the building blocks for the inner core region of lipopolysaccharide (LPS) . The bifunctionality of HldE results from a fusion of an N-terminal ribokinase superfamily domain and a C-terminal cytidylyltransferase superfamily domain; the two domains are genetically and physically separable . Structural modelling of the ribokinase domain led to the identification of amino acid residues potentially essential for catalysis. Site-directed mutagenesis of potential ATP binding site residues resulted in a dominant negative mutant phenotype . In a genetic screen for heptoseless mutants, a transposon insertion in the hldE gene was identified . Based on increased expression of sulA as a reporter gene, a ΔhldE mutant is more sensitive to exposure to the genotoxic agents nalidixic acid and mitomycin C than wild type...

## Biological Role

Component of fused heptose 7-phosphate kinase/heptose 1-phosphate adenyltransferase (complex.ecocyc.CPLX0-3661).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Catalyzes the phosphorylation of D-glycero-D-manno-heptose 7-phosphate at the C-1 position to selectively form D-glycero-beta-D-manno-heptose-1,7-bisphosphate. {ECO:0000269|PubMed:11751812}.; FUNCTION: Catalyzes the ADP transfer from ATP to D-glycero-beta-D-manno-heptose 1-phosphate, yielding ADP-D-glycero-beta-D-manno-heptose. {ECO:0000269|PubMed:11751812}.

## Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3661|complex.ecocyc.CPLX0-3661]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3052|gene.b3052]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76658`
- `KEGG:ecj:JW3024;eco:b3052;ecoc:C3026_16675;`
- `GeneID:75173174;75205361;947548;`
- `GO:GO:0005524; GO:0005829; GO:0009244; GO:0016773; GO:0033785; GO:0033786; GO:0042803; GO:0097171`
- `EC:2.7.1.167; 2.7.7.70`

## Notes

Bifunctional protein HldE [Includes: D-beta-D-heptose 7-phosphate kinase (EC 2.7.1.167) (D-beta-D-heptose 7-phosphotransferase) (D-glycero-beta-D-manno-heptose-7-phosphate kinase); D-beta-D-heptose 1-phosphate adenylyltransferase (EC 2.7.7.70) (D-glycero-beta-D-manno-heptose 1-phosphate adenylyltransferase)]
