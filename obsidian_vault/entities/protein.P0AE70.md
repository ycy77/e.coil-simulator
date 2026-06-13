---
entity_id: "protein.P0AE70"
entity_type: "protein"
name: "mazF"
source_database: "UniProt"
source_id: "P0AE70"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mazF chpA chpAK b2782 JW2753"
---

# mazF

`protein.P0AE70`

## Static

- Type: `protein`
- Source: `UniProt:P0AE70`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system. A sequence-specific endoribonuclease it inhibits protein synthesis by cleaving mRNA and inducing bacterial stasis. It is stable, single-strand specific with mRNA cleavage independent of the ribosome, although translation enhances cleavage for some mRNAs (PubMed:18854355). Cleavage occurs at the 5'-end of ACA sequences, yielding a 2',3'-cyclic phosphate and a free 5'-OH, although cleavage can also occur on the 3'-end of the first A (PubMed:15537630, PubMed:23280569). Digests 16S rRNA in vivo 43 nts upstream of the C-terminus; this removes the anti-Shine-Dalgarno sequence forming a mixed population of wild-type and 'stress ribosomes'. Stress ribosomes do not translate leader-containing mRNA but are proficient in translation of leaderless mRNA, which alters the protein expression profile of the cell; MazF produces some leaderless mRNA (PubMed:21944167). The toxic endoribonuclease activity is inhibited by its labile cognate antitoxin MazE. Toxicity results when the levels of MazE decrease in the cell, leading to mRNA degradation. This effect can be rescued by expression of MazE, but after 6 hours in rich medium overexpression of MazF leads to programmed cell death (PubMed:11222603, PubMed:8650219)...

## Biological Role

Component of MazF toxin of the MazF-MazE toxin-antitoxin system that exhibits ribonuclease activity (complex.ecocyc.CPLX0-1241), MazE-MazF antitoxin/toxin complex / DNA-binding transcriptional repressor (complex.ecocyc.CPLX0-1242).

## Annotation

FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system. A sequence-specific endoribonuclease it inhibits protein synthesis by cleaving mRNA and inducing bacterial stasis. It is stable, single-strand specific with mRNA cleavage independent of the ribosome, although translation enhances cleavage for some mRNAs (PubMed:18854355). Cleavage occurs at the 5'-end of ACA sequences, yielding a 2',3'-cyclic phosphate and a free 5'-OH, although cleavage can also occur on the 3'-end of the first A (PubMed:15537630, PubMed:23280569). Digests 16S rRNA in vivo 43 nts upstream of the C-terminus; this removes the anti-Shine-Dalgarno sequence forming a mixed population of wild-type and 'stress ribosomes'. Stress ribosomes do not translate leader-containing mRNA but are proficient in translation of leaderless mRNA, which alters the protein expression profile of the cell; MazF produces some leaderless mRNA (PubMed:21944167). The toxic endoribonuclease activity is inhibited by its labile cognate antitoxin MazE. Toxicity results when the levels of MazE decrease in the cell, leading to mRNA degradation. This effect can be rescued by expression of MazE, but after 6 hours in rich medium overexpression of MazF leads to programmed cell death (PubMed:11222603, PubMed:8650219). MazF-mediated cell death occurs following a number of stress conditions in a relA-dependent fashion and only when cells are in log phase; sigma factor S (rpoS) protects stationary phase cells from MazF-killing (PubMed:15150257, PubMed:19251848). Cell growth and viability are not affected when MazF and MazE are coexpressed. Both MazE and MazE-MazF bind to the promoter region of the mazE-mazF operon to inhibit their own transcription. MazE has higher affinity for promoter DNA in the presence of MazF (PubMed:25564525). Cross-talk can occur between different TA systems, ectopic expression of this toxin induces transcription of the relBEF TA system operon with specific cleavage of the mRNA produced (PubMed:23432955). {ECO:0000269|PubMed:11071896, ECO:0000269|PubMed:11222603, ECO:0000269|PubMed:15150257, ECO:0000269|PubMed:15537630, ECO:0000269|PubMed:18854355, ECO:0000269|PubMed:19251848, ECO:0000269|PubMed:21944167, ECO:0000269|PubMed:23280569, ECO:0000269|PubMed:23432955, ECO:0000269|PubMed:25564525, ECO:0000269|PubMed:8650219}.; FUNCTION: Might also serve to protect cells against bacteriophage; in the presence of MazE-MazF fewer P1 phages are produced than in a disrupted strain. For strain K38 most wild-type cells are killed but not by phage lysis; it was suggested that MazE-MazF causes P1 phage exclusion from the bacterial population. This phenomenon is strain dependent. {ECO:0000269|PubMed:15316771}.; FUNCTION: The physiological role of this TA system is debated. Programmed cell death (PCD) occurs when cells are at high density and depends on the presence of MazE-MazF and a quorum sensing pentapeptide, the extracellular death factor (EDF) with sequence Asn-Asn-Trp-Asn-Asn (NNWNN), probably produced from the zwf gene product glucose-6-phosphate 1-dehydrogenase (PubMed:17962566, PubMed:18310334). Cell death governed by the MazE-MazF and DinJ-YafQ TA systems seems to play a role in biofilm formation, while MazE-MazF is also implicated in cell death in liquid media (PubMed:19707553). Implicated in hydroxy radical-mediated cell death induced by hydroxyurea treatment (PubMed:20005847, PubMed:23416055). In conjunction with EDF prevents apoptotic-like death (ALD) in the presence of DNA damaging agents, probably by reducing recA mRNA levels in a non-endonuclease-mediated manner (PubMed:22412352). Other studies (in strains BW25113 and MC4100, the latter makes EDF) demonstrate MazF does not cause PCD but instead bacteriostasis and possibly a dormant state as well as persister cell generation (PubMed:24375411). {ECO:0000269|PubMed:17962566, ECO:0000269|PubMed:18310334, ECO:0000269|PubMed:19707553, ECO:0000269|PubMed:20005847, ECO:0000269|PubMed:21419338, ECO:0000269|PubMed:22412352, ECO:0000269|PubMed:23416055, ECO:0000269|PubMed:24375411, ECO:0000269|PubMed:8650219}.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1241|complex.ecocyc.CPLX0-1241]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-1242|complex.ecocyc.CPLX0-1242]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2782|gene.b2782]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AE70`
- `KEGG:ecj:JW2753;eco:b2782;ecoc:C3026_15285;`
- `GeneID:93779216;947252;`
- `GO:GO:0003677; GO:0003723; GO:0004521; GO:0006355; GO:0006402; GO:0006417; GO:0009372; GO:0016075; GO:0016787; GO:0030308; GO:0032991; GO:0040008; GO:0042803; GO:0043068; GO:0044010; GO:0044877; GO:0051607; GO:0110001; GO:0140677`
- `EC:3.1.27.-`

## Notes

Endoribonuclease toxin MazF (EC 3.1.27.-) (Toxin MazF) (mRNA interferase MazF)
