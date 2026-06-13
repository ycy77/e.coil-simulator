---
entity_id: "protein.P33647"
entity_type: "protein"
name: "chpB"
source_database: "UniProt"
source_id: "P33647"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "chpB chpBK yjfE b4225 JW4184"
---

# chpB

`protein.P33647`

## Static

- Type: `protein`
- Source: `UniProt:P33647`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system. ChpB is a sequence-specific mRNA and (weak) tmRNA endoribonuclease that inhibits protein synthesis and induces bacterial stasis. Cleavage is independent of the ribosome. Cleavage occurs at ACY sequences where Y is not C. The endoribonuclease activity is not as strong as that of MazF. The endoribonuclease activity (a toxin) is inhibited by its labile cognate antitoxin ChpS. Toxicity results when the levels of ChpS decrease in the cell, leading to mRNA degradation. Both ChpS and ChpB probably bind to the promoter region of the chpS-chpB operon to autoregulate their synthesis. {ECO:0000269|PubMed:12972253, ECO:0000269|PubMed:16413033, ECO:0000269|PubMed:21419338, ECO:0000269|PubMed:8226627}. ChpB is the toxin component of the ChpB-ChpS toxin-antitoxin system. ChpB inhibits cell growth when it is overexpressed, or when its partner protein ChpS is absent . This growth inhibition effect appears to result from ChpB's ability to cleave RNAs. Identified cleavage targets include RNAs from era, mazG, and translated tmRNA . Increased tmRNA abundance blocks the growth inhibition effects of ChpB, and loss of tmRNA leads to increased sensitivity to ChpB . An analysis of the targets and site specificity of ChpB showed cleavage site specificity, cleaving between the U and A nucleotides of a UAC motif. Like other E...

## Biological Role

Catalyzes RXN-19924 (reaction.ecocyc.RXN-19924). Component of ChpB-ChpS complex (complex.ecocyc.CPLX0-7561).

## Annotation

FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system. ChpB is a sequence-specific mRNA and (weak) tmRNA endoribonuclease that inhibits protein synthesis and induces bacterial stasis. Cleavage is independent of the ribosome. Cleavage occurs at ACY sequences where Y is not C. The endoribonuclease activity is not as strong as that of MazF. The endoribonuclease activity (a toxin) is inhibited by its labile cognate antitoxin ChpS. Toxicity results when the levels of ChpS decrease in the cell, leading to mRNA degradation. Both ChpS and ChpB probably bind to the promoter region of the chpS-chpB operon to autoregulate their synthesis. {ECO:0000269|PubMed:12972253, ECO:0000269|PubMed:16413033, ECO:0000269|PubMed:21419338, ECO:0000269|PubMed:8226627}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-19924|reaction.ecocyc.RXN-19924]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-7561|complex.ecocyc.CPLX0-7561]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4225|gene.b4225]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33647`
- `KEGG:ecj:JW4184;eco:b4225;ecoc:C3026_22815;`
- `GeneID:948747;`
- `GO:GO:0003677; GO:0003723; GO:0004521; GO:0006355; GO:0006402; GO:0016075; GO:0016891; GO:0030308; GO:0040008; GO:0043488; GO:0044010; GO:0110001`
- `EC:3.1.-.-`

## Notes

Endoribonuclease toxin ChpB (EC 3.1.-.-) (Toxin ChpB) (mRNA interferase ChpB)
