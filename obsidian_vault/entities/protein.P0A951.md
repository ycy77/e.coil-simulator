---
entity_id: "protein.P0A951"
entity_type: "protein"
name: "speG"
source_database: "UniProt"
source_id: "P0A951"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "speG b1584 JW1576"
---

# speG

`protein.P0A951`

## Static

- Type: `protein`
- Source: `UniProt:P0A951`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Involved in the protection against polyamine toxicity by regulating their concentration (PubMed:10986239, PubMed:7642535). Catalyzes the transfer of an acetyl group from acetyl coenzyme A (AcCoA) to the primary amino groups of spermidine to yield N(1)- and N(8)-acetylspermidine (PubMed:6297970, PubMed:7052085, PubMed:8077207). It can also use spermine, but not putrescine (PubMed:7052085). {ECO:0000269|PubMed:10986239, ECO:0000269|PubMed:6297970, ECO:0000269|PubMed:7052085, ECO:0000269|PubMed:7642535, ECO:0000269|PubMed:8077207}.; FUNCTION: In addition, may act as a modulator of transcription through its ability to interact with the two-component response regulator RcsB. Inhibits transcription of the small RNA regulator rprA in an acetylation-independent manner. Interaction with the DNA-binding domain of RcsB might be responsible for SpeG-dependent inhibition of RcsB-dependent rprA transcription (PubMed:30562360). SpeG does not acetylate RcsB in vitro (PubMed:30562360). {ECO:0000269|PubMed:30562360}.

## Biological Role

Catalyzes acetyl-CoA:putrescine N-acetyltransferase (reaction.R01154). Component of spermidine N-acetyltransferase (complex.ecocyc.SPERMACTRAN-CPLX).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Involved in the protection against polyamine toxicity by regulating their concentration (PubMed:10986239, PubMed:7642535). Catalyzes the transfer of an acetyl group from acetyl coenzyme A (AcCoA) to the primary amino groups of spermidine to yield N(1)- and N(8)-acetylspermidine (PubMed:6297970, PubMed:7052085, PubMed:8077207). It can also use spermine, but not putrescine (PubMed:7052085). {ECO:0000269|PubMed:10986239, ECO:0000269|PubMed:6297970, ECO:0000269|PubMed:7052085, ECO:0000269|PubMed:7642535, ECO:0000269|PubMed:8077207}.; FUNCTION: In addition, may act as a modulator of transcription through its ability to interact with the two-component response regulator RcsB. Inhibits transcription of the small RNA regulator rprA in an acetylation-independent manner. Interaction with the DNA-binding domain of RcsB might be responsible for SpeG-dependent inhibition of RcsB-dependent rprA transcription (PubMed:30562360). SpeG does not acetylate RcsB in vitro (PubMed:30562360). {ECO:0000269|PubMed:30562360}.

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R01154|reaction.R01154]] `KEGG` `database` - via EC:2.3.1.57
- `is_component_of` --> [[complex.ecocyc.SPERMACTRAN-CPLX|complex.ecocyc.SPERMACTRAN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1584|gene.b1584]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A951`
- `KEGG:ecj:JW1576;eco:b1584;ecoc:C3026_09130;`
- `GeneID:75204427;946117;`
- `GO:GO:0000287; GO:0004145; GO:0006598; GO:0015936; GO:0032991; GO:0042802; GO:0046203; GO:0046208; GO:1990235`
- `EC:2.3.1.57`

## Notes

Spermidine N(1)-acetyltransferase (SAT) (EC 2.3.1.57) (Spermidine/spermine N(1)-acetyltransferase) (SSAT)
