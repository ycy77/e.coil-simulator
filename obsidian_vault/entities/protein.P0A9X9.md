---
entity_id: "protein.P0A9X9"
entity_type: "protein"
name: "cspA"
source_database: "UniProt"
source_id: "P0A9X9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:2404279}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cspA cspS b3556 JW3525"
---

# cspA

`protein.P0A9X9`

## Static

- Type: `protein`
- Source: `UniProt:P0A9X9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:2404279}.

## Enriched Summary

FUNCTION: Binds to and stimulates the transcription of the CCAAT-containing, cold-shock-inducible promoters of the H-NS and GyrA proteins. Also binds to the inverted repeat 5'-ATTGG-3'. {ECO:0000269|PubMed:1961761}. The "Cold shock protein A," CspA, is a major cold shock protein and was shown to be detected only during early-log-phase growth at 37°C and during log phase after a shift from 37°C to 10°C . However, studies have shown that although the expression of cspA is reduced during stationary phase, cspA mRNA and CspA are detectable during all growth phases . CspA acts as a positive transcription factor of at least two cold shock genes: hns and gyrA . cspA has been shown to negatively regulate its own expression as the result of attenuation of transcription . A model of how CspA might affect the transcription of hns has been proposed . CspE inhibits the expression of cspA in vitro by increasing pause recognition for RNA polymerase at the cspA "cold box" . cspA expression was increased in a uvrY mutant strain and reduced when uvrY was overexpressed . CspA belongs to the cold shock family of proteins and was shown to be homologous to eukaryotic Y-box transcription factors . The transcription factors of this family recognize a CCAAT sequence in the regulatory region of the genes regulated...

## Annotation

FUNCTION: Binds to and stimulates the transcription of the CCAAT-containing, cold-shock-inducible promoters of the H-NS and GyrA proteins. Also binds to the inverted repeat 5'-ATTGG-3'. {ECO:0000269|PubMed:1961761}.

## Outgoing Edges (1)

- `activates` --> [[gene.b1237|gene.b1237]] `RegulonDB` `S` - regulator=CspA; target=hns; function=+

## Incoming Edges (1)

- `encodes` <-- [[gene.b3556|gene.b3556]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9X9`
- `KEGG:ecj:JW3525;eco:b3556;ecoc:C3026_19275;`
- `GeneID:86862034;948070;`
- `GO:GO:0001072; GO:0003676; GO:0003677; GO:0003697; GO:0003723; GO:0003727; GO:0005829; GO:0009409; GO:0010468; GO:0045893; GO:0060567`

## Notes

Cold shock protein CspA (CSP-A) (7.4 kDa cold shock protein) (CS7.4)
