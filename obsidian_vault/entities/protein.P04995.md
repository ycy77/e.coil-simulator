---
entity_id: "protein.P04995"
entity_type: "protein"
name: "sbcB"
source_database: "UniProt"
source_id: "P04995"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sbcB cpeA xonA b2011 JW1993"
---

# sbcB

`protein.P04995`

## Static

- Type: `protein`
- Source: `UniProt:P04995`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Degrades single-stranded DNA (ssDNA) in a highly processive manner (PubMed:23609540). Also functions as a DNA deoxyribophosphodiesterase that releases deoxyribose-phosphate moieties following the cleavage of DNA at an apurinic/apyrimidinic (AP) site by either an AP endonuclease or AP lyase (PubMed:1329027). {ECO:0000269|PubMed:1329027, ECO:0000269|PubMed:23609540}. Exonuclease I (ExoI) hydrolyzes DNA through its 3'-5' exonuclease acitivity. ExoI is specific for single-stranded DNA requiring a 3'-hydroxyl group. ExoI removes 5'-mononucleotides one at a time leaving the 5' dinucleotide intact . ExoI exhibits DNA deoxyribophosphodiesterase activity . ExoI releases deoxyribose-5-phosphate from DNA after endonuclease IV incision at apurinic/apyrimidinic (AP) sites, and 4-hydroxy-2-pentenal-5-phosphate after incision by endonuclease III at AP sites . ExoI activity has been shown to suppress illegitimate recombination by RecE . Exonuclease I activity is stimulated by EG10976-MONOMER. SSB binds to mutliple sites on exonuclease I, recruiting the enzyme to substrate and thus enhancing its activity . The nucleases, ExoI and CPLX0-3957 "SbcCD" are required for the completion of chromosome replication in E...

## Biological Role

Catalyzes 3.1.11.1-RXN (reaction.ecocyc.3.1.11.1-RXN).

## Enriched Pathways

- `eco03430` Mismatch repair (KEGG)

## Annotation

FUNCTION: Degrades single-stranded DNA (ssDNA) in a highly processive manner (PubMed:23609540). Also functions as a DNA deoxyribophosphodiesterase that releases deoxyribose-phosphate moieties following the cleavage of DNA at an apurinic/apyrimidinic (AP) site by either an AP endonuclease or AP lyase (PubMed:1329027). {ECO:0000269|PubMed:1329027, ECO:0000269|PubMed:23609540}.

## Pathways

- `eco03430` Mismatch repair (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.1.11.1-RXN|reaction.ecocyc.3.1.11.1-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2011|gene.b2011]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P04995`
- `KEGG:ecj:JW1993;eco:b2011;`
- `GeneID:946529;`
- `GO:GO:0000175; GO:0000287; GO:0003697; GO:0006274; GO:0006281; GO:0006308; GO:0008310; GO:0051575`
- `EC:3.1.11.1`

## Notes

Exodeoxyribonuclease I (ExoI) (Exonuclease I) (EC 3.1.11.1) (DNA deoxyribophosphodiesterase) (dRPase)
