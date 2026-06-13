---
entity_id: "protein.P21189"
entity_type: "protein"
name: "polB"
source_database: "UniProt"
source_id: "P21189"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "polB dinA b0060 JW0059"
---

# polB

`protein.P21189`

## Static

- Type: `protein`
- Source: `UniProt:P21189`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Thought to be involved in DNA repair and/or mutagenesis. Its processivity is enhanced by the beta sliding clamp (dnaN) and clamp loader (PubMed:1534562, PubMed:1999435). {ECO:0000269|PubMed:1534562, ECO:0000269|PubMed:1999435}. DNA polymerase II (Pol II) is a combined polymerase and exonuclease involved in replication restart following UV exposure, translesion synthesis and nucleotide excision repair. Pol II catalyzes both a DNA polymerase activity and a 3' to 5' exonuclease activity . Pol II is also required for rapid restart of DNA replication following UV irradiation . In addition to its role in translesion bypass, discussed below, Pol II is required for a nucleotide excision repair pathway that fixes DNA crosslinks . Pol II also plays a role in surviving thymine dimers and avoiding the mutagenic effects of agents such as peroxide . Pol II tends to make more errors in replication of AT-rich sequences, which differs from the behavior of most other DNA polymerases . Pol II allows replication to bypass some kinds of DNA lesions. Under certain conditions Pol II is required for bypass of abasic lesions . This bypass increases when Pol II exonuclease activity is disabled . Pol II can also bypass 3,N(4)-ethenocytosine lesions and carries out mutagenic bypass of 2-acetylaminofluorene-induced lesions, the latter resulting in -2 frameshifts...

## Biological Role

Catalyzes deoxyadenosine 5'-triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00375), deoxyguanosine 5'-triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00376), deoxycytidine triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00377), deoxythymidine triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00378), deoxynucleoside triphosphate:DNA deoxynucleotidyltransferase (reaction.R00379), DNA-DIRECTED-DNA-POLYMERASE-RXN (reaction.ecocyc.DNA-DIRECTED-DNA-POLYMERASE-RXN), RXN0-4961 (reaction.ecocyc.RXN0-4961). Bound by Magnesium cation (molecule.C00305).

## Annotation

FUNCTION: Thought to be involved in DNA repair and/or mutagenesis. Its processivity is enhanced by the beta sliding clamp (dnaN) and clamp loader (PubMed:1534562, PubMed:1999435). {ECO:0000269|PubMed:1534562, ECO:0000269|PubMed:1999435}.

## Outgoing Edges (7)

- `catalyzes` --> [[reaction.R00375|reaction.R00375]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.R00376|reaction.R00376]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.R00377|reaction.R00377]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.R00378|reaction.R00378]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.R00379|reaction.R00379]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.ecocyc.DNA-DIRECTED-DNA-POLYMERASE-RXN|reaction.ecocyc.DNA-DIRECTED-DNA-POLYMERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-4961|reaction.ecocyc.RXN0-4961]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0060|gene.b0060]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P21189`
- `KEGG:ecj:JW0059;eco:b0060;`
- `GeneID:944779;`
- `GO:GO:0000166; GO:0003677; GO:0003887; GO:0006261; GO:0008296; GO:0009432; GO:0045004`
- `EC:2.7.7.7`

## Notes

DNA polymerase II (Pol II) (EC 2.7.7.7)
