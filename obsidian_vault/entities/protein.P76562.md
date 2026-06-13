---
entity_id: "protein.P76562"
entity_type: "protein"
name: "tmcA"
source_database: "UniProt"
source_id: "P76562"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01886}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tmcA ypfI b2474 JW2459"
---

# tmcA

`protein.P76562`

## Static

- Type: `protein`
- Source: `UniProt:P76562`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01886}.

## Enriched Summary

FUNCTION: Catalyzes the formation of N(4)-acetylcytidine (ac(4)C) at the wobble position of tRNA(Met), by using acetyl-CoA as an acetyl donor and ATP (or GTP). It recognizes the wobble base of tRNA(Met), thus distinguishing between tRNA(Met) and the structurally similar tRNA(Ile2) (PubMed:18668122, PubMed:19322199). Could use an RNA helicase motor driven by ATP hydrolysis to deliver the wobble base of tRNA(Met) to the acetyltransferase domain of TmcA (Probable). {ECO:0000269|PubMed:18668122, ECO:0000269|PubMed:19322199, ECO:0000305|PubMed:19322199}.; FUNCTION: Also functions as a lysine 2-hydroxyisobutyryltransferase to regulate transcription. Can specifically catalyze the 2-hydroxyisobutyrylation (Khib) of the DNA-binding protein H-NS. Hydroxyisobutyrylation of H-NS decreases its DNA-binding activity, promotes the expression of acid-resistance genes and enhances bacterial survival under extreme acid stress. {ECO:0000269|PubMed:34903851}. tRNAMet cytidine acetyltransferase acetylates the wobble base C34 of the Elongation-tRNAMet. TmcA specifically recognizes the anticodon stem of tRNAMet, thus distinguishing between tRNAMet and tRNAIle2, which is structurally similar and has the same anticodon loop . TmcA has also been shown to be a protein-lysine 2-hydroxyisobutyryltransferase but not participate in lysine acetylation...

## Biological Role

Catalyzes RXN0-5418 (reaction.ecocyc.RXN0-5418).

## Annotation

FUNCTION: Catalyzes the formation of N(4)-acetylcytidine (ac(4)C) at the wobble position of tRNA(Met), by using acetyl-CoA as an acetyl donor and ATP (or GTP). It recognizes the wobble base of tRNA(Met), thus distinguishing between tRNA(Met) and the structurally similar tRNA(Ile2) (PubMed:18668122, PubMed:19322199). Could use an RNA helicase motor driven by ATP hydrolysis to deliver the wobble base of tRNA(Met) to the acetyltransferase domain of TmcA (Probable). {ECO:0000269|PubMed:18668122, ECO:0000269|PubMed:19322199, ECO:0000305|PubMed:19322199}.; FUNCTION: Also functions as a lysine 2-hydroxyisobutyryltransferase to regulate transcription. Can specifically catalyze the 2-hydroxyisobutyrylation (Khib) of the DNA-binding protein H-NS. Hydroxyisobutyrylation of H-NS decreases its DNA-binding activity, promotes the expression of acid-resistance genes and enhances bacterial survival under extreme acid stress. {ECO:0000269|PubMed:34903851}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5418|reaction.ecocyc.RXN0-5418]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2474|gene.b2474]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76562`
- `KEGG:ecj:JW2459;eco:b2474;ecoc:C3026_13730;`
- `GeneID:946053;`
- `GO:GO:0000049; GO:0002101; GO:0005524; GO:0005737; GO:0016747; GO:0051391; GO:0051392; GO:0106226; GO:1904812; GO:1990883`
- `EC:2.3.1.-; 2.3.1.193`

## Notes

tRNA(Met) cytidine acetyltransferase TmcA (EC 2.3.1.193) (Lysine 2-hydroxyisobutyryltransferase) (EC 2.3.1.-)
