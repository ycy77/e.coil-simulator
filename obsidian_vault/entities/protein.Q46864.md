---
entity_id: "protein.Q46864"
entity_type: "protein"
name: "mqsA"
source_database: "UniProt"
source_id: "Q46864"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mqsA ygiT b3021 JW2989"
---

# mqsA

`protein.Q46864`

## Static

- Type: `protein`
- Source: `UniProt:Q46864`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. Labile antitoxin that binds to the MqsR mRNA interferase toxin and neutralizes its endoribonuclease activity. Overexpression prevents MqsR-mediated cessation of cell growth and inhibition of cell proliferation. Initially reported to act as a cotranscription factor with MqsA (PubMed:19690171, PubMed:20105222). Following further experiments, the MqsR-MqsA complex does not bind DNA and all reported data are actually due to a small fraction of free MqsA alone binding DNA. Addition of MqsR to a preformed MqsA-promoter DNA complex causes dissociation of the MqsA-DNA complex, probably causing derepression of MqsA-repressed transcripts (PubMed:23172222). MqsA binds to 2 palindromes in the promoter region of the mqsRA operon activating its transcription. Binds to other promoters, inducing mcbR and spy and repressing cspD among others (PubMed:20105222). Binds to and represses the rpoS promoter, the master stress regulator, resulting in decreased cyclic-di-GMP, reduced stress resistance, increased cell motility and decreased biofilm formation; in these experiments 5 TA systems are missing (lacks MazEF, RelEB, ChpB, YoeB-YefM, YafQ-DinJ) (PubMed:21516113)...

## Biological Role

Component of MqsA-MqsR antitoxin/toxin complex (complex.ecocyc.CPLX0-7822).

## Annotation

FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. Labile antitoxin that binds to the MqsR mRNA interferase toxin and neutralizes its endoribonuclease activity. Overexpression prevents MqsR-mediated cessation of cell growth and inhibition of cell proliferation. Initially reported to act as a cotranscription factor with MqsA (PubMed:19690171, PubMed:20105222). Following further experiments, the MqsR-MqsA complex does not bind DNA and all reported data are actually due to a small fraction of free MqsA alone binding DNA. Addition of MqsR to a preformed MqsA-promoter DNA complex causes dissociation of the MqsA-DNA complex, probably causing derepression of MqsA-repressed transcripts (PubMed:23172222). MqsA binds to 2 palindromes in the promoter region of the mqsRA operon activating its transcription. Binds to other promoters, inducing mcbR and spy and repressing cspD among others (PubMed:20105222). Binds to and represses the rpoS promoter, the master stress regulator, resulting in decreased cyclic-di-GMP, reduced stress resistance, increased cell motility and decreased biofilm formation; in these experiments 5 TA systems are missing (lacks MazEF, RelEB, ChpB, YoeB-YefM, YafQ-DinJ) (PubMed:21516113). An earlier study showed overexpression alone increases biofilm formation, perhaps by repressing cspD; in these experiments the 5 TA systems are present (PubMed:20105222). Represses the csgD promoter. In the presence of stress, when this protein is degraded, the promoters it represses are derepressed, leading to biofilm formation (Probable). This TA system mediates cell growth during bile acid deoxycholate stress by degrading mRNA for probable deoxycholate-binding protein YgiS; bile acid detergents such as deoxycholate are important for host defense against bacterial growth in the gall bladder and duodenum (PubMed:25534751). {ECO:0000269|PubMed:19690171, ECO:0000269|PubMed:19943910, ECO:0000269|PubMed:20105222, ECO:0000269|PubMed:21516113, ECO:0000269|PubMed:23172222, ECO:0000269|PubMed:25534751, ECO:0000303|PubMed:24212724}.

## Outgoing Edges (9)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7822|complex.ecocyc.CPLX0-7822]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b0880|gene.b0880]] `RegulonDB` `S` - regulator=MqsA; target=cspD; function=-
- `represses` --> [[gene.b1037|gene.b1037]] `RegulonDB` `S` - regulator=MqsA; target=csgG; function=-
- `represses` --> [[gene.b1038|gene.b1038]] `RegulonDB` `S` - regulator=MqsA; target=csgF; function=-
- `represses` --> [[gene.b1039|gene.b1039]] `RegulonDB` `S` - regulator=MqsA; target=csgE; function=-
- `represses` --> [[gene.b1040|gene.b1040]] `RegulonDB` `S` - regulator=MqsA; target=csgD; function=-
- `represses` --> [[gene.b2741|gene.b2741]] `RegulonDB` `C` - regulator=MqsA; target=rpoS; function=-
- `represses` --> [[gene.b3021|gene.b3021]] `RegulonDB` `S` - regulator=MqsA; target=mqsA; function=-
- `represses` --> [[gene.b3022|gene.b3022]] `RegulonDB` `S` - regulator=MqsA; target=mqsR; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3021|gene.b3021]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46864`
- `KEGG:ecj:JW2989;eco:b3021;ecoc:C3026_16505;`
- `GeneID:945814;`
- `GO:GO:0006355; GO:0042803; GO:0043565; GO:0044010; GO:0046872; GO:0110001`

## Notes

Antitoxin MqsA
