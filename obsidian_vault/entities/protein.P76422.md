---
entity_id: "protein.P76422"
entity_type: "protein"
name: "thiD"
source_database: "UniProt"
source_id: "P76422"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "thiD thiJ b2103 JW2090"
---

# thiD

`protein.P76422`

## Static

- Type: `protein`
- Source: `UniProt:P76422`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the phosphorylation of hydroxymethylpyrimidine phosphate (HMP-P) to HMP-PP, and of HMP to HMP-P. Shows no activity with pyridoxal, pyridoxamine or pyridoxine. {ECO:0000269|PubMed:10075431}. The bifunctional hydroxymethylpyrimidine (HMP) kinase/phosphomethylpyrimidine (HMP-P) kinase (ThiD) is involved in the biosynthesis of the essential cofactor thiamine pyrophosphate. The two phosphorylation reactions appear to be successive, with transient formation of HMP-P . Modeling of the phosphorylation reactions based on the crystal structure of the Salmonella Typhimurium enzyme suggest an inline replacement mechanism . While reported that ThiD is a monomer (31 kDa) in solution, suggested that ThiD as well as PdxK (which is in fact a homodimer) are homotetramers. The Salmonella homolog is 91% identical to E. coli ThiD and forms a homodimer. A thiD mutant requires thiamine supplementation . E. coli encodes two enzymes with HMP kinase activity: ThiD (described here) and PDXK-CPLX PdxK. A thiD pdxK double mutant lacks all HMP kinase activity . Under anaerobiosis, FNR represses thiD expression, but it is not known if this regulation is direct or indirect . ThiD: ThiJ: Reviews:

## Biological Role

Component of hydroxymethylpyrimidine kinase / phosphomethylpyrimidine kinase (complex.ecocyc.HMP-P-KIN-CPLX).

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the phosphorylation of hydroxymethylpyrimidine phosphate (HMP-P) to HMP-PP, and of HMP to HMP-P. Shows no activity with pyridoxal, pyridoxamine or pyridoxine. {ECO:0000269|PubMed:10075431}.

## Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.HMP-P-KIN-CPLX|complex.ecocyc.HMP-P-KIN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2103|gene.b2103]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76422`
- `KEGG:ecj:JW2090;eco:b2103;ecoc:C3026_11800;`
- `GeneID:93775091;946459;`
- `GO:GO:0005524; GO:0005829; GO:0008902; GO:0008972; GO:0009228; GO:0009229; GO:0036172`
- `EC:2.7.1.49; 2.7.4.7`

## Notes

Hydroxymethylpyrimidine/phosphomethylpyrimidine kinase (EC 2.7.1.49) (EC 2.7.4.7) (Hydroxymethylpyrimidine kinase) (HMP kinase) (Hydroxymethylpyrimidine phosphate kinase) (HMP-P kinase) (HMP-phosphate kinase) (HMPP kinase)
