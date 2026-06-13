---
entity_id: "protein.P05637"
entity_type: "protein"
name: "apaH"
source_database: "UniProt"
source_id: "P05637"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "apaH b0049 JW0048"
---

# apaH

`protein.P05637`

## Static

- Type: `protein`
- Source: `UniProt:P05637`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Hydrolyzes diadenosine 5',5'''-P1,P4-tetraphosphate to yield ADP. {ECO:0000269|PubMed:6317672}. Diadenosine tetraphosphate (Ap4A) is a side product of aminoacyl-tRNA synthetases, including E. coli LYSU-CPLX LysU. Diadenosine tetraphosphatase (diadenosine 5', 5'''-P1, P4-tetraphosphate pyrophosphohydrolase, ApaH) hydrolyzes Ap4A and related molecules . ApaH decaps RNA molecules that contain Ap4 and Gp4 caps at the 5' end, generating a diphosphorylated RNA product . It has also been shown that ApaH can cleave both methylated and non-methylated NpnN caps . Epistasis experiments suggest an RNA decay pathway involving the consecutive actions of ApaH followed by G7459-MONOMER RppH, triggering the degradation of Np4-capped RNAs . Substrate specificity and reaction kinetics have been examined . ApaH cleaves after the second phosphate group of the adenosine moiety . Hydrolysis of, and potential inhibition by, pppGpp, a "Magic Spot Nucleotide" involved in the stringent response was observed for ApaH despite the lack of a Nudix hydrolase domain . An apaH mutation leads to elevated levels of Ap4A , loss of motility due to a decrease in σF-mediated gene expression, and decreased expression of cAMP-CRP-regulated genes . An apaH mutant exhibits decreased heat resistance that can be suppressed by ClpB overproduction , and decreased resistance to mild acid stress...

## Biological Role

Catalyzes P1,P4-bis(5'-adenosyl)-tetraphosphate nucleotidebisphosphohydrolase (reaction.R00125), 3.6.1.41-RXN (reaction.ecocyc.3.6.1.41-RXN), PPPGPPHYDRO-RXN (reaction.ecocyc.PPPGPPHYDRO-RXN).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Hydrolyzes diadenosine 5',5'''-P1,P4-tetraphosphate to yield ADP. {ECO:0000269|PubMed:6317672}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00125|reaction.R00125]] `KEGG` `database` - via EC:3.6.1.41
- `catalyzes` --> [[reaction.ecocyc.3.6.1.41-RXN|reaction.ecocyc.3.6.1.41-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PPPGPPHYDRO-RXN|reaction.ecocyc.PPPGPPHYDRO-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0049|gene.b0049]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P05637`
- `KEGG:ecj:JW0048;eco:b0049;ecoc:C3026_00255;`
- `GeneID:93777386;944770;`
- `GO:GO:0005737; GO:0008796; GO:0008803; GO:0010165; GO:0015949; GO:0016787; GO:0016791; GO:0110154`
- `EC:3.6.1.41`

## Notes

Bis(5'-nucleosyl)-tetraphosphatase [symmetrical] (EC 3.6.1.41) (Ap4A hydrolase) (Diadenosine 5',5'''-P1,P4-tetraphosphate pyrophosphohydrolase) (Diadenosine tetraphosphatase)
