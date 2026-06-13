---
entity_id: "protein.P0AE72"
entity_type: "protein"
name: "mazE"
source_database: "UniProt"
source_id: "P0AE72"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mazE chpAI chpR b2783 JW2754"
---

# mazE

`protein.P0AE72`

## Static

- Type: `protein`
- Source: `UniProt:P0AE72`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. Labile antitoxin that binds to the MazF endoribonuclease toxin and neutralizes its endoribonuclease activity. Is considered to be an 'addiction' molecule as the cell dies in its absence. Toxicity results when the levels of MazE decrease in the cell, leading to mRNA degradation. This effect can be rescued by expression of MazE, but after 6 hours in rich medium the overexpression of MazF leads to programmed cell death. Cell growth and viability are not affected when MazF and MazE are coexpressed. Both MazE and MazE-MazF bind to the promoter region of the mazE-mazF operon to inhibit their own transcription (PubMed:8650219). There are 3 operators to which MazE binds (PubMed:12533537). MazE has higher affinity for promoter DNA in the presence of MazF (PubMed:25564525). {ECO:0000269|PubMed:11071896, ECO:0000269|PubMed:12123459, ECO:0000269|PubMed:12533537, ECO:0000269|PubMed:19707553, ECO:0000269|PubMed:21419338, ECO:0000269|PubMed:25564525, ECO:0000269|PubMed:8650219}.; FUNCTION: Cell death governed by the MazE-MazF and DinJ-YafQ TA systems seems to play a role in biofilm formation, while MazE-MazF is also implicated in cell death in liquid media. {ECO:0000269|PubMed:15576778, ECO:0000269|PubMed:19707553}...

## Biological Role

Component of MazE-MazF antitoxin/toxin complex / DNA-binding transcriptional repressor (complex.ecocyc.CPLX0-1242), MazE antitoxin of the MazF-MazE toxin-antitoxin system / DNA-binding transcriptional repressor (complex.ecocyc.CPLX0-841).

## Annotation

FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. Labile antitoxin that binds to the MazF endoribonuclease toxin and neutralizes its endoribonuclease activity. Is considered to be an 'addiction' molecule as the cell dies in its absence. Toxicity results when the levels of MazE decrease in the cell, leading to mRNA degradation. This effect can be rescued by expression of MazE, but after 6 hours in rich medium the overexpression of MazF leads to programmed cell death. Cell growth and viability are not affected when MazF and MazE are coexpressed. Both MazE and MazE-MazF bind to the promoter region of the mazE-mazF operon to inhibit their own transcription (PubMed:8650219). There are 3 operators to which MazE binds (PubMed:12533537). MazE has higher affinity for promoter DNA in the presence of MazF (PubMed:25564525). {ECO:0000269|PubMed:11071896, ECO:0000269|PubMed:12123459, ECO:0000269|PubMed:12533537, ECO:0000269|PubMed:19707553, ECO:0000269|PubMed:21419338, ECO:0000269|PubMed:25564525, ECO:0000269|PubMed:8650219}.; FUNCTION: Cell death governed by the MazE-MazF and DinJ-YafQ TA systems seems to play a role in biofilm formation, while MazE-MazF is also implicated in cell death in liquid media. {ECO:0000269|PubMed:15576778, ECO:0000269|PubMed:19707553}.; FUNCTION: Might also serve to protect cells against bacteriophage; in the presence of MazE-MazF fewer P1 phage are produced than in a disrupted strain. For strain K38 most wild-type cells are killed but not by phage lysis; it was suggested that MazE-MazF causes P1 phage exclusion from the bacterial population. This phenomenon is strain dependent. {ECO:0000269|PubMed:15316771}.

## Outgoing Edges (5)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1242|complex.ecocyc.CPLX0-1242]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-841|complex.ecocyc.CPLX0-841]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b2781|gene.b2781]] `RegulonDB` `S` - regulator=MazE; target=mazG; function=-
- `represses` --> [[gene.b2782|gene.b2782]] `RegulonDB` `S` - regulator=MazE; target=mazF; function=-
- `represses` --> [[gene.b2783|gene.b2783]] `RegulonDB` `S` - regulator=MazE; target=mazE; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b2783|gene.b2783]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AE72`
- `KEGG:ecj:JW2754;eco:b2783;ecoc:C3026_15290;`
- `GeneID:93779215;947245;`
- `GO:GO:0003690; GO:0006355; GO:0032991; GO:0040008; GO:0042803; GO:0044010; GO:0044877; GO:0097351; GO:0110001`

## Notes

Antitoxin MazE
