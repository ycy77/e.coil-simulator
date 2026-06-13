---
entity_id: "protein.Q47155"
entity_type: "protein"
name: "dinB"
source_database: "UniProt"
source_id: "Q47155"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dinB dinP b0231 JW0221"
---

# dinB

`protein.Q47155`

## Static

- Type: `protein`
- Source: `UniProt:Q47155`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Poorly processive, error-prone DNA polymerase involved in translesion repair and untargeted mutagenesis (PubMed:10488344, PubMed:10801133). Copies undamaged DNA at stalled replication forks, which arise in vivo from mismatched or misaligned primer ends. These misaligned primers can be extended by Pol IV. Exhibits no 3'-5' exonuclease (proofreading) activity (PubMed:10488344). Overexpression of Pol IV results in increased frameshift mutagenesis. It is required for stationary-phase adaptive mutation, which provides the bacterium with flexibility in dealing with environmental stress, enhancing long-term survival and evolutionary fitness. Not seen to be involved in translesion snythesis even when stimulated by the beta slding-clamp and clamp-loading complex, which do however increase non-targeted DNA polymerase efficiency 3,000-fold, may be due to targeting to stalled replication forks on nondamaged DNA (PubMed:10801133, PubMed:16168375). Involved in translesional synthesis, in conjunction with the beta clamp from PolIII (PubMed:14592985, PubMed:14729336). {ECO:0000269|PubMed:10488344, ECO:0000269|PubMed:10801133, ECO:0000269|PubMed:11080171, ECO:0000269|PubMed:11463382, ECO:0000269|PubMed:11751576, ECO:0000269|PubMed:12060704, ECO:0000269|PubMed:14592985, ECO:0000269|PubMed:16168375, ECO:0000269|PubMed:9391106, ECO:0000305|PubMed:14729336}...

## Biological Role

Catalyzes deoxyadenosine 5'-triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00375), deoxyguanosine 5'-triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00376), deoxycytidine triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00377), deoxythymidine triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00378), deoxynucleoside triphosphate:DNA deoxynucleotidyltransferase (reaction.R00379), DNA-DIRECTED-DNA-POLYMERASE-RXN (reaction.ecocyc.DNA-DIRECTED-DNA-POLYMERASE-RXN), RXN-20927 (reaction.ecocyc.RXN-20927). Bound by Magnesium cation (molecule.C00305).

## Annotation

FUNCTION: Poorly processive, error-prone DNA polymerase involved in translesion repair and untargeted mutagenesis (PubMed:10488344, PubMed:10801133). Copies undamaged DNA at stalled replication forks, which arise in vivo from mismatched or misaligned primer ends. These misaligned primers can be extended by Pol IV. Exhibits no 3'-5' exonuclease (proofreading) activity (PubMed:10488344). Overexpression of Pol IV results in increased frameshift mutagenesis. It is required for stationary-phase adaptive mutation, which provides the bacterium with flexibility in dealing with environmental stress, enhancing long-term survival and evolutionary fitness. Not seen to be involved in translesion snythesis even when stimulated by the beta slding-clamp and clamp-loading complex, which do however increase non-targeted DNA polymerase efficiency 3,000-fold, may be due to targeting to stalled replication forks on nondamaged DNA (PubMed:10801133, PubMed:16168375). Involved in translesional synthesis, in conjunction with the beta clamp from PolIII (PubMed:14592985, PubMed:14729336). {ECO:0000269|PubMed:10488344, ECO:0000269|PubMed:10801133, ECO:0000269|PubMed:11080171, ECO:0000269|PubMed:11463382, ECO:0000269|PubMed:11751576, ECO:0000269|PubMed:12060704, ECO:0000269|PubMed:14592985, ECO:0000269|PubMed:16168375, ECO:0000269|PubMed:9391106, ECO:0000305|PubMed:14729336}.

## Outgoing Edges (7)

- `catalyzes` --> [[reaction.R00375|reaction.R00375]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.R00376|reaction.R00376]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.R00377|reaction.R00377]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.R00378|reaction.R00378]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.R00379|reaction.R00379]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.ecocyc.DNA-DIRECTED-DNA-POLYMERASE-RXN|reaction.ecocyc.DNA-DIRECTED-DNA-POLYMERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-20927|reaction.ecocyc.RXN-20927]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0231|gene.b0231]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q47155`
- `KEGG:ecj:JW0221;eco:b0231;ecoc:C3026_01095;ecoc:C3026_23835;`
- `GeneID:93777162;944922;`
- `GO:GO:0000287; GO:0000731; GO:0003684; GO:0003887; GO:0005737; GO:0006261; GO:0006974; GO:0009432; GO:0042276; GO:0070987`
- `EC:2.7.7.7`

## Notes

DNA polymerase IV (Pol IV) (EC 2.7.7.7) (Translesion synthesis polymerase IV) (TSL polymerase IV)
