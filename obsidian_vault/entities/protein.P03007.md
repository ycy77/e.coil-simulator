---
entity_id: "protein.P03007"
entity_type: "protein"
name: "dnaQ"
source_database: "UniProt"
source_id: "P03007"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dnaQ mutD b0215 JW0205"
---

# dnaQ

`protein.P03007`

## Static

- Type: `protein`
- Source: `UniProt:P03007`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: DNA polymerase III is a complex, multichain enzyme responsible for most of the replicative synthesis in bacteria. The epsilon subunit contain the editing function and is a proofreading 3'-5' exonuclease (PubMed:6340117). Contacts both the beta sliding clamp (dnaN) and the polymerase subunit (dnaE), stabilizing their interaction (PubMed:26499492). {ECO:0000269|PubMed:26499492, ECO:0000269|PubMed:6340117}. The epsilon subunit of DNA polymerase III catalyzes the 3' to 5' proofreading exonuclease activity of the holoenzyme . This activity is required to prevent spontaneous mutations and may play a role in preventing UV mutagenesis and lesion bypass synthesis as well . The epsilon subunit suppresses both misincorporation of dCMP and transversion mutations . Episilon isrequired for speed and processivity of DNA polymerase III function . In the presence of polymerase III alpha subunit, epsilon activity increases ten- to eighty-fold, and its affinity for the 3'-hydroxy terminus of DNA increases substantially . Single-stranded DNA binding protein inhibits epsilon activity during replication . The structure of epsilon complexed with a bacteriophage homolog of theta has been determined to 2.1 Å . dnaQ is induced following exposure to various mutagenic and DNA-damaging substances, often in an SOS-response-dependent manner...

## Biological Role

Catalyzes deoxyadenosine 5'-triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00375), deoxyguanosine 5'-triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00376), deoxycytidine triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00377), deoxythymidine triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00378), deoxynucleoside triphosphate:DNA deoxynucleotidyltransferase (reaction.R00379), RXN0-4961 (reaction.ecocyc.RXN0-4961). Component of replisome (complex.ecocyc.CPLX0-13320), DNA polymerase III, core enzyme (complex.ecocyc.CPLX0-2361), DNA polymerase III, holoenzyme (complex.ecocyc.CPLX0-3803).

## Enriched Pathways

- `eco03030` DNA replication (KEGG)
- `eco03430` Mismatch repair (KEGG)
- `eco03440` Homologous recombination (KEGG)

## Annotation

FUNCTION: DNA polymerase III is a complex, multichain enzyme responsible for most of the replicative synthesis in bacteria. The epsilon subunit contain the editing function and is a proofreading 3'-5' exonuclease (PubMed:6340117). Contacts both the beta sliding clamp (dnaN) and the polymerase subunit (dnaE), stabilizing their interaction (PubMed:26499492). {ECO:0000269|PubMed:26499492, ECO:0000269|PubMed:6340117}.

## Pathways

- `eco03030` DNA replication (KEGG)
- `eco03430` Mismatch repair (KEGG)
- `eco03440` Homologous recombination (KEGG)

## Outgoing Edges (9)

- `catalyzes` --> [[reaction.R00375|reaction.R00375]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.R00376|reaction.R00376]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.R00377|reaction.R00377]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.R00378|reaction.R00378]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.R00379|reaction.R00379]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.ecocyc.RXN0-4961|reaction.ecocyc.RXN0-4961]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-13320|complex.ecocyc.CPLX0-13320]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3
- `is_component_of` --> [[complex.ecocyc.CPLX0-2361|complex.ecocyc.CPLX0-2361]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-3803|complex.ecocyc.CPLX0-3803]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b0215|gene.b0215]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P03007`
- `KEGG:ecj:JW0205;eco:b0215;`
- `GeneID:946441;`
- `GO:GO:0003677; GO:0003887; GO:0004527; GO:0005829; GO:0006261; GO:0006272; GO:0006273; GO:0008408; GO:0009360; GO:0030894; GO:0044776; GO:0045004; GO:0046872`
- `EC:2.7.7.7`

## Notes

DNA polymerase III subunit epsilon (EC 2.7.7.7)
