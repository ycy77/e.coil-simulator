---
entity_id: "protein.P0AG24"
entity_type: "protein"
name: "spoT"
source_database: "UniProt"
source_id: "P0AG24"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:17616600}. Note=Is associated with pre-50S ribosomal subunits in a salt-dependent manner."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "spoT b3650 JW3625"
---

# spoT

`protein.P0AG24`

## Static

- Type: `protein`
- Source: `UniProt:P0AG24`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:17616600}. Note=Is associated with pre-50S ribosomal subunits in a salt-dependent manner.

## Enriched Summary

FUNCTION: In eubacteria ppGpp (guanosine 3'-diphosphate 5'-diphosphate) is a mediator of the stringent response which coordinates a variety of cellular activities in response to changes in nutritional abundance. This enzyme catalyzes both the synthesis and degradation of ppGpp. The second messengers ppGpp and c-di-GMP together control biofilm formation in response to translational stress; ppGpp represses biofilm formation while c-di-GMP induces it. ppGpp activates transcription of CsrA-antagonistic small RNAs CsrB and CsrC, which down-regulate CsrA's action on translation during the stringent response (PubMed:21488981). {ECO:0000269|PubMed:14622409, ECO:0000269|PubMed:19460094, ECO:0000269|PubMed:21488981}. SpoT is a key enzyme involved in the stringent response in Escherichia coli. It is a bifunctional enzyme with both hydrolase and synthetase activities . The ppGpp hydrolase activity of SpoT has a major physiological role in ppGpp degradation and is inhibited under conditions of physiological stress. Its amino acid sequence has been shown to be extensively related to that of RelA . RelA is involved in the E. coli stringent response triggered by amino acid starvation, activating (p)ppGpp synthesis via a ribosomal mechanism . SpoT provides the hydrolase activity for this RelA-dependent synthetase activity...

## Biological Role

Catalyzes guanosine-3',5'-bis(diphosphate) 3'-diphosphohydrolase (reaction.R00336), ATP:GTP 3'-diphosphotransferase (reaction.R00429), GDPPYPHOSKIN-RXN (reaction.ecocyc.GDPPYPHOSKIN-RXN), PPGPPSYN-RXN (reaction.ecocyc.PPGPPSYN-RXN), RXN0-6427 (reaction.ecocyc.RXN0-6427). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: In eubacteria ppGpp (guanosine 3'-diphosphate 5'-diphosphate) is a mediator of the stringent response which coordinates a variety of cellular activities in response to changes in nutritional abundance. This enzyme catalyzes both the synthesis and degradation of ppGpp. The second messengers ppGpp and c-di-GMP together control biofilm formation in response to translational stress; ppGpp represses biofilm formation while c-di-GMP induces it. ppGpp activates transcription of CsrA-antagonistic small RNAs CsrB and CsrC, which down-regulate CsrA's action on translation during the stringent response (PubMed:21488981). {ECO:0000269|PubMed:14622409, ECO:0000269|PubMed:19460094, ECO:0000269|PubMed:21488981}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.R00336|reaction.R00336]] `KEGG` `database` - via EC:3.1.7.2
- `catalyzes` --> [[reaction.R00429|reaction.R00429]] `KEGG` `database` - via EC:2.7.6.5
- `catalyzes` --> [[reaction.ecocyc.GDPPYPHOSKIN-RXN|reaction.ecocyc.GDPPYPHOSKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PPGPPSYN-RXN|reaction.ecocyc.PPGPPSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6427|reaction.ecocyc.RXN0-6427]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3650|gene.b3650]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AG24`
- `KEGG:ecj:JW3625;eco:b3650;`
- `GeneID:93778365;948159;`
- `GO:GO:0005829; GO:0008728; GO:0008893; GO:0015949; GO:0015969; GO:0015970; GO:0016301; GO:0042594`
- `EC:2.7.6.5; 3.1.7.2`

## Notes

Bifunctional (p)ppGpp synthase/hydrolase SpoT [Includes: GTP pyrophosphokinase (EC 2.7.6.5) ((p)ppGpp synthase) (ATP:GTP 3'-pyrophosphotransferase) (Stringent response-like protein) (ppGpp synthase II); Guanosine-3',5'-bis(diphosphate) 3'-pyrophosphohydrolase (EC 3.1.7.2) (Penta-phosphate guanosine-3'-pyrophosphohydrolase) ((ppGpp)ase)]
