---
entity_id: "protein.Q46865"
entity_type: "protein"
name: "mqsR"
source_database: "UniProt"
source_id: "Q46865"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mqsR ygiU b3022 JW2990"
---

# mqsR

`protein.Q46865`

## Static

- Type: `protein`
- Source: `UniProt:Q46865`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system. Plays a significant role in the control of biofilm formation and induction of persister cells in the presence of antibiotics. An mRNA interferase which has been reported to be translation-independent (PubMed:19690171, PubMed:19943910, PubMed:23289863). It has also been reported to be translation-dependent (PubMed:20041169). Cleavage has been reported to occur on either side of G in the sequence GCU (PubMed:19690171). Also reported to cleave after C in GC(A/U) sequences (PubMed:19943910). There are only 14 genes in E.coli W3110 (and probably also MG1655) that do not have a GCU sequence and thus are resistant to the mRNA interferase activity; among these is the gene for toxin GhoT. Overexpression of MqsR causes cessation of cell growth and inhibits cell proliferation via inhibition of translation as well as increasing persister cell formation; these effects are overcome by concomitant or subsequent expression of antitoxin MqsA. Cross-talk can occur between different TA systems. Ectopic expression of this toxin induces transcription of the relBEF TA system operon with specific cleavage of the relBEF mRNA produced (PubMed:23432955). Regulates the expression of GhoT/GhoS, a type V TA system (PubMed:23289863)...

## Biological Role

Catalyzes RXN0-5509 (reaction.ecocyc.RXN0-5509). Component of MqsA-MqsR antitoxin/toxin complex (complex.ecocyc.CPLX0-7822).

## Annotation

FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system. Plays a significant role in the control of biofilm formation and induction of persister cells in the presence of antibiotics. An mRNA interferase which has been reported to be translation-independent (PubMed:19690171, PubMed:19943910, PubMed:23289863). It has also been reported to be translation-dependent (PubMed:20041169). Cleavage has been reported to occur on either side of G in the sequence GCU (PubMed:19690171). Also reported to cleave after C in GC(A/U) sequences (PubMed:19943910). There are only 14 genes in E.coli W3110 (and probably also MG1655) that do not have a GCU sequence and thus are resistant to the mRNA interferase activity; among these is the gene for toxin GhoT. Overexpression of MqsR causes cessation of cell growth and inhibits cell proliferation via inhibition of translation as well as increasing persister cell formation; these effects are overcome by concomitant or subsequent expression of antitoxin MqsA. Cross-talk can occur between different TA systems. Ectopic expression of this toxin induces transcription of the relBEF TA system operon with specific cleavage of the relBEF mRNA produced (PubMed:23432955). Regulates the expression of GhoT/GhoS, a type V TA system (PubMed:23289863). Persistence depends on toxin GhoT activity, which MqsR controls at the post-transcriptional level by selectively degrading the antitoxin ghoS segment of the ghoST mRNA (PubMed:23289863). Overexpression leads to a dramatic increase in tolerance to the antibiotic ofloxacin. This TA system mediates cell growth during bile acid deoxycholate stress by degrading mRNA for probable deoxycholate-binding protein YgiS; bile acid detergents such as deoxycholate are important for host defense against bacterial growth in the gall bladder and duodenum (PubMed:25534751). {ECO:0000269|PubMed:19690171, ECO:0000269|PubMed:19943910, ECO:0000269|PubMed:20041169, ECO:0000269|PubMed:23289863, ECO:0000269|PubMed:23432955, ECO:0000269|PubMed:25534751}.; FUNCTION: Initially reported to act as a cotranscription factor with MqsA (PubMed:19690171, PubMed:20105222). Following further experiments, the MqsR-MqsA complex does not bind DNA and all reported data are actually due to a small fraction of free MqsA alone binding DNA. Addition of MqsR to a preformed MqsA-promoter DNA complex causes dissociation of the MqsA-DNA complex, probably causing derepression of MqsA-repressed transcripts. Does not bind DNA in the presence or absence of MqsA (PubMed:23172222). {ECO:0000269|PubMed:19690171, ECO:0000269|PubMed:20105222, ECO:0000269|PubMed:23172222}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5509|reaction.ecocyc.RXN0-5509]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-7822|complex.ecocyc.CPLX0-7822]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3022|gene.b3022]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46865`
- `KEGG:ecj:JW2990;eco:b3022;ecoc:C3026_16510;`
- `GeneID:947500;`
- `GO:GO:0004521; GO:0006355; GO:0009372; GO:0016892; GO:0017148; GO:0043488; GO:0044010; GO:0045892; GO:0061157; GO:0110001; GO:2000145`
- `EC:3.1.-.-`

## Notes

mRNA interferase toxin MqsR (EC 3.1.-.-) (Endoribonuclease MqsR) (Motility quorum-sensing regulator MqsR) (Toxin MqsR)
